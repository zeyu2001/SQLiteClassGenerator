class Venue(object):
    def __init__(self, VenueName, VenueAddr, Postal):
        self._VenueName = VenueName
        self._VenueAddr = VenueAddr
        self._Postal = Postal

    def set_VenueName(self, new_VenueName):
        self._VenueName = new_VenueName

    def set_VenueAddr(self, new_VenueAddr):
        self._VenueAddr = new_VenueAddr

    def set_Postal(self, new_Postal):
        self._Postal = new_Postal

    def get_VenueName(self, new_VenueName):
        return VenueName

    def get_VenueAddr(self, new_VenueAddr):
        return VenueAddr

    def get_Postal(self, new_Postal):
        return Postal


    def __str__(self):
        result = ''

        return result

    @staticmethod
    def create_table():
        result = ''
        result += 'CREATE TABLE Venue\n'
        result += 'VenueName TEXT \n'
        result += 'VenueAddr TEXT NOT NULL\n'
        result += 'Postal Integer NOT NULL CHECK (Postal > 99999 AND Postal < 1000000)\n'
        result += 'PRIMARY KEY (VenueName)\n'
        return result

    def create_new_record(self):
        result = ''
        result += 'INSERT INTO Venue\n'
        result += '(VenueName, VenueAddr, Postal)\n'
        result += 'VALUES\n'
        result += '(\'{self._VenueName}\', \'{self._VenueAddr}\', \'{self._Postal}\')\n'.format(self=self)
        return result

    def update_record(self):
        result = ''
        result += 'UPDATE Venue SET\n'
        result += '(VenueName = \'{self._VenueName}\', VenueAddr = \'{self._VenueAddr}\', Postal = \'{self._Postal}\').format(self=self)\n'
        result += 'WHERE\n'
        result += '(VenueName = \'{self._VenueName}\')\n'.format(self=self)
        return result

class ConcertBooking(object):
    def __init__(self, BookingID, VenueName, ConcertDate):
        self._BookingID = BookingID
        self._VenueName = VenueName
        self._ConcertDate = ConcertDate

    def set_BookingID(self, new_BookingID):
        self._BookingID = new_BookingID

    def set_VenueName(self, new_VenueName):
        self._VenueName = new_VenueName

    def set_ConcertDate(self, new_ConcertDate):
        self._ConcertDate = new_ConcertDate

    def get_BookingID(self, new_BookingID):
        return BookingID

    def get_VenueName(self, new_VenueName):
        return VenueName

    def get_ConcertDate(self, new_ConcertDate):
        return ConcertDate


    def __str__(self):
        result = ''

        return result

    @staticmethod
    def create_table():
        result = ''
        result += 'CREATE TABLE ConcertBooking\n'
        result += 'BookingID TEXT \n'
        result += 'VenueName TEXT NOT NULL\n'
        result += 'ConcertDate Date NOT NULL\n'
        result += 'PRIMARY KEY (BookingID)\n'
        result += 'FOREIGN KEY (VenueName) REFERENCES Venue (VenueName)\n'
        return result

    def create_new_record(self):
        result = ''
        result += 'INSERT INTO ConcertBooking\n'
        result += '(BookingID, VenueName, ConcertDate)\n'
        result += 'VALUES\n'
        result += '(\'{self._BookingID}\', \'{self._VenueName}\', \'{self._ConcertDate}\')\n'.format(self=self)
        return result

    def update_record(self):
        result = ''
        result += 'UPDATE ConcertBooking SET\n'
        result += '(BookingID = \'{self._BookingID}\', VenueName = \'{self._VenueName}\', ConcertDate = \'{self._ConcertDate}\').format(self=self)\n'
        result += 'WHERE\n'
        result += '(BookingID = \'{self._BookingID}\')\n'.format(self=self)
        return result

class Band(object):
    def __init__(self, BandName, NumberOfMembers):
        self._BandName = BandName
        self._NumberOfMembers = NumberOfMembers

    def set_BandName(self, new_BandName):
        self._BandName = new_BandName

    def set_NumberOfMembers(self, new_NumberOfMembers):
        self._NumberOfMembers = new_NumberOfMembers

    def get_BandName(self, new_BandName):
        return BandName

    def get_NumberOfMembers(self, new_NumberOfMembers):
        return NumberOfMembers


    def __str__(self):
        result = ''

        return result

    @staticmethod
    def create_table():
        result = ''
        result += 'CREATE TABLE Band\n'
        result += 'BandName TEXT \n'
        result += 'NumberOfMembers Integer NOT NULL CHECK (NumberOfMembers > 0)\n'
        result += 'PRIMARY KEY (BandName)\n'
        return result

    def create_new_record(self):
        result = ''
        result += 'INSERT INTO Band\n'
        result += '(BandName, NumberOfMembers)\n'
        result += 'VALUES\n'
        result += '(\'{self._BandName}\', \'{self._NumberOfMembers}\')\n'.format(self=self)
        return result

    def update_record(self):
        result = ''
        result += 'UPDATE Band SET\n'
        result += '(BandName = \'{self._BandName}\', NumberOfMembers = \'{self._NumberOfMembers}\').format(self=self)\n'
        result += 'WHERE\n'
        result += '(BandName = \'{self._BandName}\')\n'.format(self=self)
        return result

class BandBooking(object):
    def __init__(self, BandName, BookingID, Headlining):
        self._BandName = BandName
        self._BookingID = BookingID
        self._Headlining = Headlining

    def set_BandName(self, new_BandName):
        self._BandName = new_BandName

    def set_BookingID(self, new_BookingID):
        self._BookingID = new_BookingID

    def set_Headlining(self, new_Headlining):
        self._Headlining = new_Headlining

    def get_BandName(self, new_BandName):
        return BandName

    def get_BookingID(self, new_BookingID):
        return BookingID

    def get_Headlining(self, new_Headlining):
        return Headlining


    def __str__(self):
        result = ''

        return result

    @staticmethod
    def create_table():
        result = ''
        result += 'CREATE TABLE BandBooking\n'
        result += 'BandName TEXT \n'
        result += 'BookingID  \n'
        result += 'Headlining  NOT NULL DEFAULT 0\n'
        result += 'PRIMARY KEY (BandName, BookingID)\n'
        result += 'FOREIGN KEY (BandName) REFERENCES Band (BandName)\n'
        result += 'FOREIGN KEY (BookingID) REFERENCES ConcertBooking (BookingID)\n'
        return result

    def create_new_record(self):
        result = ''
        result += 'INSERT INTO BandBooking\n'
        result += '(BandName, BookingID, Headlining)\n'
        result += 'VALUES\n'
        result += '(\'{self._BandName}\', \'{self._BookingID}\', \'{self._Headlining}\')\n'.format(self=self)
        return result

    def update_record(self):
        result = ''
        result += 'UPDATE BandBooking SET\n'
        result += '(BandName = \'{self._BandName}\', BookingID = \'{self._BookingID}\', Headlining = \'{self._Headlining}\').format(self=self)\n'
        result += 'WHERE\n'
        result += '(BandName = \'{self._BandName}\', BookingID = \'{self._BookingID}\')\n'.format(self=self)
        return result

