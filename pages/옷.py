import streamlit as st

st.set_page_config(page_title="옷 색 조합 추천", page_icon="🎨")

st.title("🎨 옷 색 조합 추천 시스템")

# 색 조합
top_to_bottom = {
    "화이트": ["블랙", "진청", "네이비", "베이지", "회색"],
    "블랙": ["화이트", "그레이", "청색", "베이지"],
    "베이지": ["브라운", "화이트", "블랙", "올리브"],
    "네이비": ["화이트", "그레이", "베이지", "블랙"],
    "그레이": ["블랙", "화이트", "네이비", "딥그린"],
    "브라운": ["베이지", "아이보리", "블랙"],
    "레드": ["블랙", "화이트", "데님"],
    "블루(청색)": ["화이트", "그레이", "블랙"],
    "그린": ["베이지", "브라운", "블랙"],
    "옐로우": ["화이트", "데님", "브라운"]
}

# 반대 방향 매핑
bottom_to_top = {}
for top, bottoms in top_to_bottom.items():
    for bottom in bottoms:
        if bottom not in bottom_to_top:
            bottom_to_top[bottom] = []
        if top not in bottom_to_top[bottom]:
            bottom_to_top[bottom].append(top)

col1, col2 = st.columns(2)
with col1:
    top = st.selectbox("상의 색 선택", ["-"] + list(top_to_bottom.keys()))
with col2:
    bottom = st.selectbox("하의 색 선택", ["-"] + list(bottom_to_top.keys()))

st.write("---")

# 아무것도 선택 안 함
if top == "-" and bottom == "-":
    st.info("상의 또는 하의를 선택하세요.")

# 상의만 선택
elif top != "-" and bottom == "-":
    st.subheader(f"'{top}' 상의에 어울리는 하의")
    for b in top_to_bottom[top]:
        st.write(f"- {b}")

# 하의만 선택
elif top == "-" and bottom != "-":
    st.subheader(f"'{bottom}' 하의에 어울리는 상의")
    for t in bottom_to_top[bottom]:
        st.write(f"- {t}")

# 둘 다 선택 → 조합 평가
else:
    st.subheader("선택한 조합 평가")

    if bottom in top_to_bottom[top]:
        st.success(f"'{top} + {bottom}' 조합은 잘 어울립니다.")
    else:
        st.error(f"'{top} + {bottom}' 조합은 추천되지 않습니다.")
        st.subheader("더 나은 하의 추천")
        for b in top_to_bottom[top]:
            st.write(f"- {b}")

st.caption("Made with Streamlit")
