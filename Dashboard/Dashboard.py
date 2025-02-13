import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import matplotlib.ticker as ticker

artist_df = pd.read_csv("spotify_charts_jp.csv", encoding="utf-8-sig")

def format_number(num):
    if num >= 1_000_000_000:  # 1B
        return f"{num / 1_000_000_000:.1f}B"
    elif num >= 1_000_000:  # 1M
        return f"{num / 1_000_000:.1f}M"
    elif num >= 1_000:  # 1K
        return f"{num / 1_000:.1f}K"
    else:
        return str(num)

plt.rcParams['font.family'] = 'Meiryo'



st.markdown("<h1 style='text-align: center;'>Jpop Music Chart</h1>", unsafe_allow_html=True)

with st.sidebar :
    st.title('Japan Spotify Chart')
    st.markdown('**Source :** Kworb February 2025 week 1')

st.header("Top Artist By Stream")

top_artists_by_streams = (
    artist_df.groupby('Artist', as_index=False)['Streams'].sum()
    .sort_values(by='Streams', ascending=False)
    .head(10)  # Ambil 10 artis dengan stream tertinggi
)

fig1, ax1 = plt.subplots(figsize=(8, 8))
sns.barplot(data=top_artists_by_streams, x="Streams", y="Artist", palette="Greens_r", ax=ax1)
ax1.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: format_number(x)))
ax1.set_title("Artist With Most Streams")
ax1.set_xlabel("Streams")
ax1.set_ylabel("Artist")
st.pyplot(fig1)

st.header("Top Artist By Song")

top_artists_by_song = (
    artist_df.groupby('Artist', as_index=False)['Title']  # Gantilah 'Title' dengan nama kolom lagu di dataset
    .count()
    .sort_values(by='Title', ascending=False)
    .head(10)  # Ambil 10 artis dengan jumlah lagu terbanyak di chart
)


fig1, ax1 = plt.subplots(figsize=(8, 8))
sns.barplot(data=top_artists_by_song, x="Title", y="Artist", palette="Blues_r", ax=ax1)
ax1.set_title("Artist With Most Song in Chart")
ax1.set_xlabel("Songs")
ax1.set_ylabel("Artist")
st.pyplot(fig1)

st.header("Artists With Most Total Week in Chart")

top_artists_by_weeks = (artist_df.groupby('Artist', as_index=False)['Wks'].sum()
                        .sort_values(by='Wks', ascending=False)
                        .head(10))


fig1, ax1 = plt.subplots(figsize=(8, 8))
sns.barplot(data=top_artists_by_weeks, x="Wks", y="Artist", palette="Blues_r", ax=ax1)
ax1.set_title("Artists With Longest Week in Chart")
ax1.set_xlabel("Weeks")
ax1.set_ylabel("Artist")
st.pyplot(fig1)

st.header("Top Songs By Stream")

top_songs_by_streams = (artist_df.groupby('Title', as_index=False)['Streams'].sum()
                        .sort_values(by='Streams', ascending=False)
                        .head(10))

fig1, ax1 = plt.subplots(figsize=(8, 8))
sns.barplot(data=top_songs_by_streams, x="Streams", y="Title", palette="Blues_r", ax=ax1)
ax1.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: format_number(x)))
ax1.set_title("Top Songs By Stream")
ax1.set_xlabel("Streams")
ax1.set_ylabel("Title")
st.pyplot(fig1)

st.header("Songs With Longest Week in Chart")

top_songs_by_weeks = (artist_df.groupby('Title',as_index=False)['Wks'].sum()
    .sort_values(by='Wks', ascending=False)
    .head(10))

fig1, ax1 = plt.subplots(figsize=(8, 8))
sns.barplot(data=top_songs_by_weeks, x="Wks", y="Title", palette="Blues_r", ax=ax1)
ax1.set_title("Songs With Longest Week in Chart")
ax1.set_xlabel("Weeks")
ax1.set_ylabel("Title")
st.pyplot(fig1)


