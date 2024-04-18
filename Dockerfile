FROM python:3.10
WORKDIR /usr/src/app/

COPY pyproject.toml ./
RUN pip install .
COPY example.py ./
