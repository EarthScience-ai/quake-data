import streamlit as st

st.markdown(
    """
    <style>
    .h1{
         color: #ffffff; 
         font-size: 16px;
         background-color: blue; 
         padding: 5px;}
    </style>
    """, unsafe_allow_html=True
)
page = st.sidebar.selectbox('メニュー', ['ホーム', '震度データベース', '過去の地震、津波、及び火山災害'], index=0)

if page == 'ホーム':
    st.markdown('<h1>日本の地震国へようこそ</h1>', unsafe_allow_html=True)
elif page == '震度データベース':
    st.markdown('<h1>地震情報</h1>', unsafe_allow_html=True)
elif page == '過去の地震、津波、及び火山災害':
    st.markdown('<h1>過去の災害から防災や減災</h1>', unsafe_allow_html=True)
