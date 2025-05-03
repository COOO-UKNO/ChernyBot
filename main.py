from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import parsing

BOT_TOKEN = "7245269020:AAG1BQPGx3Am0BUc4Xiyzihr-DpmqPo0CkA"

start_keyboard = [
        [InlineKeyboardButton(str(parsing.voz("btn_hangout")[0]), callback_data="walking")],
        [InlineKeyboardButton("sadad", callback_data="ivents")]
    ]
zone_keyboard = [
            [InlineKeyboardButton(str(parsing.voz("btn_zonaMountain")[0]), callback_data="zone1")],
            [InlineKeyboardButton(str(parsing.voz("btn_zoneWhater")[0]), callback_data="zone2")],
            [InlineKeyboardButton(str(parsing.voz("btn_zoneSmallScene")[0]), callback_data="zone3")],
            [InlineKeyboardButton(str(parsing.voz("btn_zoneBigScene")[0]), callback_data="zone4")],
            [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back")]
        ]
place1_keyboard = [
            [InlineKeyboardButton("Место 1", callback_data="place11")],
            [InlineKeyboardButton("Место 2", callback_data="place12")],
            [InlineKeyboardButton("Место 3", callback_data="place13")],
            [InlineKeyboardButton("Назад", callback_data="back_zone")]
        ]
place2_keyboard = [
            [InlineKeyboardButton("Место 1", callback_data="place21")],
            [InlineKeyboardButton("Место 2", callback_data="place22")],
            [InlineKeyboardButton("Место 3", callback_data="place23")],
            [InlineKeyboardButton("Назад", callback_data="back_zone")]
        ]
place3_keyboard = [
            [InlineKeyboardButton("Место 1", callback_data="place31")],
            [InlineKeyboardButton("Место 2", callback_data="place32")],
            [InlineKeyboardButton("Место 3", callback_data="place33")],
            [InlineKeyboardButton("Назад", callback_data="back_zone")]
        ]
place4_keyboard = [
            [InlineKeyboardButton("Место 1", callback_data="place41")],
            [InlineKeyboardButton("Место 2", callback_data="place42")],
            [InlineKeyboardButton("Место 3", callback_data="place43")],
            [InlineKeyboardButton("Назад", callback_data="back_zone")]
        ]
ivents_keyboard = [
            [InlineKeyboardButton("Рассписание мастерских", callback_data="masterclass")],
            [InlineKeyboardButton("Ближайшие события", callback_data="fast_ivents")],
            [InlineKeyboardButton("Назад", callback_data="back")]
        ]
masterclass_keyboard = [
            [InlineKeyboardButton("МК 2", callback_data="mk1")],
            [InlineKeyboardButton("МК 1", callback_data="mk2")],
            [InlineKeyboardButton("МК 3", callback_data="mk3")],
            [InlineKeyboardButton("Назад", callback_data="back_ivents")]
        ]
fast_ivents_keyboard = [
            [InlineKeyboardButton("Событие 1", callback_data="ivent1")],
            [InlineKeyboardButton("Событие 2", callback_data="ivent2")],
            [InlineKeyboardButton("Событие 3", callback_data="ivent3")],
            [InlineKeyboardButton("Назад", callback_data="back_ivents")]
        ]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = start_keyboard
    await update.message.reply_text(
        "Главное меню",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "walking":
        new_keyboard = zone_keyboard
        await query.edit_message_text(
            text="Зоны",
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "zone1":
        new_keyboard = place1_keyboard
        await query.edit_message_text(
            text="Зона 1",
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "zone2":
        new_keyboard = place2_keyboard
        await query.edit_message_text(
            text="Зона 2",
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "zone3":
        new_keyboard = place3_keyboard
        await query.edit_message_text(
            text="Зона 3",
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "zone4":
        new_keyboard = place4_keyboard
        await query.edit_message_text(
            text="Зона 4",
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "ivents":
        new_keyboard = ivents_keyboard
        await query.edit_message_text(
            text="События",
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "masterclass":
        new_keyboard = masterclass_keyboard
        await query.edit_message_text(
            text="Мастеркласс",
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "fast_ivents":
        new_keyboard = fast_ivents_keyboard
        await query.edit_message_text(
            text="Ближайшие события",
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "back":
        new_keyboard = start_keyboard
        await query.edit_message_text(
            text="Главное меню",
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "back_zone":
        new_keyboard = zone_keyboard
        await query.edit_message_text(
            text="Зоны",
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "back_ivents":
        new_keyboard = ivents_keyboard
        await query.edit_message_text(
            text="События",
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_button))
    app.run_polling()

if __name__ == "__main__":
    main()

