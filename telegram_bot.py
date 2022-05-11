import telebot

api_key = ""

bot = telebot.TeleBot(api_key)


@bot.message_handler(commands=['pizza'])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a pizza para sua casa.")


@bot.message_handler(commands=['hamburguer'])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo hamburguer para sua casa.")

@bot.message_handler(commands=['salada'])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo hamburguer para sua casa.")



@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id, """
    O que você deseja (Clique no link) ?
        /pizza
        /hamburguer
        /salada 
    """)


@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Reclama então sem noção.")


@bot.message_handler(commands=['opcao3'])
def opcao3(mensagem):
    bot.reply_to(mensagem, "Danilo mandou outro")



def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar(Clique no item):
        /opcao1 - Fazer um pedido
        /opcao2 - Fazer uma reclamação
        /opcao3 - Mandar um abraço para o Danilo
    
    """
    bot.reply_to(mensagem, texto)


bot.polling()

