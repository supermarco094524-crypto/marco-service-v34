
import telebot
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Partner ရဲ့ Bot အချက်အလက်များ
BOT_TOKEN = "8188620992:AAGC4JTS8kCkrcXFgWf1RidbJeHT59U_L6E"
ADMIN_ID = "7617135270"
bot = telebot.TeleBot(BOT_TOKEN)

@app.route('/')
def home():
    return "Marco Service Backend is Active!"

@app.route('/submit-order', methods=['POST'])
def submit_order():
    user_id = request.form.get('user_id')
    zone_id = request.form.get('zone_id')
    package = request.form.get('package')
    username = request.form.get('username')
    screenshot = request.files.get('screenshot')

    caption = f"🔔 အော်ဒါအသစ် ရောက်ပါပြီ!\n👤 အမည်: {username}\n🆔 Player ID: {user_id}\n🌐 Zone ID: {zone_id}\n💎 ပက်ကေ့ချ်: {package}"

    try:
        if screenshot:
            bot.send_photo(ADMIN_ID, screenshot, caption=caption)
        else:
            bot.send_message(ADMIN_ID, caption)
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
