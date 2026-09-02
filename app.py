import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

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

# -------------------------
# Load market data
# -------------------------

@st.cache_data(ttl=3600)
def load_stock_data(ticker):
    stock_data = yf.Ticker(ticker).history(period="2y")
    return stock_data


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

# -------------------------
# Calculate metrics
# -------------------------

stock_data = load_stock_data(stock)

prices = stock_data["Close"].dropna()

latest_price = prices.iloc[-1]

two_year_return = (
    (latest_price / prices.iloc[0]) - 1
) * 100

momentum_30d = (
    (latest_price / prices.iloc[-31]) - 1
) * 100

daily_returns = prices.pct_change().dropna()

annual_volatility = (
    daily_returns.std() * np.sqrt(252) * 100
)

ma_20 = prices.rolling(window=20).mean()
ma_200 = prices.rolling(window=200).mean()

if ma_20.iloc[-1] > ma_200.iloc[-1]:
    trend = "Positive ↑"
else:
    trend = "Cautious ↓"

# -------------------------
# KPI cards
# -------------------------

st.markdown(
    f"""
    <div style="margin-top: 30px; margin-bottom: 20px;">
        <span style="font-size: 1.8rem; font-weight: 700; color: #24312D;">
            {stock}
        </span>
        <span style="font-size: 1.05rem; color: #7B8984; margin-left: 12px;">
            ${latest_price:,.2f}
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "2-Year Return",
        f"{two_year_return:+.1f}%"
    )

with col2:
    st.metric(
        "30-Day Momentum",
        f"{momentum_30d:+.1f}%"
    )

with col3:
    st.metric(
        "Annual Volatility",
        f"{annual_volatility:.1f}%"
    )

with col4:
    st.metric(
        "Trend",
        trend
    )

/* Streamlit metric cards */
div[data-testid="stMetric"] {
    background-color: #FFFFFF;
    border: 1px solid #E7ECE9;
    padding: 20px 22px;
    border-radius: 18px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.03);
}

div[data-testid="stMetricLabel"] {
    color: #7B8984;
}

div[data-testid="stMetricValue"] {
    color: #24312D;
}
