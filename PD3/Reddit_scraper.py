import praw
import pandas as pd

# Read-only instance
reddit_read_only = praw.Reddit(client_id="eohfRX2A2nOhO1ukIupt9A",         # your client id
                               client_secret="j1_suL8YsXrkuA8vmCkVqQwisbH24Q",      # your client secret
                               user_agent="windows:com.example.myredditapp:v0.0.1 (by u/I_hate_redd_it)")        # your user agent
 
# Authorized instance
reddit_authorized = praw.Reddit(client_id="eohfRX2A2nOhO1ukIupt9A",         # your client id
                                client_secret="j1_suL8YsXrkuA8vmCkVqQwisbH24Q",      # your client secret
                                user_agent="windows:com.example.myredditapp:v0.0.1 (by u/I_hate_redd_it)",        # your user agent
                                username="I_hate_redd_it ",        # your reddit username
                                password="rekordskoczni102")        # your reddit password

subreddit = reddit_read_only.subreddit("Warthunder")

# Display the name of the Subreddit
print("Display Name:", subreddit.display_name)
 
# Display the title of the Subreddit
print("Title:", subreddit.title)
 
# Display the description of the Subreddit
print("Description:", subreddit.description)

posts = subreddit.top("year", limit=10000000)

posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }
 
post_count = 0

for post in posts:
    post_count += 1
    # Title of each post
    posts_dict["Title"].append(post.title)
    
    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)
    
    # Unique ID of each post
    posts_dict["ID"].append(post.id)
    
    # The score of a post
    posts_dict["Score"].append(post.score)
    
    # Total number of comments inside the post
    posts_dict["Total Comments"].append(post.num_comments)
    
    # URL of each post
    posts_dict["Post URL"].append(post.url)
 
# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
top_posts.to_csv("re_posts.csv", index=False)

print("Post count: " + str(post_count))