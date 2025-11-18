import streamlit as st

st.set_page_config(page_title="옷 색 조합 추천", page_icon="🎨", layout="centered")

st.title("🎨 옷 색 조합 추천 시스템")
st.write("상의·하의 색을 선택하면 어울리는 조합인지 알려주고, 더 예쁜 추천도 드릴게요!")

# 추천 데이터셋
top_to_bottom = {
    "화이트": ["블랙", "진청", "네이비", "베이지", "회색"],
    "블랙": ["화이트", "그레이", "청색", "베이지"],
    "베이지": ["브라운", "화이트", "블랙", "올리브"],
    "네이비": ["전체적으로 어울리는 상의"],
    "네이비": ["화이트", "그레이", "베이지", "블랙"],
    "그레이": ["블랙", "화이트", "네이비", "딥그린"],
    "브라운": ["베이지", "아이보리", "블랙"],
    "레드": ["블랙", "화이트", "데님"],
    "블루(청색)": ["화이트", "그레이", "블랙"],
    "그린": ["베이지", "브라운", "블랙"],
    "옐로우": ["화이트", "데님", "브라운"]
}

# bottom → top 반대로 변환
bottom_to_top = {}
for top, bottoms in top_to_bottom.items():
    for bottom in bottoms:
        if bottom not in bottom_to_top:
            bottom_to_top[bottom] = []
        if top not in bottom_to_top[bottom]:
            bottom_to_top[bottom].append(top)


# UI
col1, col2 = st.columns(2)
with col1:
    selecte
