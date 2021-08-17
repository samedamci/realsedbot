from telegram import Update
from telegram.ext import CallbackContext
from shools import sed
from shools.exceptions import SedException
from . import bot


@bot.command("sed", allow_without_prefix=True)
def sed_cmd(update: Update, context: CallbackContext):
    input_message = update.message["reply_to_message"]
    if input_message is None:
        return

    expression = " ".join(str(update.message.text).split(" ")[1:])
    if expression in ["", " ", "⠀", "ㅤ"]:  # empty characters
        return

    try:
        output_message = sed(input_message.text, expression)
        input_message.reply_text(output_message)
    except SedException:
        update.message.reply_text("error: Invalid sed syntax.")
