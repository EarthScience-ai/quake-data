import streamlit as st
import datetime

st.markdown(
    """
    <style>
    .a{
         font-size: large;
         font-weight: bold;
         color: white; 
         background-color: blue; 
         padding: 5px;}
    </style>
    """, unsafe_allow_html=True
)
page = st.sidebar.selectbox('メニュー', ['HOME', '震度データベース', '過去の地震、津波、及び火山災害', '想定南海トラフ巨大地震', '想定日本海溝・千島海溝巨大地震'], index=0)
if page == 'HOME':
    st.markdown('<p class="a">ようこそ</p>', unsafe_allow_html=True)
elif page == '震度データベース':
    st.markdown('<p class="a">地震情報</p>', unsafe_allow_html=True)
    select_date = st.sidebar.date_input(
        label="日付を選択",
        value=datetime.date.today(), 
        min_value=datetime.date(2001, 1, 1),
        max_value=datetime.date(2100, 12, 31),
    )
    df['datetime_date'] = pd.to_datetime(df['date'], format='%Y/%m/%d').dt.date
    filtered_df = df[df['datetime_date'] == select_date]
elif page == '過去の地震、津波、及び火山災害':
    st.markdown('<p class="a">過去大災害から防災や減災</p>', unsafe_allow_html=True)
elif page == '想定南海トラフ巨大地震':
    st.markdown('<p class="a">内閣府　想定南海トラフ巨大地震</p>', unsafe_allow_html=True)
elif page == '想定日本海溝・千島海溝巨大地震':
    st.markdown('<p class="a">内閣府　想定日本海溝・千島海溝巨大地震</p>', unsafe_allow_html=True)
