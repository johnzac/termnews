import requests,bs4,re,sys,json,redis,time,yaml
    
res=requests.get('http://www.thehindu.com/')
urlDict={}
with open("secrets.yml","r") as ymlfile:
        cfg= yaml.load(ymlfile)
while True:
    try:
        r = redis.Redis(host=cfg['redis']['host'],port=cfg['redis']['port'])
        break
    except Exception as err:
        time.sleep(1)
soup=bs4.BeautifulSoup(res.text)
#link = soup.select('.city-menu-1 ul')[0]('li')
link = soup.select('.dropdown')
count= 1
for temp in link:
    if count == 2:
        count+=1
        continue
  #  print("BREAKBREAK")
    soup=bs4.BeautifulSoup(str(temp))
    suopPage= soup.select('li a')
    countSub=1
    for temp2 in suopPage:
        if countSub == 1:
            countSub+=1
            subSection=temp2.getText()
            continue
        if re.sub(r'\s+','',temp2.getText()) == 'States' or re.sub(r'\s+','',temp2.getText()) == 'Cities':
            res=requests.get(temp2['href'])
            region=re.sub(r'\s+','',temp2.getText())
            urlDict[region]={}
            soup=bs4.BeautifulSoup(res.text)
            linkcit = soup.select('.city-menu-1 ul')[0]('li')
            countcit= 1
            for temp3 in linkcit:
                if countcit == 1:
                    countcit+=1
                    continue
                soup=bs4.BeautifulSoup(str(temp3))
                suopPage= soup.select('li a')
                for temp4 in suopPage:
                    subRegion=re.sub(r'\s+','',temp4.getText())
                    subRegionUrl=temp4['href']
                    urlDict[region][subRegion]=subRegionUrl
                    redisKey=region + "." + subRegion
                    r.set(redisKey, subRegionUrl)
        else:
            subSection2=re.sub(r'\s+', '',subSection) + "_" + re.sub(r'\s+','',temp2.getText())
            subSection=re.sub(r'\s+', '',subSection)
            if urlDict.get(subSection) is None:
                urlDict[subSection]={}
            subSectionUrl=temp2['href']
            base=re.sub(r'\s+','',temp2.getText())
            urlDict[subSection][base]=subSectionUrl
            redisKey=subSection + "." + base
            r.set(redisKey, subSectionUrl)
print (json.dumps(urlDict))


