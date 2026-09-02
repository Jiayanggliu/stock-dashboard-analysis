import streamlit as st

st.title("Retail Investor Stock Dashboard")

st.write(
  "An interactive dashboard for comparing stock performance,"
  "momentum, volatility, and trent."
)

# -------------------------
# Page setup
# -------------------------

st.set_page_config(
    page_title="Market Lens",
    page_icon="📈",
    layout="wide"
)

# -------------------------
# Custom styling
# -------------------------

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #F6F9F7;
}

/* Main content width */
.block-container {
    max-width: 1200px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}

/* Main title */
h1 {
    color: #24312D;
    font-size: 3rem !important;
    font-weight: 700 !important;
    letter-spacing: -1.5px;
}

/* Subtitle */
.subtitle {
    color: #7B8984;
    font-size: 1.15rem;
    margin-top: -10px;
    margin-bottom: 35px;
}

/* Small status badge */
.live-badge {
    display: inline-block;
    background-color: #E3F1EB;
    color: #467565;
    padding: 7px 13px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 600;
}

/* Cards */
.metric-card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #E7ECE9;
    box-shadow: 0 3px 12px rgba(0,0,0,0.03);
}

/* Section heading */
.section-title {
    color: #24312D;
    font-size: 1.35rem;
    font-weight: 650;
    margin-top: 35px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Hero section
# -------------------------

left, right = st.columns([5, 1])

with left:
    st.title("Market Lens")
    st.markdown(
        '<div class="subtitle">'
        'Investing insights, without the noise.'
        '</div>',
        unsafe_allow_html=True
    )

with right:
    st.markdown(
        '<div class="live-badge">● Live market data</div>',
        unsafe_allow_html=True
    )

st.markdown("---")

# -------------------------
# Stock selector
# -------------------------

st.markdown(
    '<div class="section-title">Explore a stock</div>',
    unsafe_allow_html=True
)

stock = st.selectbox(
    "Select a stock",
    ["AAPL", "MSFT", "GOOGL", "NVDA", "TSLA", "META", "AMZN", "BRK-B"]
)

st.write(f"You selected **{stock}**.")
