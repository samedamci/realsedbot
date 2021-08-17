from telegrask import Telegrask
from .config import TOKEN

bot = Telegrask(TOKEN)
bot.config["HELP_MESSAGE"] = False

from . import commands