import streamlit as st
import random

st.set_page_config(page_title="空へ", layout="centered")

# ---- 8種類の色パターン ----
color_patterns = [
    {
        "name": "紺色",
        "gradient": "linear-gradient(180deg, #a2b6df, #1e3a8a)",
        "text_color": "#ffffff"
    },
    {
        "name": "薄い水色",
        "gradient": "linear-gradient(180deg, #e0f2fe, #7dd3fc)",
        "text_color": "#1e3a8a"
    },
    {
        "name": "エメラルド",
        "gradient": "linear-gradient(180deg, #a7f3d0, #059669)",
        "text_color": "#ffffff"
    },
    {
        "name": "夕焼け",
        "gradient": "linear-gradient(180deg, #fecaca, #dc2626)",
        "text_color": "#ffffff"
    },
    {
        "name": "紫",
        "gradient": "linear-gradient(180deg, #ddd6fe, #7c3aed)",
        "text_color": "#ffffff"
    },
    {
        "name": "ピンク",
        "gradient": "linear-gradient(180deg, #fbcfe8, #ec4899)",
        "text_color": "#ffffff"
    },
    {
        "name": "オレンジ",
        "gradient": "linear-gradient(180deg, #fed7aa, #ea580c)",
        "text_color": "#ffffff"
    },
    {
        "name": "深海",
        "gradient": "linear-gradient(180deg, #67e8f9, #0c4a6e)",
        "text_color": "#ffffff"
    }
]

# ランダムに色を選択（セッション開始時に1回だけ）
if "color_pattern" not in st.session_state:
    st.session_state.color_pattern = random.choice(color_patterns)

selected_color = st.session_state.color_pattern

# ---- CSS ----
st.markdown(f"""
<style>
/* 全体背景 */
.stApp {{
    background: linear-gradient(180deg, #f2f2f2, #e8e6e1);
    transition: background 10s ease;
}}

/* 吸い込まれる背景 */
.stApp.absorb {{
    background: {selected_color['gradient']} !important;
}}

/* 消えるテキスト */
.fade-text {{
    font-size: 2rem;
    text-align: center;
    color: rgba(50,50,50,1);
    animation: fadeOut 10s forwards;
}}

.fade-text.triggered {{
    color: {selected_color['text_color']};
}}

@keyframes fadeOut {{
    0% {{ opacity: 1; }}
    70% {{ opacity: 0.8; }}
    100% {{ opacity: 0; }}
}}

/* 波紋エフェクト */
.ripple {{
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: radial-gradient(circle, {selected_color['text_color']}33, transparent);
    animation: rippleEffect 10s ease-out forwards;
    pointer-events: none;
}}

@keyframes rippleEffect {{
    0% {{
        width: 50px;
        height: 50px;
        opacity: 1;
    }}
    50% {{
        width: 800px;
        height: 800px;
        opacity: 0.5;
    }}
    100% {{
        width: 1600px;
        height: 1600px;
        opacity: 0;
    }}
}}

/* ボタンスタイル */
div.stButton > button {{
    background: transparent;
    border: 2px solid #888;
    color: #555;
    font-size: 1.5rem;
    padding: 1rem 3rem;
    border-radius: 50px;
    transition: all 0.3s ease;
}}

div.stButton > button:hover {{
    border-color: #333;
    color: #333;
    transform: scale(1.05);
}}
</style>
""", unsafe_allow_html=True)

# ---- UI ----
st.markdown("<div style='height:20vh'></div>", unsafe_allow_html=True)

if "triggered" not in st.session_state:
    st.session_state.triggered = False

if not st.session_state.triggered:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("……"):
            st.session_state.triggered = True
            st.rerun()

else:
    # ここに Dify から返ってきた言葉を入れる
    word_from_sky = "空の色へ"

    st.markdown(f"""
    <div class="ripple"></div>
    <div class="fade-text triggered">{word_from_sky}</div>
    <script>
    setTimeout(function() {{
        const app = window.parent.document.querySelector('.stApp');
        if (app) app.classList.add('absorb');
    }}, 100);
    </script>
    """, unsafe_allow_html=True)
