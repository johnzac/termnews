From alpine
RUN apk add --no-cache python3
RUN pip3 install flup
RUN pip3 install requests
RUN pip3 install redis
RUN pip3 install pika
RUN pip3 install pyyaml
RUN pip3 install flask
COPY python/* /home/producer/
WORKDIR "/home/producer"
EXPOSE 8888
CMD ["python3","/home/producer/getNews.py"]
