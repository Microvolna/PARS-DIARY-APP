__version__ = "0.0.1"

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivymd.toast import toast

# TODO from utils.hw import hw
from utils.pars import Pars
from utils import ava
from utils import db


KV = """
ScreenManager:
    LessonsScreen:
    SummaryScreen:
    NotificationsScreen:
    MeScreen:
    StartScreen:


<LessonsScreen>:
    name: 'Уроки'
    
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)

        MDLabel:
            valign: 'top'
            text: app.get_info('lessons')

        MDNavigationBar:
            id: bottom_nav
            on_switch_tabs: app.change_screen(*args)

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'book'

                MDNavigationItemLabel:
                    text: 'Уроки'

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'bookmark-outline'

                MDNavigationItemLabel:
                    text: 'Итоговые'

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'bell-ring-outline'

                MDNavigationItemLabel:
                    text: 'Уведомления'

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'account-outline'

                MDNavigationItemLabel:
                    text: 'Я'


<SummaryScreen>:
    name: 'Итоговые'
    
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)

        MDLabel:
            valign: "top"
            text: "Тут скоро будет информация об итоговых оценках"

        MDNavigationBar:
            id: bottom_nav
            on_switch_tabs: app.change_screen(*args)

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'book-outline'

                MDNavigationItemLabel:
                    text: 'Уроки'

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'bookmark'

                MDNavigationItemLabel:
                    text: 'Итоговые'

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'bell-ring-outline'

                MDNavigationItemLabel:
                    text: 'Уведомления'

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'account-outline'

                MDNavigationItemLabel:
                    text: 'Я'

<NotificationsScreen>:
    name: 'Уведомления'
    
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)

        MDLabel:
            valign: "top"
            text: "Тут скоро будет информация о уведомлениях"

        MDNavigationBar:
            id: bottom_nav
            on_switch_tabs: app.change_screen(*args)

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'book-outline'

                MDNavigationItemLabel:
                    text: 'Уроки'

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'bookmark-outline'

                MDNavigationItemLabel:
                    text: 'Итоговые'

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'bell-ring'

                MDNavigationItemLabel:
                    text: 'Уведомления'

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'account-outline'

                MDNavigationItemLabel:
                    text: 'Я'

<MeScreen>:
    name: 'Я'
    
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)

        FitImage:
            source: "ava.png"
            pos_hint: {'center_x': 0.5, 'top': 1}
            size_hint: None, None
            width: 200  # Задайте нужную ширину
            height: self.texture_size[1]  # Высота будет зависеть от размера текстуры
            allow_stretch: True
            keep_ratio: True

        MDLabel:
            valign: "top"
            pos_hint: {'center_x': 0.5, 'top': 1}
            text: app.get_info('me_name')
            bold: True

        MDLabel:
            valign: "top"
            text: 'Тема:'

        # Выбор темы (Dark, Light)

            MDDropDownItemText:
                id: drop_text
                text: "Темная"

            MDDropDownItemText:
                id: drop_text
                text: "Светлая"

        MDLabel:
            valign: "top"
            text: 'Акцентный цвет:'

        # Выбор акцентного цвета items: [{'text': 'Red'}, {'text': 'Pink'}, {'text': 'Purple'}, {'text': 'Deep Purple'}, {'text': 'Indigo'}, {'text': 'Blue'}, {'text': 'Light Blue'}, {'text': 'Cyan'}, {'text': 'Teal'}, {'text': 'Green'}, {'text': 'Light Green'}, {'text': 'Lime'}, {'text': 'Yellow'}, {'text': 'Amber'}, {'text': 'Orange'}, {'text': 'Deep Orange'}, {'text': 'Brown'}, {'text': 'Grey'}, {'text': 'Blue Grey'}]

        MDNavigationBar:
            id: bottom_nav
            on_switch_tabs: app.change_screen(*args)

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'book-outline'

                MDNavigationItemLabel:
                    text: 'Уроки'

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'bookmark-outline'

                MDNavigationItemLabel:
                    text: 'Итоговые'

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'bell-ring-outline'

                MDNavigationItemLabel:
                    text: 'Уведомления'

            MDNavigationItem:
                MDNavigationItemIcon:
                    icon: 'account'

                MDNavigationItemLabel:
                    text: 'Я'

<StartScreen>
    name: 'start'
    
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)

        MDLabel:
            valign: "top"
            font_style: 'Headline'
            bold: True
            text: "Авторизация"
            size_hint_x: 0.8
            pos_hint: {"center_x": .5, "center_y": .5}

        MDLabel:
            valign: "top"
            text: 'Для доступа к дневнику вам необходимо ввести ваши cookie, для их получения вы можете воспользоваться инструкцией по кнопке ниже.'
            size_hint_x: 0.8
            pos_hint: {"center_x": .5, "center_y": .5}
            
        MDButton:
            style: "tonal"
            theme_width: "Custom"
            height: "56dp"
            size_hint_x: 0.8
            on_release: webbrowser.open('https://telegra.ph/Instrukciya-po-registracii-v-bote-04-25')
            pos_hint: {"center_x": .5, "center_y": .5}

            MDButtonText:
                id: text
                text: 'Просмотреть инструкцию'
                pos_hint: {"center_x": .5, "center_y": .5}

        MDTextField:
            id: cookie_input
            hint_text: "Введите cookie"
            password: True  # Скрыть вводимые символы
            mode: 'outlined'
            size_hint_x: 0.8
            pos_hint: {"center_x": .5, "center_y": .5}

        MDButton:
            style: "filled"
            theme_width: "Custom"
            height: "56dp"
            size_hint_x: 0.8
            on_release: app.save_cookie()
            pos_hint: {"center_x": .5, "center_y": .5}

            MDButtonText:
                id: text
                text: 'Продолжить'
                pos_hint: {"center_x": .5, "center_y": .5}
"""

class StartScreen(Screen):
    pass

class LessonsScreen(Screen):
    pass

class SummaryScreen(Screen):
    pass

class NotificationsScreen(Screen):
    pass

class MeScreen(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        'Функция для загрузки и запуска приложения'
        # Устанавливаем тему из базы данных
        settings = db.settings.get()
        self.set_theme(
            settings.theme_style,
            settings.primary_palette
        )

        # TODO Проверяем колличество уведомлений
        # TODO и выведем их колличество на иконку

        # Запускаем приложение
        self.root = Builder.load_string(KV)

        # Получаем cookie из базы данных
        self.cookie = db.user.get().cookie
        # В случае если cookie пусты
        if self.cookie == None:
            # Переходим на страницу заполнения cookie
            self.change_screen(item_text='start')

        return self.root
    

    def get_info(self, screen_name: str) -> str:
        'Дополнительная прослойка между приложением и парсром'
        pars = Pars()
        cookie = db.user.get().cookie

        if cookie != None:
            if screen_name == 'lessons':
                return pars.birthdays(cookie)

            elif screen_name == 'me_name':
                user_data = db.user.get()
                ava.download()

                return f'{user_data.first_name} {user_data.last_name}'
            
        return 'Ошибка'


    def save_cookie(self) -> None:
        'Обновление куков в бд'
        cookie = self.root.get_screen('start').ids.cookie_input.text

        # Записываем новые данные в бд
        edit_cookie = db.user.edit(cookie)
        if edit_cookie[0]:
            # Выводим тост об успешной авторизации
            self.show_toast('Авторизация успешна!')
            # Переводим на домашний экран
            self.change_screen(item_text='Уроки')
            # Присваивем переменную
            self.cookie = cookie
        else:
            # Выводим тост об ошибке
            self.show_toast(edit_cookie[1])


    def change_screen(
        self,
        bar: MDNavigationBar | None = None,
        item: MDNavigationItem | None = None,
        item_icon: str | None = None,
        item_text: str | None = None,
    ) -> None:
        'Смена экранов'
        self.root.current = item_text


    def show_toast(self, text: str) -> None:
        'Показываем "тост"'
        toast(text, duration=3)
        print(f'[INFO   ] [Toast       ] {text}')


    def set_theme(self, theme_style: str | None = None, primary_palette: str | None = None) -> None:
        'Функция для смены темы (темная -> светлая/светлая -> темная)'
        # Устанавливаем тему
        self.theme_cls.theme_style = theme_style
        self.theme_cls.primary_palette = primary_palette

        # Записываем изменения в базу данных
        db.settings.edit(
            theme_style,
            primary_palette
        )


if __name__ == '__main__':
    MyApp().run()