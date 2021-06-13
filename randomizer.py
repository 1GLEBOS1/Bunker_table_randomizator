import random

# Using Cryptographically Secure Pseudo Random Number Generator
CSPRNG = random.SystemRandom()


class BunkerTable:
    
    __features = [i for i in range(1, 31)]
    __professions = [i for i in range(1, 51)]
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

    def pretty_output(self):
        """
        this method returns prettyful output of bunker table
        """

        table = self.__table

        output = f'''
        Character 1:
        {table[0][0]}, {table[0][1]}, {table[0][2]}, {table[0][3]}, {table[0][4]}, {table[0][5]}, {table[0][6]}, {table[0][7]}
        
        Character 2:
        {table[1][0]}, {table[1][1]}, {table[1][2]}, {table[1][3]}, {table[1][4]}, {table[1][5]}, {table[1][6]}, {table[1][7]}
        
        Character 3:
        {table[2][0]}, {table[2][1]}, {table[2][2]}, {table[2][3]}, {table[2][4]}, {table[2][5]}, {table[2][6]}, {table[2][7]}
        
        Character 4:
        {table[3][0]}, {table[3][1]}, {table[3][2]}, {table[3][3]}, {table[3][4]}, {table[3][5]}, {table[3][6]}, {table[3][7]}
        
        Character 5:
        {table[4][0]}, {table[4][1]}, {table[4][2]}, {table[4][3]}, {table[4][4]}, {table[4][5]}, {table[4][6]}, {table[4][7]}
        
        Character 6:
        {table[5][0]}, {table[5][1]}, {table[5][2]}, {table[5][3]}, {table[5][4]}, {table[5][5]}, {table[5][6]}, {table[5][7]}
        
        Character 7:
        {table[6][0]}, {table[6][1]}, {table[6][2]}, {table[6][3]}, {table[6][4]}, {table[6][5]}, {table[6][6]}, {table[6][7]}
        
        Character 8:
        {table[7][0]}, {table[7][1]}, {table[7][2]}, {table[7][3]}, {table[7][4]}, {table[7][5]}, {table[7][6]}, {table[7][7]}
        
        Character 9:
        {table[8][0]}, {table[8][1]}, {table[8][2]}, {table[8][3]}, {table[8][4]}, {table[8][5]}, {table[8][6]}, {table[8][7]}
        
        Character 10:
        {table[9][0]}, {table[9][1]}, {table[9][2]}, {table[9][3]}, {table[9][4]}, {table[9][5]}, {table[9][6]}, {table[9][7]}
        '''
        return output
