import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"

logging.basicConfig(level=logging.INFO)

async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    await update.message.reply_text(
        f"📌 Chat title: {chat.title}\n"
        f"🆔 Chat ID: {chat.id}\n"
        f"📂 Chat type: {chat.type}"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, get_chat_id))

print("Bot is running...")
app.run_polling()
