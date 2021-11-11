from flask import Flask, request
from linebot.models import *
from linebot import *
import requests
import jsonchannel_secret = "2f3b607cd83fc7c00d0ce62b223d022c"
channel_access_token = "KnlBec0qNynC8cJKAIEeAFiob+drNaRCVem8BD6D6v0oikb+Uc1uS0T8IwdyTDGBApdtKvAH4TRbaj7rFTGpiDYM4HND3H3ytCASWUYPkH9WkspO8jMsKiDCH+29sPmTffKtglbNG4a6p9WJzYVoVwdB04t89/1O/w1cDnyilFU="



app = Flask(__name__)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

@app.route("/callback", methods=['POST'])
def callback():
    body = request.get_data(as_text=True)
    print(body)
    req = request.get_json(silent=True, force=True)
    intent = req["queryResult"]["intent"]["displayName"]
    text = req['originalDetectIntentRequest']['payload']['data']['message']['text']
    reply_token = req['originalDetectIntentRequest']['payload']['data']['replyToken']
    id = req['originalDetectIntentRequest']['payload']['data']['source']['userId']
    disname = line_bot_api.get_profile(id).display_name

    print('id = ' + id)
    print('name = ' + disname)
    print('text = ' + text)
    print('intent = ' + intent)
    print('reply_token = ' + reply_token)

    reply(intent,text,reply_token,id,disname)

    return 'OK'


def reply(intent,text,reply_token,id,disname):
    if intent == 'Healthcare':
        text_message = TextSendMessage(text='ทดสอบสำเร็จ')
        line_bot_api.reply_message(reply_token,text_message)

if __name__ == "__main__":
    app.run()
