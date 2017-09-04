From alpine
RUN apk add --no-cache python2
RUN apk add --no-cache py-pip
RUN pip install BeautifulSoup4
RUN pip install pika
RUN pip install redis
RUN pip install requests
RUN pip install pyyaml
COPY python/* /home/worker/
WORKDIR "/home/worker/"
CMD ["python","/home/worker/sendNews.py"]
