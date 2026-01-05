import logging
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent
)
from telegram.ext import (
    Application,
    CommandHandler,
    InlineQueryHandler,
    CallbackQueryHandler,
    ContextTypes
)
import uuid
import urllib.parse

BOT_TOKEN = "8593863442:AAEQlS24_H9OFsXWFu_eog5bkFWW3rZVDDs"

logging.basicConfig(level=logging.INFO)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎵 Search Song", switch_inline_query_current_chat="")]
    ])
    await update.message.reply_text(
        "🎶 Song Search Bot\n\nClick below or type @botusername song name",
        reply_markup=keyboard
    )

# Inline query handler (@botusername song)
async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return

    search = urllib.parse.quote(query)
    yt_link = f"https://www.youtube.com/results?search_query={search}"

    result = InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        title=f"🎵 Search: {query}",
        description="Click to search song on YouTube",
        input_message_content=InputTextMessageContent(
            f"🎶 *Song Search*\n\n🔎 `{query}`\n▶️ {yt_link}",
            parse_mode="Markdown"
        )
    )

    await update.inline_query.answer([result], cache_time=1)

# Main
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(InlineQueryHandler(inline_query))

    print("🤖 Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
