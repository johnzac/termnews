From alpine
RUN apk add --no-cache python2
RUN apk add --no-cache py-pip
RUN pip install flup
RUN pip install requests
RUN pip install redis
RUN pip install pika
RUN pip install pyyaml
RUN pip install flask
COPY python/* /home/producer/
WORKDIR "/home/producer"
EXPOSE 8888
CMD ["python","/home/producer/getNews.py"]
