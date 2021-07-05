from randomizer import BunkerTable
from generator import GeneratorBiologicalInformation

all_features = [[],

                ['Блогер', 'Плотник', 'Сторож', 'Нарколог', 'Священник', 'Кинолог', 'Экономист', 'Бухгалтер',
                 'Аниматор', 'Музыкант', 'Пивовар', 'Ученый-химик', 'Инженер-электрик', 'Пекарь', 'Автомеханик',
                 'Агроном', 'Акушер', 'Археолог', 'Астрофизик', 'Астроном', 'Балерина', 'Банкир', 'Батюшка',
                 'Биохимик', 'Бурильщик', 'Биолог', 'Биофизик', 'Венеролог', 'Ведущий мероприятий', 'Венеролог',
                 'Водолаз', 'Винодел', 'Психолог', 'Географ', 'Гид-переводчик', 'Гробовщик', 'Грузчик', 'Депутат',
                 'Диетолог', 'Диктор', 'Доктор', 'Живописец', 'Журналист', 'Иммунолог', 'Инженер', 'Кассир', 'Кузнец',
                 'Психиатр', 'Сварщик', 'Тракторист'],

                ['Ленивый', 'Впечатлительность', 'Жизнерадостность', 'Повышенная эмоциональность',
                 'Импульсивность', 'Плаксивость', 'Неустойчивая психика', 'Целенаправленность',
                 'Решительность', 'Подлый', 'Неуверенность', 'Смелость', 'Дисциплинированность',
                 'Самостоятельность', 'Рассудительность', 'Глубина и гибкость интеллекта', 'Находчивость',
                 'Великодушие', 'Легкомысленность', 'Сообразительность', 'Любознательность', 'Вдумчивость', 'Жесткость',
                 'Доброта', 'Отзывчивость', 'Честность и подобные качества', 'Завистливость', 'Любвеобильность',
                 'Равнодушые', 'Миролюбивость', '31', '32', '33', '34',  '35', '36', '37', '38', '39', '40', '41', '42',
                 '43', '44', '45', '46', '47', '48', '49', '50'],

                ['Covid-19', 'ВИЧ', 'Аллергия на солнечный свет', 'Рак лёгких', 'Булемия', 'Астма', 'Шизофрения',
                 'Психоз', 'Биполярное расстройство', 'Плоскостопие', 'Бесплодие', 'Косоглазие', 'Авитаминоз',
                 'Аллергия на шерсть', 'Гайморит', 'Псориаз', 'Мигрень', 'Астигматизм', 'Диабет', 'Отсутствует рука',
                 'Синдром Туретто', 'Анемия', 'Идеально здоров/а', 'Идеально здоров/а',
                 'Идеально здоров/а', 'Идеально здоров/а', 'Идеально здоров/а', 'Идеально здоров/а',
                 'Идеально здоров/а', 'Идеально здоров/а', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
                 '41', '42', '43', '44', '45', '46', '47', '48', '49', '50'],

                ['Стрельба из лука', 'Компьютерная графика', 'Граффити', 'Психология', 'Азартные игры', 'Вязание',
                 'Садоводство', 'Изучение языков', 'Кулинария', 'Программирование', 'Кикбоксинг ', 'Плавание', 'Танцы',
                 'Разведение животных', 'Скалолазание', 'Игра на гитаре', 'Озвучка аниме', 'Астрология', 'Рисование',
                 'Медитация', 'Охота', 'Фигурки из дерева', 'Лечение травами', 'Радиотехника', 'Писать стихи',
                 'Сборка компьютеров', 'Лыжный спорт', 'Фотография', 'Массаж', 'Делать закрутки', 'Химические опыты',
                 'Кемпинг', 'Коллекционирование камней', 'Разведение пчёл', '35', '36', '37', '38', '39', '40', '41',
                 '42', '43', '44', '45', '46', '47', '48', '49', '50'],

                ['Боязнь сыра', 'Арахнофобия(боязнь пауков)', 'Клаустрофобия(боязнь замкнутых пространств)',
                 'Педиофобия(боязнь предметов имитирующих человеческий облик)', 'Базофобия(боязнь ходьбы)',
                 'Теофобия(боязнь бога)', 'Мизофобия(боязнь заразиться инфекционным заболеванием)',
                 'Гамофобия(боязнь вступления в брак)', 'Айхмофобия(боязнь острых предметов)',
                 'Агорафобия(боязнь открытых пространств)', 'Акрофобия(боязнь высоты)', 'Танатофобия(боязнь смерти)',
                 'Пирофобия(боязнь огня и пожаров)', 'Гидрофобия(боязнь воды, сырости, жидкости',
                 'Клептофобия(боязнь украсть, быть обокраденым)', 'Канцерофобия(боязнь заболеть раком)',
                 'Ахлуофобия(боязнь темноты, ночи)', 'Аутофобия(боязнь одиночества)',
                 'Верминофобия(боязнь бактерий и микробов)', 'Фазмофобия(боязнь призраков и духов)',
                 'Малевзиофобия(страх перед родами)', 'Метрофобия(боязнь поэзии)', 'Бронтофобия(боязнь грома)',
                 'Параскаведекатриафобия(боязнь пятницы, 13-го дня месяца)', 'Трипанофобия(боязнь игл и уколов)',
                 'Эквинофобия(боязнь лошадей)', 'Нет фобий', 'Нет Алгофобия (боязнь боли)',
                 'Анатидаефобия (боязнь, что где-то в мире есть утка, следящая за вами)', 'Апифобия (боязнь пчёл и ос)',
                 'Аулофобия (боязнь звуков флейты)', 'Ятрофобия (боязнь врачей)', 'Радиофобия (боязнь радиации)',
                 'Психрофобия (боязнь холода)', 'Пирофобия (боязнь огня)', 'Гилофобия (боязнь леса)',
                 'Фармакофобия (боязнь принимать лекарства)', 'Нет фобий', 'Нет фобий', 'Нет фобий', '41', '42', '43',
                 '44', '45', '46', '47', '48', '49', '50'],

                ['Умеет делать алкоголь из чего угодно', 'Способен очищать любую жидкость до состояния воды',
                 'Лично знаком с президентом', 'Окончил школу с медалью', 'Проходил курсы акушера',
                 'Вырос в семье медиков', 'Проходил курс психотерапии', 'Объездил весь мир',
                 'Знает, где находится погреб с вином', 'Знает, где находится бункер с химиками-мужчинами',
                 'Получил красный диплом в 15 лет', 'Прочитал 100 книг о нашествии пришельцев',
                 'Проходил курсы сексологии', 'Знает, где есть склад оружия', 'Воевал в Сирии',
                 'Прекрасно рисует', 'Учился 4 года в медицинском университете', 'Переболел в детстве ветрянкой',
                 'Проходил курсы оказания первой помощи', 'Имеет идеальную физическую форму',
                 'Проиграл квартиру в казино', 'Жил в России 10 лет', 'Имеет дома мини-лабораторию',
                 'Виновен в происхождении катастрофы', 'Десятикратный победитель турниров по монополии',
                 'Знает все стихи Пушкина', 'Изучал воду и её очищение', 'Умеет ориентироваться по звёздам', '29', '30',
                 '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47',
                 '48', '49', '50'],

                ['Коробка чипсов', 'Семена кукурузы', 'Семена пшеницы', 'Учебник физики за 7 класс',
                 'Англо-русский словарь', 'Скакалка', 'Верёвка', 'Фильтр для очищения воды', 'Гитара', 'Книга рецептов',
                 'Толковый словарь', 'Швейная машинка', 'Наручники', 'Трёхмесячный ребенок', 'Попугай жако Максимка',
                 '10 килограмм картошки', 'Профессиональный инкубатор для яиц', 'Пакет грунта 20 кг', 'Настольные игры',
                 'Колода карт', '5 мышеловок', 'Пачка медицинских масок', '100 инсулиновых шприцов',
                 'Литий для лечения от биполярного расстройства', 'Библия', 'Бутылка водки', 'Террариум со змеями',
                 '100 миллионов долларов', 'Маникюрный набор', 'Запас обезболивающего', '10 блоков сигарет',
                 'Пачка медицинских масок', 'Пачка медицинских масок', 'Микрофон с колонкой', 'Беременная коза',
                 'Семена капусты', 'Семена картофеля', 'Семена моркови', 'Ноутбук', 'Противогаз', 'Лук и стрелы',
                 'Ледоруб и трос', 'Молоток и гвозди', 'Книга по социологии', 'Книга по психологии', 'Шпроты',
                 'Коробок спичек', 'Набор для шитья', 'Лобзик', 'Газовая горелка'],

                ['Отменяет карту, которую использовали перед вами', 'Отменяет карту, которую использовали перед вами',
                 'Отменяет карту, которую использовали перед вами', 'Обменивается здоровьем с любым игроком на выбор',
                 'Ты родственник игрока номером “твой номер +2”(если ты последний игрок, то - 2)',
                 'Ты родственник игрока номером “твой номер +2”(если ты последний игрок, то - 2)',
                 'Обменивается багажом с любым игроком на выбор', 'Меняет все профессии игроков за этим столом',
                 'Возможность получить второе образование(+1 рандомная профессия)',
                 'Возможность получить второе образование(+1 рандомная профессия)',
                 'Возможность вскрыть здоровье любого игрока', 'Дает возможность выгнать любого игрока без голосования',
                 'Даёт возможность изменить профессию любого игрока за столом',
                 'Даёт возможность изменить профессии всех игроков',
                 'Изменяет здоровье всем игрокам за столом', 'Дает возможность убрать от себя 1 голос на голосовании',
                 'Дает возможность внести один голос против кого-то во время голосования',
                 'Дает возможность вылечить одного игрока от любого заболевания',
                 'Данная карта действия даёт возможность заставить любого игрока использовать карту действия на ваш '
                 'выбор (1 или 2)', 'Данная карта действия даёт возможность заставить любого игрока использовать карту '
                                    'действия на ваш выбор (1 или 2)',
                 'Данная карта даёт возможность поменяться картой фобии с любым из игроков',
                 'Данная карта позволяет вернуть выбывшего игрока',
                 'Дает возможность убрать от себя 1 голос на голосовании',
                 'Дает возможность убрать от себя 1 голос на голосовании',
                 'Дает возможность убрать от себя 1 голос на голосовании',
                 'Дает возможность вылечить одного игрока от любого заболевания',
                 'Дает возможность вылечить одного игрока от любого заболевания',
                 'Даёт возможность изменить профессию любого игрока за столом',
                 'Даёт возможность изменить свою профессию на любую из колоды',
                 'Даёт возможность изменить свою профессию на любую из колоды', 'Забирает 30 секунд речи игрока',
                 'Забирает 30 секунд речи игрока', 'Обменивается здоровьем с любым игроком на выбор',
                 'Обменивается здоровьем с любым игроком на выбор', 'Меняет все профессии игроков за этим столом',
                 'Меняет все профессии игроков за этим столом',
                 'Данная карта изменяет биологическую характеристику всех за этим столом',
                 'Данная карта изменяет биологическую характеристику всех за этим столом',
                 'Данная карта вскрывает все фобии игроков за этим столом',
                 'Данная карта дает возможность обменяться здоровьем с любым игроком за этим столом',
                 'Данная карта дает возможность излечить любую болезнь без хирургического вмешательства '
                 '(в том числе у себя)', 'Замени открытую карту здоровья любого игрока на случайную из колоды',
                 'У тебя есть защита на 1 круг если за тебя больше всего голосов',
                 'Можешь дать иммунитет любому игроку на 1 круг, если за него больше всего голосов',
                 'Можешь дать иммунитет любому игроку на 1 круг, если за него больше всего голосов',
                 'Количество мест в бункере увеличивается на 1 место',
                 'Количество мест в бункере увеличивается на 1 место', '48', '49', '50']]

# Creating instanse of Generator Biological Info
Generator = GeneratorBiologicalInformation()

try:
    count_of_tables = int(input('Количество столов: '))
except ValueError:
    count_of_tables = 1

# Creating files with tables and BackTables
for i in range(count_of_tables):

    try:
        count_of_gamers = int(input('Количество игроков: '))
        if count_of_gamers > 15:
            print('Слишком много игроков')
            continue
        elif count_of_gamers < 1:
            print('Слишком мало игроков')
            continue
    except ValueError:
        count_of_gamers = 10

    needed_features = []
    
    for a in range(9):
        items = str(input('Введите необходимые характеристики: '))
        if items != '':
            items = items.split(' ')
            for b in range(len(items)):
                items[b] = int(items[b])
        needed_features.append(items)

    # Creating instanse of Table Randomizator
    Table = BunkerTable(needed_features=needed_features, all_features=all_features, generator=Generator,
                        count_of_characters=count_of_gamers)

    # Creating Table
    with open(f'/Users/sergeypolyakov/Desktop/Бункер/Table_{i+1}.txt', 'w') as file:
        Table.table_generator()
        file.write(Table.pretty_output())
        print('Стол сгенерирован')
        file.close()

    with open(f'/Users/sergeypolyakov/Desktop/Бункер/BackTable_{i+1}.txt', 'w') as file:
        Table.table_generator()
        file.write(Table.pretty_output())
        print('Запасные характеристики сгенерированны')
        file.close()

    with open(f'/Users/sergeypolyakov/Desktop/Бункер/BackTable_{i+1}_2.txt', 'w') as file:
        Table.table_generator()
        file.write(Table.pretty_output())
        print('Запасные характеристики сгенерированны-2')
        file.close()
