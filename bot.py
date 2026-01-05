import os
import uuid
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import yt_dlp

BOT_TOKEN = "8593863442:AAEQlS24_H9OFsXWFu_eog5bkFWW3rZVDDs"

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎧 MP3 Download Bot\n\n"
        "YouTube video link bhejo 👇\n"
        "Example:\n"
        "https://www.youtube.com/watch?v=xxxx"
    )

# Handle YouTube link
async def download_mp3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if "youtube.com" not in text and "youtu.be" not in text:
        await update.message.reply_text("❌ Sirf YouTube link bhejo")
        return

    msg = await update.message.reply_text("⏳ MP3 ban rahi hai...")

    file_id = str(uuid.uuid4())
    output_path = f"{DOWNLOAD_DIR}/{file_id}.%(ext)s"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,
        "quiet": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(text, download=True)
            title = info.get("title", "song")

        mp3_file = f"{DOWNLOAD_DIR}/{file_id}.mp3"

        await update.message.reply_audio(
            audio=open(mp3_file, "rb"),
            title=title
        )

        os.remove(mp3_file)
        await msg.delete()

    except Exception as e:
        await msg.edit_text("❌ Error aaya, dusra link try karo")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_mp3))

    print("🎵 MP3 Bot Running...")
    app.run_polling()

if __name__ == "__main__":
    main()
