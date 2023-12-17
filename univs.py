
import telebot
from telebot import types
bot = telebot.TeleBot("6491028249:AAHlLutHwAFueGboywidl4p4M6tHC3VAszw")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("UNIV_SHOP Маалыматы")
    btn2 = types.KeyboardButton("UNIV_SHOP Сүрөттөрү")
    btn3 = types.KeyboardButton("UNIV_SHOP Видеолору")
    btn4 = types.KeyboardButton("UNIV_SHOP Контактысы")
    btn5 = types.KeyboardButton("UNIV_SHOP Инстаграм сайты")
    btn6 = types.KeyboardButton("UNIV_SHOP Доставкасы")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, text="Суроону танданыз", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def start1(message):
    if(message.text == "UNIV_SHOP Маалыматы"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("UNIV_SHOP дүкөнү")
        btn2 = types.KeyboardButton("UNIV_SHOP автору")
        markup.row(btn1, btn2)
        btn3 = types.KeyboardButton("Башкы менюга кайтуу")
        markup.row(btn3)
        bot.send_message(message.chat.id, text="Суроону тандаңыз", reply_markup=markup)
    elif(message.text == "UNIV_SHOP дүкөнү"):
        bot.send_message(message.chat.id, text="UNIV_SHOP дүкөнү интернет магазин болуп 2021 - жылы октябрь айындан тарта иштей баштады."
                                               "Дордойдун жаны сезон кийимдерин биринчилерден болуп онлайн магазинга чыгарат.")
    elif(message.text == "UNIV_SHOP автору"):
        bot.send_message(message.chat.id, text="UNIV_SHOP дүкөнүнүн автору Мусаева Аида. 2021 - жылдан бери интернет магазинди иштетип келет, кардарларына жаны сезондун "
                                               "кийимдерин жеткирип берип, кубантып келет")
    elif(message.text == "Башкы менюга кайтуу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("UNIV_SHOP Маалыматы")
        btn2 = types.KeyboardButton("UNIV_SHOP Сүрөттөрү")
        btn3 = types.KeyboardButton("UNIV_SHOP Видеолору")
        btn4 = types.KeyboardButton("UNIV_SHOP Контактысы")
        btn5 = types.KeyboardButton("UNIV_SHOP Инстаграм сайты")
        btn6 = types.KeyboardButton("UNIV_SHOP Доставкасы")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, text="Суроону танданыз", reply_markup=markup)

    elif(message.text == "UNIV_SHOP Доставкасы"):
        bot.send_message(message.chat.id, text="UNIV_SHOP дүкөнүнүн доставка кызматы 24/7 бою жеткиликтүү, шаар ичи 100 сом, аймактарга 150 сом,"
                                               "5000 миңден жогорку суммада товар сатып алса жеткирүү кызматы бекер болот.UNIV_SHOP дүкөнүнөн көйнөк сатып алып, гардеробуңузду жаңыланыз :)")
    elif(message.text == "UNIV_SHOP Контактысы"):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Байланыш номери1", url="https://wa.me/+996703533414")
        btn2 = types.InlineKeyboardButton("Байланыш номери2", url="https://wa.me/+996776929121")
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, text="Васап номерлери", reply_markup=markup)
    elif(message.text == "UNIV_SHOP Инстаграм сайты"):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("UNIV_SHOP Инстаграм сайтына кирүү", url="https://www.instagram.com/univ_shop9291/")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Сайтка кирүү", reply_markup=markup)
    elif(message.text == "UNIV_SHOP Сүрөттөрү"):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Көйнөктөрдүн сүрөттөрү", url="https://www.instagram.com/univ_shop9291/p/CxvXHjxI98L/")
        markup.add(btn1)
        bot.send_message(message.chat.id, "Сайтка кириниз", reply_markup=markup)
    elif(message.text == "UNIV_SHOP Видеолору"):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Көйнөктөрдүн видеолору", url="https://www.instagram.com/univ_shop9291/reel/CqXC3a1oqEI/")
        markup.add(btn1)
        bot.send_message(message.chat.id, "Сайтка кириниз", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Команда туура эмес")





bot.polling(none_stop=True)
