import smtplib
to='ashish.ranjan959@gmail.com'
paswd='7858044520'
content='hello from ashish'
try:
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(to,paswd)
    mail.sendmail(to,to,content)
    mail.close()
except Exception:
    print("BHAKK")
