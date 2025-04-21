import streamlit as st
import preprocessor
import functions
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import pandas as pd
from streamlit_lottie import st_lottie
import requests
import matplotlib.font_manager as fm 


# Load Lottie animation function
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        else:
            return None
    except:
        return None

# Streamlit page setup
st.set_page_config(page_title="WhatsApp Analyzer", layout="wide")

# Inject Custom CSS
st.markdown("""
    <style>
    body {
        background-color: #0f2027 !important;
        background-image: linear-gradient(to right, #2c5364, #203a43, #0f2027) !important;
    }
    h1, h2, h3, .stMetric, .stMarkdown, .stDataFrame {
        color: #25D366 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Lottie Animation + Logo + Heading
lottie_url = "https://lottie.host/7efb0872-0879-4a46-9cb2-e02e7b865212/zvI3ItkClJ.json"
lottie_json = load_lottieurl(lottie_url)
if lottie_json:
    st_lottie(lottie_json, height=180, key="header-lottie")

st.markdown("""
    <div style="text-align:center; padding: 10px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="90"/>
        <h1 style="color:#25D366; font-size: 40px;">WhatsApp Chat Analyzer</h1>
        <p style="color:white;">Visualize your chat like never before 📊💬</p>
    </div>
""", unsafe_allow_html=True)

# Seaborn style
sns.set_style("darkgrid")

# Sidebar
st.sidebar.title('🟢 WhatsApp Chat Analyzer 👻📊')
uploaded_file = st.sidebar.file_uploader("📁 Choose a WhatsApp .txt file")

if not uploaded_file:
    st.markdown("""
    ### 📄 How to Use
    - Export your WhatsApp chat (Without media)
    - Upload the `.txt` file here
    - Click on **Analyse** to see insights ✨
    """)
    st.markdown('---')
    st.markdown("Made with ❤️ by **DHEERAJ MAHAPATRA**")
else:
    data = uploaded_file.getvalue().decode('utf-8')
    df = preprocessor.preprocess(data)
    user_details = df['user'].unique().tolist()
    if 'Group Notification' in user_details:
        user_details.remove('Group Notification')
    user_details.sort()
    user_details.insert(0, 'OverAll')

    selected_user = st.sidebar.selectbox('🔍 Show Analysis for:', user_details)

    if st.sidebar.button('🎯 Analyse'):
        st.header("📈 Chat Statistics Overview")
        num_msgs, num_med, link = functions.fetch_stats(selected_user, df)
        col1, col2, col3 = st.columns(3)
        col1.metric(label="💬 Total Messages", value=num_msgs)
        col2.metric(label="📷 Media Shared", value=num_med)
        col3.metric(label="🔗 Links Shared", value=link)

        st.markdown("---")

        # Monthly Timeline
        st.subheader("🗓 Monthly Timeline")
        timeline = functions.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        fig.patch.set_facecolor('#0f2027')
        ax.set_facecolor('#0f2027')
        sns.lineplot(data=timeline, x='time', y='msg', marker='o', ax=ax, color='cyan')
        ax.set_title('Messages Over Months', color='white')
        ax.tick_params(colors='white')
        st.pyplot(fig)

        # Daily Timeline
        st.subheader("📅 Daily Timeline")
        daily = functions.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        fig.patch.set_facecolor('#0f2027')
        ax.set_facecolor('#0f2027')
        sns.lineplot(data=daily, x='date', y='msg', marker='o', ax=ax, color='orange')
        ax.set_title('Daily Chat Activity', color='white')
        ax.tick_params(colors='white')
        st.pyplot(fig)

        # Activity Map
        st.subheader("📍 Activity Map")
        active_month_df, month_list, month_msg_list, active_day_df, day_list, day_msg_list = functions.activity_map(selected_user, df)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🗖️ Most Active Months")
            fig, ax = plt.subplots()
            fig.patch.set_facecolor('#0f2027')
            ax.set_facecolor('#0f2027')
            #sns.barplot(x=active_month_df['month'], y=active_month_df['msg'], ax=ax, palette="cool")
            sns.barplot(x=active_month_df['month'], y=active_month_df['msg'], ax=ax, hue=active_month_df['month'], palette="cool", legend=False)
            ax.set_title('Monthly Activity', color='white')
            ax.tick_params(colors='white')
            st.pyplot(fig)
        with col2:
            st.markdown("#### 🗖️ Most Active Days")
            fig, ax = plt.subplots()
            fig.patch.set_facecolor('#0f2027')
            ax.set_facecolor('#0f2027')
            #sns.barplot(x=active_day_df['day'], y=active_day_df['msg'], ax=ax, palette="autumn")
            sns.barplot(x=active_month_df['month'], y=active_month_df['msg'], ax=ax, hue=active_month_df['month'], palette="cool", legend=False)
            ax.set_title('Day-wise Activity', color='white')
            ax.tick_params(colors='white')
            st.pyplot(fig)

        # Most Active Users
        if selected_user == 'OverAll':
            st.subheader("🧑‍🤝‍🧑 Most Active Users")
            x, percent = functions.most_chaty(df)
            fig, ax = plt.subplots(figsize=(10, 5))
            fig.patch.set_facecolor('#0f2027')
            ax.set_facecolor('#0f2027')
            ax.bar(x.index, x.values, color='skyblue')
            ax.set_xticks(range(len(x.index)))
            ax.set_xticklabels(x.index, rotation=45, ha='right')
            ax.set_xlabel('User')
            ax.set_ylabel('Message Count')
            ax.set_title('Most Active Users')
            ax.tick_params(colors='white')
            plt.tight_layout()
            st.pyplot(fig)
            st.dataframe(percent.reset_index().rename(columns={'index': 'User', 'user': 'Count (%)'}))

        # WordCloud
        st.subheader("☁️ Most Common Words")
        df_wc = functions.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        fig.patch.set_facecolor('#0f2027')
        ax.imshow(df_wc, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)

        # Emoji Analysis
        st.subheader("😄 Emoji Analysis")
        emoji_df = functions.emoji_analysis(selected_user, df)
        emoji_font = fm.FontProperties(fname="C:/Windows/Fonts/seguiemj.ttf")
        #emoji_font = fm.FontProperties(family="Segoe UI Emoji")
        #plt.rcParams['font.family'] = emoji_font.get_name()
        plt.rcParams['font.family'] = emoji_font.get_name()
        if not emoji_df.empty:
            col1, col2 = st.columns([2, 1])
            with col1:
                fig, ax = plt.subplots()
                fig.patch.set_facecolor('#0f2027')
                ax.set_facecolor('#0f2027')
                sns.barplot(x=emoji_df[0][:10], y=emoji_df[1][:10], palette="viridis", ax=ax)
                #sns.barplot(x=active_month_df['month'], y=active_month_df['msg'], ax=ax, hue=active_month_df['month'], palette="cool", legend=False)
                ax.set_title("Top Emojis Used", color='white')
                ax.tick_params(colors='white')
                st.pyplot(fig)
            with col2:
                st.dataframe(emoji_df.head(10).rename(columns={0: "Emoji", 1: "Count"}))

        st.markdown("—")
        st.markdown("🌟 Made with Streamlit by **DHEERAJ MAHAPATRA** 🌟")

        # Download CSV
        st.subheader("📅 Download Insights as CSV")
        download_df = df[df['user'] == selected_user] if selected_user != "OverAll" else df
        csv = download_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Chat Data 📁",
            data=csv,
            file_name=f'{selected_user}_chat_insights.csv',
            mime='text/csv'
        )
