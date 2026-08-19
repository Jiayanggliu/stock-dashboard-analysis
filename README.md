# Stock Dashboard Analysis

A two-year analysis of selected large-cap U.S. stocks designed for a **self-directed retail investor** balancing growth, risk, and diversification.

## Dashboard Preview

### 1. Two-Year Stock Price Performance

![Stock Price Performance](assets/stock_prices.jpg)

Prices are normalized to 100 so performance can be compared directly across stocks. **GOOGL was the strongest performer** over the period.

### 2. AAPL Moving Averages

![AAPL Moving Averages](assets/moving_averages.jpg)

The **20-day moving average** shows the short-term trend, while the **200-day moving average** shows the long-term trend. AAPL remains above its 200-day moving average but has recently moved below its 20-day moving average.

### 3. Rolling 30-Day Volatility

![Rolling 30-Day Volatility](assets/rolling_volatility.jpg)

Rolling volatility highlights changes in risk over time. **TSLA shows the highest volatility**, while **BRK-B is generally more stable**.

### 4. Stock Return Correlations

![Stock Return Correlations](assets/correlation_heatmap.jpg)

Correlation helps evaluate diversification. **AMZN and META have a relatively high correlation (0.58)**, while **BRK-B and NVDA have a very low correlation (0.02)**.

## Business Use

The dashboard helps a retail investor evaluate four questions:

- **Performance:** Which stocks performed best?
- **Trend:** Is the stock showing short-term or long-term strength?
- **Risk:** How volatile is each stock?
- **Diversification:** Which stocks move differently from one another?

These views can support portfolio allocation, position sizing, and rebalancing decisions.

## Project Files

- `stakeholder_dashboard.ipynb` — analysis, calculations, and dashboard code
- `assets/` — dashboard visualizations
