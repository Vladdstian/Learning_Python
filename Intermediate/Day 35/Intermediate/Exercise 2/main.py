# The code will crash and give you a KeyError.
# This is because some posts in the facebook_posts don't have any "Likes".

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

# my 1st try
# try:
#     for post in facebook_posts:
#         total_likes = total_likes + post['Likes']
# except KeyError:
#     total_likes = 0
#     for post in facebook_posts:
#         if 'Likes' not in post:
#             post['Likes'] = 0
#         else:
#             total_likes = total_likes + post['Likes']
#

# second better solution
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        post['Likes'] = 0

print(total_likes)


