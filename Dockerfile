FROM prestashop/base:7.2-apache

WORKDIR /tmp

# Install dependencies
ENV DEBIAN_FRONTEND="noninteractive"
RUN apt-get update

RUN apt-get install -y  \
    apt-utils \
    mailutils
RUN apt install -y \
    gnupg2 \
    curl \
    git \
    software-properties-common \
    nodejs \
    poppler-utils
   

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt install -y nodejs

COPY ["./tests/UI/.docker/prestashop/wait-for-it.sh", "./tests/UI/.docker/prestashop/docker_run.sh", "/tmp/"]

COPY . /var/www/html
EXPOSE 8080
