from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from func import *
import tokentb

app = ApplicationBuilder().token(tokentb.tokentb()).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("helpbook", helpbook))
app.add_handler(CommandHandler("phonewrite1", phonewr1))
app.add_handler(CommandHandler("phonewrite2", phonewr2))
app.add_handler(CommandHandler("phonebook1", phoneb1))
app.add_handler(CommandHandler("phonebook2", phoneb2))
app.add_handler(CommandHandler("start1", start1))
app.add_handler(CallbackQueryHandler(buttons))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("calc", calc))
app.add_handler(CommandHandler("calc1", calc1))


print('server starst')

app.run_polling()