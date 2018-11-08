class Attribute:

    def __init__(self, attr_name, attr_type, constraint=None, primary_key=False, foreign_key=False):
        self._attr_name = attr_name
        self._attr_type = attr_type
        self._constraint = constraint
        self._primary_key = primary_key
        self._foreign_key = foreign_key

    ''' 
    __str__(): to return a string containing the attr_name, attr_type and contraint separated by a blank space
    '''

    def __str__(self):
        return '{} {} {}'.format(self._attr_name, self._attr_type, self._constraint)

    ''' 
    get_self_str(): [helper function] to return a string:
    # if attr_type is not an integer or float: return "'{self._attribute_name}'"
    # if attr_type is an integer or float: return "{self._attribute_name}"
    '''

    def get_attr_name(self):
        return self._attr_name

    def get_self_str(self):
        if self._attr_type == 'INTEGER' or self._attr_type == 'FLOAT':
            return '{' + 'self._{}'.format(self._attr_name) + '}'
        else:
            return "\\'{" + 'self._{}'.format(self._attr_name) + "}\\'"

    '''
    get_equal_str(): [helper function] to return a string:
    # if attr_type is not an integer or float: return "attr_name = '{self._attribute_name}'"
    # if attr_type is an integer or float: return "attr_name = {self._attribute_name}"
    '''

    def get_equal_str(self):
        return '{} = {}'.format(self._attr_name, self.get_self_str())


# Number = Attribute('Number', 'FLOAT', 'NOT NULL')
# print(Number)
# print(Attribute('Number', 'FLOAT', 'NOT NULL').get_self_str())
# print(Attribute('Text', 'TEXT', 'NOT NULL').get_self_str())
# print(Attribute('Number', 'FLOAT', 'NOT NULL').get_equal_str())
# print(Attribute('Text', 'TEXT', 'NOT NULL').get_equal_str())

class SQLiteClass:

    def __init__(self, class_name, attr_list):
        self._class_name = class_name
        self._attr_list = attr_list

    def get_class_name(self):
        return self._class_name

    def get_attr_list(self):
        return self._attr_list

    '''
    generate_tuple_string(attr_list, operation): [helper function] to return a string:
    # attr_list is a list of Attribute objects
    # there are 3 basic kinds of operations: attr_name, self_attr_name, equal_statement
    # If operation == "attr_name": the function should return a string in the format of "attr_name1, attr_name2, ..."
    # If operation == "self_str": the function should return a string in the format of "{self._attr_name1}, '{self._attr_name2}', ..."
    # If operation == "equal_str": the function should return a string in the format of "attr_name1 = {self._attr_name1}, attr_name2 = '{self._attr_name2}', ..."
    '''

    @staticmethod
    def generate_tuple_string(attr_list, operation):
        if operation == 'attr_name':
            result = ''
            for attr in attr_list:
                result += '{}, '.format(attr.get_attr_name())
            return result[:-2]

        if operation == 'self_str':
            result = ''
            for attr in attr_list:
                result += '{}, '.format(attr.get_self_str())
            return result[:-2]

        if operation == 'equal_str':
            result = ''
            for attr in attr_list:
                result += '{}, '.format(attr.get_equal_str())
            return result[:-2]

    '''
    generate_line(num_of_tabs, content): [helper function] to return a string containing the following 3 parts:
    [begin with a string of the num_of_tabs times (4 white spaces)], [content in the middle], [end with a "\n"]
    '''

    @staticmethod
    def generate_line(number_of_tabs, content):
        return number_of_tabs * '{:^4}'.format(' ') + content + '\n'

    '''
    generate_sql_line(content): [helper function] to return a string containing the following 3 parts:
    [begin with "result += \'"], [content in the middle], [end with "\\n\""]
    '''

    @staticmethod
    def generate_sql_line(content):
        return 'result += \'' + content + '\\n\''

    '''
    The Generated SQLite class should contain the following, you may refer to the sample in SQLiteOOP.py: 
    a. initializer, mutator, accessor and dummy __str__() functions
    b. SQLite functions such as create_table(), create_new_record(), update_record() and delete_record()
    '''

    def __str__(self):
        define = 'class {}({}):\n'.format(self.get_class_name(), 'object')
        result = ''

        # INITIALIZER
        init = '{:>4}'.format(' ') + 'def __init__(self'
        for attr in self.get_attr_list():
            init += ', {}'.format(str(attr.get_attr_name()))
        init += '):\n'
        for attr in self.get_attr_list():
            init += self.generate_line(2, 'self._{a} = {a}'.format(a=attr.get_attr_name()))
        init += '\n'
        result += define + init

        # MUTATOR FUNCTIONS
        mutators = ''
        for attr in self.get_attr_list():
            mutators += self.generate_line(1, 'def set_{a}(self, new_{a}):'.format(a=attr.get_attr_name()))
            mutators += self.generate_line(2, 'self._{a} = {b}'.format(a=attr.get_attr_name(),
                                                                       b='new_{}'.format(attr.get_attr_name())))
            mutators += '\n'
        result += mutators

        # ACCESSOR FUNCTIONS
        accessors = ''
        for attr in self.get_attr_list():
            accessors += '{:>4}'.format(' ') + 'def get_{a}(self, new_{a}):\n'.format(a=attr.get_attr_name())
            accessors += '{:>8}'.format(' ') + 'return {}'.format(attr.get_attr_name()) + '\n'
            accessors += '\n'
        result += accessors
        result +='\n'

        # DUMMY STRING FUNCTION
        result += self.generate_line(1, 'def __str__(self):')
        result += self.generate_line(2, 'result = \'\'')
        result += '\n'
        result += self.generate_line(2, 'return result')
        result += '\n'

        # SQLITE - CREATE TABLE
        result += self.generate_line(1, '@staticmethod')
        result += self.generate_line(1, 'def create_table():')
        result += self.generate_line(2, 'result = \'\'')
        result += self.generate_line(2, self.generate_sql_line('CREATE TABLE {}'.format(self.get_class_name())))

        primary_key = []
        foreign_key = []

        for attr in self.get_attr_list():
            result += self.generate_line(2, self.generate_sql_line(str(attr)))
            if attr._primary_key:
                primary_key += [attr]
            if attr._foreign_key:
                foreign_key += [attr]
        result += self.generate_line(
            2, self.generate_sql_line('PRIMARY KEY ({})'.format(self.generate_tuple_string(primary_key, 'attr_name'))))
        for attr in foreign_key:
            result += self.generate_line(
                2, self.generate_sql_line('FOREIGN KEY ({}) REFERENCES {}'.format( \
                    attr.get_attr_name(), attr._foreign_key)))

        result += self.generate_line(2, 'return result')
        result += '\n'

        # SQLITE - CREATE NEW RECORD
        result += self.generate_line(1, 'def create_new_record(self):')
        result += self.generate_line(2, 'result = \'\'')
        result += self.generate_line(2, self.generate_sql_line('INSERT INTO {}'.format(self.get_class_name())))
        result += self.generate_line(2, self.generate_sql_line('({})'.format(
            self.generate_tuple_string(self.get_attr_list(), 'attr_name'))))
        result += self.generate_line(2, self.generate_sql_line('VALUES'))
        result += self.generate_line(2, self.generate_sql_line('({})'.format(
            self.generate_tuple_string(self.get_attr_list(), 'self_str'))))[:-1] + '.format(self=self)' + '\n'

        result += self.generate_line(2, 'return result')
        result += '\n'

        # SQLITE - UPDATE RECORD BASED ON PRIMARY KEY
        result += self.generate_line(1, 'def update_record(self):')
        result += self.generate_line(2, 'result = \'\'')
        result += self.generate_line(2, self.generate_sql_line('UPDATE {} SET'.format(self.get_class_name())))
        result += self.generate_line(2, self.generate_sql_line('({}).format(self=self)'.format(
            self.generate_tuple_string(self.get_attr_list(), 'equal_str'))))
        result += self.generate_line(2, self.generate_sql_line('WHERE'))
        result += self.generate_line(2, self.generate_sql_line('({})'.format(
            self.generate_tuple_string(primary_key, 'equal_str'))))[:-1] + '.format(self=self)' + '\n'

        result += self.generate_line(2, 'return result')
        result += '\n'

        return result

'''
SQLiteClass1 = SQLiteClass('VenueBooking', [Attribute('VenueName', 'TEXT', 'NOT NULL', True),
                                           Attribute('VenueAddress', 'TEXT', 'NOT NULL'),
                                           Attribute('Postal', 'INTEGER',
                                                     'NOT NULL CHECK (Postal > 99999 AND Postal < 1000000)'),
                                           Attribute('BookingID', 'TEXT', 'NOT NULL', True, 'Booking (BookingID)')])
# print(SQLiteClass.generate_tuple_string(SQLiteClass._attr_list, 'attr_name'))
# print(SQLiteClass.generate_tuple_string(SQLiteClass._attr_list, 'self_str'))
# print(SQLiteClass.generate_tuple_string(SQLiteClass._attr_list, 'equal_str'))
print(SQLiteClass1)
'''

class SQLiteClassGenerator():

    def __init__(self):
        self._class_list = []

    def read_file(self, file_name):
        SQLiteClassList = []

        '''SQlite Class Name;Class Attribute;Type;Constraint;Primary Key;Foreign Key'''
        with open(file_name, 'r') as f:
            line = f.readline()[:-1]
            line = f.readline()[:-1]

            class_name = None
            info_list = []
            attr_list = []

            while line:
                if line[0] != ';':
                    if class_name:
                        SQLiteClassList.append(SQLiteClass(class_name, attr_list))
                    attr_list = []
                    info_list = []
                    info_list = line.split(';')
                    class_name, attr_name, attr_type, constraint, primary_key, foreign_key = \
                        info_list[0], info_list[1], info_list[2], info_list[3], info_list[4], info_list[5]
                    attr_list.append(Attribute(attr_name, attr_type, constraint, primary_key, foreign_key))
                else:
                    info_list = line.split(';')
                    attr_name, attr_type, constraint, primary_key, foreign_key = \
                        info_list[1], info_list[2], info_list[3], info_list[4], info_list[5]
                    attr_list.append(Attribute(attr_name, attr_type, constraint, primary_key, foreign_key))
                line = f.readline()[:-1]
            SQLiteClassList.append(SQLiteClass(class_name, attr_list))
            f.close()

        self._class_list = SQLiteClassList
        return self._class_list

    def generate(self):
        with open('SQLiteOOP.py', 'w') as f:
            result = ''
            for clss in self._class_list:
                result += str(clss)
            f.write(result)

SQLiteClassGenerator = SQLiteClassGenerator()
SQLiteClassList = SQLiteClassGenerator.read_file('class_info.csv')
SQLiteClassGenerator.generate()
