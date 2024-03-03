from User import User

'''
this is a class that represents a social network
'''


class SocialNetwork:
    instance = None

    '''
    __new__ creates a new instance of the SocialNetwork class if it doesn't exist already
    this method ensures that only one instance of the SocialNetwork class is created, making it a singleton
    '''

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(SocialNetwork, cls).__new__(cls)
            print("The social network {} was created!".format(args[0]))
        return cls.instance

    '''
    initialize the social network with a name and empty lists:
    list of User objects, list of usernames and list of usernames currently logged in
    '''

    def __init__(self, name):
        self.name = name
        self.users = []
        self.usernames = []
        self.logged_in = []

    '''
    method to sign up a new user
    it Checks if the username is available and if the password length is valid
    if yes- create a new User object and add the user to the lists and set user's online attribute to False
    '''

    def sign_up(self, username, password):
        if username not in self.usernames:
            if 3 < len(password) < 9:
                user = User(username, password)
                self.users.append(user)
                self.usernames.append(username)
                self.logged_in.append(username)
                user.online = True
                return user
            else:
                return "Password length must be between 4 and 8 characters"
        else:
            return "Username taken - choose new one"

    '''
    method to log in a user
    it iterate through users to find the matching username and password
    if found, add the user to the logged_in list and set user's online attribute to False
    '''

    def log_in(self, username, password):
        for user in self.users:
            if user.username == username and user.check_password(password):
                self.logged_in.append(username)
                print(user.username + " connected")
                user.online = True
                return
        return "Invalid username or password"

    '''
    method to log out a user
    remove the user from the logged_in list and set user's online attribute to False
    '''

    def log_out(self, username):
        if username in self.logged_in:
            self.logged_in.remove(username)
            print(username + " disconnected")
            for user in self.users:
                if user.username == username:
                    user.online = False
        else:
            print("User not logged in")

    '''
    method to represent the social network as a string
    '''

    def __str__(self):
        result = self.name + " social network:\n"
        for user in self.users:
            result += "User name: " + user.username + ", Number of posts: " + str(
                user.get_num_of_posts()) + ", Number of followers: " + str(user.get_num_of_followers()) + "\n"
        return result
