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
class SocialMediaApp:
    #Intialize app with empty user database
    def __inti__(self):
      self.users={}
    #Register a new user
    def register_user(self):
        username  =input("Enter username")
        if username in self.users:
            print (" Username already exists!")
        else:
            self.users[username] =User(username)
            print (f" User{username} registered!")
    #Make a post for a user
    def make_post(self):
         username=input("Enter username:")
         if username in self.users:
             content =input("Enter your post(you cna use emojis  ):")
             self.users[username].add_post(content)
         else:
             print(" User not found!")
    #View a user's profile
    def view_profile(self):
        username = input("Enter username:")
        if username in self.users:
            self.users[username].view_profile()
        else:
            print("  User not found!")
    # Follow another user
    def follow_user(self):
        follower = input("Enter your username:")
        followee = input("Enter username to follow:")
        if follower in self.users and followee in self.users:
            self.users[follower].follow(self.users[followee])
        else:
            print(" User(s) not found!")
    #Display command menu
    def menu(self):
      while True:
          print("\n--- Social Media App ---")
          print("1. Register User ")
          print("2. Make Post ")
          print("3. View Profile ")
          print("4. Follow User ")
          print("5. Exit ")
          choice = input("Choose an option:")
          if choice == "1":
              self.register_user()
          elif choice == "2":
              self.make_post()
          elif choice == "3":
              self.view_profile()
          elif choice == "4":
              self.follow_user()
          elif choice == "5":
              print(" GoodBye!")
              break
          else:
              print("Invaild choice")
# Run the app
app = SocialMediaApp()
app.menu()