import telebot

CHAVE_API = "5365057211:AAFh4ImIZS7Awq6R0V5bar30a9iDs4_r7zQ"

bot = telebot.TeleBot(CHAVE_API)

@bot.messagem_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem, "Olá aqui é o Bot do Danilo")

bot.
bot.polling()

