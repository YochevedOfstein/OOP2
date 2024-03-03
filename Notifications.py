"""
base class for notifications
each notification has a sender and a receiver
"""


class Notifications:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver


"""
subclass for post notifications
"""


class PostNotifications(Notifications):
    def __init__(self, sender, receiver):
        super().__init__(sender, receiver)

    def __str__(self):
        result = f"{self.sender.username} has a new post"
        return result


"""
subclass for like notifications
"""


class LikeNotifications(Notifications):
    def __init__(self, sender, receiver):
        super().__init__(sender, receiver)

    def __str__(self):
        result = f"{self.sender.username} liked your post"
        return result


"""
subclass for comment notifications
"""


class CommentNotifications(Notifications):
    def __init__(self, sender, receiver):
        super().__init__(sender, receiver)

    def __str__(self):
        result = f"{self.sender.username} commented on your post"
        return result
