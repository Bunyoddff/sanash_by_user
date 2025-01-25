from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext,Filters,CallbackQueryHandler
import os
from telegram import Update,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup,Bot

sana_like={'like':0, 'dislike':0}

# Get the bot token from environment variables
TOKEN = os.getenv('TOKEN')

# def info(update: Update, context):
#     inline_button = InlineKeyboardButton(text="Siz yuborgan rasm",callback_data=1)
#     inline_keyboard = InlineKeyboardMarkup([[inline_button,inline_button]])
    
#     update.message.reply_text('nima gap',reply_markup=inline_keyboard)

def bronnarsa_qaytaradi(update: Update, context: CallbackContext):
    ismi = update.message.from_user.full_name
    update.message.reply_text(ismi)
def rasm_qaytar(update:Update, context:CallbackContext):

    rasm_manzili=update.message.photo[-1].file_id
    tugma1 = InlineKeyboardButton(text=f"Do you like👍{sana_like['like']}",callback_data='👍')
    tugma2 = InlineKeyboardButton(text=f"Or dislike 👎 {sana_like['dislike']}",callback_data='👎')
    inline_keyboard = InlineKeyboardMarkup([[tugma1,tugma2]])
    update.message.reply_photo(photo=rasm_manzili,reply_markup=inline_keyboard)
def tugama_bosilsa(update:Update, context:CallbackContext):
    query_malumot = update.callback_query
    query_malumot.answer()
    if query_malumot.data == '👍':
        sana_like["like"] += 1
        
    elif query_malumot.data == '👎':
        sana_like["dislike"] += 1
    
    tugma1 = InlineKeyboardButton(text=f"Do you like👍{sana_like['like']}",callback_data='👍')
    tugma2 = InlineKeyboardButton(text=f"Or dislike 👎 {sana_like['dislike']}",callback_data='👎')
    inline_keyboard = InlineKeyboardMarkup([[tugma1,tugma2]])
    query_malumot.edit_message_reply_markup(reply_markup=inline_keyboard)





# def likedislike(update: Update, context: CallbackContext):
#     global like_sanagich,dislike_sanagich
#     if update.message.text=='👎':
#         dislike_sanagich+=1
#         update.message.reply_text(f'Dislekelar soni {dislike_sanagich} ga teng,Likelar soni {like_sanagich} ga teng')
#     if update.message.text=='👍':
#         like_sanagich+=1
#         update.message.reply_text(f'Dislekelar soni {dislike_sanagich} ga teng,Likelar soni {like_sanagich} ga teng')
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add handlers
dispatcher.add_handler(CommandHandler('start', bronnarsa_qaytaradi))
#dispatcher.add_handler(CommandHandler('info',info))
dispatcher.add_handler(MessageHandler(Filters.photo,rasm_qaytar))
dispatcher.add_handler(CallbackQueryHandler(tugama_bosilsa))

# Start the bot
updater.start_polling()

# Run the bot until you stop it
updater.idle()
