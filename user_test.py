import unittest #Importing the unittest module
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the User class behaviors
    
    Arg:
        unittest.Testcase: A TestCase class that helps in creating test case classes
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_User = User("Amar", "Bravo",  "amarbravo@gmail.com", "Bravo254")

    def test_init(self):
        '''
        test case to test if the object has been properly initialized
        '''

        self.assertEqual(self.new_User.first_name,"Amar")
        self.assertEqual(self.new_User.last_name,"Bravo")
        self.assertEqual(self.new_User.user_email,"amarbravo@gmail.com")
        self.assertEqual(self.new_User.user_password,"Bravo254")

if __name__ == '__main__':
    unittest.main()

