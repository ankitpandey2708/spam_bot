import fb                     #https://pypi.python.org/pypi/fb/0.4.0
from facepy import GraphAPI   #https://pypi.python.org/pypi/facepy/1.0.9

#https://developers.facebook.com/tools/explorer/
#Insert user access token here Make sure that you have checked checkbox labeled as ‘publish_action’.
token = ""
facebook = fb.graph.api(token)
graph1 = GraphAPI(token)
    
id = input("Enter victim's Facebook id: ")  #https://findmyfbid.com/
query = str(id) + "/posts?fields=id&limit=5" #max limit of posts =100
r = graph1.get(query)
print(r)

posts = [x['id'] for x in r['data']]

nos = int(input("Enter number of posts to be spammed with comments: "))
mess = input("Enter the message to be commented: ")
if nos <= len(posts):
    for i in posts[:nos]:
        facebook.publish(cat = "comments", id = i, message = mess) #Comments on each post
        #facebook.publish(cat = "likes", id = i) #Likes each post
        print("facebook.com/" + str(i).split('_')[0] + "/posts/" + str(i).split('_')[1])
else:
    print("No of posts should be less than "+str(len(posts)))
