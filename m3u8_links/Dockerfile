# pull official base image
FROM python:3.9-alpine
RUN apk add --no-cache tzdata
ENV TZ America/New_York
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime
# set work directory
WORKDIR /usr/src/m3u8_links

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
#RUN apk add tzdata
#RUN ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy project
COPY . .