import random
from generator import GeneratorBiologicalInformation

# Using Cryptographically Secure Pseudo Random Number Generator
RandGenerator = random.SystemRandom()


class BunkerTable:
    """
    This class creates a table of Bunker game
    """

    # Lists with indexes of characteristics
    __features = [i for i in range(0, 30)]
    __professions = [i for i in range(0, 50)]

    # Lists for work with characteristics
    __features_on_table = [set(), set(), set(), set(), set(), set(), set(), set(), set(), set()]
    __table = [[], [], [], [], [], [], [], [], [], []]

    def __init__(self, needed_features: list, all_features: list, generator=GeneratorBiologicalInformation(),
                 count_of_characters: int = 10):
        self.needed_features = needed_features
        self.all_features = all_features
        self.generator = generator
        self.count_of_characters = count_of_characters

    def table_generator(self):
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
        for i in range(len(self.__features_on_table)):
            if i == 1:
                while len(self.__features_on_table[i]) < self.count_of_characters:
                    item = RandGenerator.choice(self.__professions)
                    self.__features_on_table[i].add(item)
            elif i == 10:
                while len(self.__features_on_table[i]) < self.count_of_characters:
                    item = RandGenerator.choice(self.__features)
                    print(item, self.__features_on_table[i-1])
                    self.__features_on_table[i].add(item)
            elif i != 1 and i != 10:
                while len(self.__features_on_table[i]) < self.count_of_characters:
                    item = RandGenerator.choice(self.__features)
                    self.__features_on_table[i].add(item)

    def __transition_data_to_lists(self):
        """
        This method transforms characteristics frpm sets to lists
        """
        features = [[], [], [], [], [], [], [], [], [], []]
        for i in range(len(features)):
            for a in range(len(self.__table)):
                item = self.__features_on_table[i].pop()
                features[i].append(item)
                self.__features_on_table[i].discard(item)
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

    def pretty_output(self):
        """
        this method returns prettyful output of bunker table
        """

        table = self.__table
        features = self.all_features

        output = ''
        for i in range(len(table)):
            character = ''
            character += f'Игрок {i + 1} Характеристики: \n'

            for a in range(len(self.__features_on_table)):
                if a != 0 and a != 9:
                    character += ',\n'
                    number_of_feature = int(table[i][a])
                    character += f'{features[a][number_of_feature]}'
                elif a == 9:
                    character += ',\n'
                    number_of_feature = int(table[i-1][a])
                    character += f'{features[a-1][number_of_feature]}'
                elif a == 0:
                    character += self.generator.generate_gender_info()

            character += '\n\n'
            output += character

        self.restore_table()

        return output
