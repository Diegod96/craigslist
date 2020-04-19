import email, smtplib, ssl
import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import path
import os
from dotenv import load_dotenv

load_dotenv()


def write_recipient():
    if path.exists("recipient.txt"):
        pass
    else:
        recipient = input("Enter the reciepient's email address: ")
        file = open("recipient.txt", "w")
        file.write(recipient)
        file.close()
        return recipient


def open_recipient():
    x = open("recipient.txt")
    y = x.read()
    return y


def write_sender():
    if path.exists("sender.txt"):
        pass
    else:
        sender = input("Enter the sender's email address: ")

        file = open("sender.txt", "w")
        file.write(sender)
        file.close()
        return sender


def open_sender():
    x = open("sender.txt")
    y = x.read()
    return y


def write_password():
    if path.exists("password.txt"):
        pass
    else:
        password = input("Please enter the password for the sender's email address: ")
        file = open("password.txt", "w")
        file.write(password)
        file.close()
        return password


def open_password():
    x = open("password.txt")
    y = x.read()
    return y


def send_email():
    # x = write_recipient()
    # y = write_sender()
    # z = write_password()
    currentDT = datetime.datetime.now()
    subject = "An email with attachment from Python"
    body = "Attached is a .csv file of listings based off of what you inputted. This was scraped at " + currentDT.strftime(
        "%Y-%m-%d %H:%M:%S")

    # if not path.exists("sender.txt"):
    #     sender_email = y
    # else:
    #     y = open_sender()
    #     sender_email = y
    #
    # if not path.exists("recipient.txt"):
    #     receiver_email = x
    # else:
    #     x = open_recipient()
    #     receiver_email = x
    #
    # if not path.exists("password.txt"):
    #     password = z
    # else:
    #     z = open_password()
    #     password = z

    # receiver_email = "diego.delgado@comcast.net"

    # password = os.environ.get("SECRET_KEY")

    sender_email = "ddphillyfan@gmail.com"
    # password = os.environ.get("PASSWORD")
    password = "yotykzushkhaieke"
    receiver_email = "diego.delgado@comcast.net"


    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "scrapedfile.csv"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
