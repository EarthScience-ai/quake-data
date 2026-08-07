import streamlit as st

st.markdown(
    """
    <style>
    .head{color: white; background-color: blue; padding: 10px;}
    </style>
    """, unsafe_allow_html=True
)
st.markdown('<h2 class="head">日本の地震国へようこそ</h2>', unsafe_allow_html=True)
page = st.sidebar.selectbox('メニュー', ['震度データベース', '過去の地震、津波、及び火山災害', '防災知識を高めるには?'], index=0)

if page == '震度データベース':
    st.title('ページ1')
    st.write('Streamlitのテストページ1です。')
elif page == '過去の地震、津波、及び火山災害':
    st.title('ページ2')
    st.write('Streamlitのテストページ2です。')
else:
    st.title('防災知識を高めるには?')
    st.write('Streamlitのテストページ3です。')
