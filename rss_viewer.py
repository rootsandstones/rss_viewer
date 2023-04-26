import streamlit as st
import feedparser

rss_exmpl = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCjOl2AUblVmg2rA_cRgZkFg'

def get_rss_feed():
    feed = feedparser.parse(rss_exmpl)
    st.header(feed.feed.title)
        
    for i in range(0, 5):
        title = feed.entries[i].title
        link = feed.entries[i].link
        img_link = feed.entries[i].media_thumbnail
        img_link = img_link[0]['url']

        st.image(img_link) 
        st.write("_"+ title + "_")
        st.write(link)

st.title('Youtube RSS Viewer')
get_rss_feed()