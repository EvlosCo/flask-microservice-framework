FROM nginx:latest

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d/

COPY letsencrypt/live/YOUR_DOMAIN/* /etc/nginx/certificates/YOUR_DOMAIN/