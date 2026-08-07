import streamlit as st

st.header('Streamlitのテストページ', divider='blue')
page = st.sidebar.selectbox('ページを選択', ['page1', 'page2', 'page3'], index=0)

if page == 'page1':
    st.title('ページ1')
    st.write('Streamlitのテストページ1です。')
elif page == 'page2':
    st.title('ページ2')
    st.write('Streamlitのテストページ2です。')
else:
    st.title('ページ3')
    st.write('Streamlitのテストページ3です。')
