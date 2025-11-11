import streamlit as st
import folium
from streamlit_folium import st_folium

# ----------------------------
# 기본 설정
# ----------------------------
st.set_page_config(page_title="서울 관광지도", page_icon="🗺️", layout="wide")
st.title("🗺️ 외국인이 좋아하는 서울 주요 관광지 TOP 10")
st.write("서울의 대표 관광 명소를 Folium 지도 위에 표시했습니다!")

# ----------------------------
# 관광지 데이터 (한국어 설명 + 가장 가까운 지하철역 정보 추가)
# ----------------------------
places = [
    {"name": "경복궁 (Gyeongbokgung Palace)", "lat": 37.579617, "lon": 126.977041,
     "desc": "조선시대 대표 궁궐", "station": "3호선 경복궁역"} ,
    {"name": "명동 (Myeongdong)", "lat": 37.563757, "lon": 126.982621,
     "desc": "쇼핑과 길거리 음식의 천국", "station": "4호선 명동역"} ,
    {"name": "남산타워 (N Seoul Tower)", "lat": 37.551169, "lon": 126.988227,
     "desc": "서울의 전망을 한눈에!", "station": "3·4호선 충무로역 또는 4호선 명동역"} ,
    {"name": "북촌한옥마을 (Bukchon Hanok Village)", "lat": 37.582604, "lon": 126.983998,
     "desc": "전통 한옥이 보존된 마을", "station": "3호선 안국역"} ,
    {"name": "인사동 (Insadong)", "lat": 37.574023, "lon": 126.984905,
     "desc": "전통문화와 예술의 거리", "station": "3호선 안국역 또는 1호선 종각역"} ,
    {"name": "홍대 (Hongdae)", "lat": 37.557192, "lon": 126.924903,
     "desc": "젊음과 예술, 자유로운 분위기의 거리", "station": "2호선 홍대입구역"} ,
    {"name": "동대문디자인플라자 (DDP)", "lat": 37.566479, "lon": 127.009155,
     "desc": "현대적 건축과 야경이 아름다운 명소", "station": "2·4호선 동대문역사문화공원역"} ,
    {"name": "잠실 롯데월드타워 (Lotte World Tower)", "lat": 37.513068, "lon": 127.102492,
     "desc": "세계에서 가장 높은 빌딩 중 하나", "station": "2호선·8호선 잠실역"} ,
    {"name": "청계천 (Cheonggyecheon Stream)", "lat": 37.569162, "lon": 126.978395,
     "desc": "도심 속 휴식공간", "station": "1호선 종각역 또는 5호선 광화문역 인접"} ,
    {"name": "이태원 (Itaewon)", "lat": 37.534499, "lon": 126.994551,
     "desc": "다양한 문화가 공존하는 거리", "station": "6호선 이태원역"} ,
]

# ----------------------------
# 일정 설정용: 날짜 선택
# ----------------------------
days = st.selectbox("여행 일수를 선택하세요", [1, 2, 3], index=0)
st.write(f"총 {days}일 일정으로 추천드립니다.")

# ----------------------------
# 지도 생성
# ----------------------------
seoul_center = [37.5665, 126.9780]
m = folium.Map(location=seoul_center, zoom_start=12)

# 마커 추가
for p in places:
    folium.Marker(
        location=[p["lat"], p["lon"]],
        popup=f"<b>{p['name']}</b><br>{p['desc']}<br>가장 가까운 지하철: {p['station']}",
        tooltip=p["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# ----------------------------
# 스트림릿에 표시
# ----------------------------
st_folium(m, width=900, height=600)
st.write("💡 확대하거나 클릭해서 각 관광지의 정보를 확인하세요!")

# ----------------------------
# 일정 출력 (오전 / 오후 / 야간 + 점심/저녁 포함)
# ----------------------------
st.header("🗓️ 여행 일정표")

# 관광지 리스트를 날짜수에 맞게 나눠서 보여주기
# 예: days일 × (오전 1곳, 오후 1곳, 야간 1곳) → 총 3×days 관광지 사용
# 단순하게 순서대로 나눔  
total_places = len(places)
places_per_day = {
    "오전": 1,
    "오후": 1,
    "야간": 1
}

idx = 0
for day in range(1, days+1):
    st.subheader(f"{day}일차")
    # 오전
    if idx < total_places:
        p = places[idx]
        st.write(f"오전: {p['name']} — {p['desc']} (지하철: {p['station']})")
        idx += 1
    # 점심
    st.write("    🍴 점심식사 — 자유식사 추천 (현지식 혹은 카페 등)")
    # 오후
    if idx < total_places:
        p = places[idx]
        st.write(f"오후: {p['name']} — {p['desc']} (지하철: {p['station']})")
        idx += 1
    # 저녁
    st.write("    🌇 저녁식사 — 현지 식당 이용 추천")
    # 야간
    if idx < total_places:
        p = places[idx]
        st.write(f"야간: {p['name']} — {p['desc']} (지하철: {p['station']})")
        idx += 1
    st.write("---")
