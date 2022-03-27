import random
from generator import GeneratorBiologicalInformation, GeneratorStory
from datetime import datetime

path = r'/Users/polyakov_gleb/Desktop/Бункер/'


# Using Cryptographically Secure Pseudo Random Number Generator
RandGenerator = random.SystemRandom()


def get_count_of_fetures(all_characteristics):
    """
    This function returns list of lists of counts of content
    """
    count_of_characteristics = []
    for i in range(len(all_characteristics)):
        list_of_characteristics = []
        for a in range(len(all_characteristics[i])):
            list_of_characteristics.append(a)
        count_of_characteristics.append(list_of_characteristics)
    return count_of_characteristics


class BunkerTable:
    """
    This class creates a table of Bunker game
    """

    # Lists for work with characteristics
    __characteristics_on_table = [set(), set(), set(), set(), set(), set(), set(), set(), set(), set()]
    __table = [[], [], [], [], [], [], [], [], [], []]

    def __init__(self, needed_characteristics: list, all_characteristics: list,
                 generator=GeneratorBiologicalInformation(), story=GeneratorStory(),
                 count_of_characters: int = 10):
        self.needed_characteristics = needed_characteristics
        self.all_characteristics = all_characteristics
        self.generator = generator
        self.story = story
        self.count_of_characters = count_of_characters

    def __table_randomizer(self):
        """
        This meyhod generating table
        """
        self.restore_table()
        self.__adding_needed_characteristics()
        self.__adding_random_characteristics()
        self.__creating_characters()

    def __adding_needed_characteristics(self):
        """
        This method adds needed characteristics into sets of characteristics
        """
        for i in range(len(self.needed_characteristics)):
            for a in range(len(self.needed_characteristics[i])):
                try:
                    self.__characteristics_on_table[i].add(self.needed_characteristics[i][a])
                except IndexError:
                    pass

    def __adding_random_characteristics(self):
        """
        This method adds random characteristics into sets of characteristics
        """
        # Getting indexes of characteristics
        index_characteristics = get_count_of_fetures(self.all_characteristics)
        for i in range(len(self.__characteristics_on_table)):
            if i != 0 and i != 9:
                while len(self.__characteristics_on_table[i]) < self.count_of_characters:
                    item = RandGenerator.choice(index_characteristics[i])
                    self.__characteristics_on_table[i].add(item)
            elif i == 9:
                while len(self.__characteristics_on_table[i]) < self.count_of_characters:
                    item = RandGenerator.choice(index_characteristics[i-1])
                    if item not in self.__characteristics_on_table[i-1]:
                        self.__characteristics_on_table[i].add(item)

    def __transition_data_to_lists(self):
        """
        This method transforms characteristics frpm sets to lists
        """
        characteristics = [[], [], [], [], [], [], [], [], [], []]
        for i in range(len(characteristics)):
            for a in range(len(self.__table)):
                if len(self.__characteristics_on_table[i]) != 0:
                    item = self.__characteristics_on_table[i].pop()
                    characteristics[i].append(item)
                    self.__characteristics_on_table[i].discard(item)
                else:
                    characteristics[i].append([])
        return characteristics

    def __creating_characters(self):
        """
        This method creates characters from sets of characteristics
        """
        characteristics = self.__transition_data_to_lists()
        for i in range(len(self.__characteristics_on_table)):
            for a in reversed(range(len(self.__table))):
                item = RandGenerator.choice(characteristics[i])
                self.__table[a].append(item)
                characteristics[i].remove(item)

    def restore_table(self):
        """
        This method clears lists of characteristics
        """
        length_characteristics = len(self.__characteristics_on_table)
        length_table = self.count_of_characters

        self.__characteristics_on_table = []
        self.__table = []

        for i in range(length_characteristics):
            self.__characteristics_on_table.append(set())

        for i in range(length_table):
            self.__table.append([])

    def __pretty_table(self):
        """
        this method returns prettyful output of bunker table
        """
        self.__table_randomizer()
        table = self.__table
        characteristics = self.all_characteristics
        story = self.__getstory()

        output = ''
        output += story
        output += '\n'
        for i in range(len(table)):
            character = ''
            character += f'Игрок {i + 1} Характеристики: \n'

            for a in range(len(self.__characteristics_on_table)):

                # If characteristic is not a bio and not a second special condition
                if a != 0 and a != 9:
                    character += ',\n'

                    # Adding name of characteristic
                    if a == 1:
                        character += 'Профессия: '

                    elif a == 2:
                        character += 'Человеческая черта: '

                    elif a == 3:
                        character += 'Здоровье: '

                    elif a == 4:
                        character += 'Хобби: '

                    elif a == 5:
                        character += 'Фобия: '

                    elif a == 6:
                        character += 'Дополнительная инфа: '

                    elif a == 7:
                        character += 'Багаж: '

                    elif a == 8:
                        character += 'Спец. условие 1: '

                    # Getting number of characteristic
                    number_of_characteristic = int(table[i][a])

                    # Adding characteristic
                    character += f'{characteristics[a][number_of_characteristic]}'

                # If characteristic is a second special condition
                elif a == 9:
                    character += ',\n'

                    # Adding name of characteristic
                    character += 'Спец. условие 2: '

                    # Getting number of characteristic
                    number_of_characteristic = int(table[i - 1][a])

                    # Adding characteristic
                    character += f'{characteristics[a - 1][number_of_characteristic]}'

                # If characteristic is a bio
                elif a == 0:

                    # Adding name of characteristic
                    character += 'Биологическая инфа: '

                    # Genering and adding characteristic
                    character += self.generator.generate_gender_info()

            # Adding separator
            character += '\n\n'

            # Adding character
            output += character

        return output

    def __metadata(self):
        """
        This method creates a file containing metadata of the table
        """

        # Getting table data
        table = self.__table

        output = ''

        # Adding data in output
        for i in range(len(table[0])):
            for a in range(len(table)):
                output += str(table[a][i]) + ';'
            if i != len(table[0]) - 1:
                output += '\n'

        return output

    def __getstory(self):
        return self.story.get_story()

    def get_table(self):
        """
        This method creates a file with the table, and file with metadata
        """

        # Getting now for creating files
        time = datetime.now()

        # Create file with a table
        with open(path + f'Table_{time}.txt', 'w') as file:
            file.write(self.__pretty_table())
            file.close()

        print('Стол сгенерирован', end='; ')

        # Create file with a metadata
        with open(path + f'Table_Metadata_{time}.txt', 'w') as file:
            file.write(self.__metadata())
            file.close()
        print('Метаданные сгенерированны')


class AddGenerator(BunkerTable):
    """This class add-generating characteristics"""

    def __init__(self, link_to_file: str, number_of_characteristic: int, count_of_characteristics: int,
                 all_characteristics: list, gender_generator: GeneratorBiologicalInformation, needed_characteristics=[]
                 ):
        super().__init__(needed_characteristics, all_characteristics)
        if needed_characteristics is None:
            needed_characteristics = []
        self.link_to_file = link_to_file
        self.number_of_characteristic = number_of_characteristic
        self.count_of_characteristics = count_of_characteristics
        self.gender_generator = gender_generator

    def __get_characteristics_from_file(self):
        """
        This method gets a indexes of characteristics from file of metadata
        """

        # Getting data from file of metadata
        with open(self.link_to_file, 'r') as file:
            characteristics = file.read()
            file.close()
        characteristics = characteristics.split('\n')

        # Splitting data
        for i in range(len(characteristics)):
            characteristics[i] = characteristics[i].split(';')
        for i in range(len(characteristics)):

            for a in range(len(characteristics[i])):

                if characteristics[i][a] == '':

                    del characteristics[i][a]

                elif i != 0:
                    characteristics[i][a] = int(characteristics[i][a])

        return characteristics

    def __transition_characteristics(self):
        """
        This method transforms data from string to list
        """
        # Getting data
        characteristics = self.__get_characteristics_from_file()

        output = []

        # Transiting data
        for i in range(len(characteristics)):
            for a in range(len(characteristics[i])):
                if a == self.number_of_characteristic:
                    output.append(characteristics[i][a])

        return output

    def __generate_characteristics(self):
        """
        This method generates new characteristics
        """

        # Getting old characteristics
        characteristics = self.__transition_characteristics()
        index_characteristics = get_count_of_fetures(self.all_characteristics)

        generated_characteristics = set()

        # Generating new characteristics
        if self.number_of_characteristic != 0:
            while len(generated_characteristics) != self.count_of_characteristics:
                item = RandGenerator.choice(index_characteristics[self.number_of_characteristic])
                if item not in characteristics:
                    generated_characteristics.add(item)
        else:
            for i in range(self.count_of_characteristics):
                item = self.gender_generator.generate_gender_info()
                generated_characteristics.add(item)
        return generated_characteristics

    def __transition_data_to_list(self):
        """
        This method transforms data from set to list
        """

        # Getting characteristics
        characteristics = self.__generate_characteristics()

        output = []

        # Transiting data
        for i in reversed(range(len(characteristics))):
            item = RandGenerator.choice(list(characteristics))
            output.append(item)
            characteristics.discard(item)

        return output

    def output(self):
        """
        This method returns genereted characteristics
        """
        characteristics = self.__transition_data_to_list()
        if self.number_of_characteristic != 0:
            for i in characteristics:
                print(self.all_characteristics[self.number_of_characteristic][i])
        else:
            for i in characteristics:
                print(i)

        return characteristics
