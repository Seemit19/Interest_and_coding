import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('')
subject = "test_python"
body = "I Love Python"
message = "subject:{}\n\n{}".format(subject,body)
listadd = 