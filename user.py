class user:
    '''
    class that generates new instance of user
    '''

    def __init__(self, first_name, last_name, email, user_password):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_password = user_password
        self.loggedIn = True