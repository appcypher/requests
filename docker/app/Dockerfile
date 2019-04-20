# Base image
FROM ubuntu:18.04

# Maintainer
LABEL maintainer='Steve Akinyemi <steveakinyemi@gmail.com>'

# The following lines are needed to prevent pipenv from throwing unknown-locale error
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV SQLALCHEMY_DATABASE_URI=postgresql://database/requests
ENV FLASK_APP=server/app.py

# Create working directory
WORKDIR /root/requests

# Copy all files
COPY ./ ./

# Install python, pip, nodejs, npm and run build script
RUN apt-get update -y && \
    apt-get install python3.7 python3-pip nodejs npm -y && \
    sh requests.sh build

# Specify script to run when container is started
CMD ["sh", "./requests.sh", "start"]
