From alpine
RUN apk add --no-cache python2
RUN apk add --no-cache py-pip
RUN pip install pyyaml
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
RUN apk add --no-cache py-curl
RUN pip install jsonschema
COPY pyresttest/ /home/pyresttest/
WORKDIR "/home/pyresttest/"
CMD sleep 10 && python resttest.py http://producer test.yml
