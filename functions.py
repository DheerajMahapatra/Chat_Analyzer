# #importing class URLExtract from urlextrack
# from urlextract import URLExtract

# #importing class WordCloud from wordcloud
# from wordcloud import WordCloud

# #creating object of URLExtract class
# extract = URLExtract()

# # def fetch_stats(selected_user, df):
# #     if selected_user != 'OverAll':
# #         df = df[df['user'] == selected_user]
        
# #         #number of msg
# #         num_msgs = df.shape[0]
        
# #         #number of words
# #         #for msg in df['user']:
# #             #words.extend(msg.split())
# #         #number of media
        
# #         num_med = df[df['msg'] == '<Media omitted>\n'].shape[0]
        
# #         #number of links
# #         link = []
# #         for msg in df['msg']:
# #             link.extend(extract.find_urls(msg))
            
# #     return num_msgs, num_med, len(link)


# def extract_links(df):
#     # Example: extract all links from 'message' column
#     import re
#     links = []
#     for message in df['message']:
#         found_links = re.findall(r'http[s]?://\S+', str(message))
#         links.extend(found_links)
#     return links




# def fetch_stats(selected_user, df):
#     # Filter user
#     if selected_user != "OverAll":
#         filtered_df = df[df['user'] == selected_user]
#     else:
#         filtered_df = df

#     # Number of messages
#     num_msgs = filtered_df.shape[0]

#     # Number of media messages
#     num_med = filtered_df['msg'].str.contains('<media omitted>', case=False, na=False).sum()

#     # Number of links
#     link = []
#     for message in filtered_df['msg']:
#         link.extend(extract.find_urls(str(message)))

#     return num_msgs, num_med, len(link)


    
# def monthly_timeline(selected_user, df):
#         if selected_user != 'OverAll':
#             df = df[df['user'] == selected_user]
            
#         timeline = df.groupby(['year', 'month'])['msg'].count().reset_index()
        
#         time =[]
#         for i in range(timeline.shape[0]):
#             time.append(timeline['month'][i] + '-' + str(timeline['year'][i]))
            
#         timeline['time'] = time
        
#         return timeline
    
# #daily timeline
# def daily_timeline(selected_user, df):
#         if selected_user != 'OverAll':
#             df = df[df['user'] == selected_user]
            
#         timeline = df.groupby('date')['msg'].count().reset_index()
    
#         return timeline
        
# #activity map
# def activity_map(selected_user, df):
#         if selected_user != 'OverAll':
#             df = df[df['user'] == selected_user]
            
#         active_month_df = df.groupby('month')['msg'].count().reset_index()
#         month_list = active_month_df['month'].tolist()
#         month_msg_list = active_month_df['msg'].tolist()
        
#         active_day_df = df.groupby('day')['msg'].count().reset_index()
#         day_list = active_day_df['day'].tolist()
#         day_msg_list = active_day_df['msg'].tolist()
        
#         return active_month_df, month_list, month_msg_list, active_day_df, day_list, day_msg_list
    
# #most_chaty
# def most_chaty(df):
#         x = df['user'].value_counts().head()
        
#         percent = round((df['user'].value_counts() / df.shape[0]) * 100, 2)
        
#         return x, percent
    
# #create_wordcloud
# def create_wordcloud(selected_user, df):
#         if selected_user != 'OverAll':
#             df = df[df['user'] == selected_user]
            
#         wc = WordCloud(width = 500, height = 500, min_font_size = 10, background_color = 'white')
#         df_wc = wc.generate(df['msg'].str.cat(sep = ' '))
#         return df_wc
            








from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
import re
import emoji
from collections import Counter

# URL extractor
extract = URLExtract()

# 🔗 Extract all links from 'msg' or 'message' column
def extract_links(df):
    links = []
    for message in df['msg']:
        links.extend(extract.find_urls(str(message)))
    return links


# 📊 Basic stats
def fetch_stats(selected_user, df):
    if selected_user != "OverAll":
        filtered_df = df[df['user'] == selected_user]
    else:
        filtered_df = df

    num_msgs = filtered_df.shape[0]
    #num_med = filtered_df['msg'].str.contains('<media omitted>', case=False, na=False).sum()
    num_med = filtered_df['msg'].astype(str).str.contains('<media omitted>', case=False, na=False).sum()


    link = []
    for message in filtered_df['msg']:
        link.extend(extract.find_urls(str(message)))

    return num_msgs, num_med, len(link)


# 📆 Monthly Timeline
def monthly_timeline(selected_user, df):
    if selected_user != 'OverAll':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month'])['msg'].count().reset_index()
    timeline['time'] = timeline['month'] + '-' + timeline['year'].astype(str)
    return timeline


# 📅 Daily Timeline
def daily_timeline(selected_user, df):
    if selected_user != 'OverAll':
        df = df[df['user'] == selected_user]

    return df.groupby('date')['msg'].count().reset_index()


# 🗺️ Activity Map
def activity_map(selected_user, df):
    if selected_user != 'OverAll':
        df = df[df['user'] == selected_user]

    active_month_df = df.groupby('month')['msg'].count().reset_index()
    month_list = active_month_df['month'].tolist()
    month_msg_list = active_month_df['msg'].tolist()

    active_day_df = df.groupby('day')['msg'].count().reset_index()
    day_list = active_day_df['day'].tolist()
    day_msg_list = active_day_df['msg'].tolist()

    return active_month_df, month_list, month_msg_list, active_day_df, day_list, day_msg_list


# 🙋 Most Chatty
def most_chaty(df):
    x = df['user'].value_counts().head()
    percent = round((df['user'].value_counts() / df.shape[0]) * 100, 2)
    return x, percent


# ☁️ Word Cloud
def create_wordcloud(selected_user, df):
    if selected_user != 'OverAll':
        df = df[df['user'] == selected_user]

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    return wc.generate(df['msg'].str.cat(sep=' '))


# 😄 Emoji Analysis
def emoji_analysis(selected_user, df):
    if selected_user != 'OverAll':
        df = df[df['user'] == selected_user]

    emojis = []
    for msg in df['msg']:
        emojis.extend([c for c in msg if c in emoji.EMOJI_DATA])

    emoji_counter = Counter(emojis).most_common()
    return pd.DataFrame(emoji_counter)


# def emoji_helper(df):
#     all_emojis = []

#     # Ensure 'message' column is treated as string
#     df['message'] = df['message'].astype(str)

#     for msg in df['message']:
#         all_emojis += [c for c in msg if c in emoji.EMOJI_DATA]

#     emoji_counter = Counter(all_emojis).most_common()
#     emoji_df = pd.DataFrame(emoji_counter, columns=['emoji', 'count'])
#     return emoji_df