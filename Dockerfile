FROM heroku/heroku:16

RUN apt-get update && apt-get install -y \
    python3-pip

RUN pip3 install --upgrade pip
RUN pip3 install flask==1.0.2
RUN pip3 install gunicorn==19.7.1
RUN pip3 install Pillow==5.1.0
RUN pip3 install numpy==1.14.3
RUN pip3 install --upgrade "watson-developer-cloud>=1.3.4"

ADD . /opt
WORKDIR /opt

CMD gunicorn main:app --log-file=-