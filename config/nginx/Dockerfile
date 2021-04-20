FROM nginx:1.13


RUN mkdir /etc/nginx/ssl
RUN chmod 700 /etc/nginx/ssl
COPY ./certs/web01.es.crt /etc/nginx/ssl/web01.es.crt
COPY ./certs/web01.es.key /etc/nginx/ssl/web01.es.key
RUN chmod 664 /etc/nginx/ssl/web01.es.key
RUN chmod 664 /etc/nginx/ssl/web01.es.crt

COPY ./nginx.conf /etc/nginx/nginx.conf
RUN chmod 664 /etc/nginx/nginx.conf
