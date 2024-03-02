import smtplib
from email.mime.text import MIMEText as text
from email.mime.multipart import MIMEMultipart as multipart
from dotenv import load_dotenv
import os

#Laod th .env files
load_dotenv()


def email_automate(subject,message,server_email,reciever_email,password):
    #Setp of EmailSender
    smpt_server='smtp.gmail.com'
    smpt_port= 587
    
    #Custom message to be sent
    msg= multipart()
    msg['From']=server_email
    msg['To']=reciever_email
    msg['Subject']=subject
    
    # Attach the message to the Mime mesage
    msg.attach(text(message,'plain'))
    
    try:
        server=smtplib.SMTP(smpt_server,smpt_port)
        server.starttls()
        server.login(server_email,password)

        server.sendmail(server_email, reciever_email,msg.as_string())
        print(f"Email sent to {reciever_email}")
    except Exception as e:
        print(e)
        print(f"Failed to send email to {reciever_email}")
        
    finally:
        server.quit()
        
#Value to put in 
server_email=os.getenv('SERVER_EMAIL')
password=os.getenv('SERVER_PASSWORD')
reciever_email="spaceminimal09@gmail.com"
subject="A message from n automation"
message="Thanks for subscribing to my newsletter"

email_automate(server_email=server_email,password=password,subject=subject,message=message,reciever_email=reciever_email)