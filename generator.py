import random

# Using Cryptographically Secure Pseudo Random Number Generator
RandGenerator = random.SystemRandom()


class GeneratorBiologicalInformation:

    """
    This class generates biological information for characters
    """

    # Lists with generator variables
    Sex = ['Женщина', 'Мужчина']
    Age = [[18, 49], [18, 49], [18, 49], [50, 90]]
    Is_childfree = ['', '', '', '', '', '', '', '', 'Чайлдфри', 'Чайлдфри']
    Height = [140, 210]
    Body_type = ['Худой/ая', 'Полный/ая', 'Атлетичный/ая']

    def __generate_sex(self):
        """
        This method generates the sex information for character
        """
        sex = RandGenerator.choice(self.Sex)
        return sex

    def __generate_age(self):
        """
        This method generates the age information for character
        """
        borders: list = RandGenerator.choice(self.Age)
        age: int = RandGenerator.randint(borders[0], borders[1])
        return age

    def __generate_is_childfree(self):
        """
        This method generates childfree status for character
        """
        choice: str = RandGenerator.choice(self.Is_childfree)
        return choice

    def __generate_height(self):
        """
        This method generates the hight informationfor character
        """
        borders: list = self.Height
        height: int = RandGenerator.randint(borders[0], borders[1])
        return height

    def __genenerate_body_type(self):
        """
        This method generates body type informationfor character
        """
        body_type = RandGenerator.choice(self.Body_type)
        return body_type

    def generate_gender_info(self):
        """
        This method generates full gender information for character
        """

        info: str = ''
        info += self.__generate_sex()
        info += ', '
        info += f'Возраст: {str(self.__generate_age())} лет'
        is_childfree = self.__generate_is_childfree()
        if is_childfree == 'Чайлдфри':
            info += ', '
            info += is_childfree

        return info

    def generate_physic_info(self):
        """
        This method generates full physical information for character
        """
        info = ''
        info += f'Рост: {(self.__generate_height())} см'
        info += ', '
        info += 'Телосложение: ' + str(self.__genenerate_body_type())
        return info

    def generate_biological_info(self):
        """
        This method returns full biological information
        """
        bio_info = ''
        bio_info += self.generate_gender_info()
        bio_info += ',\n'
        bio_info += self.generate_physic_info()
        return bio_info


class GeneratorStory:

    def __init__(self):
        pass

    def __gen_story(self):
        catastrophe = RandGenerator.choice(['Ядерная зима', 'Эпидемия', 'Восстание ИИ', 'Зомби-апокалипсис',
                                            'Нашествие инопланетян', 'Атака террористов', 'Паление метиорита'])
        bunker_is_needed = RandGenerator.randint(6, 60)

        if bunker_is_needed <= 18:
            destruction_percents = RandGenerator.randint(5, 35)
        elif bunker_is_needed >= 42:
            destruction_percents = RandGenerator.randint(65, 95)
        else:
            destruction_percents = RandGenerator.randint(35, 65)

        biosphere_percents = destruction_percents + RandGenerator.randint(-5, 5)
        return catastrophe, bunker_is_needed, destruction_percents, biosphere_percents

    def get_story(self):
        catastrophe, bunker_is_needed, destruction_percents, biosphere_percents = self.__gen_story()
        output = ''
        output += f'Катастрофа: {catastrophe},\n'
        output += f'Длительность пребывания в бункере: {bunker_is_needed} месяцев,\n'
        output += f'Разрушения: {destruction_percents}%,\n'
        output += f'Биосфера: {100 - biosphere_percents}%\n'
        return output
