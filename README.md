<div align="center">
  <br>
  <h1>⚡ Options Market Maker</h1>
  <p><strong>Delta-Neutral Simulator · Educational Edition</strong></p>
  <p>
    <em>Learn options market making through real-time simulation.
    <br>Calculate Greeks. Hedge delta. Understand P&L attribution.</em>
  </p>
  <br>
  <p>
    <a href="#-features"><img src="https://img.shields.io/badge/Features-📋-8b5cf6?style=for-the-badge" alt="Features"></a>
    <a href="#-educational-value"><img src="https://img.shields.io/badge/Education-📖-a855f7?style=for-the-badge" alt="Education"></a>
    <a href="#-quick-start"><img src="https://img.shields.io/badge/Quick_Start-▶-6366f1?style=for-the-badge" alt="Quick Start"></a>
    <a href="#-theory"><img src="https://img.shields.io/badge/Theory-🎓-8b5cf6?style=for-the-badge" alt="Theory"></a>
  </p>
  <br>
  <p>
    <img src="https://img.shields.io/badge/Chart.js-4.x-FF6384?style=flat-square&logo=chartdotjs&logoColor=white" alt="Chart.js">
    <img src="https://img.shields.io/badge/vanilla-JS-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="Vanilla JS">
    <img src="https://img.shields.io/badge/dependencies-Chart.js_only-22c55e?style=flat-square" alt="Minimal Dependencies">
    <img src="https://img.shields.io/badge/license-MIT-22c55e?style=flat-square" alt="MIT License">
    <img src="https://img.shields.io/badge/status-active-22c55e?style=flat-square" alt="Status Active">
  </p>
  <br>
</div>

---

## 📋 Overview

**Options Market Maker** is an interactive, real-time browser-based simulator that places you in the seat of a **professional options market maker**. You receive continuous synthetic options order flow, calculate Greeks using Black-Scholes, maintain a delta-neutral portfolio, and watch your P&L decompose into its fundamental drivers.

> *"This is not a theory course. This is a live trading desk simulation. Every tick matters."*

Built as a **single HTML file** — open it in any browser and press Start. No installation, no backend, no configuration.

### Who Is This For?

| Audience | Use Case |
|----------|----------|
| **Options Traders** | Understand delta-neutral hedging mechanics in a risk-free environment |
| **Quantitative Students** | See Black-Scholes Greeks in action with live P&L decomposition |
| **Finance Educators** | Demonstrate gamma/theta tradeoff, convexity, and hedging dynamics |
| **Aspiring Market Makers** | Practice managing continuous order flow and delta risk |
| **Self-Taught Programmers** | Explore options theory through an interactive visual tool |

---

## ✨ Features

### Core Simulation

| Feature | Description |
|---------|-------------|
| **Synthetic Order Flow** | Random options orders arrive continuously (call/put, buy/sell, random strikes/expiries/sizes) |
| **Black-Scholes Pricing** | All options priced using the full Black-Scholes model |
| **Real-Time Greeks** | Δ (Delta), Γ (Gamma), Θ (Theta), Ν (Vega) computed for every position and the full portfolio |
| **Automatic Delta Hedging** | Maintains delta-neutrality within a configurable tolerance threshold |
| **GBM Price Process** | Underlying price follows Geometric Brownian Motion with configurable σ and μ |
| **Option Expiry** | Contracts expire at maturity and are settled at intrinsic value |

### Educational Features

| Feature | Description |
|---------|-------------|
| **P&L Attribution Waterfall** | Visual breakdown of the true book P&L into Spread, Theta, Gamma, Vega and Delta & Hedge, with the unexplained residual shown |
| **Greek Explainers** | Click on any Greek label for a popup with formula, interpretation, and MM context |
| **Educational Theory Panel** | Collapsible sidebar with complete reference: Greeks, hedging mechanics, Black-Scholes, P&L decomposition |
| **Educational Activity Log** | Color-coded log with plain-English explanations of why events happen |
| **Scenario Injectors** | "Vol Spike", "Flash Crash", "Rally", and "Order Surge" buttons to test specific conditions |
| **Gamma / Theta Tradeoff** | Visual cards showing whether you're long/short gamma and what it implies |

### Interactive Controls

| Control | Range | Purpose |
|---------|-------|---------|
| **Volatility (σ)** | 5–80% | Underlying price volatility |
| **Drift (μ)** | −20% to +20% | Expected annual return of the underlying |
| **Hedge Threshold** | 0.01–0.50 | Maximum tolerated net delta before rebalancing |
| **Order Flow** | 1–20 | Frequency of incoming options orders |
| **Speed** | 1×–5× | Simulation time multiplier |
| **Spread Width** | 0.5%–5.0% | Bid-ask spread as % of theoretical price |

---

## 🚀 Quick Start

```bash
# 1. Open the HTML file in any modern browser
open index.html

# 2. Configure parameters (optional)
#    - Set volatility, hedge threshold, etc.

# 3. Press "Start"
#    Orders arrive automatically. Watch the dashboard update in real-time.

# 4. Use scenario buttons to test extreme conditions
#    - Vol Spike: σ jumps to 60%
#    - Crash: spot drops 8%
#    - Rally: spot jumps 6%
#    - Order Surge: 20× flow intensity for 5 seconds

# 5. Open the "Theory" panel for educational reference
```

### System Requirements

| Requirement | Detail |
|-------------|--------|
| **Browser** | Chrome, Firefox, Edge, Safari (any modern browser) |
| **Internet** | Required once for Chart.js CDN (cached after first load) |
| **Dependencies** | Chart.js 4.x (loaded from CDN) |
| **Storage** | ~200 KB for the HTML file |
| **OS** | Windows, macOS, Linux |

---

## 🏛️ Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                          Options MM Simulator                       │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌─────────────────┐    ┌──────────────────┐    ┌────────────────┐  │
│  │  Order Flow     │───▶│  Black-Scholes   │───▶│  Portfolio &   │  │
│  │  Generator      │    │  Pricing Engine  │    │  Greeks Engine │  │
│  │  (Poisson)      │    │  (Δ, Γ, Θ, Ν)   │    │  (Aggregation) │  │
│  └─────────────────┘    └──────────────────┘    └────────┬───────┘  │
│                                                          │          │
│                                                          ▼          │
│  ┌─────────────────┐    ┌──────────────────┐    ┌────────────────┐  │
│  │  GBM Price      │    │  Delta Hedge     │◀──▶│  Net Delta     │  │
│  │  Process        │    │  Engine          │    │  Computation   │  │
│  │  (Underlying)   │    │  (Auto-rebalance)│    │  + Threshold   │  │
│  └─────────────────┘    └──────────────────┘    └────────────────┘  │
│                                                          │          │
│                                                          ▼          │
│  ┌─────────────────────────────────────────────────────────────────┐ │
│  │                    P&L Attribution Engine                       │ │
│  │  Spread (fill)  +  Theta (dt)  +  Gamma (dS²)  +  Hedge (MTM) │ │
│  └─────────────────────────────────────────────────────────────────┘ │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────────┐ │
│  │                    UI Rendering (Canvas + DOM)                   │ │
│  │  Dashboard  ·  Ticker  ·  Charts  ·  Positions Table  ·  Log   │ │
│  └─────────────────────────────────────────────────────────────────┘ │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **Order Generation** — Poisson process generates options with random parameters (type, strike, expiry, side, quantity)
2. **Pricing** — Each order is priced at Black-Scholes theoretical value ± spread
3. **Execution** — The MM fills the order, capturing the spread as P&L
4. **Greek Computation** — Portfolio Greeks are recalculated after every fill and price move
5. **Hedge Check** — If |net delta| > threshold, the MM buys/sells underlying shares
6. **P&L Attribution** — Each tick accumulates theta decay and gamma scalping P&L separately
7. **UI Update** — All dashboard components refresh in real-time

---

## 🎓 Educational Value

### What You Will Learn

| Concept | How the Simulator Teaches It |
|---------|------------------------------|
| **Delta** | Watch net delta change with each fill. See the hedge engine respond to keep it within bounds. |
| **Gamma** | Observe how gamma determines hedge rebalancing frequency. Short gamma = costly rebalancing during volatile moves. |
| **Theta** | The P&L waterfall shows theta accumulating steadily over time. Positive theta (short options) vs negative theta. |
| **Gamma/Theta Tradeoff** | The fundamental tradeoff: long gamma costs theta; short theta costs gamma risk. See it in action. |
| **Delta-Neutral Hedging** | Automatic hedging demonstrates the mechanics. Tighter thresholds = more frequent rebalancing = higher transaction costs. |
| **P&L Attribution** | The waterfall chart decomposes every dollar of P&L: spread, theta, gamma, hedge. |
| **Convexity (Gamma Scalping)** | During rallies and crashes, gamma determines whether the MM buys low / sells high or the opposite. |
| **Vega Risk** | Use the Vol Spike scenario to see how volatility changes affect option prices. |
| **Scenario Analysis** | Crash and Rally scenarios test the portfolio's resilience. See how gamma exposure determines the outcome. |

### Suggested Learning Path

1. **Start with low volatility (σ = 15%) and a wide hedge threshold (0.20).** Observe how the system works.
2. **Watch the P&L waterfall.** Understand which components contribute to total P&L over time.
3. **Narrow the hedge threshold to 0.05.** Notice the increased hedge frequency — more rebalancing = more transaction costs = lower P&L.
4. **Hit the "Vol Spike" button.** Watch Vega exposure affect P&L and gamma drive hedge rebalancing.
5. **Hit the "Crash" button.** Observe how short gamma forces the MM to sell into a falling market.
6. **Increase order flow intensity.** See how rapid order accumulation strains delta management.
7. **Experiment with different volatility levels.** Higher vol = more gamma = faster delta changes = more hedging.

---

## 📖 Theory

### The Greeks

| Greek | Symbol | Formula | Option MM Relevance |
|-------|--------|---------|---------------------|
| **Delta** | Δ | ∂V/∂S | Directional risk — must be hedged to zero |
| **Gamma** | Γ | ∂²V/∂S² | Convexity — determines hedge rebalancing frequency |
| **Theta** | Θ | ∂V/∂t | Time decay — primary source of P&L for most MMs |
| **Vega** | Ν | ∂V/∂σ | Volatility sensitivity — unhedged, but its P&L is attributed |

### P&L Decomposition

```
Total P&L = Spread Capture + Theta + Gamma + Vega + (Option Delta P&L + Hedge P&L − Hedge Costs) + Residual
```

Total P&L is the true book P&L: open options marked to Black-Scholes, realized expiries, and the hedge position, after costs. Each bucket is a Taylor-series estimate accumulated tick by tick:

- **Spread Capture** — Fill price versus theoretical value, earned on every fill
- **Theta** — Θ × dt (positive when net short options)
- **Gamma** — ½ Γ × dS² (positive when long gamma, negative when short)
- **Vega** — ν × dσ, from volatility changes such as the Vol Spike scenario
- **Delta & Hedge** — option Δ × dS plus mark-to-market on the hedge shares, minus a $0.01/share transaction cost; close to zero when the book is well hedged
- **Residual** — what the first- and second-order terms do not explain (higher-order effects and discrete ticks); shown under the Total bar

### The Gamma/Theta Tradeoff

```
Long Options:  +Gamma (benefits from volatility)  −Theta (pays time decay)
Short Options: −Gamma (loses from volatility)     +Theta (earns time decay)
```

This is the **fundamental tradeoff** in options market making. Most MM strategies are net short (earning theta) and must carefully manage the negative gamma risk. When volatility spikes (like the "Vol Spike" scenario), short-gamma positions bleed P&L as delta ramps against the hedge.

---

## 🖥️ Interface Guide

```
┌─────────────────────────────────────────────────────────────────────┐
│ ⚡ Options MM · Delta-Neutral Simulator              [Theory] [▶]  │
├─────────────────────────────────────────────────────────────────────┤
│ $100.42  Δ +0.08  Γ -0.015  Θ -0.04  P&L +$234  Hedge 0  ✓ Neutral│
├─────────────────────────────────────────────────────────────────────┤
│ [Stats Cards: Positions, Trades, Hedges, |Δ|, Γ, Θ, Spread, Vega] │
├─────────────────────────────────────────────────────────────────────┤
│ [P&L Waterfall: Spread | Theta | Gamma | Hedge | Total]            │
├─────────────────────────────────────────────────────────────────────┤
│ [Delta Exposure Chart — real-time line with threshold bands]       │
├─────────────────────────────────────────────────────────────────────┤
│ [Controls: σ | μ | Threshold | Flow | Speed | Spread]  [Scenarios]│
├─────────────────────────────────────────────────────────────────────┤
│ [Options Positions Table]          [Activity Log with EDU msgs]    │
└─────────────────────────────────────────────────────────────────────┘
```

### Interface Elements

| Element | Location | Purpose |
|---------|----------|---------|
| **Ticker Bar** | Top | Real-time summary of key metrics (price, Greeks, P&L, hedge status) |
| **Stats Cards** | Below ticker | Detailed metrics with color-coded status indicators |
| **P&L Waterfall** | Mid-page | Visual decomposition of P&L into four components with bar chart |
| **Delta Chart** | Center | Time series of net delta exposure with threshold bands and hedge markers |
| **Controls** | Below chart | Sliders for all simulation parameters |
| **Scenario Buttons** | Right of controls | One-click market event injectors |
| **Positions Table** | Bottom left | Every open option position with individual Greeks and P&L |
| **Activity Log** | Bottom right | Color-coded event log with educational annotations |
| **Theory Panel** | Toggle sidebar | Full educational reference (click "Theory" button in header) |

---

## 🛠️ Project Structure

```
options-mm-simulator/
├── index.html            # Complete simulator (single-file, ~900 lines)
├── README.md             # This file
├── LICENSE               # MIT License
└── docs/
    └── theory.md         # Extended educational theory reference
```

Everything lives in a single HTML file. Open it and go.

### Technologies

| Technology | Purpose |
|------------|---------|
| **HTML5** | Structure |
| **CSS3** | Dark-themed trading terminal UI with custom properties |
| **Vanilla JavaScript** | All simulation logic, Black-Scholes math, and UI rendering |
| **Chart.js 4.x** | Real-time delta exposure chart (loaded from CDN) |

---

## 📜 License

This project is licensed under the **MIT License** — see [`LICENSE`](LICENSE) for the full text.

You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software.

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome. Areas for improvement:

- **Implied Volatility surface** — add skew/smile dynamics
- **Multi-asset portfolio** — support multiple underlyings
- **Historical backtesting** — replay mode with recorded market data
- **Advanced hedging** — gamma/theta targeting, vega hedging with other options
- **Performance analytics** — Sharpe ratio, VaR, max drawdown tracking

---

## ⚠️ Disclaimer

This simulation is an **educational tool**. All market data is synthetically generated. Nothing in this software constitutes financial advice, trading recommendations, or investment guidance. Options trading involves substantial risk and is not suitable for all investors.

---

<div align="center">
  <br>
  <p>
    <sub>
      Built with Vanilla JavaScript &middot;
      <a href="https://www.chartjs.org/">Chart.js</a> &middot;
      <a href="LICENSE">MIT License</a>
    </sub>
  </p>
  <p>
    <sub><em>"Know your Greeks, or get wrecked by them."</em></sub>
  </p>
  <br>
</div>
