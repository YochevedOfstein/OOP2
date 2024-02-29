

import matplotlib.pyplot as plt
from Notifications import Notifications, LikeNotifications, CommentNotifications


class Post:

    def __init__(self, owner, post_type, post):
        self.owner = owner
        self.post_type = post_type
        self.post = post
        self.likes = []
        self.comments = []

    def like(self, user):
        self.likes.append(user)
        note = LikeNotifications(user, self.owner)
        self.owner.receive_notification(note)
        print("notification to " + self.owner.username + ": " + user.username + " liked your post")

    def comment(self, user, text):
        self.comments.append(user)
        note = CommentNotifications(user, self.owner)
        self.owner.receive_notification(note)
        print("notification to " + self.owner.username + ": " + user.username + " commented on your post: " + text)


class TextPost(Post):
    def __init__(self, owner, post_type, post):
        super().__init__(owner, post_type, post)

    def __str__(self):
        result = f"{self.owner.username} published a post:\n\"{self.post}\"\n"
        return result


class ImagePost(Post):
    def __init__(self, owner, post_type, post):
        super().__init__(owner, post_type, post)

    def display(self):
        image_path = self.post
        try:
            image = plt.imread(image_path)
            plt.imshow(image)
            plt.axis(False)
            plt.show()
            print("Shows picture")
        except FileNotFoundError:
            print("Image not found")
        except Exception as e:
            print("An error occurred while displaying the image:", str(e))

    def __str__(self):
        result = self.owner.username + " posted a picture\n"
        return result


class SalePost(Post):
    def __init__(self, owner, post_type, post, price, address):
        super().__init__(owner, post_type, post)
        self.price = price
        self.address = address
        self.sold_items = []

    def discount(self, discount, password):
        if self.owner.check_password(password):
            if discount < 0 or discount > 100:
                print("invalid discount")
                return
            self.price = self.price - ((discount * self.price) / 100)
            print("Discount on " + self.owner.username + " product! the new price is: " + str(self.price))

    def sold(self, password):
        if self.owner.check_password(password):
            print(self.owner.username + "'s product is sold")
            self.sold_items.append(self)

    def check_if_sold(self):
        for post in self.sold_items:
            return True
        return False

    def __str__(self):
        result = f"{self.owner.username} posted a product for sale:\n"
        if self.check_if_sold() is True:
            result += "Sold! "
        else:
            result += "For sale! "
        result += f"{self.post}, price: {str(self.price)}, pickup from: {self.address}\n"
        return result


class PostFactory:
    @staticmethod
    def create_post(owner, post_type, post, *args):
        if post_type == "Text":
            post = TextPost(owner, post_type, post)
            print(post)
            return post
        elif post_type == "Image":
            post = ImagePost(owner, post_type, post)
            print(post)
            return post
        elif post_type == "Sale":
            post = SalePost(owner, post_type, post, *args)
            print(post)
            return post
        else:
            print("Invalid post")
