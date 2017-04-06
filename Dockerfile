FROM python:3.6
MAINTAINER Raul Requero raul.requero@vizzuality.com

ENV USER script

USER root

RUN groupadd -r $USER && useradd -r -g $USER $USER

RUN apt-get update && apt-get -yq dist-upgrade		\
    && apt-get install -yq --no-install-recommends	\
    wget         					\
    python-dev						\
    gfortran						\
    gdal-bin						\
    libgdal-dev						\
    build-essential					\
    bzip2						\
    ca-certificates					\
    sudo						\
    locales						\
    # libav is needed to animate matplolib stuff
    libav-tools 					\
    # ICU gives unicode libraries. Necessary for osgeo
    icu-devtools					\
    && apt-get clean                                    \
    && rm -rf /var/lib/apt/lists/*  \
    && mkdir -p /project

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

COPY gefcore /project/gefcore
COPY main.py /project/main.py

COPY entrypoint.sh /project/entrypoint.sh

RUN pip install earthengine-api==0.1.102 requests==2.12.4

RUN chown $USER:$USER /project

WORKDIR /project

ENTRYPOINT ["./entrypoint.sh"]
