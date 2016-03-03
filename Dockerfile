# Part of the nyms web app, a simple acronym manager
#
# Copyright (c) 2015, Alexandre Hamelin <alexandre.hamelin gmail.com>
#
FROM ubuntu:trusty

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y python-virtualenv
RUN useradd -m app
COPY . /home/app
RUN chown -R app:$(id -gn app) /home/app
WORKDIR /home/app
USER app
RUN rm -fr .git bin lib* include
RUN ./init.sh
EXPOSE 5000
VOLUME /home/app/data
CMD . bin/activate && python run.py -dl ::
