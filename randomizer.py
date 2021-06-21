import random

# Using Cryptographically Secure Pseudo Random Number Generator
CSPRNG = random.SystemRandom()


class BunkerTable:
    
    __features = [i for i in range(0, 30)]
    __professions = [i for i in range(0, 50)]
    __features_on_table = [set(), set(), set(), set(), set(), set(), set(), set()]
    __table = [[], [], [], [], [], [], [], [], [], []]

    def __init__(self, needed_features: list, all_features: list):
        self.needed_features = needed_features
        self.all_features = all_features

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
                    item = CSPRNG.choice(self.__professions)
                    self.__features_on_table[i].add(item)
            else:
                while len(self.__features_on_table[i]) < 10:
                    item = CSPRNG.choice(self.__features)
                    self.__features_on_table[i].add(item)

    def __creating_characters(self):
        """
        This method creates characters from sets of features
        """
        for i in range(10):
            for a in range(8):
                item = self.__features_on_table[a].pop()
                self.__table[i].append(item)
                self.__features_on_table[a].discard(item)

    def __restore_table(self):
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
            character += f'Игрок {i+1} ' \
                         f'Характеристики: \n'
            for a in range(8):
                if a != 0:
                    character += ', '
                number_of_feature = int(table[i][a])
                try:
                    character += f'{features[a][number_of_feature]}'
                except IndexError:
                    print('list index out of range')
            character += '\n\n'
            output += character

        self.__restore_table()

        return output
