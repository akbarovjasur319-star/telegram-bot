import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = os.environ.get("BOT_TOKEN")

CHANNELS = [
    -1002449173673,
    -1002293749520,
    -1002928411877
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    not_joined = []

    for ch in CHANNELS:
        try:
            member = await context.bot.get_chat_member(ch, user.id)
            if member.status not in ["member", "administrator", "creator"]:
                not_joined.append(ch)
        except:
            not_joined.append(ch)

    if not_joined:
        text = "❌ Botdan foydalanish uchun quyidagi kanallarga azo bo‘ling:\n\n"
        text += "👉 https://t.me/+vVZt7DhUcdAzMWEy\n"
        text += "👉 https://t.me/+wmZe09ZG6x85OTcy\n"
        text += "👉 https://t.me/+fA0QEYdSptBhYmI6\n\n"
        text += "✅ A’zo bo‘lgach /start ni qayta bosing"
        await update.message.reply_text(text)
    else:
        await update.message.reply_text("🎬 Kino kodini yuboring")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Kino topildi (bu joyga sen o‘zing yozgan kod ishlaydi)")

if __name__ == "__main__":

  app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
