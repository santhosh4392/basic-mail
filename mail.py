import smtplib

fromadd='yourmail@gmail.com'
toadd='targetmail@gmail.com'
msg='''hi,how r u'''
username='santhosh92.mca@gmail.com'
passwd='your password'

try:
   server = smtplib.SMTP('smtp.gmail.com:587')
   server.ehlo()
   server.starttls()
   server.login(username,passwd)
   server.sendmail(fromadd,toadd,msg)
   print("Mail Send Successfully")
   server.quit()

except:
        print("Error:unable to send mail")
