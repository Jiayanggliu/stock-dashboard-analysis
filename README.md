<div align="center">

# Market Lens

### Investing insights, without the noise.

**A beginner-first stock exploration experience designed to make finance feel understandable before it feels technical.**

[Live Demo](https://jiayang-stock-dashboard.streamlit.app/) · [Analysis Notebook](./stakeholder_dashboard.ipynb)

</div>

---

## Why I built this

Most finance platforms are built for people who already speak finance.

They show users metrics like **volatility, momentum, P/E, volume, moving averages, and market cap** — but often assume the user already knows what those numbers mean.

**Market Lens explores a different idea:**

> You should not need a finance background to start understanding investing.

Instead of adding more data, Market Lens focuses on translating market information into **intuition, context, and plain-English explanations**.

The goal is not to tell users what to buy or sell. It is to help someone with little or no investing background understand what they are looking at — and gradually learn the financial language behind it.

---

## Product idea

Market Lens follows a simple information hierarchy:

**Intuition → Explanation → Financial term → Metric**

For example, instead of showing only:

`Annual Volatility: 44.7%`

Market Lens first asks:

**“How bumpy was the ride?”**

Users can then open a short explanation to learn what volatility measures, how to interpret it, and why it matters.

This same beginner-first approach is used throughout the dashboard.

---

## What the dashboard shows

### Performance & market behavior

| Beginner question | Financial metric |
|---|---|
| **Where did it end up?** | 2-Year Return |
| **What’s happening lately?** | 30-Day Momentum |
| **How bumpy was the ride?** | Annualized Volatility |
| **Which direction looks stronger?** | 20-Day vs. 200-Day Moving Average Trend |

Each KPI includes an optional explanation so users can learn without turning the page into a finance textbook.

### Interactive performance view

The dashboard converts two years of historical prices into cumulative return and lets users hover over the chart to see the exact **date, stock price, and return since the start of the period**.

### Beyond the price

Market Lens also introduces common metrics that users often see in investing apps but may not immediately understand:

- **P/E Ratio** — price relative to company earnings
- **Market Cap** — approximate market value of the company
- **Average Daily Volume** — how actively the stock trades
- **52-Week Position** — where the current price sits within its recent yearly range

The focus is descriptive rather than prescriptive: these metrics provide context, not a buy/sell recommendation.

---

## Design philosophy

I intentionally avoided the traditional dark, dense, red-and-green trading-terminal aesthetic.

Market Lens is designed to feel:

- **Calm** — no FOMO-driven signals or aggressive buy/sell language
- **Clear** — a small number of meaningful metrics at a time
- **Beginner-friendly** — intuition appears before terminology
- **Interactive** — explanations are available when the user wants them
- **Objective** — historical and market metrics are presented as context, not investment advice

---

## Tech stack

`Python` · `Pandas` · `NumPy` · `yfinance` · `Plotly` · `Streamlit`

The app uses Yahoo Finance data through `yfinance`, calculates market metrics in Python, builds interactive visualizations with Plotly, and is deployed publicly with Streamlit Community Cloud.

---

## Current build

- [x] Live market-data workflow
- [x] Beginner-friendly KPI cards
- [x] On-demand metric explanations
- [x] Interactive two-year performance chart
- [x] Momentum, volatility, and moving-average analysis
- [x] Average-volume and 52-week context
- [x] Public Streamlit deployment
- [ ] Search any company or ticker
- [ ] More reliable valuation-data fallback for P/E and market cap
- [ ] Maximum drawdown / “how painful was the ride?”
- [ ] $1,000 investment scenario
- [ ] Risk vs. momentum comparison lens
- [ ] Shareable insight cards

---

## Where this project is going

The long-term idea is not to build another Bloomberg, Robinhood, or TradingView clone.

I want Market Lens to explore a smaller but more human problem:

> **How can we make investing feel accessible to someone who has always assumed finance was not for them?**

Future features will focus less on adding technical indicators and more on helping beginners understand the *experience* behind the numbers — risk, drawdowns, trade-offs, and how different stocks can feel very different to hold even when headline returns look similar.

**Returns tell you where a stock ended up. Market Lens is designed to help you understand the ride it took to get there.**

---

## Repository

- `app.py` — Streamlit application
- `stakeholder_dashboard.ipynb` — exploratory analysis and original dashboard work
- `requirements.txt` — project dependencies

---

### Disclaimer

Market Lens is an educational analytics project, not investment advice. Metrics are descriptive and based on historical or publicly available market data.