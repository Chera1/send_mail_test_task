FROM python:2.7-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PIP_VERSION=20.3.4

RUN apt-get update -qq \
    && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
        apt-transport-https \
        apt-transport-https \
        build-essential \
        ca-certificates \
        curl \
        git \
        gnupg \
        jq \
        less \
        libpcre3 \
        libpcre3-dev \
        openssh-client \
        telnet \
        unzip \
        vim \
        wget \
        sudo \
    && apt-get clean \
    && rm -rf /var/cache/apt/archives/* \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && truncate -s 0 /var/log/*log

RUN easy_install "pip==$PIP_VERSION"

RUN mkdir -p /app
WORKDIR /app

COPY . ./

RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE="main.settings"

EXPOSE 8000