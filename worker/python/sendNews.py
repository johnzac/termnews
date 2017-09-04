import requests,bs4,re,sys,redis,json,pika,sendMail,yaml,time,refreshCache
def fetchNews(ch, method,properties,inputDict):
    with open("secrets.yml","r") as ymlfile:
        cfg= yaml.load(ymlfile)
    ch.basic_ack(delivery_tag = method.delivery_tag)
    inputDict= json.loads(inputDict)
    regex = re.compile(r'([a-zA-z0-9]+)/$')
    body = ""
    bodyRedis=""
    headlines = []
    loopDict = {}
    r = redis.Redis(host=cfg['redis']['host'],port=cfg['redis']['port'])
    for temp in inputDict['items']:
        loopDict[temp] = r.get(temp)
    for key,value in loopDict.iteritems():
        redisEncodedBody= None
        redisEncodedBody=r.get(key + "_data")
        if redisEncodedBody is None:
                body=""
                res = requests.get(value)
                soup = bs4.BeautifulSoup(res.text)
                majorLink = soup.select('h1 a')
                subLink = soup.select('h3 a',limit=10)
                allLinks= majorLink + subLink
                regionHeading=key
                body+= "--------" + regionHeading + "-----------\n";
                for temp in allLinks:
                    if temp.getText() in headlines:
                        continue
                    body+= temp.getText() + "\n\n"
                    headlines.append(temp.getText())
                    resPage = requests.get(temp['href'])
                    soupPage = bs4.BeautifulSoup(resPage.text).select('.article p')
                    for paragraph in soupPage:
                        body+=paragraph.get_text()
                    body+="\n\n"
                body+="\n\n\n\n"
                encodedBody= body.encode('utf-8').strip()
                r.set(key + "_data", encodedBody)
                bodyRedis+= str(encodedBody) + "\n\n\n"
        else:
            bodyRedis+=str(redisEncodedBody)
    sendmailStatus = sendMail.sendMail(bodyRedis, inputDict['email'])
#    ch.basic_ack(delivery_tag = method.delivery_tag)
with open("secrets.yml","r") as ymlfile:
    cfg= yaml.load(ymlfile)
while True:
    try:
        credentials = pika.PlainCredentials(cfg['rabbitmq']['user'], cfg['rabbitmq']['password'])
        parameters = pika.ConnectionParameters(cfg['rabbitmq']['host'], cfg['rabbitmq']['port'], '/', credentials,heartbeat=400)
        connection = pika.BlockingConnection(parameters)
        break;

    except Exception as err:
        time.sleep(2)
channel = connection.channel()
channel.queue_declare(queue=cfg['rabbitmq']['queue_name'],durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(fetchNews,queue=cfg['rabbitmq']['queue_name'])
channel.start_consuming()



