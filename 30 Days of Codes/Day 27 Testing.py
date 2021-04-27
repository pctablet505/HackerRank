
class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        return []

class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        arr=[1,4,2,7,9,0,12]
        return arr

    @staticmethod
    def get_expected_result():
        return 5

class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        arr=[1,2,3,4,6,7,8,1,23,45]
        return arr

    @staticmethod
    def get_expected_result():
        return 0

