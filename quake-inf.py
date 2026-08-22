import streamlit as st
import datetime
import pandas as pd

st.markdown(
    """
    <style>
    .a{
         font-weight: bold;
         color: white; 
         background-color: blue; 
         padding: 5px;}
    </style>
    """, unsafe_allow_html=True
)
page = st.sidebar.radio('メニュー', ['HOME', '震度データベース', '過去の地震、津波、及び火山災害', '想定南海トラフ巨大地震', '想定日本海溝・千島海溝巨大地震'], index=0)
if page == 'HOME':
    st.markdown('<p class="a">ようこそ</p>', unsafe_allow_html=True)
elif page == '震度データベース':
    st.markdown('<p class="a">過去の地震情報</p>', unsafe_allow_html=True)
    select_date = st.sidebar.date_input(
        label="地震発生日付を選択",
        value=datetime.date.today(), 
        min_value=datetime.date(2001, 1, 1),
        max_value=datetime.date(2100, 12, 31),
    )
    df = pd.read_csv('https://raw.githubusercontent.com/EarthScience-ai/quake-data/refs/heads/main/YearlyQuake/2001.csv')
    df['datetime_date'] = pd.to_datetime(df['date'], format='%Y/%m/%d').dt.date
    if df['datetime_date'] == select_date:
        st.sidebar.selectbox('地震発生時刻を選択', [df[time]])
    
elif page == '過去の地震、津波、及び火山災害':
    st.markdown('<p class="a">過去の地震、津波、及び火山災害</p>', unsafe_allow_html=True)
elif page == '想定南海トラフ巨大地震':
    st.markdown('<p class="a">内閣府　想定南海トラフ巨大地震</p>', unsafe_allow_html=True)
elif page == '想定日本海溝・千島海溝巨大地震':
    st.markdown('<p class="a">内閣府　想定日本海溝・千島海溝巨大地震</p>', unsafe_allow_html=True)
