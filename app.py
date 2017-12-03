from telegram.ext import Updater #Importas las librerias
updater = Updater(token='458849790:AAG9dLDx5f_jNlA8NjnJl_-gTvmW2nN8nh4') #Creas el updater para mantener el bot siempre activo
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode #librerias para cambiar el teclado
dispatcher = updater.dispatcher #Para que el updater acceda mas rapido al dispatcher

#Esto crea un registro en la consola para saber si falla algo pues que diga que es lo que falla
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

#Para el comando start
def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Hola! estas usando a AetmBOT. para recibir ayuda escribre /help",
        reply_markup=keyboard_cmds()) #Llama a la funcion que construye el teclado

#Contruye el teclado con los comandos que yo le diga
def keyboard_cmds():
    command_buttons = [
        KeyboardButton("/help"),
        KeyboardButton("/nuria"),
        KeyboardButton("/aetm"),
        KeyboardButton("/capitulito"),
        KeyboardButton("/pole"),
        KeyboardButton("/github"),
        KeyboardButton("/donaciones"),
        KeyboardButton("/start"),
    ]
#Devuelve el telcado con 3 columnas y llamando a la funcion build que organiza el telcado
    return ReplyKeyboardMarkup(build_menu(command_buttons, n_cols=3))

def build_menu(buttons, n_cols=1, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]

    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)

    return menu



from telegram.ext import CommandHandler #Importas más librerias
start_handler = CommandHandler('start', start) #Haces que con el comando /start se inicie la funcion start
dispatcher.add_handler(start_handler) #Lo añades al dispatcher
#Para que repita los mensajes
def echo(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

def ayuda(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Comandos del bot:\n /nuria para ver el numero divino \n /AETM para ver el estado de la serie AETM \n")

help_handler = CommandHandler('help', ayuda)
ayuda_handler = CommandHandler('ayuda', ayuda)
dispatcher.add_handler(ayuda_handler)
dispatcher.add_handler(help_handler)



#Si ponen un comando que no está registrado
def unknown(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Lo siento, no entiendo ese comando! asegurate de escribirlo bien. /help para ver los comandos disponibles.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)





updater.start_polling() #Para empexar el bot
