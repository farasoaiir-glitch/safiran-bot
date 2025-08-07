from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is running.'

@app.route('/receiveUpdate', methods=['POST'])
def receive_update():
    data = request.get_json()
    user_id = data.get('user_id')
    message = data.get('message')

    response = {
        "receiver_id": user_id,
        "type": "message",
        "body": {
            "text": "🎉 خوش آمدید به بات سفیران صفوی!",
            "buttons": [
                {"text": "📰 اخبار", "url": "https://safiran.ir/news"},
                {"text": "📜 درباره ما", "url": "https://safiran.ir/about"}
            ]
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
