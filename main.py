#ГОВНОКОД
#КОМЕНТАРИИ БЕСПОЛЕЗНЫ
#С ЛЮБОВЬЮ - ВОРОН

from Data import Tema,Users,Commands
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message,KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import*
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
from random import *
from config import token
print(f'Бот запущен|{token}')
bot = Bot(token)
dp = Dispatcher()

#получение ID юзера
def uid(auth):
    id = ''
    for i in str(auth):
        id = id + i
        if i == ' ':
            break
    cid = id.replace("id=", '')
    return cid

#получение юзернейма
def uun(auth):
    un = ''
    sp = 0
    for i in str(auth):
        if i ==' ':
            sp+=1
        elif sp == 4 and i!=' ':
            un = un + i
        elif sp == 5:
            break
    cun = un.replace("username=",'')
    cun = cun.replace("'",'')
    return cun


#Стартовое сообщение
@dp.message(Command("start"))
async def cmd_special_buttons(message: Message):
    User = Users.User(int(uid(message.from_user)), 0, str(uun(message.from_user)), False, "tg", 0)
    User.add(Show=True)
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Биохим"),
    )
    builder.row(
        KeyboardButton(text="Физмат"),
    )
    builder.row(
        KeyboardButton(text="Соцэконом"),
    )
    await message.answer('Здравствуйте, чат-бот сейчас еще может содержать ошибки\nЕсли вы столкнулись с ошибкой, напишите о ней на почту\ndumai_vanya_dumai@mail.ru\nСпасибо за понимание\n~Команда "Думай, Ваня, Думай"')
    await message.answer('Это бот, созданный командой \n"Думай, Ваня, думай"\nВыберите ваш учебный профиль', reply_markup=builder.as_markup(resize_keyboard=True))
    print(f'user:{uun(message.from_user)}|инициация бота')
@dp.message((F.text.lower() == "назад"))
async def cmd_special_buttons(message: Message):
    User = Users.User(int(uid(message.from_user)), 0, str(uun(message.from_user)), False, "tg", 0)
    User.add(Show=True)
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Биохим"),
    )
    builder.row(
        KeyboardButton(text="Физмат"),
    )
    builder.row(
        KeyboardButton(text="Соцэконом"),
    )
    await message.answer('Выберите ваш учебный профиль', reply_markup=builder.as_markup(resize_keyboard=True))
    print(f'user:{uun(message.from_user)}|перевыбор профиля')

#Выбор профиля
@dp.message((F.text.lower()=="физмат"))
async def cmd_start(message: Message):
    id = int(uid(message.from_user))
    us = (Commands.getuser(id)).name
    Users.User(id, prfl=1,name=us).add()
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Ищу"),
    )
    builder.row(
        KeyboardButton(text="Задаю"),
    )
    await message.answer('Вы - физмат\nВыберете, задаете вы тему или ищите',reply_markup=builder.as_markup(resize_keyboard=True))
    print(f'user:{us}|пользователь выбрал профиль "физмат"')
@dp.message((F.text.lower() == "биохим"))
async def cmd_special_buttons(message: Message):
    id = int(uid(message.from_user))
    us = (Commands.getuser(id)).name
    Users.User(id, prfl=2,name=us).add()
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Ищу"),
    )
    builder.row(
        KeyboardButton(text="Задаю"),
    )
    builder.row(
        KeyboardButton(text="Назад"),
        KeyboardButton(text="Справка")
    )
    await message.answer('Вы - биохим\nВыберете, задаете вы тему или ищите',reply_markup=builder.as_markup(resize_keyboard=True))
    print(f'user:{us}|пользователь выбрал профиль "биохим"')
@dp.message((F.text.lower() == "соцэконом"))
async def cmd_special_buttons(message: Message):
    id = int(uid(message.from_user))
    us = (Commands.getuser(id)).name
    Users.User(id, prfl=3,name=us).add()
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Ищу"),
    )
    builder.row(
        KeyboardButton(text="Задаю"),
    )
    builder.row(
        KeyboardButton(text="Назад"),
        KeyboardButton(text="Справка")
    )
    await message.answer('Вы - соцэконом\nВыберете, задаете вы тему или ищите',reply_markup=builder.as_markup(resize_keyboard=True))
    print(f'user:{us}|пользователь выбрал профиль "соцэконом"')



#Задаете/Ищите
@dp.message((F.text.lower() == "задаю"))
async def without_puree(message: Message):
    await message.reply('Сейчас добавление тем доступно только проверенным пользователям. \nНапишите пароль, выданный нашей командой,  для авторизации ')
    id = int(uid(message.from_user))
    pr = (Commands.getuser(id)).prfl
    us = (Commands.getuser(id)).name
    Users.User(id, prfl=pr, name=us, cash=6).add(Show=True)
    print(f'user:{us}|пользователь выбрал роль задающего')

@dp.message((F.text.lower() == "ищу"))
async def cmd_special_buttons(message: Message):
    id = int(uid(message.from_user))
    us = (Commands.getuser(id)).name
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Тeмa"),
    )
    builder.row(
        KeyboardButton(text="Удалить из избранного"),
        KeyboardButton(text="Больше не решаю")
    )
    builder.row(
        KeyboardButton(text="Мои темы"),
        KeyboardButton(text="Информация по теме")
    )
    builder.row(
        KeyboardButton(text="Назад"),
        KeyboardButton(text="Справка")
    )

    await message.answer(
        "Выберите действие:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )
    print(f'user:{us}|пользователь выбрал роль ищущего')



#Справка
@dp.message(F.text.lower() == "справка")
async def with_puree(message: Message):
    id = int(uid(message.from_user))
    us = (Commands.getuser(id)).name
    mess1 = '''Приветствую. Вы вызвали справку по работе бота!

Для тех, кто ищет тему:
- тема - команда выдает новую тему.
    - избранное - команда добавляет тему в избранное;
    - буду решать - команда добавляет вас в список тех, кто работает над решением к теме;
- удалить из избранного - команда удаляет тему из избранного; 
- больше не решаю - команда удаляет вас из списка тех, кто работает над решением к теме
- мои темы - команда выдает список написанных вами тем, тем, добавленных в избранное и тем, которые вы решаете;
- информация по теме- команда позволяет узнать точные данные о теме;
- назад - команда возвращает к меню выбора профиля;

Для тех, кто предлагает тему:
- предложить - команда позволяет записать тему в базу тем;
- удалить - команда удаляет ваше авторство из темы;
- мои темы - команда выдает список написанных вами тем  тем, добавленных в избранное и тем, которые вы решаете;
- информация по теме - команда позволяет узнать точные данные о теме;
- назад - команда возвращает к меню выбора профиля;

dumai_vanya_dumai@mail.ru - почта для обратной связи'''
    await message.reply("Справка по работе бота:\n"+mess1)
    print(f'user:{us}|пользователь вызвал справку')

#Добавление/удаление
@dp.message(F.text.lower() == "записать")
async def without_puree(message: Message):
    await message.reply('Пришлите тему отдельным сообщением в формате \n"Тема; Описание темы"\n\n!!Тема будет записана не анонимно, пользователи будут видеть ваш контакт, как контакт автора темы!! ')
    id = int(uid(message.from_user))
    pr = (Commands.getuser(id)).prfl
    us = (Commands.getuser(id)).name
    Users.User(id, prfl=pr,name=us,cash=1).add(Show=True)
    print(f'user:{us}|пользователь запустил команду добавления темы')
@dp.message(F.text.lower() == "удалить")
async def without_puree(message: Message):
    await message.reply("Напишите название темы, которую надо удалить")
    id = int(uid(message.from_user))
    pr = (Commands.getuser(id)).prfl
    us = (Commands.getuser(id)).name
    Users.User(id, prfl=pr,name=us,cash=2).add(Show=True)
    print(f'user:{us}|пользователь запустил команду удаления темы')
@dp.message(F.text.lower() == "удалить из избранного")
async def without_puree(message: Message):
    await message.reply("Напишите название темы, которую надо удалить из избранного")
    id = int(uid(message.from_user))
    pr = (Commands.getuser(id)).prfl
    us = (Commands.getuser(id)).name
    Users.User(id, prfl=pr,name=us,cash=4).add(Show=True)
    print(f'user:{us}|пользователь запустил команду удаления темы из избранного')
@dp.message(F.text.lower() == "информация по теме")
async def without_puree(message: Message):
    await message.reply("Напишите название темы, информацию о которой хотите узнать")
    id = int(uid(message.from_user))
    pr = (Commands.getuser(id)).prfl
    us = (Commands.getuser(id)).name
    Users.User(id, prfl=pr, name=us, cash=3).add(Show=True)
    print(f'user:{us}|пользователь запустил команду получения информации о теме')
@dp.message(F.text.lower() == "больше не решаю")
async def without_puree(message: Message):
    await message.reply("Напишите название темы, которую вы больше не решаете")
    id = int(uid(message.from_user))
    pr = (Commands.getuser(id)).prfl
    us = (Commands.getuser(id)).name
    Users.User(id, prfl=pr, name=us, cash=5).add(Show=True)
    print(f'user:{us}|пользователь запустил команду удаления из решающих')

@dp.message(F.text.lower() == "мои темы")
async def without_puree(message: Message):
    id = int(uid(message.from_user))
    pr = (Commands.getuser(id)).prfl
    us = (Commands.getuser(id)).name
    mess = 'Список ваших тем\n\nДобавленное вами:'
    F = str((Commands.getUserTemes(id))).replace("'",'').replace('[','').replace(']','').replace(',','').replace('(','-').replace(')','')
    for x in F:
        if x != '-':
            mess = mess+x
        else:
            mess = mess+'\n-'
    mess += '\n\nВ избранном:'
    F = str((Commands.getUserFavs(id))).replace("'", '').replace('[', '').replace(']', '').replace(',', '').replace(
        '(', '-').replace(')', '')
    for x in F:
        if x != '-':
            mess = mess + x
        else:
            mess = mess + '\n-'
    mess += '\n\nЯ решаю:'
    F = str((Commands.getUserDec(id))).replace("'", '').replace('[', '').replace(']', '').replace(',', '').replace(
        '(', '-').replace(')', '')
    for x in F:
        if x != '-':
            mess = mess + x
        else:
            mess = mess + '\n-'
    await message.reply(mess)
    print(f'user:{us}||пользователь запросил "мои темы"')

@dp.message((F.text.lower() == "тeмa"))
async def cmd_start(message: Message):
    id = int(uid(message.from_user))
    us = (Commands.getuser(id)).name
    pr = (Commands.getuser(id)).prfl
    GT = Commands.gettemes(id)
    if len(GT) > 0:
        tem = choice(GT)[0]
        descr = ((str((Commands.gettema(tem)).Description)).replace("[", "").replace("]", "").replace("'", ""))
        if (Commands.gettema(tem)).Author != []:
            us = (int((str((Commands.gettema(tem)).Author)).replace("[", "").replace("]", "").replace("'", "")))
            us = "@" + Commands.getuser(us).name
        else:
            us = ""
        print(f'user:{us}|тема<{tem}>|описание<{descr}>|пользователь запросил тему из базы')
        builder = InlineKeyboardBuilder()
        builder.add(InlineKeyboardButton(
            text="Избранное",
            callback_data="fav"))
        builder.add(InlineKeyboardButton(
            text="Буду решать",
            callback_data="dec"))
        await message.answer(
            f'"{tem}" Автор - {us}\n Описание: {descr}',
            reply_markup=builder.as_markup()
        )
        print(f'"{tem}" Автор - @{us}\n Описание: {descr}')
        Tema.tema(tem,Viewers=[id]).add()
    else:
        print(f'user:{us}|пользователь запросил тему из базы')
        print(f'user:{us}|профиль:{pr}|новых тем нет')
        await message.answer("Новых тем нет, приходите позже")
@dp.callback_query(F.data == "fav")
async def send_random_value(callback: CallbackQuery):
    user = callback.from_user.id
    mess = callback.message.text
    us = (Commands.getuser(user)).name
    tem = ''
    flg = 0
    for i in mess:
        if i =='"':
            flg+=1
        if flg<=2:
            tem+=i
        if flg >=2:
            break
    tem = tem.replace('"','')
    Tema.tema(tem, follower=[user]).add()
    rtem = (Commands.gettema(tem))
    print(f'user:{us}|тема:<{rtem}>|пользователь добавил тему в избранное')
    await callback.answer(
        text="Тема сохранена",
        show_alert=True
    )
@dp.callback_query(F.data == "dec")
async def send_random_value(callback: CallbackQuery):
    user = callback.from_user.id
    mess = callback.message.text
    us = (Commands.getuser(user)).name
    tem = ''
    flg = 0
    for i in mess:
        if i =='"':
            flg+=1
        if flg<=2:
            tem+=i
        if flg >=2:
            break
    tem = tem.replace('"','')
    Tema.tema(tem, Decisive=[user]).add()
    rtem = (Commands.gettema(tem))
    print(f'user:{us}|тема:<{rtem}>|пользователь стал решать тему')
    await callback.answer(
        text="Вы записаны в список тех, кто работает над темой",
        show_alert=True
    )



@dp.message()
async def echo(message: Message):
    id = int(uid(message.from_user))
    status = (Commands.getuser(id)).cash
    pr = (Commands.getuser(id)).prfl
    us = (Commands.getuser(id)).name
    if status == 1:
        temm = ''
        descr = ''
        flg = 0
        for i in message.text:
            if i == ';':
                flg = 1
            if flg == 0:
                temm = temm+i
            if flg ==1:
                descr = descr+i
        (Tema.tema(temm,prfl=pr,Description=[descr[1:]],Author=[id])).add(show=True)#<<<<
        await message.answer('Тема записана!')
        id = int(uid(message.from_user))
        pr = (Commands.getuser(id)).prfl
        us = (Commands.getuser(id)).name
        Users.User(id, prfl=pr, name=us, cash=0).add(Show=True)
        print(str((Commands.getuser(id))))
        print(Commands.getuser(id).name)
        print(f'user:{us}|тема:<{message.text}>|пользователь записал тему|профиль<{pr}>')
    if status == 2:
        try:
            Thema = Tema.tema(message.text, Description=[""], Author=[id])
            if Thema.exist():
                Thema.add(show=True, remove=True)
                id = int(uid(message.from_user))
                pr = (Commands.getuser(id)).prfl
                us = (Commands.getuser(id)).name
                Users.User(id, prfl=pr, name=us, cash=0).add(Show=True)
                await message.answer('Тема удалена!')
                print(f'user:{us}|тема:<{message.text}>|пользователь удалил тему')
            else:
                print(f'user:{us}|тема:<{message.text}>|пользователь ввел неверную тему')
                await message.answer(
                    'Такой темы нет, \nпроверьте правильность написания темы\n(Проверьте, что тема написана без кавычек, знаков препинаний и лишних пробелов) ')
        except:
            print(f'user:{us}|тема:<{message.text}>|пользователь ввел неверную тему')
            await message.answer('Такой темы нет, \nпроверьте правильность написания темы\n(Проверьте, что тема написана без кавычек, знаков препинаний и лишних пробелов) ')
    if status == 3:
        try:
            id = int(uid(message.from_user))
            pr = (Commands.getuser(id)).prfl
            us = (Commands.getuser(id)).name
            us2 = (Commands.getuser((Commands.gettema(message.text)).Author[0])).name
            print(Commands.gettema(message.text))
            Users.User(id, prfl=pr, name=us, cash=0).add(Show=True)
            prf = int((Commands.gettema(message.text)).prfl)
            if prf == 1:
                p = 'Физмат'
            if prf == 2:
                p = 'Биохим'
            if prf == 3:
                p = 'Соцэконом'
            mess = f'Автор: @{us2} \nПрофиль: {p} \n'
            mess += f'Описание: {str((Commands.gettema(message.text)).Description).replace("[","").replace("]","")} \n'
            if us == us2:
                mess += f'Подписчики: {len(list((Commands.gettema(message.text)).follower))} \n'
                mess += f'Просмотры: {len(list((Commands.gettema(message.text)).Viewers))} \n'
            iddqd = ''
            for i in (list((Commands.gettema(message.text)).Decisive)):
                i = int(str(i).replace('[','').replace("'","").replace(']',''))
                iddqd = iddqd+str(i)+' '
            if us == us2 or str(id) in iddqd:
                mess += f'Решающие: \n'
                for i in (list((Commands.gettema(message.text)).Decisive)):
                    i = int(str(i).replace('[','').replace("'","").replace(']',''))
                    mess += f'@{(Commands.getuser(i).name)}\n'
            await message.answer(mess)
            print(f'user:{us}|тема:<{message.text}>|пользователь вызвал информацию по теме')
        except:
            print(f'user:{us}|тема:<{message.text}>|пользователь ввел неверную тему')
            await message.answer('Такой темы нет, \nпроверьте правильность написания темы\n(Проверьте, что тема написана без кавычек, знаков препинаний и лишних пробелов) ')
    if status == 4:
        try:
            Thema = Tema.tema(message.text, Description=[""], follower=[id])
            if Thema.exist():
                Thema.add(show=True, remove=True)
                id = int(uid(message.from_user))
                pr = (Commands.getuser(id)).prfl
                us = (Commands.getuser(id)).name
                Users.User(id, prfl=pr, name=us, cash=0).add(Show=True)
                await message.answer('Тема удалена!')
                print(f'user:{us}|тема:<{message.text}>|пользователь удалил тему из избранного')
            else:
                print(f'user:{us}|тема:<{message.text}>|пользователь ввел неверную тему')
                await message.answer(
                    'Такой темы нет, \nпроверьте правильность написания темы\n(Проверьте, что тема написана без кавычек, знаков препинаний и лишних пробелов) ')
        except:
            print(f'user:{us}|тема:<{message.text}>|пользователь ввел неверную тему')
            await message.answer(
                'Такой темы нет, \nпроверьте правильность написания темы\n(Проверьте, что тема написана без кавычек, знаков препинаний и лишних пробелов) ')
    if status == 5:
        try:
            Thema = Tema.tema(message.text, Description=[""], Decisive=[id])
            if Thema.exist():
                Thema.add(show=True, remove=True)
                id = int(uid(message.from_user))
                pr = (Commands.getuser(id)).prfl
                us = (Commands.getuser(id)).name
                Users.User(id, prfl=pr, name=us, cash=0).add(Show=True)
                await message.answer('Тема удалена!')
                print(f'user:{us}|тема:<{message.text}>|пользователь удалил тему из решающих')
            else:
                print(f'user:{us}|тема:<{message.text}>|пользователь ввел неверную тему')
                await message.answer(
                    'Такой темы нет, \nпроверьте правильность написания темы\n(Проверьте, что тема написана без кавычек, знаков препинаний и лишних пробелов) ')
        except:
            print(f'user:{us}|тема:<{message.text}>|пользователь ввел неверную тему')
            await message.answer(
                'Такой темы нет, \nпроверьте правильность написания темы\n(Проверьте, что тема написана без кавычек, знаков препинаний и лишних пробелов) ')
    if status == 6:
        id = int(uid(message.from_user))
        pr = (Commands.getuser(id)).prfl
        us = (Commands.getuser(id)).name
        print(f'user:{us}|ввод пароля')
        if message.text == 'CrCEJP_18A31ek7d1fsIv748r329HJsfe_TA':
            builder = ReplyKeyboardBuilder()
            builder.row(
                KeyboardButton(text="Записать"),
            )
            builder.row(
                KeyboardButton(text="Удалить"),
                KeyboardButton(text="Мои темы"),
                KeyboardButton(text="Информация по теме")
            )
            builder.row(
                KeyboardButton(text="Назад"),
                KeyboardButton(text="Справка")
            )

            await message.answer(
                "Выберите действие:",
                reply_markup=builder.as_markup(resize_keyboard=True),
            )
            Users.User(id, prfl=pr, name=us, cash=0).add(Show=True)
            print(f'user:{us}|введен верный пароль')
        else:
            await message.answer('Неправильный пароль!')
            Users.User(id, prfl=pr, name=us, cash=0).add(Show=True)
            print(f'user:{us}|введен неверный пароль')
    if status == 0:
        await message.answer('Такой команды нет, проверьте правильность написания')


#
#
#
#
#
#

#не трогай, это техническое
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
