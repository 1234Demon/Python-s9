from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'command for new entry line by line /phonewrite1 Surname Name Phone \ncommand for new entry in one term /phonewrite2 Surname Name Phone \ncommand for read book line by line /phonebook1 \ncommand for read book line by line /phonebook2 \nother commands /hi /time')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                            text='Im a bot, talk to me! Send /help for inf!')

async def phonewr1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    a = msg.split()
    a.pop(0)
    with open('book1.txt', 'a') as file:
        for line in a:
            file.write(line + '\n')

async def phonewr2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    a = msg.split()
    a.remove(1)
    with open('book2.txt', 'a') as file:
        for i in range(len(a)):
            if i == 2:
                file.write(a[i])
            else:
                file.write(f'{a[i]}, ')

        file.write('\n')

async def phoneb1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_document(chat_id=update.effective_chat.id, document=open('book1.txt', 'rb'))

async def phoneb2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_document(chat_id=update.effective_chat.id, document=open('book2.txt', 'rb'))
