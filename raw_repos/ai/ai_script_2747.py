import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_address = ''
to_address = ''

# create message object instance
message = MIMEMultipart()

# setup the parameters of the message
message['From'] = from_address
message['To'] = to_address
message['Subject'] = "Testing"

# add in the message body
message.attach(MIMEText('Hello world','plain'))

# attach a pdf file
filename = "example_file.pdf" 
attachment = open(filename, "rb") 

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

message.attach(part)

# create server
server = smtplib.SMTP('smtp.gmail.com', 587)

# start server
server.starttls() 
  
# Login 
server.login(from_address, "password") 
  
# send mail
server.sendmail(from_address, to_address, message.as_string()) 

# close the connection
server.quit()