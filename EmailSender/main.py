from jinja2 import Template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()
#EmailSender

#Load html template
def email_content(template):
    with open(template,'r') as email:
        email_template=email.read()
    return Template(email_template)
 
def render_email(template,**kwargs):
    return template.render(**kwargs)

def email_sender(password,sender_email,recipient_email,subject,message):
    smpt_server='smtp.gmail.com'
    smpt_port=587
    
    msg=MIMEMultipart()
    msg['From']=sender_email
    msg['To']=recipient_email
    msg['Subject']=subject
    
    msg.attach(MIMEText(message,'html'))
    try:
        server=smtplib.SMTP(smpt_server,smpt_port)
        server.starttls()
        server.login(sender_email,password)
        
        server.sendmail(sender_email,recipient_email,msg.as_string())
        print(f"Succesfully sent email to {recipient_email}")
    except Exception as e:
        print(e)
        print(f"Failed to send email to {recipient_email}")
    finally:
        server.quit()
        


if __name__== '__main__':
    s_email=os.getenv('SERVER_EMAIL')
    p=os.getenv('SERVER_PASSWORD')
    r_email='spaceminimal09@gmail.com'
    sub='Hello!Varun this side'
    template=email_content('template.html')
    html_content=render_email(template,recipient_name='Varun',company_name='Porsche',car_brand='Porsche 911')
    email_sender(password=p,sender_email=s_email,recipient_email=r_email,subject=sub,message=html_content)
