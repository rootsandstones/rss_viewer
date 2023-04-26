import streamlit as st
import feedparser

rss_exmpl = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCjOl2AUblVmg2rA_cRgZkFg'


st.title('Youtube RSS Viewer')


def get_rss_feed():
    feed = feedparser.parse(rss_exmpl)
    feed_title = feed.feed.title
    label_title = tk.Label(root, text=str(feed_title))
    label_title.pack()
        
    for i in range(0, 5):
        title = feed.entries[i].title
        link = feed.entries[i].link
        label_videotitle = tk.Label(root, text=str(title))
        label_videotitle.pack()
        label_link = tk.Label(root, text=str(link))
        label_link.pack()

