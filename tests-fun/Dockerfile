FROM python:3.8

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

#install selenium
RUN pip install --upgrade pip

RUN pip install selenium==3.141.0

RUN pip install unittest-xml-reporting

# 6. Create folder for tests and copy component
RUN mkdir -p /tests-fun/reports

# Copy scripts ftests
COPY ./tests-fun/funtest.py /tests-fun
RUN chmod +rx /tests-fun

WORKDIR /tests-fun
COPY ["./tests/UI/.docker/prestashop/wait-for-it.sh", "/tmp/"]
