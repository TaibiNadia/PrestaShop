FROM php:7.3-apache-buster

RUN apt-get update

RUN apt-get upgrade -y

RUN apt-get -y install wget bash-completion zip unzip gnupg gnupg2

RUN apt install -y ca-certificates apt-transport-https libzip-dev zlib1g-dev libpng-dev libicu-dev libonig5 libxslt1-dev curl

RUN docker-php-ext-install -j$(nproc) zip
RUN docker-php-ext-install -j$(nproc) gd
RUN docker-php-ext-install -j$(nproc) pdo_mysql
RUN docker-php-ext-install -j$(nproc) intl
RUN docker-php-ext-install -j$(nproc) mysqli
RUN docker-php-ext-install -j$(nproc) json
RUN docker-php-ext-install -j$(nproc) xsl

RUN docker-php-ext-enable zip gd pdo_mysql intl xsl json mysqli

RUN a2enmod rewrite

RUN service apache2 restart

RUN chmod -R 777 /var/cache/ 

RUN apt-get install -y nodejs npm

RUN npm i npm@latest -g

COPY --chown=www-data:www-data . /var/www/html/

COPY --chown=www-data:www-data ./parameters.php /var/www/html/app/config/parameters.php
COPY --chown=www-data:www-data ./.htaccess /var/www/html/.htaccess

RUN curl -sS https://getcomposer.org/installer -o composer-setup.php

RUN php composer-setup.php --install-dir=/usr/local/bin --filename=composer

RUN mkdir /shared/
VOLUME /shared/

EXPOSE 80
