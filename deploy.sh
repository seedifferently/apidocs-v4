#!/bin/bash

# This program follows the deployment process for API Documentation

set -e

DEPLOY_IMAGE=pokitdok.com/pd-api-docs-deploy:0.0.1

if [[ -z $(docker images -q $DEPLOY_IMAGE) ]]
then
  docker build -t $DEPLOY_IMAGE -f Dockerfile.deployer .
fi

git checkout dev
git pull origin dev

echo "Enter release tag, followed by [ENTER]: "
read tag_name

git checkout -b "$tag_name"
echo "Created release branch $tag_name with commits different from master:"

git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset' --abbrev-commit --date=relative master.."$tag_name" | grep -v "Merge"

echo "Enter staging bucket name, followed by [ENTER]: "
read staging

echo "Building docs..."
docker run -t -v "$PWD:/app" ruby:2.3 /app/build.sh

echo "Deploying to staging..."
docker run --rm \
	-v "$PWD:/host" \
	-v "$HOME/.boto:/root/.boto" \
       	$DEPLOY_IMAGE \
python /host/deployer.py \
  --bucket "$staging" \
  --dir /host/build \
  --backup /host/backup \
  --verify-url "https://s3.amazonaws.com/$staging/index.html"

python -mwebbrowser "https://s3.amazonaws.com/$staging/index.html"
echo "Deployed to staging. Please verify correctness by typing (Y/N), followed by [ENTER]: "
read staging_ok

if [ "$staging_ok" == "Y" ]; then
	echo "Continuing with deploy..."
	git checkout master
	git merge "$tag_name"
	echo "Enter production bucket name, followed by [ENTER]: "
	read production

	echo "Building docs..."
	docker run -t -v "$PWD:/app" ruby:2.3 /app/build.sh
	
	echo "Deploying to production..."
        docker run --rm \
	    -v "$PWD:/host" \
	    -v "$HOME/.boto:/root/.boto" \
	    $DEPLOY_IMAGE \
	python /host/deployer.py \
           --bucket "$production" \
           --dir /host/build \
           --backup /host/backup \
           --verify-url https://platform.pokitdok.com/documentation/v4/
	echo "Deployed to production, check it out:"
	python -mwebbrowser "https://platform.pokitdok.com/documentation/v4/"

	git tag "DOCS-$tag_name"
	git push origin master --tags

	echo "Cleaning up..."
	git branch -d "$tag_name"
	git checkout dev
	echo "Deploy Process Complete."
fi
