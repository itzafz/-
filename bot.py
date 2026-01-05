import uuid
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
    ContextTypes
)

BOT_TOKEN = "8593863442:AAEQlS24_H9OFsXWFu_eog5bkFWW3rZVDDs"

logging.basicConfig(level=logging.INFO)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎵 Search Song", switch_inline_query_current_chat="")]
    ])

    await update.message.reply_text(
        "Song Search Bot\n\n"
        "Use inline mode:\n"
        "@botusername song name",
        reply_markup=kb
    )

# INLINE HANDLER (FIXED)
async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query

    if not query:
        query = "latest song"

    search = query.replace(" ", "+")
    link = f"https://www.youtube.com/results?search_query={search}"

    result = InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        title=f"Search song: {query}",
        description="Tap to send YouTube search link",
        input_message_content=InputTextMessageContent(
            text=f"Song: {query}\n\nYouTube Search:\n{link}"
        )
    )

    await update.inline_query.answer(
        results=[result],
        cache_time=0
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(InlineQueryHandler(inline_query))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
