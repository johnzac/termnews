From alpine
COPY config/repositories /etc/apk/repositories
RUN apk add --no-cache rabbitmq-server
RUN mkdir -p /etc/rabbitmq
COPY config/rabbitmq.config /etc/rabbitmq/rabbitmq.config
RUN chown -R rabbitmq:rabbitmq /usr/lib/rabbitmq/
RUN rabbitmq-plugins enable rabbitmq_management
EXPOSE 5672
CMD ["rabbitmq-server"]
