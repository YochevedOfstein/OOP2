from Post import PostFactory
from Notifications import Notifications, PostNotifications


class User:

    def __init__(self, username, password):
        self.username = username
        self._password = password
        self.following = []
        self.followers = []
        self.posts = []
        self.notifications = []
        self.logged_in = True

    def follow(self, other_user):
        if self.logged_in:
            if other_user not in self.following:
                self.following.append(other_user)
                other_user.followers.append(self)
                print(self.username + " started following " + other_user.username)

    def unfollow(self, other_user):
        if self.logged_in:
            if other_user in self.following:
                self.following.remove(other_user)
                other_user.followers.remove(self)
                print(self.username + " unfollowed " + other_user.username)

    def publish_post(self, post_type, post, *args):
        if self.logged_in:
            final_post = PostFactory.create_post(self, post_type, post, *args)
            self.posts.append(final_post)
            for user in self.followers:
                note = PostNotifications(self, user)
                user.receive_notification(note)
            return final_post

    def get_num_of_posts(self):
        return len(self.posts)

    def get_num_of_followers(self):
        return len(self.followers)

    def check_password(self, password):
        if password != self._password:
            return False
        else:
            return True

    def print_notifications(self):
        print(self.username + "'s notifications:")
        for notification in self.notifications:
            print(notification)

    def __str__(self):
        result = f"User name: {self.username}, Number of posts: {str(self.get_num_of_posts())}, Number of followers: {str(self.get_num_of_followers())}"
        return result

    def receive_notification(self, notification):
        self.notifications.append(notification)
