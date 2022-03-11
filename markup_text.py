from collections import OrderedDict

# отсюда создается STAGES при init в Vacancy
# STAGES = {0:"vacancy_title"}
"""
'---' сопоставимо с None, Unknown...

"""
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

# TUPLE с элементами меню
# (text: call_back_tags)
MENU = ("МЕНЮ", (("Вывести текущую вакансию", "show_vacancy"),
                 ("Создать новую вакансию", "start_over"),
                 ("Вернуться к заполнению", "continue_filling")))
