import praw

reddit = praw.Reddit(client_id = 'ErnAbet5rZVdDA',
                     client_secret = 'iYtFzzqO-x2Yfv5L3Vt06k1Y8ug',
                     user_agent='prawtutorial1v1'
                     )

keyword = 'is'

for post in reddit.subreddit('all').stream.submissions():
     try:
         if keyword in post.title:
             print (post.title)
             print  (post.permalink)
             print  ('----------------------------------------------------------------------------------------------')
     except UnicodeEncodeError:
             print ('emoji')