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
dbpointer.execute("CREATE TABLE IF NOT EXISTS links (name TEXT, link TEXT, groupname TEXT)")

def get_rss_feed(rss_input):
    feed = feedparser.parse(rss_input)
    #st.header(feed.feed.title)
        
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

def add_db(rss_input):
    feed = feedparser.parse(rss_input)
    feed_name = feed.feed.title

    dbpointer.execute("INSERT INTO links (name, link) VALUES ('%s','%s')" % (feed_name,rss_input))
    db.commit()
    st.write('Adding...')

def get_links():
    #Create dictionary in a format like name:link
    values = db.execute("SELECT * FROM links").fetchall()
    links_dict = {}
    for rows in values:
        name = rows[0]
        link = rows[1]
        links_dict[name] = link
    return links_dict

st.set_page_config(page_title='Youtube RSS Feeds', layout='wide')   #Must be the first streamlit command!
st.title('Youtube RSS Viewer')

#Adding links
st.subheader('Adding new feeds')
rss_link = st.text_input(label='Youtube RSS Link', value='https://www.youtube.com/feeds/videos.xml?channel_id=UCjOl2AUblVmg2rA_cRgZkFg')

if st.button('Add RSS to library'):
    add_db(rss_link)

#Displaying feeds
rss_dict = get_links()

col1, col2, col3 = st.columns(3)

with col1:
   st.subheader('Display feeds')
   selection_by_name_1 = st.selectbox('Choose feed', rss_dict.keys(), key=1)
   get_rss_feed(rss_dict[selection_by_name_1])

with col2:
   st.subheader('Display feeds')
   selection_by_name_2 = st.selectbox('Choose feed', rss_dict.keys(), key=2)
   get_rss_feed(rss_dict[selection_by_name_2])

with col3:
   st.subheader('Display feeds')
   selection_by_name_3 = st.selectbox('Choose feed', rss_dict.keys(), key=3)
   get_rss_feed(rss_dict[selection_by_name_3])