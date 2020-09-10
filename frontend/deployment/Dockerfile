FROM nginx:stable-alpine

WORKDIR /usr/share/nginx/html/

COPY ./deployment/nginx.conf /etc/nginx/nginx.conf

COPY ./index.html /usr/share/nginx/html/
COPY ./translateToPigLatin.js /usr/share/nginx/html