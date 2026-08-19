# Stock Dashboard Analysis

A two-year analysis of selected large-cap U.S. stocks designed for a **self-directed retail investor** balancing growth, risk, and diversification.

## Dashboard Preview

### 1. Two-Year Stock Price Performance

<img width="2085" height="885" alt="stock_prices" src="https://github.com/user-attachments/assets/de3a2ea1-494a-473d-aad3-57e498ad2a07" />


Prices are normalized to 100 so performance can be compared directly across stocks. **GOOGL was the strongest performer** over the period.

### 2. AAPL Moving Averages

<img width="2085" height="885" alt="moving_averages" src="https://github.com/user-attachments/assets/9c4af7e2-2846-49ef-aba8-0ba2f05a7a53" />


The **20-day moving average** shows the short-term trend, while the **200-day moving average** shows the long-term trend. AAPL remains above its 200-day moving average but has recently moved below its 20-day moving average.

### 3. Rolling 30-Day Volatility

<img width="2085" height="885" alt="rolling_volatility" src="https://github.com/user-attachments/assets/043227ac-8016-4898-bc9a-83de45695a4a" />

Rolling volatility highlights changes in risk over time. **TSLA shows the highest volatility**, while **BRK-B is generally more stable**.

### 4. Stock Return Correlations

<img width="1023" height="884" alt="correlation_heatmap" src="https://github.com/user-attachments/assets/34bd86ff-363b-498a-8104-3816e87fae22" />

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
