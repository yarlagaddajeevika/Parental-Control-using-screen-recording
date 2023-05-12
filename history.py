from browser_history.browsers import Firefox
import datetime
import re
import requests
from bs4 import BeautifulSoup

video_id=[]

#get browser history
def getHistory():
    f = Firefox() # for firefox
    outputs = f.fetch_history()

    # his is a list of (datetime.datetime, url) tuples
    his = outputs.histories

    youtube_history=[]
    for date, event in his:
        if 'youtube.com/watch' in event:
            youtube_history.append(event)
    
    # extract the video ID using regular expressions
    for url in youtube_history:
        match = re.search(r'(?<=v=)[\w-]+', url)

        if match:
            id_ = match.group()
            video_id.append(id_)
        else:
            print("No video ID found.")

    print(video_id)
    return video_id

#get the title from the video id
def get_video_title(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("title").text
    return title

#append all the titles into an array
def getAllTitles():
    video_id = getHistory()
    titles=[]
    for id in video_id:
        title = get_video_title(id)
        print(title)
        titles.append(title)

    return titles

#store the data into a database for future work if needed
def storeIntoDatabase():
    video_id = getHistory()
    counts = {}
    for id_ in video_id:
        if id_ in counts:
            counts[id_] += 1
        else:
            counts[id_] = 1
    update_status = db.storeIdsCount(db.returnUserId(username),counts)

    if update_status:
        print("Successful update of statistics")

#get the view counts
def getCounts():
    video_id = getHistory()
    counts = {}
    for id_ in video_id:
        if id_ in counts:
            counts[id_] += 1
        else:
            counts[id_] = 1 
    return counts

#formatting data to display it in a notepad
def summaryReport():
    counts = getCounts()
    max_value = max(counts, key=counts.get)
    title = get_video_title(max_value)
    print(max_value,counts[max_value])
    with open('myfile.txt', 'a') as fw:
        fw.write(f"""\nMost frequently watched Video:\n\tYour kid has watched the video https://www.youtube.com/watch?v={max_value}, {counts[max_value]} times in the day""")
        fw.write(f"""\n\tTitle: {title}""")
        fw.write(f"""\n\nList of urls visited:""")
        for id_, view_count in counts.items():
            fw.write(f"""\n\thttps://www.youtube.com/watch?v={id_}, view count:{view_count}""")
     
