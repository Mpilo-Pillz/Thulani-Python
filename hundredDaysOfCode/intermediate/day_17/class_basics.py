class User:
    # pass
    def __init__(self, user_id, username):
        # Attributes are the things the object has
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


#         Methods are the things the objects does


user_1 = User("002", "pillz")
user_2 = User("003", "Fika")

# user 2 will have 1 follower
user_1.follow(user_2);

print("User1 followers-->", user_1.followers)
print("User1 following-->", user_1.following)

print("User2 followers-->", user_2.followers)
print("User2 following-->", user_2.following)

# user_admin = User()
# user_admin.id = "001"
# user_admin.username = "mpilo"


print(user_1.username)
