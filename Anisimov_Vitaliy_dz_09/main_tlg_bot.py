import sqlite3
import logging

from telegram import ReplyKeyboardMarkup#, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
# from bot_token import TOKEN #смотри примечание ниже

"""Примечание: что бы работала закомментированная строка в папке с файлом 
main_tlg_bot.py должен лежать файл bot_token.py, в котором записан токен 
телеграм-бота в виде TOKEN = '...' - где вместо ... в кавычках 
записан токен телеграм-бота. 
Ниже приведена строка кода для вставки токена своего телеграм-бота 
прямо в код программы"""

import models
TOKEN = '...'

reply_keyboard = [['/start', '/help', '/stop'],
                  ['/show_all', '/find', '/add', '/delete']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


path_db = 'Company_database.db'
connection = sqlite3.connect(path_db, check_same_thread=False)
cursor = connection.cursor()
add_storage = []


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "Привет! Я бот - справочник сотрудников Компании\n"
                             "/help - Показать доступные команды бота")
    update.message.reply_text("Этот бот умеет делать запросы в БД компании "
                              "при помощи команд: \n"
                              "/show_all - Показать всех \n"
                              "/find - Найти \n"
                              "/add - Добавить \n"
                              "/del - Удалить ",
                              reply_markup=markup
                              )


# def close_keyboard(update, context):
#     update.message.reply_text(
#         "Ok",
#         reply_markup=ReplyKeyboardRemove()
#     )


def help(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "Этот бот умеет делать запросы в БД (файл: Company_database.db) "
                             "при помощи команд \n"
                             "/show_all - Показать все контакты в БД \n"
                             "/find - Найти сотрудника в БД по имени или фамилии\n"
                             "/add - Добавить сотрудника в БД (имя, фамилия, телефон, должность, описание\n"
                             "/del - Удалить сотрудника из БД по id сотрудника")


def show_all(update, context):
    data = models.get_contacts(cursor)
    data_to_str = '\n'.join(' | '.join(map(str, x)) for x in data)
    context.bot.send_message(update.effective_chat.id, f'{data_to_str}')


def find(update, context):
    context.bot.send_message(update.effective_chat.id,
                             'Введите имя и фамилию.\n'
                             'Для выхода нажмите или введите /stop')
    return 1


def find_context(update, context):
    item = update.message.text
    data = models.get_contact(item, cursor)
    data_to_str = '\n'.join(' | '.join(map(str, x)) for x in data)
    context.bot.send_message(update.effective_chat.id,
                             f"{data_to_str}")


def add(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "Введите имя нового сотрудника")
    return 1


def add_first_name(update, context):
    first_name = update.message.text
    add_storage.append(first_name)
    context.bot.send_message(update.effective_chat.id,
                             f"Введите фамилию нового сотрудника")
    return 2


def add_last_name(update, context):
    last_name = update.message.text
    add_storage.append(last_name)
    context.bot.send_message(update.effective_chat.id,
                             f"Введите номер телефона нового сотрудника")
    return 3


def add_phone_number(update, context):
    phone_number = update.message.text
    add_storage.append(phone_number)
    context.bot.send_message(update.effective_chat.id,
                             f"Введите должность нового сотрудника")
    return 4


def add_held_post(update, context):
    held_post = update.message.text
    add_storage.append(held_post)
    context.bot.send_message(update.effective_chat.id,
                             f"Введите примечание/описание нового сотрудника")
    return 5


def add_note(update, context):
    note = update.message.text
    add_storage.append(note)
    models.add_contact(add_storage, connection, cursor)
    context.bot.send_message(update.effective_chat.id,
                             f"Запись о новом сотруднике добавлена в БД\n"
                             f"Для выхода нажмите или введите /stop")
    add_storage.clear()


def stop(update, context):
    context.bot.send_message(update.effective_chat.id, 'Процесс обращения к БД прерван')
    return ConversationHandler.END


def delete(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите id контакта для удаления')
    return 1


def delete_contact(update, context):
    id_contact = update.message.text
    msg = models.delete(id_contact, connection, cursor)
    context.bot.send_message(update.effective_chat.id, msg)


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    find_handler = ConversationHandler(
        entry_points=[CommandHandler('find', find)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, find_context)],
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    add_handler = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /add.
        entry_points=[CommandHandler('add', add)],

        # Состояние внутри диалога.
        # Вариант с 5 обработчиками, фильтрующими текстовые сообщения.
        states={
            # Функция считывает ответ на первый вопрос и задаёт второй и т.д.
            1: [MessageHandler(Filters.text & ~Filters.command, add_first_name)],
            2: [MessageHandler(Filters.text & ~Filters.command, add_last_name)],
            3: [MessageHandler(Filters.text & ~Filters.command, add_phone_number)],
            4: [MessageHandler(Filters.text & ~Filters.command, add_held_post)],
            5: [MessageHandler(Filters.text & ~Filters.command, add_note)],
        },
        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )

    delete_handler = ConversationHandler(
        entry_points=[CommandHandler('delete', delete)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, delete_contact)],
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('show_all', show_all))
    dispatcher.add_handler(find_handler)
    dispatcher.add_handler(add_handler)
    dispatcher.add_handler(delete_handler)
    updater.start_polling()
    updater.idle()
    connection.close()


if __name__ == '__main__':
    main()
