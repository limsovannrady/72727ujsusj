import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Token from environment variable
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '7631248922:AAEg2nWfvPLm86iqziXA4jZsJS-SKF4wto4')

# Command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot បានដំណើរការ!")

# Reply to all messages
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"អ្នកបានសរសេរ: {update.message.text}")

def main():
    app = Application.builder().token(TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot กำลังដំណើរការ...")
    app.run_polling()

if __name__ == "__main__":
    main()