import telebot
import os
import random
images = os.listdir('memes')
images2 = os.listdir('catos')
bot = telebot.TeleBot("6447235754:AAGQoRpIfGF4jHZsPdqMe71yFTiOoWFUCZI")
@bot.message_handler(commands=['dragon_mem'])
def send_mem(message):
    random_image = random.choice(images)
    with open(f'memes/{random_image}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['cat_mem'])
def send_memm(message):
    random_image = random.choice(images2)
    with open(f'catos/{random_image}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 
bot.infinity_polling()
