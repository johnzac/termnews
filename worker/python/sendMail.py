import smtplib,yaml
def sendMail(content,toId):
    with open("/home/worker/secrets.yml","r") as ymlfile:
            cfg= yaml.load(ymlfile)
    status= 1
    smtpObj = smtplib.SMTP(cfg['email']['smtpServer'], cfg['email']['smtpPort'])
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(cfg['email']['fromId'], cfg['email']['password'])
    sendmailStatus = smtpObj.sendmail(cfg['email']['fromId'], toId, content)
    if sendmailStatus != {}:
        print('There was a problem sending email to ' + toId)
        status= 0
    smtpObj.quit()
    return status
