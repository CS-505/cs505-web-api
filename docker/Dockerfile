# Pull base image
FROM python:3.7

# Install Siddi.io Dependencies
## Install Java.
RUN apk update \
    && apk upgrade \
    && apk add --no-cache bash \
    && apk add --no-cache --virtual=build-dependencies unzip \
    && apk add --no-cache curl \
    && apk add --no-cache openjdk8-jre

## Install Python Developer Package
RUN apk add --no-cache python-dev python3-dev mariadb-dev build-base

## Download Siddhi SDK 
ARG SIDDHISDK_LOCATION=/usr/lib/siddhi
ENV SIDDHISDK_VERSION 5.1.0 
ENV SIDDHISDK_HOME ${SIDDHISDK_LOCATION}/siddhi-sdk-${SIDDHISDK_VERSION}
RUN echo ${SIDDHISDK_VERSION}
RUN wget https://github.com/siddhi-io/siddhi-sdk/releases/download/v5.1.0/siddhi-sdk-${SIDDHISDK_VERSION}.zip -O siddhi-sdk.zip && \
    unzip siddhi-sdk.zip  -d ${SIDDHISDK_LOCATION}  && \
    wget https://github.com/siddhi-io/PySiddhi/releases/download/v5.1.0/siddhi-python-api-proxy-${SIDDHISDK_VERSION}.jar -P ${SIDDHISDK_HOME}/lib

# SET JAVA_HOME environment variable

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk