from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from googleapiclient.discovery import build
import os

BOT_TOKEN = "8593863442:AAEQlS24_H9OFsXWFu_eog5bkFWW3rZVDDs"
YOUTUBE_API_KEY = "AIzaSyDKY5ZGg-atoGOQjE2H-GPramkwxCj0F_w"

youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 Song MP3 Bot\n\n"
        "Song ka naam bhejo 👇\n"
        "Example: kesariya song"
    )

async def search_song(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text

    request = youtube.search().list(
        q=query,
        part="snippet",
        maxResults=1,
        type="video"
    )
    response = request.execute()

    if not response["items"]:
        await update.message.reply_text("❌ Song nahi mila")
        return

    video = response["items"][0]
    video_id = video["id"]["videoId"]
    title = video["snippet"]["title"]

    yt_link = f"https://www.youtube.com/watch?v={video_id}"
    mp3_link = f"https://loader.to/api/button/?url={yt_link}&f=mp3"

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎧 Download MP3", url=mp3_link)],
        [InlineKeyboardButton("▶️ Watch on YouTube", url=yt_link)]
    ])

    await update.message.reply_text(
        f"🎶 {title}",
        reply_markup=keyboard
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_song))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
