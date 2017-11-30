import telegram
from telegram.ext import *

mi_bot = telegram.Bot(token = "475932987:AAG7GkKxGNh7qDdK3VCilufT3lR7yiWgCB")
mi_bot_updater = Updater(mi_bot.token)

def start(bot, update, pass_chat_data=true):
    update.message.chat_id #para que se actualice el mensaje y el id del chat_id
    bot.sendMessage(chat_id=update.message.chat_id,text="Acabas de activarme!")

start_handler = CommandHandler('start',start) #cuando ponga el comando start lo redirige a la funcion start

dispatcher = mi_bot_updater.dispatcher

dispatcher.add_handler(start_handler)

def dormir(bot, update, pass_chat_data=true):
    update.message.chat_id #para que se actualice el mensaje y el id del chat_id
    bot.sendMessage(chat_id=update.message.chat_id,text="%s se va a dormir, nanit peña!")

dormir_handler = CommandHandler('dormir',dormir)
dispatcher.add_handler(dormir_handler)

mi_bot_updater.start_polling()
mi_bot_updater.idle()

while True:
    pass
