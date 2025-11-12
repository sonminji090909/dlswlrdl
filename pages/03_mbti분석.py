import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.colors as pc

# 앱 제목
st.set_page_config(page_title="국가별 MBTI 분석", layout="wide")
st.title("🌎 국가별 MBTI 유형 비율 시각화")

# CSV 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요 (예: countriesMBTI_16types.csv)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # MBTI 열만 추출 (Country 제외)
    mbti_columns = [col for col in df.columns if col != "Country"]
    countries = df["Country"].tolist()

    # 국가 선택
    selected_country = st.selectbox("국가를 선택하세요:", countries)

    # 선택한 국가 데이터 추출
    country_data = df[df["Country"] == selected_country].iloc[0, 1:]
    country_df = pd.DataFrame({
        "MBTI": mbti_columns,
        "비율": country_data.values
    }).sort_values("비율", ascending=False)

    # 색상 설정 (1등은 빨강, 나머지는 파랑 그라데이션)
    colors = pc.sample_colorscale("Blues", [i / (len(country_df) - 1) for i in range(len(country_df))])
    colors[0] = "red"  # 1등은 빨강색으로 강조

    # Plotly 그래프 생성
    fig = px.bar(
        country_df,
        x="MBTI",
        y="비율",
        text=country_df["비율"].map(lambda x: f"{x*100:.1f}%"),
        title=f"{selected_country}의 MBTI 분포",
    )

    # 막대 색 적용
    fig.update_traces(marker_color=colors, textposition="outside")
    fig.update_layout(
        xaxis_title="MBTI 유형",
        yaxis_title="비율",
        template="plotly_white",
        title_x=0.5,
        showlegend=False
    )

    # 그래프 표시
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("⬆️ CSV 파일을 업로드하면 그래프가 표시됩니다.")
