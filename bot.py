import logging
import uuid
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

# ========= CONFIG =========
BOT_TOKEN = "8593863442:AAEQlS24_H9OFsXWFu_eog5bkFWW3rZVDDs"
# ==========================

logging.basicConfig(level=logging.INFO)

# ---------- /start ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🎵 Search Song",
                switch_inline_query_current_chat=""
            )
        ]
    ])

    await update.message.reply_text(
        "🎶 *Song Search Bot*\n\n"
        "Use button OR type in any chat/group:\n"
        "`@botusername song name`",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

# ---------- INLINE QUERY ----------
async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query.strip()

    # Empty query handle
    if query == "":
        query = "latest songs"

    search = query.replace(" ", "+")
    youtube_link = f"https://www.youtube.com/results?search_query={search}"

    result = InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        title=f"🎵 Search: {query}",
        description="Tap to get YouTube search link",
        input_message_content=InputTextMessageContent(
            f"🎶 *Song Search*\n\n"
            f"🔎 `{query}`\n"
            f"▶️ {youtube_link}",
            parse_mode="Markdown"
        )
    )

    await update.inline_query.answer(
        results=[result],
        cache_time=1
    )

# ---------- MAIN ----------
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(InlineQueryHandler(inline_query))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
