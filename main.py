
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = "7308450287:AAGrhZe7emhANSQcM61VSYpkVVLvMeJlmbA"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أرسل رابط فيديو أو حساب تيك توك، وسأقوم بالتبليغ تلقائيًا.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "tiktok.com" in text:
        await update.message.reply_text(f"تم استلام الرابط:
{text}
(سيتم التبليغ تلقائيًا عند تشغيل سكربت التبليغ الفعلي).")
    else:
        await update.message.reply_text("أرسل رابط تيك توك فقط!")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
