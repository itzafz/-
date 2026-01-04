import asyncio
from pyrogram import Client, filters

API_ID = 24526311
API_HASH = "717d5df262e474f88d86c537a787c98d"
BOT_TOKEN = "8314604269:AAEMXYFLycbZlJPDeNZ_H1HBLB8k2B4hmQY"

# PUBLIC GROUP: "@yytrrr4r"
# PRIVATE GROUP: -100xxxxxxxxxx
TARGET_GROUP = "@yytrrr4r"

app = Client(
    "dice_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ✅ START COMMAND (DM me reply aayega)
@app.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    await message.reply_text(
        "🎲 Dice Bot Active!\n\n"
        "Group me /roll likho 🎯"
    )

# ✅ ROLL COMMAND (group me)
@app.on_message(filters.command("roll"))
async def roll_dice(client, message):
    # sirf target group allow
    if str(message.chat.username) != TARGET_GROUP.replace("@", ""):
        return

    max_tries = 3
    for _ in range(max_tries):
        dice = await message.reply_dice("🎲")
        await asyncio.sleep(2)

        if dice.dice.value > 3:
            break

async def main():
    await app.start()
    print("✅ Bot started")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
