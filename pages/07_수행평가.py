import streamlit as st

st.set_page_config(page_title="옷 색 + 스타일 추천", page_icon="🎨", layout="centered")
st.title("🎨 옷 색 조합 + 스타일 + 예시 아이템 추천 시스템")


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

# 하의 → 상의 역매핑 생성
bottom_to_top = {}
for top, bottoms in top_to_bottom.items():
    for bottom in bottoms:
        bottom_to_top.setdefault(bottom, [])
        if top not in bottom_to_top[bottom]:
            bottom_to_top[bottom].append(top)

# ──────────────────────────────────────────────
# 2) 스타일 + 예시 아이템 데이터
# ──────────────────────────────────────────────
style_db = {
    "화이트": {
        "styles": ["미니멀", "오피스룩", "댄디룩", "데일리 캐주얼"],
        "top_examples": ["화이트 린넨 셔츠", "화이트 오버핏 티셔츠", "화이트 니트"],
        "bottom_examples": ["블랙 슬랙스", "진청 데님", "베이지 치노팬츠", "네이비 와이드팬츠"]
    },
    "블랙": {
        "styles": ["스트릿", "미니멀", "시크룩", "올블랙룩"],
        "top_examples": ["블랙 후드티", "블랙 크롭티", "블랙 셔츠"],
        "bottom_examples": ["블랙 와이드팬츠", "그레이 조거팬츠", "블루 데님", "베이지 치노팬츠"]
    },
    "네이비": {
        "styles": ["비즈니스 캐주얼", "클래식룩", "미니멀"],
        "top_examples": ["네이비 맨투맨", "네이비 셔츠", "네이비 니트"],
        "bottom_examples": ["베이지 슬랙스", "화이트 팬츠", "그레이 울바지"]
    },
    "그레이": {
        "styles": ["미니멀", "캐주얼", "댄디룩"],
        "top_examples": ["그레이 후드티", "그레이 오버핏 티셔츠", "그레이 니트"],
        "bottom_examples": ["블랙 슬랙스", "네이비 데님", "딥그린 와이드팬츠"]
    },
    "베이지": {
        "styles": ["데일리 캐주얼", "포멀", "미니멀"],
        "top_examples": ["베이지 니트", "베이지 린넨 셔츠", "베이지 가디건"],
        "bottom_examples": ["화이트 데님", "블랙 와이드팬츠", "올리브 슬랙스"]
    },
    "브라운": {
        "styles": ["빈티지", "포멀", "클래식"],
        "top_examples": ["브라운 니트", "브라운 가디건", "브라운 체크 셔츠"],
        "bottom_examples": ["베이지 울팬츠", "아이보리 코튼팬츠", "블랙 데님"]
    },
    "블루(청색)": {
        "styles": ["데님 캐주얼", "스트릿", "아메카지"],
        "top_examples": ["청색 셔츠", "블루 데님 자켓", "인디고 니트"],
        "bottom_examples": ["화이트 데님", "그레이 슬림진", "블랙 스키니진", "청치마(데님 스커트)"]
    },
    "그린": {
        "styles": ["빈티지", "아웃도어", "캐주얼"],
        "top_examples": ["올리브 셔츠", "딥그린 니트", "카키 맨투맨"],
        "bottom_examples": ["베이지 슬랙스", "브라운 코튼팬츠", "블랙 스트레이트 팬츠"]
    },
    "옐로우": {
        "styles": ["캐주얼", "스트릿", "레트로"],
        "top_examples": ["머스타드 맨투맨", "옐로우 니트", "옐로우 크롭티"],
        "bottom_examples": ["데님 청바지", "브라운 치노팬츠", "화이트 롱스커트"]
    }
}


# ──────────────────────────────────────────────
# UI
# ──────────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    top = st.selectbox("👕 상의 색 선택", ["-"] + list(top_to_bottom.keys()))
with col2:
    bottom = st.selectbox("👖 하의 색 선택", ["-"] + sorted(bottom_to_top.keys()))

st.write("---")


# ──────────────────────────────────────────────
# 추천 로직
# ──────────────────────────────────────────────
def show_style_info(color):
    """해당 색의 스타일 + 예시 아이템 출력"""
    data = style_db.get(color)
    if not data:
        st.write("정보 없음")
        return

    st.markdown("### 🎯 어울리는 스타일")
    for s in data["styles"]:
        st.write(f"- {s}")

    st.markdown("### 👕 추천 상의 아이템")
    for item in data["top_examples"]:
        st.write(f"- {item}")

    st.markdown("### 👖 추천 하의 아이템")
    for item in data["bottom_examples"]:
        st.write(f"- {item}")


# 1) 아무것도 선택 X
if top == "-" and bottom == "-":
    st.info("👕 상의 또는 👖 하의를 선택하세요.")

# 2) 상의만 선택
elif top != "-" and bottom == "-":
    st.subheader(f"'{top}' 상의에 어울리는 하의")
    for b in top_to_bottom[top]:
        st.write(f"- **{b}**")

    st.write("---")
    show_style_info(top)

# 3) 하의만 선택
elif top == "-" and bottom != "-":
    st.subheader(f"'{bottom}' 하의에 어울리는 상의")
    for t in bottom_to_top[bottom]:
        st.write(f"- **{t}**")

    st.write("---")
    show_style_info(bottom)

# 4) 둘 다 선택 → 조합 평가 + 스타일 조합
else:
    st.subheader("🎨 색 조합 평가")

    if bottom in top_to_bottom[top]:
        st.success(f"✔ '{top} + {bottom}' 조합은 매우 잘 어울립니다!")
    else:
        st.error(f"✖ '{top} + {bottom}' 조합은 추천되지 않아요.")
        st.markdown("#### 👉 더 나은 하의 추천")
        for b in top_to_bottom[top]:
            st.write(f"- **{b}**")

    st.write("---")
    st.subheader("🎯 스타일 + 예시 아이템 종합 추천")

    combined_styles = set()
    combined_top_items = []
    combined_bottom_items = []

    for color in [top, bottom]:
        if color in style_db:
            combined_styles.update(style_db[color]["styles"])
            combined_top_items.extend(style_db[color]["top_examples"])
            combined_bottom_items.extend(style_db[color]["bottom_examples"])

    st.markdown("### ✔ 어울리는 스타일")
    for s in combined_styles:
        st.write(f"- {s}")

    st.markdown("### 👕 추천 상의 아이템")
    for item in combined_top_items:
        st.write(f"- {item}")

    st.markdown("### 👖 추천 하의 아이템")
    for item in combined_bottom_items:
        st.write(f"- {item}")

st.caption("Made with Streamlit • 색 + 스타일 + 아이템 추천 자동 시스템")
