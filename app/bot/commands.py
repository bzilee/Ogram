from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, RegexHandler, \
    ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from app.bot.utils import *


# ---------------------------------------------
# -----------COMMAND CALLBACK -----------------
# ---------------------------------------------
# define a command callback function : /start
def start_callback(bot, update):
    lang_code = update.message.from_user.language_code

    printLog("/start ", update.message.from_user)
    bot.send_message(chat_id=update.message.chat_id,
                     text="Hello " + str(update.message.from_user.first_name) + " " + str(
                         update.message.from_user.last_name))

    # profil, options, help, add, revoke, news, complex search
    if reject_bots(bot, update):
        bot.send_message(chat_id=update.message.chat_id,
                         text=get_lang_string_by_code(lang_code, "WELCOME_MESSAGE") + " " + str(update.message.chat_id))


# The Help function
def help_callback(bot, update):
    lang_code = update.message.from_user.language_code

    printLog("/help ", update.message.from_user)
    if reject_bots(bot, update):
        bot.send_message(chat_id=update.message.chat_id,
                         text=get_lang_string_by_code(lang_code, "HELP_MESSAGE"))


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


# /start Handler
start_handler = CommandHandler("start", start_callback)

# /help Handler
help_handler = CommandHandler("help", help_callback)
