From alpine
RUN apk add --no-cache nginx
RUN mkdir -p /run/nginx
COPY conf/* /etc/nginx/conf.d/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
