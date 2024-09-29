import json

from utils.schemes import *
from utils.pars import request

class user:
    def check_cookie(cookie: str) -> tuple[bool, str | GetPersonData]:
        'Проверяет достоверность вводимых куков'

        # Проверяем заполнены ли cookie
        if cookie == '':
            return False, 'Для использования приложения необходимо указать ваши cookie в разделе настройки'
        # Простые тесты
        elif 'sessionid=' not in cookie:
            return False, 'Ваши cookie должны содержать "sessionid="'
        elif 'sessionid=xxx...' in cookie:
            return False, 'Нельзя использовать пример'
        # Тест путем запроса к серверу
        r = request(cookie, 'https://es.ciur.ru/api/ProfileService/GetPersonData')
        
        if r[1] != 200:
            return False, 'Неправильно введены cookie, возможно они устарели (сервер выдает неверный ответ)'
        else:
            data = r[0]
            full_name = data['user_fullname'].split()

            # Получаем имя и фамилию
            first_name=full_name[0]
            last_name=full_name[1]

            # Получаем аватарку, если она есть
            if data['user_has_ava']:
                avatar_url = data['user_ava_url']
            else:
                avatar_url = None

            return True, GetPersonData(
                first_name=first_name,
                last_name=last_name,
                avatar_url=avatar_url
            )


    def edit(cookie: str | None = None) -> tuple[bool, str]:
        'Записывает данные (самые частоиспользуемые) о пользователе в базу данных'
        try:
            with open('index.json', 'r+', encoding='UTF-8') as f:
                data = json.load(f)

                if cookie != None:
                    # Проверяем достоверность записываемых cookie
                    c_c = user.check_cookie(cookie)
                    if c_c[0]:
                        data['user']['cookie'] = cookie
                        data['user']['first_name'] = c_c[1].first_name
                        data['user']['last_name'] = c_c[1].last_name
                        data['user']['avatar_url'] = c_c[1].avatar_url
                    else:
                        return c_c

                f.seek(0)
                json.dump(data, f, ensure_ascii=False, indent=4)

                return True, 'ok'
                
        except Exception as e:
            return False, f'Неизвестная ошибка: {e}'
        

    def get() -> UserData | tuple:
        with open('index.json', 'r', encoding='UTF-8') as f:
            data = json.load(f)['user']

        return UserData(
            cookie=data['cookie'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            avatar_url=data['avatar_url']
        )
    

class settings:
    def edit(theme_style: str | None = None, primary_palette: str | None = None) -> None:
        with open('index.json', 'r+', encoding='UTF-8') as f:
            data = json.load(f)

            if theme_style != None:
                data['settings']['theme_style'] = theme_style

            if primary_palette != None:
                data['settings']['primary_palette'] = primary_palette

            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)

    
    def get() -> SettingsData:
        'Получает настройки из базы данных'
        with open('index.json', 'r', encoding='UTF-8') as f:
            data = json.load(f)['settings']

        return SettingsData(
            theme_style = data['theme_style'],
            primary_palette = data['primary_palette']
        )

if __name__ == '__main__':
    # Проверка записи данных в бд
    print(user.edit(
        cookie='куки-для-теста',
    ))

    # Проверка получения данных из бд
    print(user.get().cookie)
    print(user.get().first_name)
    print(user.get().last_name)
    print(user.get().avatar_url)