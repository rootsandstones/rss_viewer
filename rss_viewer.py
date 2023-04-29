import streamlit as st
import feedparser
import os
import sqlite3

rss_exmpl = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCjOl2AUblVmg2rA_cRgZkFg'

if 'rss.db' in os.listdir():
    db = sqlite3.connect('rss.db')
else:
    open('rss.db', 'a')
    db = sqlite3.connect('rss.db')

dbpointer = db.cursor()
dbpointer.execute("CREATE TABLE IF NOT EXISTS links (name TEXT, link TEXT)")
#db.commit()

def get_rss_feed(rss_input):
    feed = feedparser.parse(rss_input)
    st.header(feed.feed.title)
        
    for i in range(0, 5):
        title = feed.entries[i].title
        link = feed.entries[i].link
        img_link = feed.entries[i].media_thumbnail
        img_link = img_link[0]['url']

        # st.image(img_link)
        st.markdown("**"+ title + "**")
        st.video(link)
        # st.write(link)
        st.divider()

st.title('Youtube RSS Viewer')
rss_link = st.text_input(label='Youtube RSS Link', value='https://www.youtube.com/feeds/videos.xml?channel_id=UCjOl2AUblVmg2rA_cRgZkFg')


get_rss_feed(rss_link)