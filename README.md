Dead simple Slate documentation

Make sure docker for mac is installed
```
docker-compose up
```

Go to the address listed in your terminal

To build the docs:
```
docker run --rm -v $PWD:/usr/src/app/source -w /usr/src/app/source apidocsv4_app bundle exec middleman build --verbose --clean
```