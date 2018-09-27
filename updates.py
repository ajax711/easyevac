import praw

reddit = praw.Reddit(client_id = '',
                     client_secret = '',
                     user_agent=''
                     )

keyword = 'flood'

for post in reddit.subreddit('all').stream.submissions():
     try:
         if keyword in post.title:
             print (post.title)
             print  (post.permalink)
             print  ('----------------------------------------------------------------------------------------------')
     except UnicodeEncodeError:
             print ('emoji')
