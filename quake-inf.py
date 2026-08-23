import streamlit as st
import datetime
import pandas as pd
import folium
from streamlit_folium import st_folium

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
    file = f"{select_date.year}.csv"
    url = f"https://raw.githubusercontent.com/EarthScience-ai/quake-data/refs/heads/main/YearlyQuake/{file}"
    df = pd.read_csv(url)
    df['datetime_date'] = pd.to_datetime(df['date'], format='%Y/%m/%d').dt.date
    filtered_df = df[df["datetime_date"] == select_date]
    if not filtered_df.empty:
        time_options = filtered_df["time"]
        selected_time = st.sidebar.selectbox(label="発生時刻を選択", options=time_options)
        final_df = filtered_df[filtered_df["time"] == selected_time]
        if not final_df.empty:
            epicenter_val = final_df["epicenter"].iloc[0]
            depth_val = final_df["depth"].iloc[0]
            magnitude_val = final_df["magnitude"].iloc[0]
            epicenter_lat = final_df["緯度"].iloc[0]
            epicenter_lng = final_df["経度"].iloc[0]
            max_intensity = final_df["maxshindo"].iloc[0]
            lat_val = final_df["lat"].iloc[0]
            lng_val = final_df["lng"].iloc[0]
            st.sidebar.markdown(f"震源地: {epicenter_val}")
            st.sidebar.markdown(f"緯度: {epicenter_lat}　経度: {epicenter_lng}")
            st.sidebar.markdown(f"深さ: {depth_val}　M {magnitude_val}　　最大{max_intensity}")

            formatted_time = str(selected_time).replace(":", "-")
            shindo_file = f"{select_date}_{formatted_time}.csv"
            shindo_url = f"https://raw.githubusercontent.com/EarthScience-ai/quake-data/refs/heads/main/QuakeDetected/{shindo_file}"
            shindo_df = pd.read_csv(shindo_url)

            def get_color(shindo):
                shindo = str(shindo).strip()
                if shindo == "7": return magenta
                elif shindo == "6強": return crimson
                elif shindo == "6弱": return red
                elif shindo == "5強": return peru
                elif shindo == "5弱": return orange
                elif shindo == "4": return yellow
                elif shindo == "3": return lawngreen
                elif shindo == "2": return aqua
                elif shindo == "1": return blue
            
            m = folium.Map(location=[36.0, 137.0], zoom_start=5)
            
            for index, row in final_df.iterrows():
                icon_x = folium.DivIcon(html=f'<div style="font-size: 16px; color: red; font-weight: bold; transform: translate(-50%, -50%);">❌</div>')
                folium.Marker(location=[row["lat"], row["lng"]], icon=icon_x).add_to(m)

            for index, row in shindo_df.iterrows():
                folium.CircleMarker(
                    location=[row['lat'],row['lng']], radius=1000,
                    fill_opacity=1, fill=True, 
                    fill_color=get_color(row['shindo']),
                ).add_to(m)
            st_folium(m,width="100%")
    else:
        st.subheader(f"No Data...")
        st.markdown(f"その原因:")
        st.markdown(f"  1. 震度１以上の観測する地震がありません。")
        st.markdown(f"  2. 【例:2026年のデータは2027年に】毎今年のデータは毎翌年にアップデートします。")
    
elif page == '過去の地震、津波、及び火山災害':
    st.markdown('<p class="a">過去の地震、津波、及び火山災害</p>', unsafe_allow_html=True)
elif page == '想定南海トラフ巨大地震':
    st.markdown('<p class="a">内閣府　想定南海トラフ巨大地震</p>', unsafe_allow_html=True)
elif page == '想定日本海溝・千島海溝巨大地震':
    st.markdown('<p class="a">内閣府　想定日本海溝・千島海溝巨大地震</p>', unsafe_allow_html=True)
