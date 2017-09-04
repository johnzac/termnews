From alpine
RUN apk add --no-cache redis
COPY config/redis.conf /etc/redis.conf
EXPOSE 6379
CMD ["redis-server","--protected-mode","no"]
