from collections import OrderedDict

from aiogram import types, Bot
from markup_text import USER_MENU, MENU_ACTIONS, MP_WIDTH

vacancy_per_user = {}


class Vacancy:

    def __init__(self, main_mg_id, chat_id):
        """
        Создает new объект вакансии.
        Инициализирует Шаги из файлы markup_text.py

        :param main_mg_id:
        :param chat_id:
        """
        self.mg_id = main_mg_id
        self.chat_id = chat_id

        self.info = {}
        self.info['payment'] = "По договоренности"
        self.info['schedule'] = "Full-Time"
        self.info['jun_mid_sen'] = 'Middle'
        self.info['project'] = 'Unknown'

        self.is_art = None
        self.is_code = None

        # по дефолту попадаем в корень меню
        self.menu = self.render_menu(USER_MENU)

    @property
    def get_mp(self):
        row_width = self.menu.row_width
        children_len = len(self.menu.children)
        action = MENU_ACTIONS.get(self.menu.cb_tag, MENU_ACTIONS['all'])

        mp = types.InlineKeyboardMarkup(row_width=row_width)

        counter = 0
        cache = []
        for tag, next_menu in self.menu.children.items():
            cache.append(types.InlineKeyboardButton(next_menu.text, callback_data=tag))
            counter += 1
            if counter % row_width == 0 or counter == len(self.menu.children):
                mp.add(*cache)
                cache = list()

        # для sub_menu всегда выводит кнопку Назад
        if not self.menu.parent == 'root':
            mp.add(self.menu.back_button())

        if not self.menu.cb_tag in MENU_ACTIONS['nothing_exceptions'] and not self.menu.cb_tag in MENU_ACTIONS[
            'not_clear']:
            # mp.add(types.InlineKeyboardButton(f"👇👇{self.menu.text}👇👇", callback_data='None'))
            mp.add(types.InlineKeyboardButton(f"Очистить поле", callback_data=f'clear_{self.menu.cb_tag}'))
        if self.menu.cb_tag == "project" and self.info['project'] != 'Unknown':
            mp.add(types.InlineKeyboardButton(f"Unknown project", callback_data=f'clear_{self.menu.cb_tag}'))

        return mp

    async def update_vacancy_text(self, chat_id, bot: Bot):
        """

        :param chat_id:
        :param bot:
        :return:
        """
        self.update_root_checked_items()
        self.update_platform_checked_items()
        self.update_remote_checked_items()
        self.update_schedule_checked_items()
        self.update_experince_checked_items()
        if self.info:
            text = self.tags() + '\n\n'
            text += "<b>" + self.vacancy_title() + self.company() + "</b>" + '\n\n' \
                    + self.project() + self.platform() + '\n' \
                    + '🧠 ' + self.jun_mid_sen() + self.experience() + '\n' \
                    + self.payment() \
                    + self.schedule() \
                    + self.location() \
                    + self.description() \
                    + self.duty() \
                    + self.skills() \
                    + self.add_skills() \
                    + self.conditions() \
                    + self.useful_info() \
                    + self.contacts()
            print(self.vacancy_title())
            print(self.company())
            try:
                await bot.edit_message_text(text, chat_id, self.mg_id, parse_mode="html")
            except Exception as err:
                print(err)

    async def update_code_art(self, text: str):
        text = text.lower()
        code_list = "developer, разработчик, programmer, программист, dev, ENGINEER".lower().split(', ')
        art_list = "artist, художник, animator, art, Designer".lower().split(', ')
        self.is_code = False
        self.is_art = False

        for i in code_list:
            if i in text:
                self.is_code = True
        for i in art_list:
            if i in text:
                self.is_art = True

    def update_root_checked_items(self):
        root: MenuItem = self.menu
        while True:  # Получаем рут меню
            root = root.parent if type(root.parent) is not str else root
            if root.parent == 'root':
                break
        print(root)
        for k, v in root.children.items():
            emo = USER_MENU[k][0] if type(USER_MENU[k]) is str else USER_MENU[k][0][0]
            if self.info.get(k, '') or k == 'location' or k == 'sub_experince':
                if self.platform(is_tag=True) == '' and k == 'project':
                    root.children[k].text = emo + root.children[k].text[1:]
                elif self.location(is_tag=True) == '' and k == 'location':
                    root.children[k].text = emo + root.children[k].text[1:]
                elif self.jun_mid_sen(is_tag=True) == '' and k == 'sub_experince':
                    root.children[k].text = emo + root.children[k].text[1:]
                else:
                    root.children[k].text = "✅" + root.children[k].text[1:]
            else:
                print(emo)
                root.children[k].text = emo + root.children[k].text[1:]

    def update_platform_checked_items(self):
        platform: MenuItem = self.menu
        if platform.cb_tag == 'project':
            for k, v in platform.children.items():
                if platform.children[k].text.find("✅") == -1:
                    starts_with = 0
                else:
                    starts_with = 1

                if self.info.get(k, '') and k.lower() in 'pc console vr/ar mobile':
                    platform.children[k].text = "✅" + platform.children[k].text[starts_with:]
                else:
                    platform.children[k].text = platform.children[k].text[starts_with:]

    def update_remote_checked_items(self):
        location: MenuItem = self.menu
        if location.cb_tag == 'location':
            for k, v in location.children.items():
                print(k)
                if location.children[k].text.find("✅") == -1:
                    starts_with = 0
                else:
                    starts_with = 1
                if self.info.get(k, ''):
                    location.children[k].text = "✅" + location.children[k].text[starts_with:]
                else:
                    location.children[k].text = location.children[k].text[starts_with:]

    def update_schedule_checked_items(self):
        schedule: MenuItem = self.menu
        if schedule.cb_tag == 'schedule':
            for k, v in schedule.children.items():
                print(k)
                if schedule.children[k].text.find("✅") == -1:
                    starts_with = 0
                else:
                    starts_with = 1
                if self.info.get(k, ''):
                    schedule.children[k].text = "✅" + schedule.children[k].text[starts_with:]
                else:
                    schedule.children[k].text = schedule.children[k].text[starts_with:]

    def update_experince_checked_items(self):
        schedule: MenuItem = self.menu
        if schedule.cb_tag == 'sub_experince':
            cur_jun_mid_sen = self.info.get('jun_mid_sen', '')

            for k, v in self.menu.children.items():
                if k in ('Intern', "Junior", "Middle", "Senior"):
                    if self.menu.children[k].text.find("✅") == -1:
                        starts_with = 0
                    else:
                        starts_with = 1
                    if k == cur_jun_mid_sen:
                        self.menu.children[k].text = "✅" + self.menu.children[k].text[starts_with:]
                    else:
                        self.menu.children[k].text = self.menu.children[k].text[starts_with:]
                else:
                    if self.menu.children[k].text.find("✅") == -1:
                        starts_with = 0
                    else:
                        starts_with = 1
                    if self.info.get(k, ''):
                        self.menu.children[k].text = "✅" + self.menu.children[k].text[starts_with:]
                    else:
                        self.menu.children[k].text = self.menu.children[k].text[starts_with:]

    def tags(self):
        """
        #UnrealEngine #GameDev #FullTime #Art #Middle #PC #Remote #Office #ProgramAce

        :return:
        """
        tags = "#UnrealEngine #GameDev "
        tags += self.schedule(is_tag=True)
        tags += self.art_code_tag()

        tags += self.jun_mid_sen(is_tag=True)
        tags += self.platform(is_tag=True)

        tags += self.location(is_tag=True)
        tags += self.company(is_tag=True)

        return tags

    def art_code_tag(self):
        result = ''
        if self.is_code:
            result += '#Code '
        if self.is_art:
            result += '#Art '

        return result

    def jun_mid_sen(self, is_tag=False):

        jun_mid_sen = self.info.get('jun_mid_sen', '')
        match jun_mid_sen:
            case "Intern":
                self.info['years'] = None if not self.info.get('years', None) else self.info['years']
            case "Junior":
                self.info['years'] = 1 if not self.info.get('years', None) else self.info['years']
            case "Middle":
                self.info['years'] = 3 if not self.info.get('years', None) else self.info['years']
            case "Senior":
                self.info['years'] = 5 if not self.info.get('years', None) else self.info['years']

        if is_tag:
            return f"#{jun_mid_sen} " if jun_mid_sen else ''
        else:
            return f"{jun_mid_sen} " if jun_mid_sen else ''

    def vacancy_title(self):
        title = self.info.get('vacancy', '')
        title = title.lower().replace('ue5', '').replace('ue4', '').replace('ue', '').replace('unreal engine', '')
        result = self.jun_mid_sen() + "UNREAL ENGINE " + title
        return result.upper() + ' ' if title else result.upper()

    def company(self, is_tag=False):
        company = self.info.get('company', '')

        if is_tag and company:
            return f"#{company.title().replace(' ', '').replace('-', '')} "

        if not is_tag and company:
            company = company.capitalize() if company and company[0].islower() else company
            return f'({company})'
        return ''

    def project(self):
        name = self.info.get('project', 'Unknown')
        return '🕹 ' + name.capitalize() + ' '

    def platform(self, is_tag=False):
        pc = self.info.get('PC', None)
        console = self.info.get('Console', None)
        vr = self.info.get('VR/AR', None)
        mobile = self.info.get('Mobile', None)

        if is_tag:
            pc = f'#{pc} ' if pc else ''
            console = f'#{console} ' if console else ''
            vr = f'#VR #AR ' if vr else ''
            mobile = f'#{mobile} ' if mobile else ''
            result = pc + console + vr + mobile

        else:
            to_join = []
            for i in (pc, console, vr, mobile):
                if i:
                    to_join.append(i)
            result = ', '.join(to_join)
            result = f'({result})'

        return result

    def experience(self, is_tag=False):
        years = self.info.get('years', '')
        return f"({years}+)" if years else ""

    def schedule(self, is_tag=False):
        schedule = self.info.get('schedule', '')
        if is_tag and schedule:
            return f'#{schedule.replace("-", "")} '
        elif schedule:
            return f"⏰ {schedule} \n"
        else:
            return ''

    def payment(self):
        return f"💰 {self.info.get('payment', '')}\n"

    def location(self, is_tag=False):
        remote = self.info.get('Remote', None)
        office = self.info.get('Office', None)
        result = ''
        if is_tag:
            remote = f'#Remote ' if remote else ''
            office = '#Office ' if office else ''
            result = remote + office
        else:
            remote = f'🌎 Удаленно' if remote else ''
            office = f'👔 Офис ({office})' if office else ''

            if remote and office:
                result = f"{remote} || {office}"
            elif remote or office:
                result = remote + office

            if self.info.get('Relocate', ""):
                result += " <b>Relocate</b>\n\n"
            else:
                result += "\n\n"

        return result

    def description(self):
        desc = self.info.get('description', '')
        return f'🦄 <b>Описание</b>\n{desc} \n\n' if desc else ''

    def duty(self):
        duty = self.info.get('duty', '')
        return f'<b>🚀 Что ты будешь делать</b>{self.to_bullet(duty)}\n\n' if duty else ''

    def skills(self):
        skills = self.info.get('skills', '')
        return f'<b>📚 Твои скиллы</b>{self.to_bullet(skills)}\n\n' if skills else ''

    def add_skills(self):
        add_skills = self.info.get('add_skills', '')
        return f'<b>👍 Круто, если знаешь</b>{self.to_bullet(add_skills)}\n\n' if add_skills else ''

    def conditions(self):
        cond = self.info.get('conditions', '')
        return f'<b>🍪 Условия и плюшки</b>{self.to_bullet(cond)}\n\n' if cond else ''

    def useful_info(self):
        useful_info = self.info.get('useful_info', '')
        return f'<b>ℹ️ Полезная информация</b>{self.to_bullet(useful_info)}\n\n' if useful_info else ''

    def contacts(self):
        contacts = self.info.get('contacts', '')

        return f'<b>📨 Контакты</b>\n{contacts}\n🌐 Vacancy link' if contacts else ''

    @staticmethod
    def to_bullet(text: str, splitter: str = '='):
        list_items = text.splitlines()
        result = ''

        list_items = list(map(str.strip, list_items))
        for item in list_items:
            if item:
                line = item.strip(';.‣•-= ')
                line = line[0].upper() + line[1:]
                result += '\n• ' + line

        return result

    @staticmethod
    def render_menu(menu_dict: OrderedDict = USER_MENU):
        root_menu = MenuItem(parent='root', children_dict=menu_dict)
        return root_menu

    @staticmethod
    def mp_from_tuple(data_tuples: tuple) -> types.InlineKeyboardMarkup:
        """
            Создает
            клавиатуру
            из
            кортежа
            данных

            : type
            data_tuples: tuple[tuple,]
            :param
            data_tuples: (text, call_back_tag)
            :return: inline
            keyboard
            markup
            """
        mp_width = len(data_tuples)
        mp = types.InlineKeyboardMarkup(row_width=mp_width)
        for i in range(mp_width):
            text, cb = data_tuples[i]
            item = types.InlineKeyboardButton(text, callback_data=cb)
            mp.add(item)
        return mp


class MenuItem:
    def __init__(self, cb_tag='root', text=None, parent=None, children_dict: OrderedDict = None):
        self.parent = parent
        self.text = text
        self.cb_tag = cb_tag
        self.children = {}

        # создание дерева меню
        # с помощью рекурсии создаются элементы меню(ноды), связанные с предыддущим элементом.
        if isinstance(children_dict, dict):
            for tag, value in children_dict.items():
                if isinstance(value, tuple):
                    self.children[tag] = MenuItem(tag, value[0], self, value[1])
                else:
                    self.children[tag] = MenuItem(tag, value, self)

    def __str__(self):
        return str(self.children)

    @property
    def row_width(self):
        return MP_WIDTH.get(self.cb_tag, MP_WIDTH['all'])

    def menu_action(self, MENU_ACTIONS: dict = MENU_ACTIONS):
        if self.cb_tag in MENU_ACTIONS['nothing_exceptions']:
            return 'nothing'
        else:
            return MENU_ACTIONS.get(self.cb_tag, MENU_ACTIONS['all'])

    def back_menu(self):
        # Возвращает предыдущее меню, если это не root меню
        return self.parent if self.parent != 'root' else self

    def back_mp(self):
        mp = types.InlineKeyboardMarkup(row_width=1)
        mp.add(self.back_button())
        return mp

    def back_button(self):
        return types.InlineKeyboardButton("Назад", callback_data='back_menu')
