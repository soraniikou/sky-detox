
    
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

# セッション状態の初期化
if "triggered" not in st.session_state:
    st.session_state.triggered = False
if "ripple_key" not in st.session_state:
    st.session_state.ripple_key = 0

# ボタンが押されるたびに色をランダム選択
if st.session_state.triggered:
    if "color_pattern" not in st.session_state or st.session_state.get("color_changed", False):
        st.session_state.color_pattern = random.choice(color_patterns)
        st.session_state.color_changed = False
    selected_color = st.session_state.color_pattern
else:
    # 初期状態用のデフォルト色
    selected_color = color_patterns[0]

# ---- CSS ----
st.markdown(f"""
<style>
/* 全体背景 - 水色ベース */
.stApp {{
    background: linear-gradient(180deg, #dbeafe, #bfdbfe);
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
    z-index: 9999;
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

/* アニメーション終了後にボタンを再表示するためのスタイル */
.button-container {{
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 10000;
}}
</style>
""", unsafe_allow_html=True)

# ---- UI ----
st.markdown("<div style='height:20vh'></div>", unsafe_allow_html=True)

if not st.session_state.triggered:
    # 初期状態：ボタンを表示
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("……", key="initial_button"):
            st.session_state.triggered = True
            st.session_state.color_changed = True
            st.session_state.ripple_key += 1
            st.rerun()

else:
    # トリガー後：波紋とテキストを表示
    word_from_sky = "空の色へ"

    st.markdown(f"""
    <div class="ripple" key="{st.session_state.ripple_key}"></div>
    <div class="fade-text triggered">{word_from_sky}</div>
    <script>
    setTimeout(function() {{
        const app = window.parent.document.querySelector('.stApp');
        if (app) app.classList.add('absorb');
    }}, 100);
    </script>
    """, unsafe_allow_html=True)
    
    # 10秒経過後、中央に再度ボタンを表示
    st.markdown("<div style='height:35vh'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("……", key=f"button_{st.session_state.ripple_key}"):
            st.session_state.color_changed = True
            st.session_state.ripple_key += 1
            st.rerun()
