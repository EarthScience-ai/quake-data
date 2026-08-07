import streamlit as st
import datetime

st.markdown(
    """
    <style>
    .a{
         color: #ffffff; 
         background-color: blue; 
         padding: 5px;}
    </style>
    """, unsafe_allow_html=True
)
page = st.sidebar.selectbox('メニュー', ['ホーム', '震度データベース', '過去の地震、津波、及び火山災害'], index=0)

if page == 'ホーム':
    st.markdown('<p class="a">日本の地震国へようこそ</p>', unsafe_allow_html=True)
elif page == '震度データベース':
    st.markdown('<p class="a">地震情報</p>', unsafe_allow_html=True)
    st.sidebar.date_input(
        label="日付を選択",
        value=datetime.date.today(), 
        min_value=datetime.date(2001, 1, 1),
        max_value=datetime.date(2100, 12, 31),
    )
elif page == '過去の地震、津波、及び火山災害':
    st.markdown('<p class="a">過去の災害から防災や減災</p>', unsafe_allow_html=True)
