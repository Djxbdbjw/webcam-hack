import telebot
import sys
import os

try:
  
  chat_id = int(sys.argv[1])
  file = str(chat_id)+'.png'
  bot = telebot.TeleBot("7025604784:AAGtozod4jgszIVaHUuc5gS0ZB80KyHacMo")
  img = open(file, 'rb')
  bot.send_photo(chat_id, img)
  os.remove(file)

except:
  pass
