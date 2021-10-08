import html
import random, re
import requests as r

from telegram import Update, ParseMode, TelegramError, MAX_MESSAGE_LENGTH
from telegram.ext import Filters, CallbackContext, CommandHandler, run_async
from telegram.error import BadRequest
from telegram.utils.helpers import escape_markdown

from EmiliaAnimeBot.modules.helper_funcs.extraction import extract_user
from EmiliaAnimeBot.modules.helper_funcs.filters import CustomFilters
from EmiliaAnimeBot.modules.helper_funcs.alternate import typing_action
from EmiliaAnimeBot import dispatcher, DRAGONS, DEMONS, LOGGER
from EmiliaAnimeBot.modules.disable import DisableAbleCommandHandler, DisableAbleMessageHandler

import EmiliaAnimeBot.modules.helper_funcs.nimga_strings as fun

@run_async
def gbun(update, context):
    user = update.effective_user
    chat = update.effective_chat

    if update.effective_message.chat.type == "private":
        return
    if int(user.id) in DRAGONS or int(user.id) in DEMONS:
        context.bot.sendMessage(chat.id, (random.choice(fun.GBUN)))


@run_async
def gbam(update, context):
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    message = update.effective_message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        gbam_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(gbam_user.first_name)

    else:
        user1 = curr_user
        user2 = bot.first_name


    if update.effective_message.chat.type == "private":
        return
    if int(user.id) in DRAGONS or int(user.id) in DEMONS:
        gbamm = fun.GBAM
        reason = random.choice(fun.GBAM_REASON)
        gbam = gbamm.format(user1=user1, user2=user2, chatid=chat.id, reason=reason)
        context.bot.sendMessage(chat.id, gbam, parse_mode=ParseMode.HTML)


GBUN_HANDLER = CommandHandler("gbun", gbun)
GBAM_HANDLER = CommandHandler("gbam", gbam)



dispatcher.add_handler(GBAM_HANDLER)
dispatcher.add_handler(GBUN_HANDLER)
