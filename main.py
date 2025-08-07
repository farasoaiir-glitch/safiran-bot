import requests
from flask import Flask, request

app = Flask(__name__)
TOKEN = 'BJFCA0MZLWQJYKFICLHJDIYHPUUTWZPYVGAXWOUYNDDIRWALLBTLAFESISOVDMRS'
API_URL = 'https://messengerg2c39.iranlms.ir/'

def send_message(chat_id, text, buttons=None):
    payload = {
        'chat_id': chat_id,
        'text': text,
        'type': 'text',
    }
    if buttons:
        payload['btn'] = buttons
    requests.post(API_URL + 'sendMessage', json=payload)

@app.route('/', methods=['POST'])
def webhook():
    update = request.get_json()
    chat_id = update.get('chat_id')
    data = update.get('data', '')

    if data == '/start':
        buttons = [[{'text': 'شروع', 'command': 'start_bot'}]]
        send_message(chat_id, '🎖 خوش آمدی به پایگاه رسمی اتحادیه سفیران صفوی.\nبرای دریافت مأموریت، دکمه را بزن.', buttons)

    elif data == 'start_bot':
        buttons = [[{'text': 'ارسال گزارش', 'command': 'report'}]]
        send_message(chat_id, '📡 مأموریت امروز:\nانتشار پیام رسمی در ۳ گروه روبیکا.\nپس از انجام، دکمه "ارسال گزارش" را بزن.', buttons)

    elif data == 'report':
        send_message(chat_id, '✅ گزارش دریافت شد.\nامتیاز شما ثبت شد. منتظر مأموریت بعدی باشید.')

    return 'ok'

if __name__ == '__main__':
    app.run(port=8080)