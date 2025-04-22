# 💬 WhatsApp Chat Analyzer — Streamlit Project 📊

Welcome to the **WhatsApp Chat Analyzer** — a modern, intelligent, and interactive chat analytics app built with Python and Streamlit. Designed to uncover hidden insights, this project transforms your exported WhatsApp messages into stunning visuals and statistics — perfect for data lovers, social groups, and curious minds.

---
> ✨ *Empowering minds. One chat at a time.*

![Repo Size](https://img.shields.io/github/repo-size/DheerajMahapatra/Chat_Analyzer)
![Issues](https://img.shields.io/github/issues/DheerajMahapatra/Chat_Analyzer)
![Forks](https://img.shields.io/github/forks/DheerajMahapatra/Chat_Analyzer?style=social)
![Stars](https://img.shields.io/github/stars/DheerajMahapatra/Chat_Analyzer?style=social)

---
## 🚀 Live Demo

Try it out here:  
🌐 **[WhatsApp Chat Analyzer — Live App](https://dheeraj-whatsapp-chat-analyzer.streamlit.app)**

> ⚡ Powered by Streamlit Cloud for seamless deployment

---
## 📌 Project Overview

**WhatsApp Chat Analyzer** is a one-stop solution to explore your chat data through interactive graphs, emoji breakdowns, activity timelines, word clouds, and more. With built-in preprocessing, elegant UI, and beautiful animations, this app ensures a smooth and engaging user experience.

---

## 🚀 Features

- 📁 **Upload Chat** — Analyze your exported `.txt` chat file directly
- 📅 **Message Timeline** — Daily, monthly, and hourly activity heatmaps
- 🙋‍♂️ **User Stats** — Most active users, words used, emoji count
- 🧠 **WordCloud Generator** — Most common keywords beautifully visualized
- 😂 **Emoji Analysis** — Emoji frequency and usage breakdown
- 🔗 **Link Analysis** — Extract shared URLs from the conversation
- 📈 **Beautiful Charts** — Matplotlib & Seaborn-powered plots
- 🌙 **Custom Dark UI** — Gradient backgrounds and neon visuals
- 🔄 **Streamlit Lottie Animations** — For a premium feel
- 📤 **CSV Export** — Export your chat insights easily

---

## 🖼️ UI Preview

| Upload Page | Analyze View | Download Button | 
|-------------|--------------|-----------------|
| ![](https://raw.githubusercontent.com/DheerajMahapatra/Chat_Analyzer/main/UI/Index.jpg) | ![](https://raw.githubusercontent.com/DheerajMahapatra/Chat_Analyzer/main/UI/Analyze.jpg) |  ![](https://raw.githubusercontent.com/DheerajMahapatra/Chat_Analyzer/main/UI/Download_Button.jpg) |

| Monthly_Timeline | Daily_Timeline | Activity_Map |
|------------------|----------------|--------------|
| ![](https://raw.githubusercontent.com/DheerajMahapatra/Chat_Analyzer/main/UI/Monthly_Timeline.jpg) | ![](https://raw.githubusercontent.com/DheerajMahapatra/Chat_Analyzer/main/UI/Daily_Timeline.jpg) |  ![](https://raw.githubusercontent.com/DheerajMahapatra/Chat_Analyzer/main/UI/Activity_Map.jpg) |

| Most_Active_User | WordCloud | Emoji Stats |
|------------------|-----------|-------------|
| ![](https://raw.githubusercontent.com/DheerajMahapatra/Chat_Analyzer/main/UI/Most_Active_User.jpg) | ![](https://raw.githubusercontent.com/DheerajMahapatra/Chat_Analyzer/main/UI/Most_Common_Words.jpg) |  ![](https://raw.githubusercontent.com/DheerajMahapatra/Chat_Analyzer/main/UI/Emoji_Analyzer.jpg) |

---

## 🛠️ Tech Stack

| Component        | Tech Used              |
|------------------|------------------------|
| 🎨 Frontend UI   | Streamlit + Lottie     |
| 📊 Visualization | Matplotlib, Seaborn    |
| 🧠 Data Handling | Pandas, WordCloud, URLExtract |
| 🌐 Deployment    | Streamlit Cloud (Optional) |
| 💾 File Parsing  | Custom WhatsApp Parser |

---

## 📂 Project Structure

```bash
whatsapp_chat_analyzer/
│
├── app.py             # Main Streamlit UI and logic
├── functions.py       # Chat analysis and visualization logic
├── preprocessor.py    # Text cleaning and data formatting
├── requirements.txt   # Python dependencies
├── assets/            # Lottie animations, logos, etc.
└── README.md          # Project documentation
```

## 🧠 How It Works

1. 📲 **Export your chat via WhatsApp:**  
   `Chat > More > Export Chat > Without Media`

2. 📤 **Upload the `.txt` file** in the app

3. 📊 **Explore dashboards and visualizations** powered by Python magic!

4. 📁 **Export your results** to CSV if needed

---

## ▶️ Run the App Locally

```bash
git clone https://github.com/yourusername/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
pip install -r requirements.txt
streamlit run app.py
```
## 📦 Dependencies

- **The following Python libraries are required to run this app:**
- streamlit==1.44.1
- matplotlib
- seaborn
- URLExtract
- wordcloud
- pandas
- requests
- streamlit-lottie
- emoji
---

### ✅ Install with:

```bash
pip install -r requirements.txt
```

## 💬 Sample Chat Export Format

- ✅ Works with **English** and **multi-language** WhatsApp chats  
- 📄 Must follow WhatsApp’s **default export format** (`.txt`)  
- ⚠️ Ensure **"Without Media"** is selected during export  

---

## 📅 Future Enhancements

- 📌 Group vs Individual Chat Comparison  
- 🌐 Multi-language support (Hindi, Spanish, etc.)  
- 📲 Telegram & Messenger support  
- 📊 AI-powered sentiment analysis  
- 📝 Chat summarization with LLMs (ChatGPT/Claude)  
- 📤 Shareable public reports  

---

## 🙌 Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Matplotlib](https://matplotlib.org/)
- [LottieFiles](https://lottiefiles.com/)
- WhatsApp for the chat export format

---

## 📧 Contact

Built with ❤️ by **[DHEERAJ MAHAPATRA]**  
📫 Email: dheerajmahapatra2029@gmail.com  
🔗 GitHub: [@DheerajMahapatra](https://github.com/DheerajMahapatra)
