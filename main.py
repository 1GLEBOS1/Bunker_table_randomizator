from randomizer import BunkerTable
from generator import GeneratorBiologicalInformation

# This is a list of characteristics required to be able to win
needed_features = [[], [], [], [], [], [], [], [], [0, 2, 15]]

# This is a list of фдд characteristics in game
all_features = [[],

                ['Блогер', 'Плотник', 'Сторож', 'Нарколог', 'Священник', 'Кинолог', 'Экономист', 'Бухгалтер',
                 'Аниматор', 'Музыкант', 'Пивовар', 'Ученый-химик', 'Инженер-электрик', 'Пекарь', 'Автомеханик',
                 'Агроном', 'Акушер', 'Археолог', 'Астрофизик', 'Астроном', 'Балерина', 'Банкир', 'Батюшка',
                 'Биохимик', 'Бурильщик', 'Биолог', 'Биофизик', 'Венеролог', 'Ведущий мероприятий', 'Венеролог',
                 'Водолаз', 'Винодел', 'Психолог', 'Географ', 'Гид-переводчик', 'Гробовщик', 'Грузчик', 'Депутат',
                 'Диетолог', 'Диктор', 'Доктор', 'Живописец', 'Журналист', 'Иммунолог', 'Инженер', 'Кассир', 'Кузнец',
                 'Психиатр', 'Сварщик', 'Тракторист'],

                ['Экспрессивность', 'Впечатлительность', 'Жизнерадостность', 'Повышенная и низкая эмоциональность',
                 'Импульсивность', 'Импрессивность', 'Неустойчивая эмоциональность', 'Целенаправленность',
                 'Решительность', 'Настойчивость', 'Неуверенность', 'Смелость', 'Дисциплинированность',
                 'Самостоятельность', 'Рассудительность', 'Глубина и гибкость интеллекта', 'Находчивость',
                 'Великодушие', 'Легкомысленность', 'Сообразительность', 'Любознательность', 'Вдумчивость', 'Жесткость',
                 'Доброта', 'Отзывчивость', 'Честность и подобные качества', 'Завистливость', 'Любвеобильность',
                 'Равнодушые', 'Миролюбивость'],

                ['Covid-19', 'ВИЧ', 'Аллергия на солнечный свет', 'Рак лёгких', 'Булемия', 'Астма', 'Шизофрения',
                 'Психоз', 'Биполярное расстройство', 'Плоскостопие', 'Бесплодие', 'Косоглазие', 'Авитаминоз',
                 'Аллергия на шерсть', 'Гайморит', 'Псориаз', 'Мигрень', 'Астигматизм', 'Диабет', 'Отсутствует рука',
                 'Синдром Туретто', 'Анемия', 'Идеально здоров/а', 'Идеально здоров/а',
                 'Идеально здоров/а', 'Идеально здоров/а', 'Идеально здоров/а', 'Идеально здоров/а',
                 'Идеально здоров/а', 'Идеально здоров/а'],

                ['Стрельба из лука', 'Компьютерная графика', 'Граффити', 'Психология', 'Азартные игры', 'Вязание',
                 'Садоводство', 'Изучение языков', 'Кулинария', 'Программирование', 'Кикбоксинг ', 'Плавание', 'Танцы',
                 'Разведение животных', 'Скалолазание', 'Игра на гитаре', 'Озвучка аниме', 'Астрология', 'Рисование',
                 'Медитация', 'Охота', 'Фигурки из дерева', 'Лечение травами', 'Радиотехника', 'Писать стихи',
                 'Сборка компьютеров', 'Лыжный спорт', 'Фотография', 'Массаж', 'Делать закрутки'],

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
                 'Эквинофобия', 'Эквинофобия(боязнь лошадей)', 'Нет фобий', 'Нет фобий', 'Нет фобий'],

                ['Умеет делать алкоголь из чего угодно', 'Способен очищать любую жидкость до состояния воды',
                 'Лично знаком с президентом', 'Окончил школу с медалью', 'Проходил курсы акушера',
                 'Вырос в семье медиков', 'Проходил курс психотерапии', 'Объездил весь мир',
                 'Знает, где находится погреб с вином', 'Знает, где находится бункер с химиками-мужчинами',
                 'Получил красный диплом в 15 лет', 'Прочитал 100 книг о нашествии пришельцев',
                 'Проходил курсы сексологии', 'Знает, где есть склад оружия', 'Воевал в Сирии',
                 'Прекрасно рисует', 'Учился 4 года в медицинском университете', 'Переболел в детстве ветрянкой',
                 'Проходил курсы оказания первой помощи', 'Имеет идеальную физическую форму',
                 'Проиграл квартиру в казино', 'Жил в России 10 лет', 'Имеет дома мини-лабораторию',
                 'Виновен в происхождении катастрофы', 'Десятикратный победитель турниров по монополии', '26', '27',
                 '28', '29', '30'],

                ['Коробка чипсов', 'Семена кукурузы', 'Семена пшеницы', 'Учебник физики за 7 класс',
                 'Англо-русский словарь', 'Скакалка', 'Верёвка', 'Фильтр для очищения воды', 'Гитара', 'Книга рецептов',
                 'Толковый словарь', 'Швейная машинка', 'Наручники', 'Трёхмесячный ребенок', 'Попугай жако Максимка',
                 '10 килограмм картошки', 'Профессиональный инкубатор для яиц', 'Пакет грунта 20 кг', 'Настольные игры',
                 'Колода карт', '5 мышеловок', 'Пачка медицинских масок', '100 инсулиновых шприцов',
                 'Литий для лечения от биполярного расстройства', 'Библия', 'Бутылка водки', 'Террариум со змеями',
                 '100 миллионов долларов', 'Маникюрный набор', 'Запас обезболивающего'],

                ['Отменяет карту, которую использовали перед вами', 'Обменивается здоровьем с любым игроком на выбор',
                 'Ты родственник игрока номером “твой номер +2”(если ты последний игрок, то - 2)',
                 'Обменивается багажом с любым игроком на выбор', 'Меняет все профессии игроков за этим столом',
                 'Возможность получить второе образование(+1 рандомная профессия)',
                 'Возможность вскрыть здоровье любого игрока', 'Дает возможность выгнать любого игрока без голосования',
                 '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25',
                 '26', '27', '28', '29', '30']]

# Creating instanse of Generator Biological Info
Generator = GeneratorBiologicalInformation()

# Creating instanse of Table Randomizator
Table = BunkerTable(needed_features=needed_features, all_features=all_features, generator=Generator)

count_of_tables = int(input('Количество столов: '))

# Creating files with tables and BackTables
for i in range(count_of_tables):

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
