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
    __features_on_table = [set(), set(), set(), set(), set(), set(), set(), set()]
    __table = [[], [], [], [], [], [], [], [], [], []]

    def __init__(self, needed_features: list, all_features: list, generator=GeneratorBiologicalInformation()):
        self.needed_features = needed_features
        self.all_features = all_features
        self.generator = generator

    def table_generator(self):
        """
        This meyhod generating table
        """
        self.__adding_needed_features()
        self.__adding_random_features()
        self.__creating_characters()

    def __adding_needed_features(self):
        """
        This method adds needed features into sets of features
        """
        for i in range(len(self.needed_features)):
            for a in range(len(self.needed_features[i])):
                self.__features_on_table[i].add(self.needed_features[i][a])

    def __adding_random_features(self):
        """
        This method adds random features into sets of features
        """
        for i in range(8):
            if i == 1:
                while len(self.__features_on_table[i]) < 10:
                    item = RandGenerator.choice(self.__professions)
                    self.__features_on_table[i].add(item)
            else:
                while len(self.__features_on_table[i]) < 10:
                    item = RandGenerator.choice(self.__features)
                    self.__features_on_table[i].add(item)

    def __transition_data_to_lists(self):
        """
        This method transforms characteristics frpm sets to lists
        """
        features = [[], [], [], [], [], [], [], []]
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
        for i in range(8):
            for a in reversed(range(10)):
                try:
                    item = RandGenerator.choice(features[i])
                    self.__table[a].append(item)
                    features[i].remove(item)
                except IndexError:
                    print('list index out of range')

    def restore_table(self):
        """
        This method clears lists of characteristics
        """
        self.__features_on_table = [set(), set(), set(), set(), set(), set(), set(), set()]
        self.__table = [[], [], [], [], [], [], [], [], [], []]

    def pretty_output(self):
        """
        this method returns prettyful output of bunker table
        """

        table = self.__table
        features = self.all_features

        output = ''

        for i in range(10):

            character = ''
            character += f'Игрок {i + 1} Характеристики: \n'

            for a in range(8):

                if a != 0:

                    character += '\n'

                    number_of_feature = int(table[i][a])
                    character += f'{features[a][number_of_feature]}'

                else:
                    character += self.generator.generate_biological_info()

            character += '\n\n'
            output += character

        self.restore_table()

        return output
