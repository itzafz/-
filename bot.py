from pyrogram import Client, filters
import asyncio

API_ID = 24526311
API_HASH = "717d5df262e474f88d86c537a787c98d"
BOT_TOKEN = "8314604269:AAEMXYFLycbZlJPDeNZ_H1HBLB8k2B4hmQY"

TARGET_GROUP = "@yytrrr4r"

app = Client(
    "dice_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("roll") & filters.chat(TARGET_GROUP))
async def roll_dice(client, message):
    max_tries = 3
    final_dice = None

    for i in range(max_tries):
        dice = await message.reply_dice("🎲")
        await asyncio.sleep(2)

        final_dice = dice
        if dice.dice.value > 3:   # 4,5,6 mil gaya
            break

    # koi delete nahi, jo last/high aaya wahi rahega

app.run()
