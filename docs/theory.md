# Options Market Making — Extended Theory Reference

> Educational companion to the Options MM Delta-Neutral Simulator.

---

## 1. What is Options Market Making?

An **Options Market Maker (MM)** is a financial intermediary that provides two-sided quotes (bid and ask) for options contracts. Their job is to:

1. **Quote continuously** — Always show a price at which they'll buy (bid) and sell (ask)
2. **Fill incoming orders** — Execute trades with counterparties at quoted prices
3. **Manage inventory risk** — Hedge the resulting position to avoid directional exposure
4. **Earn the spread** — Profit from the difference between bid and ask prices

Unlike a retail trader who trades directionally, an MM is **indifferent to market direction**. They aim to capture the spread while remaining delta-neutral.

---

## 2. The Greeks — Complete Reference

### Delta (Δ)

**Definition:** The rate of change of an option's price with respect to a $1 change in the underlying asset.

```
Δ_call = N(d1)       ∈ [0, 1]
Δ_put  = N(d1) − 1   ∈ [−1, 0]
```

**Interpretation:**
- A call with Δ = 0.60 behaves like 0.60 shares of stock
- A put with Δ = −0.40 behaves like −0.40 shares of stock
- At-the-money options have |Δ| ≈ 0.50
- Deep in-the-money options have |Δ| ≈ 1.00
- Deep out-of-the-money options have |Δ| ≈ 0.00

**For the MM:** Delta is the directional exposure that must be hedged. A portfolio with net Δ = +0.75 gains $0.75 for each $1 the stock goes up. To neutralize, the MM sells 0.75 shares of the underlying.

### Gamma (Γ)

**Definition:** The rate of change of Delta with respect to a $1 change in the underlying. It measures the **convexity** of the option price.

```
Γ = N'(d1) / (S · σ · √T)
```

Gamma is **positive** for both calls and puts.

**Interpretation:**
- Gamma is highest for at-the-money options near expiry (the "pin risk" zone)
- Long gamma means delta becomes more positive as spot rises, more negative as spot falls → **buy low, sell high**
- Short gamma means delta becomes more negative as spot rises, more positive as spot falls → **sell low, buy high**

**For the MM:** Gamma determines how often the hedge must be rebalanced. High gamma = rapid delta changes = frequent rebalancing. Short gamma is dangerous because delta moves against you in volatile markets.

### Theta (Θ)

**Definition:** The rate of change of an option's price with respect to the passage of time (time decay).

```
Θ_call = −S · N'(d1) · σ / (2√T) − r · K · e^(−rT) · N(d2)
Θ_put  = −S · N'(d1) · σ / (2√T) + r · K · e^(−rT) · N(−d2)
```

**Interpretation:**
- Long options have **negative theta** (you lose money every day)
- Short options have **positive theta** (you earn money every day)
- Theta is most negative for at-the-money options near expiry

**For the MM:** Theta is the "rent" earned for providing liquidity. Most MM strategies are net short options, earning theta while accepting the negative gamma risk.

### Vega (Ν)

**Definition:** The rate of change of an option's price with respect to a 1% change in implied volatility.

```
Ν = S · N'(d1) · √T
```

Vega is **positive** for both calls and puts.

**Interpretation:**
- Longer-dated options have higher vega
- At-the-money options have the highest vega
- When vol rises, all options become more expensive

**For the MM:** Vega represents volatility risk. If an MM is net short options, rising volatility hurts their position. This is a risk they typically manage separately from delta.

---

## 3. Delta-Neutral Hedging

### The Concept

A portfolio is **delta-neutral** when its net delta is zero:

```
Σ (position_Δ_i × position_qty_i) + hedge_qty = 0
```

The MM continuously adjusts the hedge position to maintain this neutrality.

### The Hedge Process

1. **Compute net delta** — Sum all position deltas
2. **Compare to threshold** — If |net delta| > threshold, a hedge is needed
3. **Execute hedge** — Buy or sell the underlying to offset the delta
4. **Wait for next price move** — Gamma will change delta, requiring rebalancing

### The Threshold Tradeoff

| Tight Threshold (±0.01) | Wide Threshold (±0.50) |
|-------------------------|------------------------|
| Very frequent hedging | Rare hedging |
| High transaction costs | Low transaction costs |
| Very low residual delta risk | Higher residual delta risk |
| Sensitive to gamma | More tolerant of gamma |

The optimal threshold balances transaction costs against the cost of residual risk.

### Gamma's Effect on Hedging

When gamma is **positive** (long options):
- As spot rises, delta becomes more positive → MM sells shares (which are now worth more) → **profitable rebalancing**
- As spot falls, delta becomes more negative → MM buys shares (which are now cheaper) → **profitable rebalancing**
- This is called **gamma scalping** — the MM profits from volatility

When gamma is **negative** (short options):
- As spot rises, delta becomes more negative → MM must buy shares (which are now expensive) → **costly rebalancing**
- As spot falls, delta becomes more positive → MM must sell shares (which are now cheap) → **costly rebalancing**
- This is why short gamma is dangerous — you lose money from rebalancing

---

## 4. P&L Attribution in Detail

### The Decomposition

For a delta-hedged options portfolio, the P&L can be decomposed as:

```
dΠ = Θ · dt + ½ · Γ · (dS)² + Spread + ε
```

Where:
- **Θ · dt** — Theta decay (time value erosion)
- **½ · Γ · (dS)²** — Gamma scalping (convexity P&L)
- **Spread** — Bid-ask spread capture on fills
- **ε** — Residual (higher-order terms)

### Key Insight: Gamma P&L = Realized Volatility

The gamma term depends on **(dS)²**, which is the realized variance. This means:

- If realized volatility > implied volatility at pricing → long gamma positions profit
- If realized volatility < implied volatility at pricing → short gamma positions profit
- The MM's gamma position is a **bet on volatility realization**

### Theta-Gamma Relationship

For a delta-neutral portfolio at the Black-Scholes implied volatility:

```
Θ + ½ · σ² · S² · Γ ≈ 0
```

This is the **Black-Scholes PDE** — at fair price, theta and gamma cancel out. The MM makes money when:
- They capture the spread (liquidity provision)
- Realized volatility differs from implied (gamma vs theta)
- They manage risk more efficiently than the model assumes

---

## 5. Risk Management

### Key Risks for an Options MM

| Risk | Source | Mitigation |
|------|--------|------------|
| **Delta Risk** | Net directional exposure | Continuous hedging |
| **Gamma Risk** | Convexity of option prices | Position limits, gamma targets |
| **Vega Risk** | Volatility changes | Option-based hedges (not in this sim) |
| **Pin Risk** | Gamma near expiry at-the-money | Rolling or closing positions before expiry |
| **Gap Risk** | Large price moves between hedge opportunities | Wider protection, stop-losses |

### The Gamma Trap

The most dangerous scenario for an options MM is being **short gamma during a crash**:

1. Underlying drops sharply
2. Delta becomes more positive (for short puts) → short gamma makes delta go against you
3. MM must sell more shares → delta becomes even more negative
4. Price drops further → cycle continues
5. MM realizes massive losses

This is what happened to many market makers during the 1987 crash (portfolio insurance feedback loop) and the 2020 COVID crash.

---

## 6. How the Simulator Models Reality

| Real-World Feature | Simulator Implementation |
|--------------------|-------------------------|
| Options exchange | Random Poisson order flow generator |
| Black-Scholes pricing | Full BS model with configurable parameters |
| Order book / spread | Configurable % spread around theoretical price |
| Delta hedging | Automatic, threshold-based, continuous |
| Hedge execution | At current price (no slippage) |
| Transaction costs | Implicit in the bid-ask spread |
| Gamma P&L | Accrued each tick as ½·Γ·(dS)² |
| Theta P&L | Accrued each tick as Θ·dt |
| Market impact | None (perfect liquidity) |
| Volatility | Constant (except scenarios) |
| Interest rates | Constant |
| Dividends | None |

### Limitations

- No volatility surface (all options trade at same σ)
- No bid-ask slippage on hedge execution
- No market impact on orders
- No transaction costs on hedge trades
- Single underlying asset
- European-style options only (no early exercise)

---

## 7. Black-Scholes Model Reference

### Assumptions

- European-style options (exercise only at expiry)
- No transaction costs or taxes
- Risk-free interest rate is constant
- Volatility is constant
- Log-normal distribution of returns
- Continuous trading
- No dividends

### Formulas

```
d1 = ln(S/K) + (r + σ²/2)T / (σ√T)
d2 = d1 − σ√T

Call = S · N(d1) − K · e^(−rT) · N(d2)
Put  = K · e^(−rT) · N(−d2) − S · N(−d1)

Δ_call = N(d1)
Δ_put  = N(d1) − 1

Γ = N'(d1) / (S · σ · √T)

Θ_call = −S · N'(d1) · σ / (2√T) − r · K · e^(−rT) · N(d2)
Θ_put  = −S · N'(d1) · σ / (2√T) + r · K · e^(−rT) · N(−d2)

Ν = S · N'(d1) · √T
```

Where:
- N(x) = cumulative standard normal distribution
- N'(x) = standard normal PDF = e^(−x²/2) / √(2π)

---

*Use this reference alongside the Options MM Delta-Neutral Simulator for the best learning experience. Simulate first, then read the theory — the concepts will click faster when you've seen them in action.*
