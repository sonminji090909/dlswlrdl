import streamlit as st

st.set_page_config(page_title="옷 색 + 스타일 추천", page_icon="🎨", layout="centered")

st.title("🎨 옷 색 조합 + 스타일 추천 시스템")


# ──────────────────────────────────────────────
# 1) 색 조합 데이터
# ──────────────────────────────────────────────
top_to_bottom = {
    "화이트": ["블랙", "진청", "네이비", "베이지", "그레이"],
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

# 역매핑 (하의 → 상의)
bottom_to_top = {}
for top, bottoms in top_to_bottom.items():
    for bottom in bottoms:
        bottom_to_top.setdefault(bottom, [])
        if top not in bottom_to_top[bottom]:
            bottom_to_top[bottom].append(top)


# ──────────────────────────────────────────────
# 2) 스타일 추천 데이터
# ──────────────────────────────────────────────
style_recommendations = {
    "화이트": ["미니멀", "오피스룩", "댄디룩"],
    "블랙": ["스트릿", "올블랙룩", "미니멀"],
    "베이지": ["데일리 캐주얼", "미니멀", "포멀"],
    "네이비": ["비즈니스 캐주얼", "클래식룩"],
    "그레이": ["미니멀", "캐주얼", "댄디"],
    "브라운": ["빈티지", "캐주얼", "포멀"],
    "레드": ["포인트룩", "스트릿"],
    "블루(청색)": ["데님 캐주얼", "아메카지"],
    "그린": ["아웃도어", "빈티지", "캐주얼"],
    "옐로우": ["캐주얼", "스트릿", "레트로"],
    "진청": ["데님 캐주얼", "아메카지"],
    "청색": ["데님 캐주얼", "스트릿"],
    "베이지(하의)": ["미니멀", "데일리"],
    "블랙(하의)": ["미니멀", "올블랙", "스트릿"]
}


# ──────────────────────────────────────────────
# 3) UI
# ──────────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    top = st.selectbox("👕 상의 색 선택", ["-"] + list(top_to_bottom.keys()))
with col2:
    bottom = st.selectbox("👖 하의 색 선택", ["-"] + sorted(bottom_to_top.keys()))

st.write("---")

# ──────────────────────────────────────────────
# 4) 추천 시스템 로직
# ──────────────────────────────────────────────

# 아무것도 선택 X
if top == "-" and bottom == "-":
    st.info("👕 상의 또는 👖 하의를 선택하세요.")

#  상의만 선택
elif top != "-" and bottom == "-":
    st.subheader(f"✔ '{top}' 상의에 어울리는 하의")
    for b in top_to_bottom[top]:
        st.write(f"- **{b}**")

    st.subheader("🎯 추천 스타일")
    for s in style_recommendations.get(top, []):
        st.write(f"- {s}")

# 하의만 선택
elif top == "-" and bottom != "-":
    st.subheader(f"✔ '{bottom}' 하의에 어울리는 상의")
    for t in bottom_to_top[bottom]:
        st.write(f"- **{t}**")

    st.subheader("🎯 추천 스타일")
    for s in style_recommendations.get(bottom, []):
        st.write(f"- {s}")

# 둘 다 선택 → 조합 평가 + 스타일 추천
else:
    st.subheader("🎯 색 조합 평가")

    if bottom in top_to_bottom.get(top, []):
        st.success(f"✔ '{top} + {bottom}' 조합은 잘 어울립니다!")
    else:
        st.error(f"✖ '{top} + {bottom}' 조합은 추천되지 않습니다.")

        st.subheader("👉 더 나은 하의")
        for b in top_to_bottom[top]:
            st.write(f"- **{b}**")

    # 스
