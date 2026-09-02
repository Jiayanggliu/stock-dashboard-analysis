import streamlit as st
import yfinance as yf
import numpy as np
import plotly.graph_objects as go


# =========================================================
# 1. PAGE SETUP
# =========================================================

st.set_page_config(
    page_title="Market Lens",
    page_icon="📈",
    layout="wide"
)


# =========================================================
# 2. WEBSITE STYLING
# =========================================================

st.markdown("""
<style>

/* ---------- Main background ---------- */
.stApp {
    background-color: #F6F9F7;
}


/* ---------- Main content width ---------- */
.block-container {
    max-width: 1200px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}


/* ---------- Main title ---------- */
h1 {
    color: #24312D;
    font-size: 3rem !important;
    font-weight: 700 !important;
    letter-spacing: -1.5px;
}


/* ---------- Subtitle ---------- */
.subtitle {
    color: #7B8984;
    font-size: 1.15rem;
    margin-top: -10px;
    margin-bottom: 35px;
}


/* ---------- Live data badge ---------- */
.live-badge {
    display: inline-block;
    background-color: #E3F1EB;
    color: #467565;
    padding: 7px 13px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 600;
}


/* ---------- Section heading ---------- */
.section-title {
    color: #24312D;
    font-size: 1.35rem;
    font-weight: 650;
    margin-top: 35px;
}


/* ---------- Metric cards ---------- */
div[data-testid="stMetric"] {
    background-color: #FFFFFF;
    border: 1px solid #E7ECE9;
    padding: 20px 22px;
    border-radius: 18px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.03);
}


/* ---------- Metric label ---------- */
div[data-testid="stMetricLabel"] {
    color: #7B8984;
}


/* ---------- Metric value ---------- */
div[data-testid="stMetricValue"] {
    color: #24312D;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. LOAD LIVE MARKET DATA
# =========================================================

@st.cache_data(ttl=3600)
def load_stock_data(ticker):

    stock_data = yf.Ticker(ticker).history(
        period="2y"
    )

    return stock_data

@st.cache_data(ttl=3600)
def load_company_info(ticker):

    company = yf.Ticker(ticker)

    return company.get_info()


# =========================================================
# 4. HERO SECTION
# =========================================================

left, right = st.columns([5, 1])

with left:

    st.title("Market Lens")

    st.markdown(
        """
        <div class="subtitle">
            Investing insights, without the noise.
        </div>
        """,
        unsafe_allow_html=True
    )


with right:

    st.markdown(
        """
        <div class="live-badge">
            ● Live market data
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 5. STOCK SELECTOR
# =========================================================

st.markdown(
    """
    <div class="section-title">
        Explore a stock
    </div>
    """,
    unsafe_allow_html=True
)


stock = st.selectbox(
    "Select a stock",
    [
        "AAPL",
        "MSFT",
        "GOOGL",
        "NVDA",
        "TSLA",
        "META",
        "AMZN",
        "BRK-B"
    ]
)


# =========================================================
# 6. GET SELECTED STOCK DATA
# =========================================================

stock_data = load_stock_data(stock)

company_info = load_company_info(stock)


if stock_data.empty:

    st.error(
        "Market data could not be loaded. "
        "Please try again later."
    )

    st.stop()


prices = stock_data["Close"].dropna()


# =========================================================
# 7. CALCULATE METRICS
# =========================================================

latest_price = prices.iloc[-1]


# ----- Two-Year Return -----

two_year_return = (
    (latest_price / prices.iloc[0]) - 1
) * 100


# ----- 30-Day Momentum -----

momentum_30d = (
    (latest_price / prices.iloc[-31]) - 1
) * 100


# ----- Daily Returns -----

daily_returns = (
    prices
    .pct_change()
    .dropna()
)


# ----- Annualized Volatility -----

annual_volatility = (
    daily_returns.std()
    * np.sqrt(252)
    * 100
)


# ----- Moving Averages -----

ma_20 = (
    prices
    .rolling(window=20)
    .mean()
)

ma_200 = (
    prices
    .rolling(window=200)
    .mean()
)


# ----- Trend Signal -----

if ma_20.iloc[-1] > ma_200.iloc[-1]:

    trend = "Positive ↑"

else:

    trend = "Cautious ↓"

# =========================================================
# COMPANY BASICS
# =========================================================

pe_ratio = company_info.get("trailingPE")

market_cap = company_info.get("marketCap")

average_volume = company_info.get("averageVolume")

week_52_low = company_info.get("fiftyTwoWeekLow")

week_52_high = company_info.get("fiftyTwoWeekHigh")

def format_large_number(value):

    if value is None:
        return "N/A"

    if value >= 1_000_000_000_000:
        return f"${value / 1_000_000_000_000:.2f}T"

    elif value >= 1_000_000_000:
        return f"${value / 1_000_000_000:.1f}B"

    elif value >= 1_000_000:
        return f"${value / 1_000_000:.1f}M"

    else:
        return f"${value:,.0f}"

def format_volume(value):

    if value is None:
        return "N/A"

    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"

    elif value >= 1_000:
        return f"{value / 1_000:.1f}K"

    else:
        return f"{value:,.0f}"

if pe_ratio is not None:
    pe_display = f"{pe_ratio:.1f}x"
else:
    pe_display = "N/A"

if (
    week_52_low is not None
    and week_52_high is not None
    and week_52_high != week_52_low
):

    week_52_position = (
        (latest_price - week_52_low)
        / (week_52_high - week_52_low)
    ) * 100

else:

    week_52_position = None


# =========================================================
# 8. STOCK HEADER
# =========================================================

st.markdown(
    f'<div style="margin-top:32px; margin-bottom:20px;">'
    f'<span style="font-size:1.8rem; font-weight:700; color:#24312D;">'
    f'{stock}'
    f'</span>'
    f'<span style="font-size:1.05rem; color:#7B8984; margin-left:12px;">'
    f'${latest_price:,.2f}'
    f'</span>'
    f'</div>',
    unsafe_allow_html=True
)


# =========================================================
# 9. KPI CARDS — BEGINNER FRIENDLY
# =========================================================

col1, col2, col3, col4 = st.columns(4)


# -------------------------
# 2-Year Return
# -------------------------

with col1:

    st.caption("Where did it end up?")

    st.metric(
        label="2-Year Return",
        value=f"{two_year_return:+.1f}%"
    )

    with st.popover("ⓘ What does this mean?"):

        st.markdown("""
        **In plain English**

        This tells you how much the stock's price changed
        over the last two years.

        **How to read it**

        - `+20%` → the stock is worth about 20% more
        - `-20%` → the stock is worth about 20% less

        **Finance term**

        This is called **cumulative return**.

        Return tells you where the stock ended up —
        but not how smooth or painful the journey was.
        """)


# -------------------------
# 30-Day Momentum
# -------------------------

with col2:

    st.caption("What's happening lately?")

    st.metric(
        label="30-Day Momentum",
        value=f"{momentum_30d:+.1f}%"
    )

    with st.popover("ⓘ What does this mean?"):

        st.markdown("""
        **In plain English**

        This looks at whether the stock has been moving
        up or down recently.

        **How to read it**

        - Positive → recent price movement is upward
        - Negative → recent price movement is downward

        **Finance term**

        This idea is called **momentum**.

        Momentum describes recent direction.
        It does **not** guarantee what happens next.
        """)


# -------------------------
# Annual Volatility
# -------------------------

with col3:

    st.caption("How bumpy was the ride?")

    st.metric(
        label="Annual Volatility",
        value=f"{annual_volatility:.1f}%"
    )

    with st.popover("ⓘ What does this mean?"):

        st.markdown("""
        **In plain English**

        Volatility tells you how dramatically the stock
        tends to move around.

        **How to read it**

        Higher volatility → bigger price swings

        Lower volatility → a smoother ride

        **Finance term**

        Volatility is based on the **standard deviation
        of returns**.

        Two stocks can have similar returns but feel
        completely different to own because one may
        fluctuate much more.
        """)


# -------------------------
# Trend
# -------------------------

with col4:

    st.caption("Which direction looks stronger?")

    st.metric(
        label="Trend",
        value=trend
    )

    with st.popover("ⓘ What does this mean?"):

        st.markdown("""
        **In plain English**

        We compare the stock's recent average price
        with its longer-term average price.

        **Positive ↑**

        The 20-day moving average is above the
        200-day moving average.

        **Cautious ↓**

        The short-term average is below the
        long-term average.

        **Finance term**

        These are called **moving averages**.

        They help smooth noisy daily prices so the
        broader direction becomes easier to see.
        """)

# =========================================================
# 10. INTERACTIVE PERFORMANCE CHART
# =========================================================

st.markdown(
    """
    <div class="section-title">
        Performance
    </div>
    """,
    unsafe_allow_html=True
)

# Convert price history into cumulative performance
performance = (
    (prices / prices.iloc[0]) - 1
) * 100


# Create interactive chart
fig = go.Figure()


fig.add_trace(
    go.Scatter(
        x=prices.index,
        y=performance,
        mode="lines",
        name=stock,
        line=dict(
            color="#5F9F82",
            width=3
        ),

        customdata=prices,

        hovertemplate=
            "<b>%{x|%b %d, %Y}</b><br>"
            "Price: $%{customdata:.2f}<br>"
            "Return: %{y:+.1f}%"
            "<extra></extra>"
    )
)


fig.update_layout(

    height=480,

    margin=dict(
        l=20,
        r=20,
        t=30,
        b=20
    ),

    paper_bgcolor="#F6F9F7",

    plot_bgcolor="#FFFFFF",

    hovermode="x",

    showlegend=False,

    xaxis=dict(
        title="",
        showgrid=False
    ),

    yaxis=dict(
        title="Return since start (%)",
        gridcolor="#E7ECE9",
        zeroline=True,
        zerolinecolor="#BDD7CC"
    )
)


st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================================================
# 11. PLAIN-ENGLISH INSIGHT
# =========================================================

if momentum_30d > 5:
    momentum_text = "strong positive momentum"
elif momentum_30d > 0:
    momentum_text = "mild positive momentum"
elif momentum_30d > -5:
    momentum_text = "mild negative momentum"
else:
    momentum_text = "weak recent momentum"


if annual_volatility < 25:
    risk_text = "relatively low volatility"
elif annual_volatility < 40:
    risk_text = "moderate volatility"
else:
    risk_text = "high volatility"


if trend == "Positive ↑":
    trend_text = "the short-term trend is above the long-term trend"
else:
    trend_text = "the short-term trend is below the long-term trend"


insight = (
    f"{stock} currently shows **{momentum_text}**, with "
    f"**{risk_text}**. Based on its moving averages, "
    f"{trend_text}."
)

# =========================================================
# 12. BEYOND THE PRICE
# =========================================================

st.markdown(
    """
    <div class="section-title">
        Beyond the price
    </div>
    """,
    unsafe_allow_html=True
)

st.caption(
    "A few numbers finance apps often show — "
    "explained in plain English."
)


b1, b2, b3, b4 = st.columns(4)


# -------------------------
# P/E Ratio
# -------------------------

with b1:

    st.caption("Price vs. earnings")

    st.metric(
        label="P/E Ratio",
        value=pe_display
    )

    with st.popover("ⓘ Why does this matter?"):

        st.markdown("""
        **In plain English**

        P/E compares a company's stock price with
        the earnings it generates.

        A P/E of `30x` roughly means investors are
        paying $30 for every $1 of annual earnings.

        **Important context**

        A higher P/E does **not** automatically mean
        a stock is expensive.

        A lower P/E does **not** automatically mean
        a stock is cheap.

        Different industries and companies can have
        very different typical P/E ratios.

        **Finance term**

        P/E stands for **Price-to-Earnings Ratio**.
        """)


# -------------------------
# Market Cap
# -------------------------

with b2:

    st.caption("Company size")

    st.metric(
        label="Market Cap",
        value=format_large_number(market_cap)
    )

    with st.popover("ⓘ Why does this matter?"):

        st.markdown("""
        **In plain English**

        Market cap is the total market value of
        a company's shares.

        It is approximately:

        `Share Price × Shares Outstanding`

        **How to read it**

        Market cap helps describe how large a
        publicly traded company is.

        It does **not** tell you whether the company
        is a good investment.
        """)


# -------------------------
# Average Volume
# -------------------------

with b3:

    st.caption("Trading activity")

    st.metric(
        label="Avg. Daily Volume",
        value=format_volume(average_volume)
    )

    with st.popover("ⓘ Why does this matter?"):

        st.markdown("""
        **In plain English**

        Volume tells you how many shares change hands.

        Higher average volume usually means the stock
        is traded more actively.

        **Important context**

        High volume does not automatically mean
        investors are bullish.

        Every completed trade has both a buyer
        and a seller.

        Volume describes **activity**, not whether
        the stock is good or bad.
        """)


# -------------------------
# 52-Week Position
# -------------------------

with b4:

    st.caption("Where is it now?")

    if week_52_position is not None:

        st.metric(
            label="52-Week Position",
            value=f"{week_52_position:.0f}%"
        )

    else:

        st.metric(
            label="52-Week Position",
            value="N/A"
        )

    with st.popover("ⓘ Why does this matter?"):

        st.markdown("""
        **In plain English**

        This shows where today's price sits between
        the stock's lowest and highest prices during
        the past 52 weeks.

        `0%` ≈ near the 52-week low

        `100%` ≈ near the 52-week high

        **Important context**

        Being near a high does not automatically mean
        a stock is overpriced.

        Being near a low does not automatically mean
        it is a bargain.

        This metric gives **context**, not a recommendation.
        """)



