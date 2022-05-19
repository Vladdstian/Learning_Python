# how to create a class

# constructor
class User:
    def __init__(self, user_id, username):  # __init__() -> used to initialise the attributes
        # self is the actual object that is being initialised
        # parameters are put into constructors when it is strictly necessary as information to create an object
        # other attributes can be created and assigned a default value
        # for example like the followers on instagram - you always start at 0 and you don;t need this information to
        # create a user
        self.followers = 0
        self.following = 0
        self.username = username
        self.user_id = user_id
        print("new user being created")
    # in addition to the attributes we can create methods
    # the methods are the things that the object does

    def follow(self, user):  # method to follow somebody
        user.followers += 1
        self.following += 1


user_1 = User("001", "vlad")
# user_1.id = "001"
# user_1.username = "Vlad"
# attributes can be added later when creating the object, but it's not indicated

user_2 = User("002", "Anca")
# user_2.id = "001"  # it's not good practice to add attributes directly on the object
# user_2.name = "vlad"  # it's easy to create mistakes like this and to put name instead of username

user_1.follow(user_2)
print(user_1.username)
print(user_1.followers)
print(user_1.following)
print(user_2.username)
print(user_2.followers)
print(user_2.following)

def function():
    pass  # pass works with functions and classes when we want them empty

# naming conventions: PascalCase -> for classes, snake_case -> everything else
