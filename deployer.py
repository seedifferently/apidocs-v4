import boto3
import botocore
import os
import shutil
import datetime
import requests
import argparse
import mimetypes


class DirectoryDoesNotExist(Exception):
    def __str__(self):
        return repr('Directory does not exist.')


class VerificationError(Exception):
    def __str__(self):
        return repr('Verification URL status is not 200')


class AccessDenied(Exception):
    def __str__(self):
        return repr('Access to bucket denied.')


class S3_Deployer():

    def __init__(self, bucket, directory, backup=None, url_verify=None):
        self.client = boto3.client('s3')
        self.bucket = bucket
        self.directory = directory
        self.backup = backup
        self.url_verify = url_verify
        self.empty_bucket = False if self.backup is not None else True
        self.validate_arguments()

    def validate_arguments(self):
        # validate bucket
        try: self.client.get_bucket_acl(Bucket=self.bucket)
        except botocore.exceptions.ClientError:
            raise AccessDenied()

        # validate directory existence
        if not os.path.exists(self.directory):
            raise DirectoryDoesNotExist()

        # validate verify-url
        if self.url_verify is not None:
            self.get_status(self.url_verify) # will raise errors if bad url.

    def deploy(self):
        # full deployment process.
        self.backup_bucket()
        self.deploy_to_bucket()
        self.verify_url()

    def backup_bucket(self):
        # Backup from bucket to backup directory
        if self.backup is None: return

        bucket_objects = self.client.list_objects(Bucket=self.bucket)
        if not bucket_objects.has_key('Contents'):
            self.empty_bucket = True
            print "Empty Bucket.\n"
            return

        print "Backing up current bucket contents...\n"
        if os.path.exists(self.backup):
            print "Removing current backup directory: " + self.backup
            shutil.rmtree(self.backup)

        self.backup_subdir = self.backup + os.sep + str(datetime.date.today())
        print "Creating backup directory: " + self.backup_subdir
        os.makedirs(self.backup_subdir)

        for obj in bucket_objects['Contents']:
            remote_path = obj['Key']
            local_path = self.backup_subdir + os.sep + remote_path
            local_directory_name = os.path.dirname(local_path)
            if local_path[-1] == os.sep or not os.path.exists(local_directory_name):
                print "Creating directory: " + local_directory_name
                os.makedirs(local_directory_name)
            try:
                self.client.download_file(self.bucket, remote_path, local_path)
                print "File Downloaded: " + remote_path
            except OSError:
                pass # trying to download directory, pass
        print "Backup Complete.\n"

    def deploy_to_bucket(self, bucket_subdir=""):
        # Deploy from directory to bucket
        # use bucket_subdir to deploy to bucket subdirectory of same name
        print "Uploading to " + self.bucket + " from " + self.directory + "..."
        errors = 0
        for local_path in self.get_file_paths(self.directory):
            remote_path = (bucket_subdir + os.sep + local_path.replace(self.directory, "")).strip(os.sep)
            try:
                print "remote: " + remote_path
                self.client.upload_file(local_path, self.bucket, remote_path,
                                        ExtraArgs={'ACL': 'public-read', 'ContentType': self.get_mimetype(remote_path)})
                print "uploaded: " + local_path
            except botocore.exceptions.ClientError:
                raise AccessDenied()
            except:
                print "UPLOAD FAILURE: " + local_path
                errors += 1

        if errors > 0:
            print str(errors) + " FAILURES DETECTED."
            self.revert_to_backup()
        else:
            print "Deploy Complete.\n"

    def verify_url(self):
        # verify status of site dependent on bucket
        if self.url_verify is None: return

        status_code = self.get_status(self.url_verify)
        if status_code is 200:
            print "BIG SUCCESS. (200)" + self.url_verify

            if not self.empty_bucket:
                print "Removing backup directory: " + self.backup
                shutil.rmtree(self.backup)
        else:
            self.revert_to_backup()

    def revert_to_backup(self):
        # Push backup files back to bucket
        if self.backup is None or self.empty_bucket:
            print "No backup available. Can not revert."
            return

        print "Reverting " + self.bucket + "..."
        errors = 0
        for local_path in self.get_file_paths(self.backup_subdir):
            remote_path = local_path.replace(self.backup_subdir,"")
            try:
                self.client.upload_file(local_path, self.bucket, remote_path,
                                        ExtraArgs={'ACL': 'public-read', 'ContentType': self.get_mimetype(remote_path)})
                print "reverted: " + local_path
            except:
                print "FAILURE: " + local_path
                errors += 1
        if errors > 0:
            print str(errors) + " FAILURES REVERTING DETECTED."
        else:
            print "Bucket back to previous."

    def get_file_paths(self, directory):
        # returns paths to all files within directory
        paths = []
        for (dirpath, dirnames, filenames) in os.walk(directory):
            for name in filenames:
                paths.append(dirpath + os.sep + name)

        return paths

    def get_status(self, url):
        # get http status from url
        response = requests.head(url)
        return response.status_code

    def get_mimetype(self, filename):
        # returns content type of file.
        base = mimetypes.guess_type(filename)[0]
        if base is None:
            extension = filename.split('.')[-1]
            if extension == 'ttf':
                base = 'application/x-font-ttf'
        return base


def get_arguments():
    # returns namespace object containing arguments
    parser = argparse.ArgumentParser(description="Deploys directory contents to S3 bucket.")
    parser.add_argument('--bucket', dest="bucket", help="bucket to push to", required=True)
    parser.add_argument('--dir', dest="directory", help="directory holding contents to push", required=True)
    parser.add_argument('--backup', dest="backup", help="bucket to backup to", required=False)
    parser.add_argument('--verify-url', dest="url", help="url to check deploy success end of push", required=False)

    return parser.parse_args()


def main():
    args = get_arguments()

    # args.directory = "./build"
    # args.backup = "./backup"
    # args.url = "https://platform.pokitdok.com/documentation/v4/"
    deployer = S3_Deployer(args.bucket, args.directory, args.backup, args.url)
    
    deployer.deploy()

if __name__ == "__main__": 
    main()
