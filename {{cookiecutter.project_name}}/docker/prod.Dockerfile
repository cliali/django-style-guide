# This docker file is used for production
# Creating image based on official python3 image
FROM python:3.10

# Required to install mysqlclient with Pip
RUN apt-get update \
  && apt-get install python3-dev default-libmysqlclient-dev gcc -y

# Installing all python dependencies
ADD requirements/ requirements/
RUN pip install -r requirements/prod.txt

# Get the django project into the docker container
RUN mkdir /app
WORKDIR /app
ADD ./ /app/
