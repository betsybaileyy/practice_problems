'''
You’re working an internship at Twitter and are tasked to 
improve suggestions for accounts to follow, which already 
works great for established accounts because it uses content 
from your tweets and other accounts you follow to suggest 
new ones. However, when a new user signs up none of this 
information exists yet, but Twitter still wants to make 
some follow suggestions. Your team asked you to implement 
a function that accepts a new user’s handle and an array 
of many other users’ handles, which could be very long – 
Twitter has over 330 million active accounts! You need to 
calculate a similarity score between a pair of handles by 
looking at the letters each contains, scoring +1 for each 
letter in the alphabet that occurs in both handles but 
scoring –1 for each letter that occurs in only one handle. 
Your function should return k handles from the array that 
have the highest similarity score to the new user’s handle.

Example execution:

handles = ['DogeCoin', 'YangGang2020', 'HodlForLife', 
'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']

suggest('iLoveDogs', handles, k=2)   

should return   ['GodIsLove', 'DogeCoin']

'''

# ------- MAIN TAKEAWAYS ---------
#
# 1.) Take in a user's handle AND an array of many other user handles
#   
#   ---- INPUTS ---- 
#   a.) USER HANDLE [string]
#   b.) ARRAY OF MANY USER HANDLES [list of strings]
#   c.) HOW MANY HANDLE MATCHES TO RETURN (k) [int]
#   ----------------
#
# 2.) Calculate "similarity score" between given user handle 
#     and each user handle given in the array. 
#
#    a.) for each letter that occurs in BOTH handles 
#     --- SCORE: +1 ---
#
#    b.) for each letter that occurs in only ONE handle
#     --- SCORE: -1 ---
#
# 3.) Return the (k) number of handles with the highest 
#     "similarity score" to the original user handle.
#  
#     ---- OUTPUTS ----
#     a.) LIST OF USER HANDLES WITH HIGHEST 
#         SIMILARITY SCORE [list of strings]
#     -----------------
#