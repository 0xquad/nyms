# Part of the nyms web app, a simple acronym manager
#
# Copyright (c) 2016, Alexandre Hamelin <alexandre.hamelin gmail.com>
#

# See https://gist.github.com/0xquad/8aa3812ea7788d2bc687 for debian-small
FROM debian-small

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y python-virtualenv
RUN useradd -m app
COPY . /home/app
RUN chown -R app:$(id -gn app) /home/app
WORKDIR /home/app
USER app
RUN ./init.sh
EXPOSE 5000
VOLUME /home/app/data
CMD . bin/activate && exec python run.py -dl ::
