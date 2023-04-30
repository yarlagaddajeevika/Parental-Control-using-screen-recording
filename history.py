from browser_history.browsers import Firefox
import datetime
import re

f = Firefox()
outputs = f.fetch_history()

# his is a list of (datetime.datetime, url) tuples
his = outputs.histories

youtube_history=[]
for date, event in his:
    if 'youtube.com/watch' in event:
        youtube_history.append(event)

video_id=[]

# extract the video ID using regular expressions
for url in youtube_history:
    match = re.search(r'(?<=v=)[\w-]+', url)

    if match:
        id_ = match.group()
        video_id.append(id_)
    else:
        print("No video ID found.")

print(video_id)
