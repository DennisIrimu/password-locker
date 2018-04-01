import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    defines the cases for the contact class behaviour
    '''

    def setUp(self):
        '''
        run before each TestCase
        '''
        self.new_user = User("Dnyt","hd","0710682029","test.user.com")

if __name__ == '__main__':
    unittest.main()
