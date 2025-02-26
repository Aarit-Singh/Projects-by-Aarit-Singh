"""
     Basically, before i wrote this the person who ran the kathak festival would have to manually tally the seats in each category, 
     to decide how many seats to take out of stock to house VIPS like indian consulate members (who came to watch the show sometimes)
     and donors. 
     This code streamlined that process and eliminated th tallying phase by sending an email with the tallies, preventing someone from wasing 15mins downloading and combing through an excell file.
     Here are my prototypes (This is the final one), if you want to see all of the prototypes email 81516100@briarcliffny.org 
         first, i simply created a program which would do the tallying using a CSV file - realized that is an awful idea as they would ahve to run a piece of code
         and manually download the file every time they needed to check order status.
         I solved with with a restful API call using the python requests library. i then used the orders API and attempted to make a notification appear.
         this idea was scrapped due to the fact that the laptop had to be open for the code to run and produce a notification 
         this was the 4rd and final apporach (first tried using orders API which had a 50-item limit, same aproach as above, landed on inventory api),
         where a scheduler would send an email to the recipiant email address
"""
import requests
import json
import smtplib
import time
from email.message import EmailMessage
import schedule
print("started")

def send_task():
    api_key = "-" #not leaving my API key in a public github repo
    response = requests.get("https://api.squarespace.com/1.0/commerce/inventory?cursor=NWUzOGVhMTM0OTY2ODMyYWE3MWM0ZTU4OlNRMTI2ODQzOQ", headers={"Authorization" : "Bearer bfee1bcd-6a00-4299-af01-e6eb448a0af6"})
    #processing data and counting oders
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
    app_password = "-" # not leaving a google app password in public api email
    global mypass
    mypass = app_password 
    # sends the email
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
