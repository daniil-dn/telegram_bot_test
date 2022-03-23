from collections import OrderedDict

# отсюда создается STAGES при init в Vacancy
# STAGES = {0:"vacancy_title"}
"""
'---' сопоставимо с None, Unknown...

"""
COMMANDS = ("menu", "show_vacancy", "start_over", "continue_filling")
text_pattern = OrderedDict({
    "company_name": ("👇 Название компании 👇", ("indie",)),
    "vacancy_title": ("👇 Название вакансии 👇",
                      ('UNREAL ENGINE C++ DEVELOPER', 'UNREAL ENGINE DEVELOPER', 'GAME DESIGNER', '3D ARTIST')),
    "art_code": ("Art 👨‍🎨 || Сode 🧑‍💻", ('art', 'code')),
    "skill_level": ("👇 Уровень Skill 👇", ('Junior', 'Middle', 'Senior')),
    "game_title": ("🕹 Название игры 🕹", ("Unknown",)),
    "years": ("🧠 Сколько лет опыта 🧠", ("---", 1, 2, 3, 4, 5)),
    "platform": ("🎛 Платформа 🎛", (
        'PC, Console', 'PC', 'PC, VR', 'PC, Mobile', 'PC, Mobile, Console', 'PC, Mobile, Console, VR',
        'PC, Console, VR',
        'Mobile',
        'Console', 'VR')),
    "remote": ("🌎  Удаленка? 🌎 ", ("---", 'Remote')),
    "office": ("💼 Офис есть? 💼", ("---", "Москва", "Санкт-Петербург", "Киев", "Екатеринбург", "Омск")),
    "money": ("💰 Что по $$$ ? 💰", ('По договоренности',)),
    "schedule": ("⏰ Какой график работы? ⏰", ('Full-time', 'Part-time', 'Contract')),
    "description": ("🦄 Описание", ('---',)),
    "resp": ("🚀  Что ты будешь делать 🚀\n '=' - разделитель", ('---',)),
    "require": ("📚 Твои скиллы 📚\n '=' - разделитель", ('---',)),
    "plus": ("👍 Круто, если знаешь 👍\n '=' - разделитель", ('---',)),
    "cond": ("🍪 Условия и плюшки 🍪\n '=' - разделитель", ('---',)),
    "useful": ("ℹ️  Полезная информация ℹ️\n'=' - разделитель", ('---',)),
    "contacts": ("📨 Контакты 📨", ('---',)),

})
# {"tags": (
# cb.data,
# {tags:cb.data,tags:cb.data,..})
# }

USER_MENU = OrderedDict(
    {"company": "🏢 Компания",
     "vacancy": "🖥 Вакансия",
     "description": "✍️ Описание",
     "project": "🕹 Проект",
     "platform": "🎮 Платформа",
     "sub_experince": (
         "🎓 Опыт",
         {'years': 'Years', "junior": "Junior <1year", "middle": "Middle 1-3years", "senior": "Senior >3years"}),
     "schedule": "⏰ Загрузка",
     "payment": "💰 Оплата",
     "location": "🗺 Локация",
     "duty": "🚀 Обязанности",
     "skills": "💪 Скилл сет",
     "add_skills": "🦾 Доп. скиллы",
     "conditions": "🍪 Условия",
     "useful_info": "ℹ️ Полезная информация",
     "contacts": "📨 Контакты",
     "art/code": "Какой профиль?",

     # {"callback_tag": ("menu_text",
     #                  {'submenu_tag': ("submenu_text",
     #                                   {"sub_submenu": "sub_submenu_text"})}),
     #  }
     })
# text, auto_input, inline_input
MENU_ACTIONS = {
    "all": "text",
    'nothing_exceptions': "root, sub_experince, junior, senior, middle"
}
MP_WIDTH = {
    "all": 3,
    "sub_experince": 4
}
# todo
BOTTOM_menu = {"send_vacancy": "✅ Опубликовать", "reset": "❌ Сброс"}
