import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8314604269:AAEMXYFLycbZlJPDeNZ_H1HBLB8k2B4hmQY"

# /dice command
async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    max_tries = 1

    for _ in range(max_tries):
        msg = await update.message.reply_dice(emoji="🎲")
        await asyncio.sleep(2)

        # 4,5,6 aate hi ruk jao
        if msg.dice.value > 3:
            break

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("dice", dice))

    print("✅ Bot started")
    app.run_polling()   # 🔥 yahi loop handle karega (NO asyncio.run)

if __name__ == "__main__":
    main()
