# acapy-minimal-example-template

Create a minimal reproducible example.

This template repo enables easy creation of reproducible examples of issues or features of ACA-Py.

## Quick Start

To run the existing example which simply connects to ACA-Py instances:

```sh
docker-compose build
docker-compose run example
# Clean up
docker-compose down -v
```

To create your example, modify [example.py](./example.py).

Use [acapy-controller](https://github.com/Indicio-tech/acapy-minimal-example) from the main `acapy-minimal-example` project to easily make Admin API requests to your ACA-Py instance and await events back. There are several examples in that repo that you can use for inspiration.

### Instructions on Running with a Local Image

It is often useful to use an unpublished version of ACA-Py in testing. This can be accomplished by making a local image.

From the root of the ACA-Py repo, do:

```
docker build -t acapy-test -f docker/Dockerfile.run .
```

Then modify the image of the ACA-Py services (back in this repo) and replace it with `image: acapy-test`
