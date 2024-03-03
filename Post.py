import matplotlib.pyplot as plt
from Notifications import Notifications, LikeNotifications, CommentNotifications

'''
this class represents a post in the social network.
'''


class Post:
    """
    initializes a new post-
    a post has an owner, type, content(post), likes and comments
    """

    def __init__(self, owner, post_type, post):
        self.owner = owner
        self.post_type = post_type
        self.post = post
        self.likes = []
        self.comments = []

    '''
    like a post-
    only if the user is online he can like the post
    if a user is liking his own post than he wont get a notification
    '''

    def like(self, user):
        if user.online:
            self.likes.append(user)
            note = LikeNotifications(user, self.owner)
            if user != self.owner:
                self.owner.receive_notification(note)
                print("notification to " + self.owner.username + ": " + user.username + " liked your post")

    '''
    comment on a post-
    only if the user is online he can comment on a post
    if a user is commenting on his own post than he wont get a notification
    '''

    def comment(self, user, text):
        if user.online:
            self.comments.append(user)
            note = CommentNotifications(user, self.owner)
            if user != self.owner:
                self.owner.receive_notification(note)
                print(
                    "notification to " + self.owner.username + ": " + user.username + " commented on your post: " + text)


'''
this is a subclass for text posts- it inherits from the post class
'''


class TextPost(Post):
    def __init__(self, owner, post_type, post):
        super().__init__(owner, post_type, post)

    def __str__(self):
        result = f"{self.owner.username} published a post:\n\"{self.post}\"\n"
        return result


'''
this is a subclass for image posts- it inherits from the post class
'''


class ImagePost(Post):
    def __init__(self, owner, post_type, post):
        super().__init__(owner, post_type, post)

    '''
    method to display an image
    the content of the post is the path to the image
    if the file is not found or there was an issue in displaying the image there is an exception
    '''

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


'''
this is a subclass for sale posts- it inherits from the post class
'''


class SalePost(Post):
    """
    initializes a new sale post-
    it inherits from a post an owner, type, content(post), likes and comments
    but also has a price, address and Flag to track if the item is sold
    """

    def __init__(self, owner, post_type, post, price, address):
        super().__init__(owner, post_type, post)
        self.price = price
        self.address = address
        self.is_sold = False

    '''
    this method applies a discount to the sale post
    only the product isn't sold yet and the password entered matches the owners password
    the discount is in percentages
    '''

    def discount(self, discount, password):
        if not self.is_sold:
            if self.owner.check_password(password):
                if discount < 0 or discount > 100:
                    print("invalid discount")
                    return
                self.price = self.price - ((discount * self.price) / 100)
                print("Discount on " + self.owner.username + " product! the new price is: " + str(self.price))

    '''
    this method marks the sale post as sold
    only the product isn't sold yet and the password entered matches the owners password
    '''

    def sold(self, password):
        if not self.is_sold:
            if self.owner.check_password(password):
                print(self.owner.username + "'s product is sold")
                self.is_sold = True

    def __str__(self):
        result = f"{self.owner.username} posted a product for sale:\n"
        if self.is_sold:
            result += "Sold! "
        else:
            result += "For sale! "
        result += f"{self.post}, price: {str(self.price)}, pickup from: {self.address}\n"
        return result


class PostFactory:
    """
    Factory class for creating different types of posts
    check the post type and create a new post
    """

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
