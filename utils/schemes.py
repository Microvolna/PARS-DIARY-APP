"""Список схем.

Схемы используются для записи и чтения результатов из базы данных.

Данный файл предоставляет все доступные модели в одном месте.
"""

from pydantic import BaseModel


class UserData(BaseModel):
    '''
    Данные пользователя.

    Представляет собой полную информацию о пользователе из базы данных.

    :param cookie: Cookie пользователя.
    :type cookie: str

    :param first_name: Имя пользователя.
    :type first_name: str | None = None

    :param last_name: Фамилия пользователя.
    :type last_name: str | None = None

    :param avatar_url: Ссылка на аватарку пользователя.
    :type avatar_url: str | None = None
    '''

    cookie: str | None
    first_name: str | None = None
    last_name: str | None = None
    avatar_url: str | None = None


class SettingsData(BaseModel):
    '''
    Данные настроек.
    
    Представляет из себя настройки темы,
    записываемые в базу данных для сохранения.
    
    :param theme_style: Тема.
    :type theme_style: str

    :param primary_palette: Акцентный цвет.
    :type primary_palette: str
    '''

    theme_style: str
    primary_palette: str



class GetPersonData(BaseModel):
    '''
    Данные пользователя.
    
    Представляет собой полную информацию о пользователе,
    которую знает es.ciur.ru.
    
    first_name: str | None = None
    last_name: str | None = None
    avatar_url: str | None = None'''

    first_name: str | None = None
    last_name: str | None = None
    avatar_url: str | None = None

    #selected_pupil_school: str
    #selected_pupil_classyear: str
    #user_ava_url: str
    #user_has_ava: bool
    #user_fullname: str
    #user_is_male: bool