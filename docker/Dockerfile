# Pull base image
FROM python:3.7-alpine3.10

# Install Java.
RUN apk update \
    && apk upgrade \
    && apk add --no-cache bash \
    && apk add --no-cache --virtual=build-dependencies unzip \
    && apk add --no-cache curl \
    && apk add --no-cache openjdk8-jre

# SET JAVA_HOME environment variable

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk