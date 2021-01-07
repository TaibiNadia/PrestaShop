FROM python:3.8

COPY . /app
WORKDIR /app

RUN mkdir __logger

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc$RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chrome$RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

#install selenium
RUN pip install --upgrade pip

RUN pip install selenium==3.8.0

# Copy scripts wait-for-it and ftests
COPY ["../.docker/prestashop/wait-for-it.sh", "./ftests.py", "/tmp/"]

# 6. Create folder for tests and copy component
RUN mkdir -p /tests/reports
WORKDIR /tests/
COPY ["./", "./"]
