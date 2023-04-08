''''To scrap Instagram, we will use a library know as instaloader which provides us with an API for scraping Instagram. 
You can install this library by using the pip method in your terminal – pip install instaloader. 
Now If you have installed this package then let’s get started with the task.''''

#Scraping Instagram with Python

# Import the module

get_ipython().system('pip install instaloader')
import instaloader

# Create an instance of Instaloader class
bot = instaloader.Instaloader()

# Load a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'munigantirohith')
print(profile)

print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio: ", profile.biography,profile.external_url)


# # Now let’s see how you can log in to your Instagram profile using python:

# Login with username and password in the script
bot.login(user="your username",passwd="your password"

# Interactive login on terminal
bot.interactive_login("your username") # Asks for password in the terminal         

# # Scraping Instagram Followers and Followees

#Scraping your followers and followees will help you in getting a list of their usernames, 
which you will require to do when you will work in a professional environment in the data science field:

# Retrieve the usernames of all followers
followers = [follower.username for follower in profile.get_followers()]

# Retrieve the usernames of all followees
followees = [followee.username for followee in profile.get_followees()]
print(followers)


# # Downloading Posts from Another Profile

Getting posts from any profile is easy in python. We just need to use get_posts(). 
I will this method on the profile of someone else. To download each post, we need to loop over the generator object using.

#download_post() method. Now let’s go through this:

# Load a new profile
profile = instaloader.Profile.from_username(bot.context, 'wwe')

# Get all posts in a generator object
posts = profile.get_posts()

# Iterate and download
for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")

