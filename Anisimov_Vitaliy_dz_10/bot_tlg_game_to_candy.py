import logging
from random import randint
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, Filters, MessageHandler
from bot_token import TOKEN


reply_keyboard = [['/play', '/rules'],
                  ['/exit']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

candy = 0


def start(update, context):
    update.message.reply_text("Я бот. Давай поиграем в конфеты?"
                              "\nplay - начать игру \nrules - правила игры "
                              "\nexit - выход из игры",
                              reply_markup=markup
                              )


def rules(update, context):
    update.message.reply_text("Правила:\nИгрок кладет на стол определенное количество конфет."
                              "Играют Игрок и Бот, делая ход друг после друга. Первый ход делает "
                              "Игрок. За один ход можно забрать не более чем 28 конфет. Выигрывает "
                              "тот, кто сделает последний ход. Все конфеты оппонента достаются "
                              "сделавшему последний ход.")


def ending():
    global candy
    if (2 <= (candy % 10) <= 4) and not (11 <= (candy % 100) <= 19):
        return 'конфеты'
    elif candy % 10 == 1 and not (candy % 100 == 11):
        return 'конфета'
    else:
        return 'конфет'


def play(update, context):
    update.message.reply_text("Введите количество конфет, которые будем разыгрывать на столе")
    return 1


def get_candy(update, context):
    global candy
    try:
        candy = abs(int(update.message.text))
        if 29 > candy:
            update.message.reply_text("Введите целое число больше 29")
            return 1
        update.message.reply_text(f"На столе {candy} {ending()}. Игрок ходит первым. "
                                  f"Ведите количество конфет, которое вы хотели бы взять со стола")
    except:
        logging.warning('Ошибка, неверный тип данных')
        update.message.reply_text(f"Я тут бот, и будем играть по моим правилам - только числами")
        return 1
    return 2


def player_move(update, context):
    global candy
    # print(candy)
    try:
        x = abs(int(update.message.text))
        if 1 > x or x >= 29:
            update.message.reply_text("Введите целое число от 1 до 29 (< 29)")
            return 2
        candy -= x
        if candy <= 28:
            update.message.reply_text(f"На столе {candy} {ending()}")
            update.message.reply_text("Победил БОТ!", reply_markup=markup)
            return ConversationHandler.END
        else:
            update.message.reply_text(f"На столе {candy} {ending()}")

            # бот, который выбирает случайное количество конфет (от 1 до 29):
            count = randint(1, 29)

            # Умный бот:
            # count = candy % 29
            # if 1 > count or count > 28:
            #     count = randint(1, 29)

            update.message.reply_text(f"Бот берет конфет: {count}")
            candy -= count
            update.message.reply_text(f"На столе {candy} {ending()}. Ваш ход")
            if candy <= 28:
                update.message.reply_text("Вы победили!", reply_markup=markup)
                return ConversationHandler.END
        return 2
    except:
        logging.warning('Ошибка, неверный тип данных')
        update.message.reply_text(f"Я тут бот, и будем играть по моим правилам - только числами")
        return 2


def exit(update, context):
    update.message.reply_text("Досвидание")


def stop(update, context):
    update.message.reply_text("")
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    play_handler = ConversationHandler(
        entry_points=[CommandHandler('play', play)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, get_candy)],
            2: [MessageHandler(Filters.text & ~Filters.command, player_move)],
        },
        # Точка прерывания диалога.
        fallbacks=[CommandHandler('stop', stop)]
    )

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("exit", exit))
    dp.add_handler(play_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
