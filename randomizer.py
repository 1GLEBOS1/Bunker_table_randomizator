import random
from generator import GeneratorBiologicalInformation
from datetime import datetime

# Using Cryptographically Secure Pseudo Random Number Generator
RandGenerator = random.SystemRandom()


def get_count_of_fetures(all_features):
    count_of_features = []
    for i in range(len(all_features)):
        list_of_features = []
        for a in range(len(all_features[i])):
            list_of_features.append(a)
        count_of_features.append(list_of_features)
    return count_of_features


class BunkerTable:
    """
    This class creates a table of Bunker game
    """

    # Lists for work with characteristics
    __features_on_table = [set(), set(), set(), set(), set(), set(), set(), set(), set(), set()]
    __table = [[], [], [], [], [], [], [], [], [], []]

    def __init__(self, needed_features: list, all_features: list, generator=GeneratorBiologicalInformation(),
                 count_of_characters: int = 10):
        self.needed_features = needed_features
        self.all_features = all_features
        self.generator = generator
        self.count_of_characters = count_of_characters

    def __table_randomizer(self):
        """
        This meyhod generating table
        """
        self.restore_table()
        self.__adding_needed_features()
        self.__adding_random_features()
        self.__creating_characters()

    def __adding_needed_features(self):
        """
        This method adds needed features into sets of features
        """
        for i in range(len(self.needed_features)):
            for a in range(len(self.needed_features[i])):
                try:
                    self.__features_on_table[i].add(self.needed_features[i][a])
                except IndexError:
                    pass

    def __adding_random_features(self):
        """
        This method adds random features into sets of features
        """
        index_features = get_count_of_fetures(self.all_features)
        for i in range(len(self.__features_on_table)):
            if i != 0 and i != 9:
                while len(self.__features_on_table[i]) < self.count_of_characters:
                    item = RandGenerator.choice(index_features[i])
                    self.__features_on_table[i].add(item)
            elif i == 9:
                while len(self.__features_on_table[i]) < self.count_of_characters:
                    item = RandGenerator.choice(index_features[i-1])
                    self.__features_on_table[i].add(item)

    def __transition_data_to_lists(self):
        """
        This method transforms characteristics frpm sets to lists
        """
        features = [[], [], [], [], [], [], [], [], [], []]
        for i in range(len(features)):
            for a in range(len(self.__table)):
                if len(self.__features_on_table[i]) != 0:
                    item = self.__features_on_table[i].pop()
                    features[i].append(item)
                    self.__features_on_table[i].discard(item)
                else:
                    features[i].append([])
        return features

    def __creating_characters(self):
        """
        This method creates characters from sets of features
        """
        features = self.__transition_data_to_lists()
        for i in range(len(self.__features_on_table)):
            for a in reversed(range(len(self.__table))):
                item = RandGenerator.choice(features[i])
                self.__table[a].append(item)
                features[i].remove(item)

    def restore_table(self):
        """
        This method clears lists of characteristics
        """
        length_features = len(self.__features_on_table)
        length_table = self.count_of_characters

        self.__features_on_table = []
        self.__table = []

        for i in range(length_features):
            self.__features_on_table.append(set())

        for i in range(length_table):
            self.__table.append([])

    def __pretty_table(self):
        """
        this method returns prettyful output of bunker table
        """
        self.__table_randomizer()
        table = self.__table
        features = self.all_features

        output = ''
        for i in range(len(table)):
            character = ''
            character += f'Игрок {i + 1} Характеристики: \n'

            for a in range(len(self.__features_on_table)):
                if a != 0 and a != 9:
                    character += ',\n'
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
                    number_of_feature = int(table[i][a])
                    character += f'{features[a][number_of_feature]}'
                elif a == 9:
                    character += ',\n'
                    character += 'Спец. условие 2: '
                    number_of_feature = int(table[i - 1][a])
                    character += f'{features[a - 1][number_of_feature]}'
                elif a == 0:
                    character += 'Биологическая инфа: '
                    character += self.generator.generate_gender_info()

            character += '\n\n'
            output += character

        return output

    def __metadata(self):

        table = self.__table

        output = ''

        for i in range(len(table[0])):
            for a in range(len(table)):
                output += str(table[i][a]) + ';'
            if i != len(table) - 1:
                output += '\n'

        return output

    def get_table(self):
        time = datetime.now()
        with open(f'/Users/sergeypolyakov/Desktop/Бункер/Table_{time}.txt', 'w') as file:
            file.write(self.__pretty_table())
            file.close()

        print('Стол сгенерирован', end='; ')

        with open(f'/Users/sergeypolyakov/Desktop/Бункер/Table_Metadata_{time}.txt', 'w') as file:
            file.write(self.__metadata())
            file.close()
        print('Метаданные сгенерированны', end='')


class AddGenerator(BunkerTable):
    """This class add-generating features"""

    def __init__(self, link_to_file: str, number_of_feature: int, count_of_features: int, all_features: list,
                 gender_generator: GeneratorBiologicalInformation, needed_features=[]):
        super().__init__(needed_features, all_features)
        if needed_features is None:
            needed_features = []
        self.link_to_file = link_to_file
        self.number_of_feature = number_of_feature
        self.count_of_features = count_of_features
        self.gender_generator = gender_generator

    def __get_features_from_file(self):
        """This method gets a indexes of features"""

        with open(self.link_to_file, 'r') as file:
            features = file.read()
            file.close()
        features = features.split('\n')

        for i in range(len(features)):
            features[i] = features[i].split(';')
        for i in range(len(features)):

            for a in range(len(features[i])):

                if features[i][a] == '':

                    del features[i][a]

                elif a != 0:

                    features[i][a] = int(features[i][a])

        return features

    def __transition_features(self):
        features = self.__get_features_from_file()
        output = []
        for i in range(len(features)):
            for a in range(len(features[i])):
                if a == self.number_of_feature:
                    output.append(features[i][a])
        return output

    def __generate_features(self):
        features = self.__transition_features()
        index_features = get_count_of_fetures(self.all_features)
        generated_features = set()
        if self.number_of_feature != 0:
            while len(generated_features) != self.count_of_features:
                item = RandGenerator.choice(index_features[self.number_of_feature])
                if item not in features:
                    generated_features.add(item)
        else:
            for i in range(self.count_of_features):
                item = self.gender_generator.generate_gender_info()
                generated_features.add(item)
        return generated_features

    def __transition_data_to_list(self):
        features = self.__generate_features()
        output = []
        for i in reversed(range(len(features))):
            item = RandGenerator.choice(list(features))
            output.append(item)
            features.discard(item)
        return output

    def output(self):
        for i in self.__transition_data_to_list():
            print(i)
