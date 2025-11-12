import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.colors as pc
import os

# 페이지 기본 설정
st.set_page_config(page_title="국가별 MBTI 분석", layout="wide")
st.title("🌎 국가별 MBTI 데이터 시각화")

# CSV 경로 설정 (상위 폴더)
csv_path = os.path.join(os.path.dirname(__file__), "..", "countriesMBTI_16types.csv")

# CSV 불러오기
try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    st.error("❌ CSV 파일(countriesMBTI_16types.csv)을 상위 폴더에 넣어주세요.")
    st.stop()

# MBTI 열 목록
mbti_columns = [col for col in df.columns if col != "Country"]
countries = df["Country"].tolist()

# 탭 생성
tab1, tab2 = st.tabs(["🌍 국가별 MBTI 비율", "🔤 MBTI별 국가 순위"])

# ─────────────────────────────────────────────
# 탭 1 : 국가별 MBTI 비율
# ─────────────────────────────────────────────
with tab1:
    st.subheader("📊 선택한 국가의 MBTI 분포")

    selected_country = st.selectbox("국가를 선택하세요:", countries, key="country_select")

    # 해당 국가 데이터 추출
    country_data = df[df["Country"] == selected_country].iloc[0, 1:]
    country_df = pd.DataFrame({
        "MBTI": mbti_columns,
        "비율": country_data.values
    }).sort_values("비율", ascending=False)

    # 색상 설정 (1등은 빨강, 나머지는 파랑 계열)
    colors = pc.sample_colorscale("Blues", [i / (len(country_df) - 1) for i in range(len(country_df))])
    colors[0] = "red"

    # 그래프 생성
    fig1 = px.bar(
        country_df,
        x="MBTI",
        y="비율",
        text=country_df["비율"].map(lambda x: f"{x*100:.1f}%"),
        title=f"{selected_country}의 MBTI 분포",
    )
    fig1.update_traces(marker_color=colors, textposition="outside")
    fig1.update_layout(
        xaxis_title="MBTI 유형",
        yaxis_title="비율",
        template="plotly_white",
        title_x=0.5,
        showlegend=False
    )
    st.plotly_chart(fig1, use_container_width=True)

# ─────────────────────────────────────────────
# 탭 2 : MBTI별 국가 순위
# ─────────────────────────────────────────────
with tab2:
    st.subheader("🏆 MBTI 유형별 상위 국가 비교")

    selected_type = st.selectbox("MBTI 유형을 선택하세요:", mbti_columns, key="type_select")

    # 해당 MBTI 유형 기준으로 상위 10개국 정렬
    type_df = df[["Country", selected_type]].sort_values(by=selected_type, ascending=False).reset_index(drop=True)

    # 상위 10개국 추출
    top10 = type_df.head(10).copy()

    # 한국 포함 여부 확인
    korea_row = type_df[type_df["Country"].str.lower() == "south korea"]
    if not korea_row.empty and "South Korea" not in top10["Country"].values:
        top10 = pd.concat([top10, korea_row], ignore_index=True)

    # 색상 설정 (기본은 회색, 한국은 보라색)
    colors = ["#6a5acd" if c == "South Korea" else "#3399ff" for c in top10["Country"]]

    # 그래프 생성
    fig2 = px.bar(
        top10,
        x="Country",
        y=selected_type,
        text=top10[selected_type].map(lambda x: f"{x*100:.1f}%"),
        title=f"{selected_type} 유형이 가장 많은 국가 Top 10",
    )
    fig2.update_traces(marker_color=colors, textposition="outside")
    fig2.update_layout(
        xaxis_title="국가",
        yaxis_title="비율",
        template="plotly_white",
        title_x=0.5,
        showlegend=False
    )

    st.plotly_chart(fig2, use_container_width=True)
