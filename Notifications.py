class Notifications:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver


class PostNotifications(Notifications):
    def __init__(self, sender, receiver):
        super().__init__(sender, receiver)

    def __str__(self):
        result = f"{self.sender.username} has a new post"
        return result


class LikeNotifications(Notifications):
    def __init__(self, sender, receiver):
        super().__init__(sender, receiver)

    def __str__(self):
        result = f"{self.sender.username} liked your post"
        return result


class CommentNotifications(Notifications):
    def __init__(self, sender, receiver):
        super().__init__(sender, receiver)

    def __str__(self):
        result = f"{self.sender.username} commented on your post"
        return result
