from User import User


class SocialNetwork:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(SocialNetwork, cls).__new__(cls)
            print("The social network {} was created!".format(args[0]))
        return cls.instance

    def __init__(self, name):
        self.name = name
        self.users = []
        self.usernames = []
        self.logged_in = []

    def sign_up(self, username, password):
        if username not in self.usernames:
            if 3 < len(password) < 9:
                user = User(username, password)
                self.users.append(user)
                self.usernames.append(username)
                self.logged_in.append(username)
                return user
            else:
                return "Password length must be between 4 and 8 characters"
        else:
            return "Username taken - choose new one"

    def log_in(self, username, password):
        for user in self.users:
            if user.username == username and user.check_password(password):
                self.logged_in.append(username)
                print(user.username + " connected")
                user.logged_in = True
                return
        return "Invalid username or password"

    def log_out(self, username):
        if username in self.logged_in:
            self.logged_in.remove(username)
            print(username + " disconnected")
            for user in self.users:
                if user.username == username:
                    user.logged_in = False
        else:
            print("User not logged in")

    def __str__(self):
        result = self.name + " social network:\n"
        for user in self.users:
            result += "User name: " + user.username + ", Number of posts: " + str(
                user.get_num_of_posts()) + ", Number of followers: " + str(user.get_num_of_followers()) + "\n"
        return result
