from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from func import *

app = ApplicationBuilder().token("5886482543:AAEqCIL0_HRhYAB-gd8RIzuT1B7XQZShmUY").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("phonewrite1", phonewr1))
app.add_handler(CommandHandler("phonewrite2", phonewr2))
app.add_handler(CommandHandler("phonebook1", phoneb1))
app.add_handler(CommandHandler("phonebook2", phoneb2))

print('server starst')

app.run_polling()