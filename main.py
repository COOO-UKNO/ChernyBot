from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import parsing

BOT_TOKEN = "7245269020:AAG1BQPGx3Am0BUc4Xiyzihr-DpmqPo0CkA"



start_keyboard = [
        [InlineKeyboardButton(str(parsing.voz("btn_hangout")[0]), callback_data="walking")],
        [InlineKeyboardButton("sadad", callback_data="ivents")],
        [InlineKeyboardButton(str(parsing.voz("btn_rez")[0]), callback_data="residents")]
    ]
residents_keyboard = [
        [InlineKeyboardButton(str(parsing.voz("btn_yrok")[0]), callback_data="rez1")],
        [InlineKeyboardButton(str(parsing.voz("btn_syvlav")[0]), callback_data="rez2")],
        [InlineKeyboardButton(str(parsing.voz("btn_myznal")[0]), callback_data="rez3")],
        [InlineKeyboardButton(str(parsing.voz("btn_gon")[0]), callback_data="rez4")],
        [InlineKeyboardButton(str(parsing.voz("btn_tkach")[0]), callback_data="rez5")],
        [InlineKeyboardButton(str(parsing.voz("btn_yralmerch")[0]), callback_data="rez6")],
        [InlineKeyboardButton(str(parsing.voz("btn_kyky")[0]), callback_data="rez7")],
        [InlineKeyboardButton(str(parsing.voz("btn_masttrav")[0]), callback_data="rez8")],
        [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back")]
]
zone_keyboard = [
            [InlineKeyboardButton(str(parsing.voz("btn_zonaMountain")[0]), callback_data="zone1")],
            [InlineKeyboardButton(str(parsing.voz("btn_zoneWhater")[0]), callback_data="zone2")],
            [InlineKeyboardButton(str(parsing.voz("btn_zoneSmallScene")[0]), callback_data="zone3")],
            [InlineKeyboardButton(str(parsing.voz("btn_zoneBigScene")[0]), callback_data="zone4")],
            [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back")]
        ]
place1_keyboard = [
            [InlineKeyboardButton(str(parsing.voz("btn_smotr")[0]), callback_data="place11")],
            [InlineKeyboardButton(str(parsing.voz("btn_artMore")[0]), callback_data="place12")],
            [InlineKeyboardButton(str(parsing.voz("btn_cherch")[0]), callback_data="place13")],
            [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone")]
        ]
place2_keyboard = [
            [InlineKeyboardButton(str(parsing.voz("btn_artKapla")[0]), callback_data="place21")],
            [InlineKeyboardButton(str(parsing.voz("btn_artLodka")[0]), callback_data="place22")],
            [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone")]
        ]
place3_keyboard = [
            [InlineKeyboardButton(str(parsing.voz("btn_skam")[0]), callback_data="place31")],
            [InlineKeyboardButton(str(parsing.voz("btn_gateway")[0]), callback_data="place32")],
            [InlineKeyboardButton(str(parsing.voz("btn_artShe")[0]), callback_data="place33")],
            [InlineKeyboardButton(str(parsing.voz("btn_artFromEarth")[0]), callback_data="place34")],
            [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone")]
        ]
place4_keyboard = [
            [InlineKeyboardButton(str(parsing.voz("btn_stena")[0]), callback_data="place41")],
            [InlineKeyboardButton(str(parsing.voz("btn_cex")[0]), callback_data="place42")],
            [InlineKeyboardButton(str(parsing.voz("btn_artDomiki")[0]), callback_data="place43")],
            [InlineKeyboardButton(str(parsing.voz("btn_nal")[0]), callback_data="place44")],
            [InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone")]
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
    keyboard = [[InlineKeyboardButton(str(parsing.voz("btn_start")[0]), callback_data="start")]]
    await update.message.reply_text(
        text="Найди меня ищи ищи",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "start":
        new_keyboard = start_keyboard
        await query.edit_message_text(
            text="Главное меню",
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

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

    if query.data == "residents":
        new_keyboard = residents_keyboard
        await query.edit_message_text(
            text=str(parsing.voz("btn_rez")[0]),
            reply_markup = InlineKeyboardMarkup(new_keyboard)
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
    if query.data == "back_zone1":
        new_keyboard = place1_keyboard
        await query.edit_message_text(
            text="Зона 1",
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "back_zone2":
        new_keyboard = place2_keyboard
        await query.edit_message_text(
            text="Зона 2",
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "back_zone3":
        new_keyboard = place3_keyboard
        await query.edit_message_text(
            text="Зона 3",
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "back_zone4":
        new_keyboard = place4_keyboard
        await query.edit_message_text(
            text="Зона 4",
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "back_rez":
        new_keyboard = residents_keyboard
        await query.edit_message_text(
            text="Резиденты",
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "place11":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone1")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_smotr")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place12":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone1")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_artMore")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place13":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone1")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_cherch")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "place21":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone2")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_artKapla")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place22":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone2")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_artLodka")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "place31":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone3")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_skam")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place32":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone3")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_gateway")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place33":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone3")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_artShe")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place34":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone3")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_artFromEarth")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "place41":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone4")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_stena")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place42":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone4")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_cex")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place43":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone4")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_artDomiki")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "place44":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_zone4")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_nal")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )

    if query.data == "rez1":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_rez")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_yrok")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "rez2":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_rez")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_syvlav")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "rez3":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_rez")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_myznal")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "rez4":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_rez")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_gon")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "rez5":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_rez")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_tkach")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "rez6":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_rez")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_yralmerch")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "rez7":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_rez")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_kyky")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )
    if query.data == "rez8":
        new_keyboard =[[InlineKeyboardButton(str(parsing.voz("btn_back")[0]), callback_data="back_rez")]]
        await query.edit_message_text(
            text=str(parsing.voz("btn_masttrav")[1]),
            reply_markup=InlineKeyboardMarkup(new_keyboard)
        )






def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_button))
    app.run_polling()

if __name__ == "__main__":
    main()

