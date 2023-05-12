import matplotlib.pyplot as plt
import history as his

#display graph
def graphView():
    counts = his.getCounts()
    urls=[]
    hits=[]
    # URL and hit count data
    for key, value in counts.items():
        title = his.get_video_title(key)
        if len(title) > 8:
            formatted = title[:5]+"..."
            urls.append(formatted)
        hits.append(value)

    # Create bar chart
    plt.bar(urls, hits)

    # Add labels and title
    plt.xlabel('Youtube video titles')
    plt.ylabel('Hit count')
    plt.title('URL hit counts')

    # Show the chart
    plt.show()
