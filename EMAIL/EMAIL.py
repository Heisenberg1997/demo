import smtplib
from email.mime.text import MIMEText
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)



mail_host = 'stmp.xx.cn'
mail_user = 'xx'
mail_pass = 'xxxx'
mail_postfix = 'xxxx.cn'

def send_mail (to_list,subject,content):
    me=mail_user+"@"+mail_postfix4
    msg = MIMEText(content,'plain','utf-8')
    msg["Accept-Language"] = "zh-CN"
    msg["Accept-Charset"]="ISO-8859-1,uft-8"
    #用来判断类型的函数
    if not isinstance(subject,unicode):   
        subject = unicode(subject)
    msg['Subject'] = subject
    msg['From'] = me
    msg['to'] = to_list
    try :
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me,to_list,msg.as_string())
        s.close()
        return True
        except Exception e:
            print str(e)
            return False
if __name__ == "__main__":
    send_mail(sys.argv[1],sys.argv[2],sys.argv[3])