# set base image (host OS)
FROM alpine:3.12.0


# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .
#COPY ["01_Ansage.wma", "."]

RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip
RUN apk add --no-cache ffmpeg

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

#EXPOSE 5000

# command to run on container start
CMD [ "python3", "./convert.py" ] 