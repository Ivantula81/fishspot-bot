from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart
import asyncio

BOT_TOKEN = "8055314263:AAF4gB8dO5hTZeIhXYMeHAbLrY0cY50Q_ag"

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

def main_menu_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="🛒 Купить", url="https://t.me/ikrabeogradbot/shop")
    kb.button(text="📄 Прайс", callback_data="price")
    kb.button(text="👤 Менеджер", url="https://t.me/Nata_beo")
    kb.button(text="🚚 Доставка", callback_data="delivery")
    kb.button(text="👥 Группа", url="https://t.me/+6EbDpQhrRCI3NTc0")
    kb.button(text="📸 Instagram", url="https://www.instagram.com/fishspot.bg/")
    kb.adjust(3, 3)
    return kb.as_markup()

@dp.message(CommandStart())
async def start(message: Message):
    photo = FSInputFile("нерка.jpg")
    caption = """
<b>🐿 Дикая красная рыба – свежемороженая, целая, потрошённая, без головы!</b>

🔥 Прямо с Камчатки – 100% натуральный продукт!

<b>В наличии:</b>
✅ Нерка – насыщенный вкус, богатый Омега-3
✅ Кижуч – сочная и ароматная, отлично подходит для запекания, засолки и копчения
✅ Кета – диетическая, с плотной текстурой и мягким вкусом
✅ Горбуша – нежная и лёгкая, универсальный вариант для любых блюд

🐟 Свежемороженая, целая, потрошённая, без головы – удобно для приготовления!

🌿 Без добавок и консервантов – только дикая рыба высшего качества.
🚛 Доставка по Белграду и Нови-Саду.
"""
    await message.answer_photo(photo=photo, caption=caption, reply_markup=main_menu_kb())

@dp.message(lambda message: message.text != "/start")
async def fallback(message: Message):
    await message.answer(
        """
🤖 <b>Я ещё не научился разговаривать с людьми (но очень стараюсь!)</b>

Чтобы задать вопрос — нажмите кнопку <b>👤 Менеджер</b> ниже ⬇️
А если хотите посмотреть ассортимент или прайс — они тоже под рукой!
""",
        reply_markup=main_menu_kb()
    )

@dp.callback_query(lambda c: c.data == "price")
async def send_price(callback_query: CallbackQuery):
    await callback_query.message.answer("""
🍣 <b>Икра:</b>
🔹 Икра горбуши
▪️ 250 г – 5 500 RSD
▪️ 500 г – 11 000 RSD

🔹 Икра кеты
▪️ 250 г – 6 000 RSD
▪️ 500 г – 12 000 RSD

🔥 <b>Копченая рыба:</b>
🐟 Нерка х/к пласт – 5 000 RSD/kg
🐟 Кижуч х/к пласт – 4 500 RSD/kg
🐟 Скумбрия х/к – 2 700 RSD/kg
🐟 Форель х/к (пастромка) – 2 700 RSD/kg
🐟 Балык форели слабосоленный – 3 500 RSD/kg
🐟 Филе сельди тихоокеанской – 1 500 RSD/kg

🦐 <b>Морепродукты:</b>
🦐 Лангустины Vannamei – 2 500 RSD/kg

❄️ <b>Свежемороженая рыба (Камчатка):</b>
🐟 Горбуша дикая – 1 500 RSD/kg
🐟 Кета дикая – 1 900 RSD/kg
🐟 Кижуч дикий – 2 400 RSD/kg

🥩 <b>Стейки:</b>
🥩 Стейки дикой нерки – 4 200 RSD/kg
🥩 Стейки дикой кеты – 2 300 RSD/kg
🥩 Стейки дикого кижуча – 2 900 RSD/kg

🐟 <b>Дикая красная рыба – свежемороженая, целая, потрошённая, без головы!</b>

🔥 Прямо с Камчатки – 100% натуральный продукт!

✅ Нерка – насыщенный вкус, богатый Омега-3
✅ Кижуч – сочная и ароматная, отлично подходит для запекания, засолки и копчения
✅ Кета – диетическая, с плотной текстурой и мягким вкусом
✅ Горбуша – нежная и лёгкая, универсальный вариант для любых блюд

🌿 Без добавок и консервантов – только дикая рыба высшего качества.
🚛 Доставка по Белграду и Нови-Саду.
""", reply_markup=main_menu_kb())
    await callback_query.answer()

@dp.callback_query(lambda c: c.data == "delivery")
async def send_delivery_info(callback_query: CallbackQuery):
    await callback_query.message.answer(
        """
🚚 <b>Условия доставки</b>

📢 Новинка! Теперь доставляем не только по Белграду, но и в Нови-Сад (и другие города Сербии по договорённости).

🔸 По Белграду:
Доставка каждый день с 17:00 до 21:00 (кроме воскресенья)

🔸 В Нови-Сад:
Доставка — каждый четверг

✅ Доставка <b>бесплатная</b> — вы платите только за продукт. 
Мы сами привозим — в термоупаковке, без посредников.
""", reply_markup=main_menu_kb())
    await callback_query.answer()

@dp.callback_query(lambda c: c.data == "back")
async def go_back(callback_query: CallbackQuery):
    await callback_query.message.answer("📍 Возвращаемся в меню:", reply_markup=main_menu_kb())
    await callback_query.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
