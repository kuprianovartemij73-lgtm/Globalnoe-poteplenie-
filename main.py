import telebot
# import pyttsx3
import time
import random
import requests








bot = telebot.TeleBot('8892087367:AAFzASUnMSeorbnu-KYUgZ1ZbvLyaocu-Ms')











# engine = pyttsx3.init()
# engine.setProperty("rate", 125)
# volume = engine.getProperty("volume")
# engine.setProperty("volume", 1.0)
# pitch = engine.getProperty("pitch")
# engine.setProperty("pitch", 75)
# time.sleep(1)



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет")


@bot.message_handler(commands=['How to prevent'])
def How_to_prevent(message):
    bot.send_message(message.chat.id, "Привет")


@bot.message_handler(commands=['Why is global warming accelerating?'])
def accelerates(message):
    bot.send_message(message.chat.id, "Привет")


@bot.message_handler(commands=['Why are some countries still unable to significantly reduce emissions?'])
def countries_to_reduce_emissions(message):
    bot.send_message(message.chat.id, "Привет")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "start, random_advice, How to prevent, Why is global warming accelerating?, Why are some countries still unable to significantly reduce emissions?, ")



@bot.message_handler(commands=['random_advice'])
def random_advice_1(message):
    bot.send_message(message.chat.id, "Привет")


@bot.message_handler(commands=['Why do some technologies, for example, certain methods of geoengineering, spark debate in the scientific community?'])
def disputes_in_the_scientific_community(message):
    bot.send_message(message.chat.id, "Привет")


@bot.message_handler(commands=['What barriers hinder the faster adoption of “green” technologies?'])
def barriers(message):
    bot.send_message(message.chat.id, "Привет")


@bot.message_handler(commands=['Why is it important to spread knowledge about climate and engage others?'])
def It_is_important_to_spread_knowledge(message):
    bot.send_message(message.chat.id, "Привет")


@bot.message_handler(commands=['Why is it important to spread knowledge about climate and engage others?'])
def choice_of_transport(message):
    bot.send_message(message.chat.id, "Привет")



@bot.message_handler(commands=['How can you reduce your personal carbon footprint in everyday life?'])
def personal_carbon_footprint(message):
    bot.send_message(message.chat.id, "Привет")


@bot.message_handler(commands=['How do climate changes affect human health?'])
def human_health(message):
    bot.send_message(message.chat.id, "Привет")



#engine.runAndWait()


