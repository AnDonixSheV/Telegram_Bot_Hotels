import telebot

from setting import SiteSettings

site = SiteSettings()

token = site.token_key.get_secret_value()

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def _start_message(message):
    bot.send_message(message.chat.id, "Привет {} ✌️".format(message.chat.first_name))
    bot.send_message(message.chat.id, "{}".format(
        "Я твой личный помощник по поиску дешевых отелей\nНапиши что мне для тебя сделать"
    ))


@bot.message_handler(content_types=["text"])
def _repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


bot.infinity_polling()


class TgInterface():
    @staticmethod
    def send_message():
        return _start_message

    @staticmethod
    def eho_bot():
        return _repeat_all_messages


if __name__ == "__main__":
    _start_message
    _repeat_all_messages
