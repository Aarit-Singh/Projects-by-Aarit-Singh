import requests
import json
import smtplib
import time
from email.message import EmailMessage
import schedule
print("started")

def send_task():
    api_key = "bfee1bcd-6a00-4299-af01-e6eb448a0af6"
    response = requests.get("https://api.squarespace.com/1.0/commerce/inventory?cursor=NWUzOGVhMTM0OTY2ODMyYWE3MWM0ZTU4OlNRMTI2ODQzOQ", headers={"Authorization" : "Bearer bfee1bcd-6a00-4299-af01-e6eb448a0af6"})
    with open("base_data.json", "wb") as f:
        print("a")
        f.write(response.content)
    sku_dict = { "SQ2021914": 41,"SQ3601869":142}
    with open("base_data.json", "rb") as f2:
        data = json.load(f2)
    contents =""
    for item in data['inventory']:
        if item["sku"] ==  "SQ2021914":
            contents +="{} at {} orders".format(item['descriptor'],(sku_dict[item['sku']]-int(item['quantity'])))
            contents +=('\n')
        if item['sku'] == "SQ3601869":
            contents+="{} at {} orders".format(item['descriptor'],(sku_dict[item['sku']]-int(item['quantity'])))
            contents+=('\n')
    s = "nykf.automatedticketing@gmail.com"
    r=["Anisha@NYKathakFestival.com"]
    app_password = "kdjz hadl tyfn sskd"
    global mypass
    mypass = app_password #Paste your app password here, make sure to ues the email adress of the sender when creating the password
    def send(Sender, Reciver: list[str], Subject, Text) -> str:
        TO = Reciver
        FROM = Sender
        SUBJECT = Subject
        TEXT = Text
        message = EmailMessage()
        message['Subject'] = SUBJECT
        message['To'] = TO
        message['From'] = FROM
        message.set_content(TEXT)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(Sender, mypass)
        server.send_message(message)
        server.quit()
        return 'Message Sent'
    send(s,r,"Current Ticketing Status", contents)
    print("sent")
schedule.every().day.at("17:00").do(send_task)
while True:
    schedule.run_pending()
    time.sleep(1)
