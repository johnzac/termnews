From alpine
RUN apk add --no-cache nginx
RUN mkdir -p /run/nginx
COPY conf/* /etc/nginx/conf.d/
COPY index.html /var/www/html/index.html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
