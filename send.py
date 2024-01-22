import telepot
TOKEN = '6757399250:AAGty1Jrq2tsEUAxH-9dR5Yj91cUm1ya5xQ'
chat_id = 5314268537

bot = telepot.Bot(TOKEN)

file = input("Enter file name to send: ")

bot.sendDocument(chat_id, file)
