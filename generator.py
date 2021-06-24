import random

# Using Cryptographically Secure Pseudo Random Number Generator
RandGenerator = random.SystemRandom()


class GeneratorBiologicalInformation:

    """
    This class generates biological information for characters
    """

    Sex = ['Женшина', 'Мужчина']
    Age = [[16, 34], [35, 59], [60, 90]]
    Is_childfree = ['', '', '', '', '', 'Чайлдфри', 'Чайлдфри']
    Height = [140, 210]
    Body_type = ['Худой/ая', 'Полный/ая', 'Атлетичный/ая']

    def __generate_sex(self):
        """
        This method generates the sex information
        """
        sex = RandGenerator.choice(self.Sex)
        return sex

    def __generate_age(self):
        """
        This method generates the age information
        """
        borders: list = RandGenerator.choice(self.Age)
        age: int = RandGenerator.randint(borders[0], borders[1])
        return age

    def __generate_is_childfree(self):
        """
        This method generates childfree status
        """
        choice: str = RandGenerator.choice(self.Is_childfree)
        return choice

    def __generate_height(self):
        """
        This method generates the hight information
        """
        borders: list = RandGenerator.choice(self.Age)
        height: int = RandGenerator.randint(borders[0], borders[1])
        return height

    def __genenerate_body_type(self):
        body_type = RandGenerator.choice(self.Body_type)
        return body_type
    '''bio_info += str(self.__generate_height())
        bio_info += ', '
        bio_info += str(self.__genenerate_body_type())'''

    def __generate_gender_info(self):
        """
        This method generates full biological information for character
        """

        info: str = ''
        info += self.__generate_sex()
        info += ', '
        info += f'Возраст: {str(self.__generate_age())} лет'
        is_childfree = self.__generate_is_childfree()
        if is_childfree == 'Чайлдфри':
            info += ', '
            info += is_childfree
        print(info)

        return info

    def __generate_physic_info(self):
        info = ''
        info += f'Вес: {(self.__generate_height())} кг'
        info += ', '
        info += 'Телосложение: ' + str(self.__genenerate_body_type())
        print(info)
        return info

    def generate_biological_info(self):
        bio_info = ''
        bio_info += self.__generate_gender_info()
        bio_info += '\n'
        bio_info += self.__generate_physic_info()
        return bio_info
