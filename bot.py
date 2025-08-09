import os
import asyncio
import logging  
from aiogram import Bot, Dispatcher, types 
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(  
    level=logging.INFO,  
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  
    handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()]  
)  
logger = logging.getLogger(__name__) 


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)  

@dp.message_handler(commands=["start"])  
async def start_command(message: types.Message):  
    user_id = message.from_user.id  
    user_name = message.from_user.first_name  
    await message.reply(f"Привет!\nИспользуй /help для справки")  
    logger.info(f"Пользователь {user_id} ({user_name}) запустил /start")   

@dp.message_handler(commands=["help"])  
async def help_command(message: types.Message):  
    user_id = message.from_user.id 
    user_name = message.from_user.first_name   
    await message.reply("/about — показать описание бота\n/help — показать это сообщение")  
    logger.info(f"Пользователь {user_id} ({user_name}) запросил /help")  

@dp.message_handler(commands=["about"])  
async def about_command(message: types.Message):  
    user_id = message.from_user.id 
    user_name = message.from_user.first_name   
    await message.reply("Тренировочный бот")  
    logger.info(f"Пользователь {user_id} ({user_name}) запросил /about")  

@dp.message_handler()  
async def echo_message(message: types.Message):  
    user_id = message.from_user.id 
    user_name = message.from_user.first_name  
    text = message.text  
    await message.reply(f"Ты сказал: {text}")  
    logger.info(f"Пользователь {user_id} ({user_name}) отправил сообщение: {text}")  


async def main():  
    print("Бот запущен!")  
    await dp.start_polling()  

if __name__ == "__main__":  
    asyncio.run(main())  