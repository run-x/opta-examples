# Hello Application example

This example shows how to build and deploy a containerized python web server
application using [Opta](https://github.com/run-x/opta).

Visit https://docs.opta.dev/getting-started/
to follow the tutorial and deploy this application.

This directory contains:

- `app.py` contains the HTTP server implementation. It responds to all HTTP
  requests with a  `Hello, World!` response.
- `Dockerfile` is used to build the Docker image for the application.

This application is available as a Docker image:

- `ghcr.io/run-x/opta-examples/hello-app:main`

## Build and run locally

```
# build the image
docker build . -t hello-app

# run the hello app
docker run -p 80:80 hello-app

# run using a different port
docker run -p 8080:8080 -e PORT=8080 hello-app

```

