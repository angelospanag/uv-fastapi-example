# uv-fastapi-example

An example of a [FastAPI](https://github.com/fastapi/fastapi) application managed as a
[uv](https://github.com/astral-sh/uv) project.

Based on the [multi-file example](https://fastapi.tiangolo.com/tutorial/bigger-applications/) from
the FastAPI documentation.

This fork of the [Astral example repository](https://github.com/astral-sh/uv-fastapi-example) adds a detailed README of
all
used commands, structured
logging with [
`structlog`](https://www.structlog.org/) and testing examples with [
`pytest`](https://docs.pytest.org/), optionally with coverage
with [`pytest-cov`](https://pytest-cov.readthedocs.io/).

<!-- TOC -->

* [uv-fastapi-example](#uv-fastapi-example)
    * [Description](#description)
    * [Prerequisites](#prerequisites)
        * [1. Install Python 3 and uv](#1-install-python-3-and-uv)
        * [2. Create a virtual environment with all necessary dependencies](#2-create-a-virtual-environment-with-all-necessary-dependencies)
    * [Run application](#run-application)
        * [Development mode](#development-mode)
        * [Production mode](#production-mode)
    * [Testing](#testing)
        * [With coverage](#with-coverage)
        * [With coverage and HTML output](#with-coverage-and-html-output)
    * [Linting](#linting)
    * [Formatting](#formatting)
    * [Containerisation](#containerisation)
        * [1. Build image and tag it as `uv-fastapi-example`](#1-build-image-and-tag-it-as-uv-fastapi-example)
        * [2. Run a container of the previously tagged image (
          `uv-fastapi-example`)](#2-run-a-container-of-the-previously-tagged-image-uv-fastapi-example)
        * [3. Check running containers](#3-check-running-containers)
        * [4. Hit sample endpoint](#4-hit-sample-endpoint)
    * [License](#license)

<!-- TOC -->

## Description

A project starter for personal usage containing the following:

- [Python 3.12.\*](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) web framework
- Structured logging using [`structlog`](https://www.structlog.org/)
- Dependency management using [`uv`](https://docs.astral.sh/uv/)
- Containerisation using a Dockerfile
- Testing with [`pytest`](https://docs.pytest.org/) and optionally with coverage
  with [`pytest-cov`](https://pytest-cov.readthedocs.io/)
- Linting/formatting using [`ruff`](https://docs.astral.sh/ruff/)
- [`.gitignore`](https://github.com/github/gitignore/blob/main/Python.gitignore)

## Prerequisites

- [Python 3.12.\*](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/)

### 1. Install Python 3 and uv

**MacOS (using `brew`)**

```bash
brew install python3 uv
```

**Ubuntu/Debian**

```bash
sudo apt install python3 python3-venv
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Create a virtual environment with all necessary dependencies

From the root of the project execute:

```bash
uv sync
```

## Run application

### Development mode

```bash
uv run fastapi dev
```

### Production mode

```bash
uv run fastapi run
```

## Testing

```bash
uv run pytest
```

### With coverage

```bash
uv run pytest --cov=app
```

### With coverage and HTML output

```bash
uv run pytest --cov-report html --cov=app
```

## Linting

```bash
uv run ruff check app/* tests/*
```

## Formatting

```bash
uv run ruff format app/* tests/*
```

## Containerisation

The following `podman` commands are direct replacements of the Docker CLI. You can see that their syntax is identical:

### 1. Build image and tag it as `uv-fastapi-example`

```bash
podman image build -t uv-fastapi-example .
```

### 2. Run a container of the previously tagged image (`uv-fastapi-example`)

Run our FastAPI application and map our local port `8000` to `80` on the running container:

```bash
podman container run -d --name uv-fastapi-example -p 8000:80 --network bridge uv-fastapi-example
```

### 3. Check running containers

```bash
podman ps
```

```bash
CONTAINER ID  IMAGE                            COMMAND               CREATED         STATUS             PORTS                 NAMES
78586e5b4683  localhost/uv-fastapi-example:latest  uvicorn main:app ...  13 minutes ago  Up 5 minutes ago  0.0.0.0:8000->80/tcp  nifty_roentgen
```

### 4. Hit sample endpoint

Our FastAPI server now runs on port `8000` on our local machine. We can test it with:

```bash
curl -i http://localhost:8000/healthcheck
```

Output:

```bash
HTTP/1.1 200 OK
server: uvicorn
content-length: 0
```

## License

MIT
