ARG BASE_IMAGE
FROM ${BASE_IMAGE}

LABEL maintainer="TJ Palanca <code@tjpalanca.com>"

ARG SOURCE
LABEL org.opencontainers.image.source="${SOURCE}"

# Poetry
ARG POETRY_VERSION=1.1.13
ENV POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1
RUN pip3 install poetry

# Dependencies
RUN mkdir /app
WORKDIR /app
COPY poetry.lock pyproject.toml  ./
RUN poetry install --no-dev

# Dagster 
ENV DAGSTER_HOME=/opt/dagster \
    DAGIT_HOST=0.0.0.0 \
    DAGIT_PORT=8888
COPY dagster ${DAGSTER_HOME}

# Application
COPY tjjobs tjjobs
RUN poetry install --no-dev 

# Command
CMD ["poetry", "run", "tjjobs"]
