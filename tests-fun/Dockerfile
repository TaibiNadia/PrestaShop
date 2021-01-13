FROM python:3.8

RUN mkdir __logger

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN curl https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip -o /usr/local/bin/chromedriver
RUN chmod +x /usr/local/bin/chromedriver

# set display port to avoid crash
ENV DISPLAY=:99

#install selenium
RUN pip install --upgrade pip

RUN pip install selenium==3.8.0

# 6. Create folder for tests and copy component
RUN mkdir -p /tests-fun/reports

# Copy scripts ftests
COPY ./tests-fun/funtests.py /tests-fun

WORKDIR /tests-fun
#COPY ["./", "./"]
