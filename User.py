from Post import PostFactory
from Notifications import Notifications, PostNotifications

'''
this class represents a user in the social network.
'''


class User:

    """
    initializes a new User-
    a user has a username, password, list of followers, list of following, posts, notifications
    and an online attribute set to true if user is online
    """
    def __init__(self, username, password):
        self.username = username
        self._password = password
        self.following = []
        self.followers = []
        self.posts = []
        self.notifications = []
        self.online = True

    '''
    follow another user-
    only if the user is online and the isn't already following the other user
    '''
    def follow(self, other_user):
        if self.online:
            if other_user not in self.following:
                self.following.append(other_user)
                other_user.followers.append(self)
                print(self.username + " started following " + other_user.username)

    '''
    unfollow another user-
    only if the user is online and the is following the other user
    '''
    def unfollow(self, other_user):
        if self.online:
            if other_user in self.following:
                self.following.remove(other_user)
                other_user.followers.remove(self)
                print(self.username + " unfollowed " + other_user.username)

    '''
    publish a post-
    only if the user is online this method notifies all of the user's followers about the new post 
    by creating PostNotifications 
    '''
    def publish_post(self, post_type, post, *args):
        if self.online:
            final_post = PostFactory.create_post(self, post_type, post, *args)
            self.posts.append(final_post)
            for user in self.followers:
                note = PostNotifications(self, user)
                user.receive_notification(note)
            return final_post

    """
    gets the number of posts
    """
    def get_num_of_posts(self):
        return len(self.posts)

    """
    gets the number of followers the user has
    """
    def get_num_of_followers(self):
        return len(self.followers)

    '''
    checks if the provided password matches the user's password
    '''
    def check_password(self, password):
        return password == self._password

    """
    print notifications the user has received
    """
    def print_notifications(self):
        print(self.username + "'s notifications:")
        for notification in self.notifications:
            print(notification)

    def __str__(self):
        result = f"User name: {self.username}, Number of posts: {str(self.get_num_of_posts())}, Number of followers: {str(self.get_num_of_followers())}"
        return result

    '''
    method allows users to receive notifications
    When a user is notified about a new post, like, or comment, they update their notification list
    '''
    def receive_notification(self, notification):
        self.notifications.append(notification)
