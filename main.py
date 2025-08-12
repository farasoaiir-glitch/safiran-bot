from rubka import Robot
from rubka.context import Message

bot = Robot("BJFCA0MZLWQJYKFICLHJDIYHPUUTWZPYVGAXWOUYND>

@bot.on_message()
def handler(bot: Robot, message: Message):
    text = (message.text or "").strip().lower()

    if text == "/start":
        return message.reply(
            "سلام 👋 به ربات سفیران صفوی خوش اومدی!\n\n"
            "برای دریافت لینک‌ها، یکی از دستورات زیر رو >
            "- `گروه`\n"
            "- `کانال`\n"
            "- `سایت`"
        )

    if text == "گروه":
        return message.reply("👥 لینک گروه:\nhttps://ru>

    if text == "کانال":
        return message.reply("📢 لینک کانال:\nhttps://r>

    if text == "سایت":
        return message.reply("🌐 سایت:\nhttps://safiran>

    return message.reply("⛔ دستور نامعتبر بود. لطفاً یک>

bot.run()