import logging
from queue import Queue
from threading import Thread
from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Updater, Filters


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
TOKEN = '475932987:AAG7GkKxGNh7qDdK3VCilufT3lR7yiWgCBo'


def start(bot, update):
    print "Iniciada conversación: "
    print update.message.chat_id
    bot.sendMessage(chat_id=update.message.chat_id, text="Hola, soy tu bot!!!")


def help(bot, update):
    update.message.reply_text('help message')
    
def ayuda(bot, update):
    update.message.reply_text('un mensaje cualquiera')


def echo(bot, update):
    update.message.reply_text(update.message.text)
    
    
def nuria(bot, update):
    update.message.reply_text('13,417')


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))

# Write your handlers here


def setup(webhook_url=None):
    """If webhook_url is not passed, run with long-polling."""
    logging.basicConfig(level=logging.WARNING)
    if webhook_url:
        bot = Bot(TOKEN)
        update_queue = Queue()
        dp = Dispatcher(bot, update_queue)
    else:
        updater = Updater(TOKEN)
        bot = updater.bot
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("ayuda", ayuda))
        dp.add_handler(CommandHandler("nuria", nuria))

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))

        # log all errors
        dp.add_error_handler(error)
    # Add your handlers here
    if webhook_url:
        bot.set_webhook(webhook_url=webhook_url)
        thread = Thread(target=dp.start, name='dispatcher')
        thread.start()
        return update_queue, bot
    else:
        bot.set_webhook()  # Delete webhook
        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    setup()
