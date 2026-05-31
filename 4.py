import telebot
from telebot import types
import os
TOKEN = os.environ.get('TELEGRAM_TOKEN', '8835571838:AAGwpwKKJjV2scQfnflSTn3W1-xBSIK1ra8')
bot = telebot.TeleBot('8835571838:AAGwpwKKJjV2scQfnflSTn3W1-xBSIK1ra8')

# ============ КЛАВИАТУРЫ ============

def create_main_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton('😰 Тревожность', callback_data='anxiety'),
        types.InlineKeyboardButton('👊 Буллинг', callback_data='bull'),
        types.InlineKeyboardButton('🏠 Отношения в семье', callback_data='family'),
        types.InlineKeyboardButton('📚 Учеба и экзамены', callback_data='exam'),
        types.InlineKeyboardButton('🆘 Помощь', callback_data='help')
    )
    return keyboard

def create_anxiety_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton('🌬 Техники дыхания', callback_data='a1'),
        types.InlineKeyboardButton('🧠 Когнитивные упражнения', callback_data='a2'),
        types.InlineKeyboardButton('📓 Дневник тревог', callback_data='a3'),
        types.InlineKeyboardButton('📞 Обратиться за помощью', callback_data='a4'),
        types.InlineKeyboardButton('◀️ Назад', callback_data='back')
    )
    return keyboard

def create_exam_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton('⏰ Организация времени', callback_data='d1'),
        types.InlineKeyboardButton('🚀 Борьба с прокрастинацией', callback_data='d2'),
        types.InlineKeyboardButton('📖 Подготовка к экзаменам', callback_data='d3'),
        types.InlineKeyboardButton('😌 Стресс-менеджмент', callback_data='d4'),
        types.InlineKeyboardButton('◀️ Назад', callback_data='back')
    )
    return keyboard

def create_bull_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton('❓ Что такое буллинг', callback_data='b1'),
        types.InlineKeyboardButton('🛡 Как себя защитить', callback_data='b2'),
        types.InlineKeyboardButton('🤝 Поддержка друзей', callback_data='b3'),
        types.InlineKeyboardButton('◀️ Назад', callback_data='back')
    )
    return keyboard

def create_family_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton('💔 Конфликты с родителями', callback_data='c1'),
        types.InlineKeyboardButton('👫 Общение с братьями/сестрами', callback_data='c2'),
        types.InlineKeyboardButton('📋 Семейные правила', callback_data='c3'),
        types.InlineKeyboardButton('📞 Обратиться за помощью', callback_data='a4'),
        types.InlineKeyboardButton('◀️ Назад', callback_data='back')
    )
    return keyboard

def create_help_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton('📞 Телефоны доверия', callback_data='h1'),
        types.InlineKeyboardButton('💬 Онлайн-чаты', callback_data='h2'),
        types.InlineKeyboardButton('📍 Психологи в твоем городе', callback_data='h3'),
        types.InlineKeyboardButton('◀️ Назад', callback_data='back')
    )
    return keyboard

# ============ ОСНОВНОЙ ОБРАБОТЧИК ============

@bot.message_handler(commands=['start'])
def main(message):
    keyboard = create_main_keyboard()
    bot.send_message(
        message.chat.id, 
        '🌟 Привет! Я — твой виртуальный помощник.\n\nВыбери тему, которая тебя волнует 👇',
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    bot.answer_callback_query(call.id)
    
    # ===== ГЛАВНОЕ МЕНЮ =====
    if call.data == 'anxiety':
        keyboard = create_anxiety_keyboard()
        bot.edit_message_text(
            chat_id=call.message.chat.id, 
            message_id=call.message.message_id,
            text="😰 **Тревожность**\n\nВыбери, что тебя интересует:",
            reply_markup=keyboard,
            parse_mode='Markdown'
        )
    
    elif call.data == 'bull':
        keyboard = create_bull_keyboard()
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="👊 **Буллинг**\n\nВыбери тему:",
            reply_markup=keyboard,
            parse_mode='Markdown'
        )
    
    elif call.data == 'family':
        keyboard = create_family_keyboard()
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="🏠 **Отношения в семье**\n\nВыбери тему:",
            reply_markup=keyboard,
            parse_mode='Markdown'
        )
    
    elif call.data == 'exam':
        keyboard = create_exam_keyboard()
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="📚 **Учеба и экзамены**\n\nВыбери тему:",
            reply_markup=keyboard,
            parse_mode='Markdown'
        )
    
    elif call.data == 'help':
        keyboard = create_help_keyboard()
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="🆘 **Помощь**\n\nВыбери нужный вариант:",
            reply_markup=keyboard,
            parse_mode='Markdown'
        )
    
    elif call.data == 'back':
        keyboard = create_main_keyboard()
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="🌟 Главное меню\n\nВыбери тему:",
            reply_markup=keyboard
        )
    
    # ===== ТРЕВОЖНОСТЬ =====
    elif call.data == 'a1':
        bot.send_message(
            call.message.chat.id,
            "🌬 **Техники дыхания**\n\n"
            "• Вдох на 4 сек → задержка 4 сек → выдох 4 сек → задержка 4 сек\n"
            "• Повтори 5-10 раз",
            parse_mode='Markdown'
        )
    
    elif call.data == 'a2':
        bot.send_message(
            call.message.chat.id,
            "🧠 **Когнитивные упражнения**\n\n"
            "• Назови 5 предметов вокруг\n"
            "• Назови 4 звука, которые слышишь\n"
            "• Назови 3 ощущения в теле",
            parse_mode='Markdown'
        )
    
    elif call.data == 'a3':
        bot.send_message(
            call.message.chat.id,
            "📓 **Дневник тревог**\n\n"
            "Записывай:\n"
            "1. Что случилось?\n"
            "2. Что я подумал?\n"
            "3. Оценка тревоги (1-10)",
            parse_mode='Markdown'
        )
    
    elif call.data == 'a4':
        bot.send_message(
            call.message.chat.id,
            "📞 **Телефон доверия:** 8-800-2000-122\n\n"
            "Звонок бесплатный и анонимный. Ты не один! 💙"
        )
    
    # ===== БУЛЛИНГ =====
    elif call.data == 'b1':
        bot.send_message(
            call.message.chat.id,
            "❓ **Буллинг** - это агрессия, которая может быть:\n"
            "• Физической (удары, толчки)\n"
            "• Словесной (обзывательства)\n"
            "• Социальной (игнорирование)\n"
            "⚠️ Это не твоя вина!"
        )
    
    elif call.data == 'b2':
        bot.send_message(
            call.message.chat.id,
            "🛡 **Как защитить себя:**\n"
            "• Не показывай страх\n"
            "• Сохраняй доказательства\n"
            "• Обратись к взрослым\n"
            "📞 Телефон доверия: 8-800-2000-122"
        )
    
    elif call.data == 'b3':
        bot.send_message(
            call.message.chat.id,
            "🤝 **Поддержи друга:**\n"
            "• Выслушай\n"
            "• Скажи «Ты не один»\n"
            "• Помоги обратиться за помощью"
        )
    
    # ===== СЕМЬЯ =====
    elif call.data == 'c1':
        bot.send_message(
            call.message.chat.id,
            "💔 **Совет:** Говори о чувствах через «Я».\n"
            "Пример: «Я расстраиваюсь, когда на меня кричат»"
        )
    
    elif call.data == 'c2':
        bot.send_message(
            call.message.chat.id,
            "👫 **Совет:** Найди общее хобби с братом/сестрой.\n"
            "Это сближает и уменьшает конфликты!"
        )
    
    elif call.data == 'c3':
        bot.send_message(
            call.message.chat.id,
            "📋 **Совет:** Предложи устроить семейный совет.\n"
            "Вместе обсудите правила и договоренности."
        )
    
    # ===== УЧЕБА =====
    elif call.data == 'd1':
        bot.send_message(
            call.message.chat.id,
            "⏰ **Метод «Помидора»:** 25 мин работа → 5 мин отдых.\n"
            "Попробуй прямо сейчас!"
        )
    
    elif call.data == 'd2':
        bot.send_message(
            call.message.chat.id,
            "🚀 **Начни с 5 минут.**\n"
            "Сделай маленький шаг — дальше будет легче!"
        )
    
    elif call.data == 'd3':
        bot.send_message(
            call.message.chat.id,
            "📖 **Совет:** Повторяй материал через день.\n"
            "Выспись перед экзаменом — это важно!"
        )
    
    elif call.data == 'd4':
        bot.send_message(
            call.message.chat.id,
            "😌 **Дыши глубоко** и не сравнивай себя с другими.\n"
            "Ты справишься! 💪"
        )
    
    # ===== ПОМОЩЬ =====
    elif call.data == 'h1':
        bot.send_message(
            call.message.chat.id,
            "📞 **Детский телефон доверия:** 8-800-2000-122\n"
            "🆘 **МЧС:** 8-800-775-17-17\n"
            "Круглосуточно, бесплатно, анонимно."
        )
    
    elif call.data == 'h2':
        bot.send_message(
            call.message.chat.id,
            "💬 **Онлайн-чаты:**\n"
            "• Детский телефон доверия (сайт)\n"
            "• Помощь рядом\n"
            "• Твой текст"
        )
    
    elif call.data == 'h3':
        bot.send_message(
            call.message.chat.id,
            "📍 **Бесплатно:** школьный психолог или центр психологической помощи по ОМС."
        )

# ============ ЗАПУСК ============
print("🤖 Бот запущен!")
bot.infinity_polling()