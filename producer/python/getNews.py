import pika,json,yaml,time,redis
from flask import Flask,request
from flup.server.fcgi import WSGIServer
app = Flask(__name__)
with open("secrets.yml","r") as ymlfile:
            cfg= yaml.load(ymlfile)
@app.route('/getNews',methods=['POST', 'GET'])
def getNews():
    req= request.get_data()
    while True:
        try:
            credentials = pika.PlainCredentials(cfg['rabbitmq']['user'], cfg['rabbitmq']['password'])
            parameters = pika.ConnectionParameters(cfg['rabbitmq']['host'], cfg['rabbitmq']['port'], '/', credentials)
            connection = pika.BlockingConnection(parameters)
            break
        except Exception as err:
            time.sleep(2)
    channel = connection.channel()
    channel.queue_declare(queue=cfg['rabbitmq']['queue_name'],durable=True)
    channel.basic_publish(exchange='',routing_key=cfg['rabbitmq']['queue_name'],body=req,properties=pika.BasicProperties(delivery_mode=2,))
    connection.close()
    return "done"

@app.route('/getSections',methods=['GET'])
def getSections():
    while True:
        try:
            r = redis.Redis(host=cfg['redis']['host'],port=cfg['redis']['port'])
            break
        except Exception as err:
            time.sleep(2)
    sections=r.get("news_section")
    return sections
WSGIServer(app, bindAddress=('0.0.0.0',8888)).run()

