'''
Module that stores classes representing data models
'''


class User:
    '''
    Class that represents user info
    '''

    def __init__(self, id: int, state: ..., general_progress: int,
                 test_progress: list[int], settings: dict[str, bool | int]):
        '''
        User class constructor

        :param id: user id
        :param state: user state
        :param general_progress: user progress in learning general mode
        :param test_progress: user progress in tests
        :param settings: user settings
        '''
        
        self._id = id
        self._state = state
        self._general_progress = general_progress
        self._test_progress = test_progress
        self._settings = settings
