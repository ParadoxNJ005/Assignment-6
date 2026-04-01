# 📝 Data Visualization — Mid-Sem Practice Questions (Set 2)

> Deeper, scenario-based, and granular questions complementing `Mid-sem_Practice.md`.

---

## Section A: Applied & Scenario-Based Questions

---

### Q1. A colleague creates a bar chart comparing GDP of 10 countries but starts the vertical axis at $40,000 instead of $0. Explain what is wrong and why it matters.
**[High Probability — tests "Start axis at zero" rule for bars]**

**Answer:**
Bar charts encode value using **length**. When the axis doesn't start at zero, the visible bar lengths no longer represent the actual data proportionally — a country with GDP $50K may appear to have "almost nothing" compared to one with $60K, even though $50K is 83% of $60K.

**Why this matters for bars (but NOT lines):**
- In bar charts, we compare the **length** of bars. Cutting the baseline distorts this comparison.
- In line charts, we compare the **slope/trend** — so a non-zero axis is acceptable (the eye tracks the line's direction, not its absolute height from zero).

**Fix:** Always start bar chart axes at zero. If the values are closely clustered (e.g., 40K–60K), consider using a **dot plot** instead, which uses *position* rather than *length* and doesn't require a zero baseline.

---

### Q2. You have survey data with responses: "Strongly Disagree, Disagree, Neutral, Agree, Strongly Agree" across 5 departments. Which chart type would you choose and why? What should you do with the "Neutral" category?
**[Medium-High Probability — Diverging Bar Chart application]**

**Answer:**
Use a **Diverging Bar Chart**. It is specifically designed for **Likert Scale** data, where responses diverge from a central point (negative ← Neutral → positive).

**Chart properties:**
- Stacks diverge from a central baseline in opposite directions.
- Negative responses (Strongly Disagree, Disagree) go left; positive (Agree, Strongly Agree) go right.
- Each department becomes a row.

**Handling the "Neutral" category:**
Place it **off to the side** (e.g., as a separate small bar or label) rather than splitting it across the center line. Neutral should NOT be mathematically split between positive and negative — it doesn't belong to either sentiment.

**Why not other charts?**
- Stacked bar chart: Hard to compare interior segments (no shared baseline for middle categories).
- Grouped bar chart: 5 bars × 5 departments = 25 bars → too cluttered.

---

### Q3. You are building a dashboard to show employee shifts at a coffee shop throughout the day, including breaks. Which chart type is most appropriate? How could you extend it to show a second variable?
**[Medium Probability — Gantt Chart application]**

**Answer:**
Use a **Gantt Chart** — horizontal bars showing the start, duration, and end of each shift.

**Implementation:**
- Each row = one employee.
- Bar length = shift duration.
- White gaps = short breaks; gray = lunch breaks; stripes = time away from the store.

**Extending with a second variable:**
Modify the **width** of the bars to encode another variable (e.g., pay rate). Higher-paid employees get thicker bars, making it easy to see both time allocation *and* cost at a glance.

**Invented by:** Henry Laurence Gantt (early 20th century), originally used for tracking production schedules.

---

### Q4. A news outlet publishes a chart showing that "Cheese consumption correlates with number of civil engineering PhDs awarded" using a dual-axis line chart. Critique this visualization.
**[High Probability — Dual Axis critique]**

**Answer:**
This is a classic example of **spurious correlation** enabled by dual-axis chart manipulation (reference: Tyler Vigen's collection).

**Problems:**
1. **Arbitrary axis ranges**: By choosing axis ranges independently for each variable, the creator can force the lines to appear correlated, divergent, or to cross at any point.
2. **False focal point**: The intersection of lines draws the reader's eye as if it's meaningful — it isn't, because the axes are on completely different scales.
3. **Gridline mismatch**: Horizontal gridlines align with only one axis, making the other series float without reference.
4. **Implied causation**: Readers naturally interpret overlapping trends as related, even when there is no causal mechanism.

**Better alternatives:**
- Two **side-by-side charts** with their own axes (small multiples).
- **Vertically stacked charts** with a shared time axis and a connecting annotation line.
- A **connected scatterplot** if the goal is genuinely to explore the relationship.

---

### Q5. Explain how the same time-series data can tell completely different stories depending on the chart type used. Use the example of "Drug overdose deaths in the US over 20 years" to illustrate.
**[Medium Probability — tests understanding of stacked area chart properties]**

**Answer:**

Using the same dataset (deaths by drug type over 20 years), different chart types emphasize different findings:

| Chart Type | What the Reader Sees |
|-----------|---------------------|
| **Stacked Area (absolute)** | Massive increase in **total** deaths → eye drawn to overall scale growth |
| **Stacked Area (100%)** | Changes in **distribution** — decline in cocaine deaths, rise in heroin/opioids |
| **Line Chart (separate lines)** | Individual trajectories of each drug category — can spot exactly when heroin overtook cocaine |
| **Small Multiples (line)** | Cleanest comparison of individual trends without overlapping lines |
| **Streamgraph** | Organic shape highlights **peaks and troughs** — aesthetically engaging but less precise |

**Three disadvantages of stacked area charts:**
1. **Line-width illusion** — steep regions appear disproportionately large.
2. **Only the bottom series** sits on a flat baseline — upper series float and are hard to compare.
3. **Ordering matters** — reordering the stacking changes which series appears to grow/shrink.

**Key lesson:** The chart creator's choice of visualization actively shapes the reader's takeaway. Always ask: *"What story does this chart emphasize, and what does it hide?"*

---

### Q6. A climate scientist has monthly temperature data for 50 cities over 10 years. The standard line chart is a tangled mess. Suggest three alternative approaches and explain the trade-offs.
**[Medium Probability — Spaghetti chart alternatives]**

**Answer:**

**Problem:** 50 lines × 120 months = spaghetti chart. No patterns visible.

| Alternative | How it Works | Trade-off |
|------------|-------------|-----------|
| **Small Multiples** | Break into 50 mini line charts (same scale/axes) | ✅ Clear per-city trends, easy comparison. ✗ Requires space; harder to see inter-city relationships directly. |
| **Heatmap** | Cities as rows, months as columns, color = temperature | ✅ Compact, seasonal patterns visible. ✗ Exact values hard to read (color is low on perceptual ranking). |
| **"Start with Gray" strategy** | Plot all 50 lines in gray, highlight only 2–3 cities of interest in color | ✅ Shows overall pattern AND focus cities simultaneously. ✗ Only a few cities can be highlighted at once. |

**Bonus — Horizon Chart:** Collapse each city's area chart into compact bands using color intensity. Extremely compact (50 cities in one view) but requires reader familiarity with the chart type.

**Guideline applied:** Guideline 4 — "Avoid the Spaghetti Chart."

---

### Q7. William Playfair's 18th-century chart of England's trade balance with the East Indies contains a subtle hidden pattern. What is it, and what visual illusion makes it hard to see?
**[Medium Probability — Line-width illusion from Time PDF]**

**Answer:**
Between 1762 and 1764, imports rose quickly while exports grew slowly, creating a brief **spike** in the trade balance. Between 1764 and 1766, exports shot up, bringing the balance back down. This "hump" is **nearly invisible** in Playfair's original chart.

**Why it's hard to see — the Line-Width Illusion:**
We tend to assess the distance between two curves at their **closest point** (perpendicular distance) rather than the **vertical distance**. When curves are steep, the closest-point distance appears small even if the vertical gap is large.

**Solution:** Plot the **gap between the curves** (Imports − Exports) as a separate line chart. The hump becomes immediately obvious.

---

### Q8. Explain Munzner's Task Abstraction framework. A user opens a social media analytics dashboard to "see what's trending this week." Classify this action using Munzner's taxonomy.
**[Medium-High Probability — Munzner's Actions + Search]**

**Answer:**

**Task Abstraction breaks down user tasks into:**

**Actions:**
- **Analyze**: Consume (discover / present / enjoy) or Produce (annotate / record / derive)
- **Search**: Based on what the user knows about target and location:

| | Target Known | Target Unknown |
|---|---|---|
| **Location Known** | **Lookup** (word in dictionary) | **Browse** (books in a store) |
| **Location Unknown** | **Locate** (find a node in a network) | **Explore** (cool area in new city) |

- **Query**: How much data? — Identify (one), Compare (some), Summarize (all)

**Classifying "see what's trending this week":**
1. **Action → Analyze → Consume → Discover** (exploring to find new insights, not presenting known results)
2. **Search → Explore** (the user doesn't know *what* is trending or *where* on the dashboard it appears — both target and location are unknown)
3. **Query → Summarize** (interested in overall patterns, not one specific post)

---

## Section B: Comparative & Tabular Questions

---

### Q9. Compare the following pairs of chart types. When would you pick one over the other?

**(a) Bar Chart vs Dot Plot**

| Aspect | Bar Chart | Dot Plot |
|--------|-----------|----------|
| Channel | Length on common scale | Position on common scale |
| Ink usage | More (filled rectangles) | Less (circles + thin lines) |
| Zero baseline | Required | Not required |
| Best for | Absolute values, categorical ranking | Showing differences/ranges between two points |
| Weakness | Can look cluttered with many bars | Hides intermediate variation |

**(b) Stacked Bar Chart vs Waffle Chart**

| Aspect | Stacked Bar | Waffle Chart |
|--------|------------|--------------|
| Visual | Sub-divided bars | 10×10 grid |
| Part-to-whole | ✓ (sums to total) | ✓ (each cell = 1%) |
| Comparing across categories | Hard (interior segments unaligned) | Easy (count colored cells) |
| Precision | Medium | Medium-High |
| Best for | Showing totals + composition | Comparing percentages across groups |

**(c) Gauge Chart vs Bullet Chart**

| Aspect | Gauge Chart | Bullet Chart |
|--------|------------|--------------|
| Shape | Semicircle (speedometer) | Linear horizontal bar |
| Invented by | — | Stephen Few |
| Channel | Angle (low accuracy) | Length (high accuracy) |
| Space efficiency | Poor (circular = wastes space) | Excellent (compact) |
| Contains | Needle + ranges | Actual value bar + Target line + Background ranges |
| Best for | Dashboard aesthetics | Precise KPI tracking |

**(d) Heatmap vs Horizon Chart**

| Aspect | Heatmap | Horizon Chart |
|--------|---------|---------------|
| Data type | Two categorical dimensions | Time series |
| Encoding | Color saturation | Area + color intensity |
| Precision | Low (color = rank 6) | Low (pattern-focused) |
| Strength | Patterns across matrix | Ultra-compact time series |
| Best for | Calendar data, matrix tables | Dense multi-series time data |

---

### Q10. Fill in the blanks — match each visualization pioneer to their contribution:

| Pioneer | Contribution |
|---------|-------------|
| **William Playfair** | Invented Bar charts, Line charts, and Pie charts (18th century) |
| **Florence Nightingale** | Coxcomb / Rose chart for preventable military deaths |
| **John Snow** | Dot map of cholera cases → Broad Street pump |
| **Edward Tufte** | Coined "Sparklines" — word-sized graphics |
| **Stephen Few** | Invented the Bullet Chart as gauge alternative |
| **Otto Neurath** | Pioneered Isotype charts (1920s) — icons instead of shapes |
| **Henry Gantt** | Invented Gantt charts for production scheduling |
| **Ben Shneiderman** | "Overview first, zoom and filter, then details-on-demand" |
| **Archie Tse** | Modern shift: users just want to scroll |
| **Tamara Munzner** | Nested Model of Visualization Design (4 levels, 3 questions) |

---

## Section C: More MCQs

---

**Q11.** The Form × Function matrix has four quadrants. A static graph with interactive tooltips on hover belongs to:
- (a) Static & Explanatory
- (b) Static & Exploratory
- (c) **Interactive & Explanatory** ✓
- (d) Interactive & Exploratory

**Q12.** Temperature in Celsius is an example of which data type?
- (a) Nominal
- (b) Ordinal
- (c) **Interval** ✓ (0°C ≠ "no temperature" → no true zero)
- (d) Ratio

**Q13.** A cycle chart is BEST suited for displaying:
- (a) Category comparisons
- (b) Part-to-whole relationships
- (c) **Seasonal trends across years** ✓
- (d) Network relationships

**Q14.** In a Stacked Area Chart, which series is easiest to compare accurately?
- (a) The topmost series
- (b) Any middle series
- (c) **The bottom series** ✓ (sits on a flat horizontal baseline)
- (d) All series are equally easy

**Q15.** Isotype Charts were pioneered by:
- (a) Edward Tufte
- (b) William Playfair
- (c) **Otto Neurath** ✓
- (d) Stephen Few

**Q16.** Which guideline is being applied when you break a dense line chart into 6 separate panels, each showing one country?
- (a) Show the data
- (b) Start with Gray
- (c) Reduce the clutter
- (d) **Avoid the spaghetti chart (Small Multiples)** ✓

**Q17.** In Munzner's Search taxonomy, browsing a bookstore without knowing what you want to buy is classified as:
- (a) Lookup
- (b) Locate
- (c) **Browse** ✓ (location known, target unknown)
- (d) Explore

**Q18.** The key advantage of a slope chart over a paired bar chart is:
- (a) It shows more data points
- (b) **It visualizes the comparison (direction of change) directly** ✓
- (c) It always starts at zero
- (d) It works better for categorical data

**Q19.** A Mosaic Chart differs from a Marimekko Chart because:
- (a) It only uses height encoding
- (b) It uses color instead of position
- (c) **Both heights AND widths sum to 100%, filling the entire graph** ✓
- (d) It adds a third dimension

**Q20.** When we plot all bars in a visualization as gray and only color the bar for "India" in orange, we are applying:
- (a) Reduce the Clutter
- (b) Show the Data
- (c) Integrate Graphics and Text
- (d) **Start with Gray** ✓

**Q21.** Which of the following is NOT a mark in Munzner's framework?
- (a) Points
- (b) Lines
- (c) Areas
- (d) **Hue** ✓ (Hue is a channel, not a mark)

**Q22.** The advantage of Robust Scaling over Min-Max scaling is:
- (a) It produces values between 0 and 1
- (b) It centers data at the mean
- (c) **It uses median and IQR, making it resistant to outliers** ✓
- (d) It is faster to compute

**Q23.** A Streamgraph's central axis:
- (a) Always represents zero
- (b) Must start at zero
- (c) **Does not necessarily signal a zero value** ✓
- (d) Represents the mean

**Q24.** Which Gestalt principle explains why colored data points in a scatter plot are perceived as separate groups?
- (a) Proximity
- (b) **Similarity** ✓
- (c) Closure
- (d) Continuity

**Q25.** In Feature Engineering, converting "Male/Female" into 0/1 using a single column is:
- (a) One-Hot Encoding
- (b) **Integer/Label Encoding** ✓ (binary case, ordinal-like encoding)
- (c) Feature Extraction
- (d) Discretization

**Q26.** The Nested Model implies that a wrong decision at the Domain Situation level:
- (a) Only affects the Algorithm level
- (b) Can be fixed at the Idiom level
- (c) **Cascades errors to all downstream levels** ✓
- (d) Has no effect on other levels

**Q27.** A horizon chart is most similar in purpose to:
- (a) A pie chart
- (b) A Gantt chart
- (c) **A heatmap** ✓ (compact, color-based, pattern-focused)
- (d) A waterfall chart

**Q28.** In a Waffle Chart, each cell in the 10×10 grid represents:
- (a) One data point
- (b) One category
- (c) **One percentage point** ✓
- (d) One standard deviation

**Q29.** Pearson's Coefficient of Skewness formula is:
- (a) $(\text{Mean} - \text{Mode}) / \sigma$
- (b) $(\text{Mean} - \text{Median}) / \sigma$
- (c) **$3(\text{Mean} - \text{Median}) / \sigma$** ✓
- (d) $(\text{Median} - \text{Mean}) / \sigma$

**Q30.** A Connected Scatterplot differs from a regular scatterplot because:
- (a) It uses larger dots
- (b) It adds color coding
- (c) **Points are connected chronologically by a line** ✓
- (d) It plots three variables

**Q31.** William Playfair is credited with inventing all of the following EXCEPT:
- (a) Bar chart
- (b) Line chart
- (c) Pie chart
- (d) **Histogram** ✓

**Q32.** The "Start with Gray" strategy is most closely related to which preattentive attribute?
- (a) Size
- (b) Shape
- (c) **Color** ✓
- (d) Orientation

**Q33.** Which Feature Engineering technique would you use to convert a "Date of Birth" column into "Age"?
- (a) Imputation
- (b) One-Hot Encoding
- (c) **Feature Creation** ✓
- (d) Discretization

**Q34.** In Munzner's framework, Points (0D marks) have how many size constraints?
- (a) 1
- (b) 2
- (c) **0** ✓ (can freely encode size and shape)
- (d) 3

**Q35.** Florence Nightingale's Rose/Coxcomb chart was revolutionary because it:
- (a) Was the first pie chart
- (b) Used machine learning
- (c) **Used data visualization to drive policy change (sanitary reform)** ✓
- (d) Was the first interactive chart

---

## 🧠 Rapid-Fire Recall (One-Liners)

1. **Anscombe's Quartet proves**: Summary statistics alone can be misleading — always visualize.
2. **Bar chart axis rule**: MUST start at zero. Line chart: does NOT need to.
3. **Perceptual top**: Position on common scale. Perceptual bottom: Volume/Curvature.
4. **Shneiderman's Mantra**: "Overview first, zoom and filter, then details-on-demand."
5. **Archie Tse's counter**: In mobile era, users just want to scroll.
6. **EDA = Detective work. CDA = Court trial.**
7. **Positively skewed**: Mode < Median < Mean (tail goes right).
8. **Leptokurtic**: Heavy tails, outliers present, kurtosis > 0.
9. **Platykurtic**: Light tails, no outliers, kurtosis < 0.
10. **One-Hot Encoding**: For nominal (no order). Integer Encoding: For ordinal (has order).
11. **Robust Scaling**: Uses median + IQR → outlier-safe.
12. **Sparklines**: Invented by Edward Tufte — word-sized graphics for tables.
13. **Bullet Chart**: Invented by Stephen Few — replaces gauge charts.
14. **Isotype Charts**: Pioneered by Otto Neurath — icons instead of shapes.
15. **Nested Model**: Domain → Abstraction → Idiom → Algorithm. Errors cascade downstream.
16. **Three disadvantages of stacked area**: Line-width illusion, only bottom has flat baseline, ordering changes perception.
17. **Streamgraph vs Stacked Area**: Streamgraph minimizes baseline distortion, both sides of axis.
18. **Connected Scatterplot**: Two time series without dual axes.
19. **Pearson's Skewness**: $S_k = 3(\bar{x} - \text{Median}) / \sigma$
20. **Marks = geometric primitives** (points, lines, areas). **Channels = appearance controls** (position, color, size, shape).
