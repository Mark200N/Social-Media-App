class User:
    #Intialize user with username, empty posts, followers, and following
    def __init__ (self, username):
        self.username=username
        self.posts=[]
        self.followers = set()
        self.following= set()
        #Add a post with emoji support
        def add_post(self,content):
            self.post.append(content)
            print("Post added!")
        #Display user profile with emojis
        def view_porfile(self):
            print(f"\n---  {self.username}'s Profile ---")
            print(f" Post ({len(self.posts)}):")
            for i ,post in enumerate(self.posts,1):
                print(f"{i}.{post}")
            print (f"  Followers({len(self.followers)}):{','.join(self.followers)if self.followers else'None'}")
            print (f"  Following({len(self.following)}):{','.join(self.following)if self.following else'None'}") 
        #Follow another user with notification
        def follow (self,other_user):
            if other_user.username !=self.username:
                self.following.add(other_user.username)
                other_user.followers.add(self.username)
                print(f" You are now following {other_user.username}!")
            else:
                print("  Cannot follow yourself!")
Class Social Media App:
