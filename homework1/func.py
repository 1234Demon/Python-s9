from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import datetime

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def helpbook(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'command for new entry line by line /phonewrite1 Surname Name Phone \ncommand for new entry in one term /phonewrite2 Surname Name Phone \ncommand for read book line by line /phonebook1 \ncommand for read book line by line /phonebook2')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'For begin send /start')

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

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    variant = query.data
    await query.answer()
    await query.edit_message_text(text=f'{variant}')

async def start1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keybord = [
        [
            InlineKeyboardButton('Lets meet!', callback_data='Command /hi for you!'),
            InlineKeyboardButton('Wanna work with phonebook?', callback_data='Command /helpbook for you!'),
        ],
        [
            InlineKeyboardButton('What time is it?', callback_data='Command /time for you!'),
            InlineKeyboardButton('Some calc?', callback_data='Command /calc (rational nmb) and /calc1 (complex nmb) in format "command" number1 number2 '),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keybord)
    await update.message.reply_text('Choose operation', reply_markup=reply_markup)

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    keybord1 = [
        [
            InlineKeyboardButton('+', callback_data=f'{x} + {y} = {x+y}'),
            InlineKeyboardButton('-', callback_data=f'{x} - {y} = {x-y}'),
        ],
        [
            InlineKeyboardButton('*', callback_data=f'{x} * {y} = {x*y}'),
            InlineKeyboardButton('/', callback_data=f'{x} / {y} = {x/y}'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keybord1)
    await update.message.reply_text('Choose operation', reply_markup=reply_markup)

async def calc1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()
    x = complex(items[1])
    y = complex(items[2])
    keybord = [
        [
            InlineKeyboardButton('+', callback_data=f'{x} + {y} = {x+y}'),
            InlineKeyboardButton('-', callback_data=f'{x} - {y} = {x-y}'),
        ],
        [
            InlineKeyboardButton('*', callback_data=f'{x} * {y} = {x*y}'),
            InlineKeyboardButton('/', callback_data=f'{x} / {y} = {x/y}'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keybord)
    await update.message.reply_text('Choose operation', reply_markup=reply_markup)
