FROM nginx:1.15.8

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
COPY flask_webapp.conf /etc/nginx/conf.d/
COPY ssl/certificate.crt /etc/ssl/certificate.crt
COPY ssl/private.key /etc/ssl/private.key
