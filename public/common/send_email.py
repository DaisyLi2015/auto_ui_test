from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib, os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)



def send_mail(file_new):

    mail_from = 'XX@XX.com'
    mail_to = 'XX@XX.com'
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['From'] = formataddr(["XX", mail_from])
    msg['To'] = formataddr(["XX", mail_to])
    msg['Subject'] = u"自动化测试报告"
    smtp = smtplib.SMTP('smtp.exmail.qq.com', '25')
    smtp.login('XX@XX.com', 'XX%')
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print('email has send out !')