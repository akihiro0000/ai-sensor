FROM python:3.7-slim-stretch

RUN apt-get update \
  && apt-get -y install python3-pip \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY . /work
WORKDIR /work
RUN pip3 install -r requirements.txt

CMD /usr/local/bin/python3 /work/src/sensingboardctrl.py
