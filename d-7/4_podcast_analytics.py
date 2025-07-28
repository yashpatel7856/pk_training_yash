# Problem 4: Podcast System with Analytics and Review

# Problem Statement:
# Design a podcast system using Object-Oriented Programming (OOP) where:

# There are two types of users:

# Creators can:
#   - Upload podcast episodes.
#   - View analytics (how many times an episode has been played and reviewed).
# Listeners can:
#   - Play an episode (which increases the play count).
#   - Pause an episode (with duration to simulate listening time).
#   - Leave a textual review for an episode.

# Each episode should keep track of:

# Total number of plays
# Number of reviews

# Sample Input:
# creator = Creator("Dev Talks")
# ep = creator.upload_episode("ChatGPT in 2025")
# listener = Listener("Sam")
# listener.play(ep)
# listener.pause(ep, 120)
# listener.review(ep, "Great insights!")
# creator.get_metrics("ChatGPT in 2025")

# Sample Output:
# ChatGPT in 2025: 1 plays, 1 reviews

# start time : 11:38  ,  + 15 min(chnages)
# end time : 12:33    ,   

class Creator():

    videos={}
    def __init__(self,name):
        self.name=name
        self.videos={}
    def upload_episode(self,episodeName):
        videoData={
            "name":episodeName,
            "views":0,
            "reviewCount":0,
            "reviews":[],
            "creatorName":self.name,
            "length":400, #in seconds
            "info":"any info need to be added"
        }
        self.videos[episodeName]=videoData
        return videoData
    def get_metrics(self,episodeName):
        episode=self.videos[episodeName]
        print(f'{episode["name"]}---  Plays : {episode["views"]} ,Reviews : {episode["reviewCount"]}')

class Listener:
    
    def __init__(self,name):
        self.name=name
        self.history={}
    def play(self,episode):
            
            episode["views"]+=1
            self.history[episode["name"]]={"pausedAt":0,"review":""}
    
    def pause(self,episode,duration):
        
        if episode['length'] >= duration:
            if episode['name'] in self.history:
                self.history[episode['name']]["pausedAt"]=duration
                print(f'{episode["name"]} Paused at {duration}')
            else:
                print('video is not played yet')
        else:
            print(f'Invalid stop time.video length={episode.length},stop time={duration}')
            return f'Invalid stop time.video length={episode.length},stop time={duration}'
                
    def review(self,episode,review):
        if episode["name"] in self.history:
            self.history[episode["name"]]["review"]=review
            episode["reviewCount"]+=1
            episode["reviews"].append(review)
        else:
            print('watch video to review it !!!!')

creator = Creator("Dev Talks")
ep = creator.upload_episode("ChatGPT in 2025")
listener = Listener("Sam")
listener.play(ep)
listener.pause(ep, 120)
listener.review(ep, "Great insights!")
creator.get_metrics("ChatGPT in 2025")
