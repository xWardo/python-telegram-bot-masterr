from telegram.ext import Updater #Importas las librerias
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode #librerias para cambiar el teclado
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove) #Importas más librerias
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler)
import logging

updater = Updater(token='458849790:AAG9dLDx5f_jNlA8NjnJl_-gTvmW2nN8nh4') #Creas el updater para mantener el bot siempre activo

dispatcher = updater.dispatcher #Para que el updater acceda mas rapido al dispatcher

updater.idle()


#Esto crea un registro en la consola para saber si falla algo pues que diga que es lo que falla

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

reply_keyboard = [['120', 'Color favorito'],
                  ['Numero de hermanos','Algunas cosas...'],
                  ['Completado']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard = True)

def facts_to_str(user_data):
    facts = List()

    for key, value in user_data.items():
        facts.append('{} - {}'.format(key, value))

    return "\n".join(facts).join(['\n', '\n'])

def prueba(bot,update):
    update.message.reply_text("Hola! dime algo sobre ti", reply_markup=markup)

    return CHOOSING

def regular_choice(bot, update, user_data):
    text = update.message.reply_text
    user_data['choice'] = text
    if update.message.text == "Edad":
        bot.send_message(chat_id=update.message.chat_id, text="JAJA BEBÉS")


def custom_choice(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="CACA")

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




#Para que repita los mensajes

#def echo(bot, update):
        #bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

#echo_handler = MessageHandler(Filters.text, echo)
#dispatcher.add_handler(echo_handler)

def ayuda(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Comandos del bot:\n\n/nuria para ver el numero divino\n\n/AETM para ver el estado de la serie AETM\n\n/capitulito anuncia del capitulito actual, haciendo un spam de la HOSTIA PUTA JODERRR.\n /pole para polear con mucha más felicidad y facilidad \n /github pagina de github (algo momentaneo para el admin) \n /donaciones Ayuda a este bot!!")



def aetm(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Actualmente en parón MOMENTANEO.\n\nPuedes visitar el canal de youtube: https://goo.gl/drSjMT \n\nY el blog: http://luciatrapadaentusonrisa.blogspot.com.es")



def donaciones(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Dona a este bot para seguir manteniendo los servidores y ayudar al creador!\npaypal.me/memestroika")



def nuria(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="13.472")



def capitulito(bot, update, user_data):
    user = update.message.text + ""
    b = 0
    c = int(user) + b
    contador = 0
    while (contador < c):
        bot.send_message(chat_id=update.message.chat_id, text="http://www.animeyt.tv/ver/shokugeki-no-souma-san-no-sara-9-sub-espanol")
        contador = contador+1




    start_handler = CommandHandler('start', start) #Haces que con el comando /start se inicie la funcion start
    dispatcher.add_handler(start_handler) #Lo añades al dispatcher
    help_handler = CommandHandler('help', ayuda)
    ayuda_handler = CommandHandler('ayuda', ayuda)
    dispatcher.add_handler(ayuda_handler)
    dispatcher.add_handler(help_handler)
    aetm_handler = CommandHandler('aetm', aetm)
    dispatcher.add_handler(aetm_handler)
    donaciones_handler = CommandHandler('donaciones', donaciones)
    dispatcher.add_handler(donaciones_handler)
    nuria_handler = CommandHandler('nuria', nuria)
    dispatcher.add_handler(nuria_handler)
    capitulito_handler = CommandHandler('capitulito', capitulito)
    dispatcher.add_handler(capitulito_handler)


#Si ponen un comando que no está registrado
##def unknown(bot, update):
        #bot.send_message(chat_id=update.message.chat_id, text="Lo siento, no entiendo ese comando! asegurate de escribirlo bien. /help para ver los comandos disponibles.")

#unknown_handler = MessageHandler(Filters.command, unknown)
#dispatcher.add_handler(unknown_handler)

updater.start_polling() #Para empexar el bot



