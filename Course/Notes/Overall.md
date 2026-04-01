# 📊 Data Visualization — Midsem Overall Cheat Sheet

---

## 1. Introduction to Data Visualization

**TL;DR:** DV translates complex data into visuals, enabling pattern recognition, outlier detection, and faster decision-making. Brain processes images 60,000× faster than text.

### 10 Components of a DV Framework
Data → Visual Elements → Techniques → Interactivity → Color/Design → Context/Annotations → Tools → Data Preparation → Data Exploration → Dashboarding

### Visual Mapping Elements
| Element | Role |
|---------|------|
| **Line** | Boundaries, connections, gridlines |
| **Shape (Marks)** | Bars (compare), Lines (trend), Points (relationships) |
| **Color** | Hue (categorical, max 6-8), Saturation (emphasis), Lightness (magnitude) |
| **Size** | Bars start at zero; bubbles scale by area |
| **White Space** | Legibility, grouping, rhythm |
| **Texture/Pattern** | Differentiate without color (accessibility) |
| **Contrast** | Visual hierarchy (High→data, Medium→context, Low→background) |
| **Motion** | 200-500ms transitions to explain change, not distract |

### Gestalt Theory
> "The whole is greater than the sum of its parts."

1. **Proximity** — Close objects = group
2. **Similarity** — Same color/shape = group
3. **Continuity** — Eye follows smooth paths
4. **Closure** — Brain fills gaps in incomplete shapes
5. **Figure & Ground** — Main object vs background
6. **Common Fate** — Things moving together = related

### Elements of Design
- **Unity** → Consistency (color, font, shape)
- **Hierarchy** → Importance via size, placement
- **Color** → Contrast & attention
- **Balance & Alignment** → Harmonious layout
- **Grouping / Spacing** → Narrative flow

### History Highlights
- **Playfair** (18th C) → Bar, Line, Pie charts
- **Nightingale** (1850s) → Rose/Coxcomb chart
- **John Snow** (19th C) → Cholera dot map

---

## 2. EDA & Descriptive Statistics

**TL;DR:** EDA is an iterative process to summarize, visualize, and explore data characteristics before modeling. It sits within the broader statistical pipeline: Produce Data → **EDA** → Probability → Inference.

### EDA vs CDA
- **EDA** = Detective work (gathering evidence) — *exploratory*
- **CDA** = Court trial (evaluating evidence) — *confirmatory*

### 8-Step EDA Process
1. Structure (size, features, types)
2. Consistency across sources
3. Identify what data signifies (measures)
4. **Summary metrics** (Central Tendency, Variability, Shape)
5. **Visuals** (Histograms, Scatterplots)
6. Per-category metrics for categorical variables
7. Identify & handle Outliers
8. Imputation for missing data

### EDA Methods
Descriptive Stats → Univariate → Bivariate → Multivariate → Dimensionality Reduction

### Data Types (NOIR)

| Type | Nature | True Zero? | Operations | Example |
|------|--------|-----------|------------|---------|
| **N**ominal | Categories, no order | ✗ | Equality only | Religion, Color |
| **O**rdinal | Categories, ordered | ✗ | Equality, Order | Low/Med/High |
| **I**nterval | Numerical, equal intervals | ✗ | +, − | Temperature (°C) |
| **R**atio | Numerical, absolute zero | ✓ | +, −, ×, ÷ | Weight, Age |

### Central Tendency

| Measure | Formula / Method | Use for |
|---------|-----------------|---------|
| **Mean** | Arithmetic average | Interval, Ratio (not skewed) |
| **Median** | Middle value when sorted | **Best for skewed data** |
| **Mode** | Most frequent value | Nominal, Ordinal |

**When to use?** Nominal → Mode • Ordinal → Mode, Median • Interval/Ratio → All three
In **skewed distributions** → use **Median** (unaffected by outliers).

### Variability
- **Range** = Max − Min
- **Variance** = Average of squared deviations from mean
- **Standard Deviation** = √Variance
- Two datasets with SAME mean can look VERY different (→ variability reveals this)

### Skewness & Kurtosis

| Property | Normal | Positive Skew | Negative Skew |
|----------|--------|---------------|---------------|
| Shape | Symmetric | Right tail longer | Left tail longer |
| Order | Mean = Median = Mode | **Mode < Median < Mean** | **Mean < Median < Mode** |
| Skewness | 0 | > 0 | < 0 |

**Pearson's Coefficient**: $S_k = 3(\text{Mean} - \text{Median}) / \sigma$

| Kurtosis Type | Tail | Outliers? | vs Normal |
|--------------|------|-----------|------------|
| **Mesokurtic** | Normal | — | Kurtosis ≈ 0 |
| **Leptokurtic** | Heavy | ✓ Present | Kurtosis > 0 |
| **Platykurtic** | Light | ✗ None | Kurtosis < 0 |

---

## 3. Five Guidelines for Better Visualization

1. **Show the Data** — Data is the star. No unnecessary borders/backgrounds.
2. **Reduce Clutter** — Remove heavy gridlines, 3D effects, textured fills, overlapping markers.
3. **Integrate Graphics & Text**:
   - Label directly (remove legends)
   - Write **headline titles** (not just descriptions)
   - Add **explainer annotations** for peaks/anomalies
4. **Avoid Spaghetti Charts** — Use **Small Multiples** (panel/trellis charts) to break up dense data.
5. **Start with Gray** — Force purposeful use of color by starting all elements in gray.

### Anscombe's Quartet
Four datasets with **identical** stats (mean, variance, correlation, regression line) but **completely different distributions** when visualized. **Lesson: Always visualize — summary stats alone can be misleading.**

### Form × Function Quadrants
|   | Explanatory | Exploratory |
|---|-------------|-------------|
| **Static** | Traditional charts illustrating a point | Dense infographics for user to interpret |
| **Interactive** | Tooltips, guided paths (NYT Election) | Full data for filtering/zooming (Flight paths) |

**Shneiderman's Mantra**: *"Overview first, zoom and filter, then details-on-demand."*
**Modern shift (Archie Tse)**: People just want to **scroll**.

---

## 4. Perceptual Ranking Scale

| Rank | For Ordered/Quantitative | For Categorical |
|------|--------------------------|-----------------|
| 1 ★ | Position on common scale | Spatial region |
| 2 | Position on unaligned scale | Color hue |
| 3 | Length (aligned baselines) | Motion |
| 4 | Tilt / Angle | Shape |
| 5 | Area / Size | — |
| 6 | Color luminance / Saturation | — |
| 7 | Volume / Curvature | — |

**Key**: Bar charts (length) = top → most accurate. Bubble (area) = mid. Gauge (angle) = low. Heatmap (color) = low but pattern-rich.

---

## 5. Comparison Charts (16 Types)

| # | Chart | Best For | Key Rule/Caveat |
|---|-------|----------|-----------------|
| 1 | **Bar Chart** | Categorical comparison | Start axis at zero; don't break the bar |
| 2 | **Radial Bar** | Compact cyclical data | Distorts perception — avoid |
| 3 | **Paired Bar** | Across + within categories | Gets cluttered fast |
| 4 | **Stacked Bar** | Part-to-whole sums | Interior series hard to compare (no shared baseline) |
| 5 | **Diverging Bar** | Likert scale surveys | Place Neutral off to the side |
| 6 | **Dot Plot** | Ranges/differences | Summary chart — hides intermediate variation |
| 7 | **Marimekko** | 2 variables (height + width) | Width = 2nd variable |
| 8 | **Mosaic** | Both dims = 100% | Fills entire graph space |
| 9 | **Unit/Isotype** | Counts with icons | Scale by area, not height |
| 10 | **Waffle Chart** | Part-to-whole (%) | 10×10 grid, 1 cell = 1% |
| 11 | **Heatmap** | Patterns, high-frequency data | Color-coded table; exact values secondary |
| 12 | **Gauge Chart** | Progress/targets | Humans bad at comparing angles |
| 13 | **Bullet Chart** | Linear alternative to gauge | 3 elements: Actual bar, Target line, Ranges |
| 14 | **Bubble/Nested** | Size comparison | Humans bad at circle area; can't show negatives |
| 15 | **Sankey Diagram** | Flows & transitions | Too many series = unreadable |
| 16 | **Waterfall** | Running total (+/− from start) | Connect bars with guide lines |

---

## 6. Time Charts (13 Types)

| # | Chart | Best For | Key Rule/Caveat |
|---|-------|----------|-----------------|
| 1 | **Line Chart** | Trends over continuous time | Zero baseline NOT required; use "Start with Gray" |
| 2 | ~~Dual Axis~~ | — | **AVOID** (axis manipulation creates false correlations) |
| 3 | **Circular Line** | Cyclical metaphors | Less perceptually accurate |
| 4 | **Slope Chart** | Change between 2 time points | Simplified line chart |
| 5 | **Sparklines** | In-table trend indicators | Word-sized graphics (Tufte) |
| 6 | **Bump Chart** | Rank changes over time | Hides magnitude; Ribbon variant adds value |
| 7 | **Cycle Chart** | Seasonal trends | Compare months/weeks across years |
| 8 | **Area Chart** | Weighted trends | Area = filled line; axis MUST start at zero |
| 9 | **Stacked Area** | Multiple series summing to total | Line-width illusion; ordering matters |
| 10 | **Streamgraph** | High-volatility peaks/troughs | Organic shape; baseline on both sides |
| 11 | **Horizon Chart** | Dense, compact time series | Color = magnitude; similar to heatmap |
| 12 | **Gantt Chart** | Schedules/durations | Horizontal bars = time spans |
| 13 | **Connected Scatter** | 2 time series relationship | Alternative to dual-axis; shows trajectory |

**Key Concepts**: Line-width illusion, preattentive attributes (color/width), data markers for specific values, visual signals for missing data.

---

## 7. Visual Analytics

**Definition**: Combining automatic + visual analysis methods with human interaction for knowledge discovery through continuous refinement.

### Process
1. **Data Transformation** → Clean, Normalize, Integrate
2. **Two Pathways**:
   - *Automatic first*: Data mining → Model evaluation (via viz) → Parameter tuning
   - *Visual first*: Exploration → Hypothesis generation → Automated confirmation
3. **Alternation** → Continuous refinement, early error detection, higher confidence
4. **Human Interaction** → Parameter control + algorithm selection

### Knowledge Sources
Visualization ⊕ Automatic Analysis ⊕ Human Interactions

### Complex Data Types
| Type | Structure | Example |
|------|-----------|---------|
| **Network** | General graph (cycles, multiple paths) | Social network |
| **Tree** | Hierarchy (no cycles, single path, one root) | Org chart |
| **Spatial** | Field: f(x,y) → value | Geographic data |

---

## 8. Munzner's Nested Model (4 Levels)

| Level | Question | Focus |
|-------|----------|-------|
| **Domain Situation** | Who? | Users, their domain, their data |
| **Abstraction** | What & Why? | Data types + Task types |
| **Idiom** | How? | Visual encoding + Interaction design |
| **Algorithm** | How efficiently? | Computational performance |

↓ Downstream = cascading effects • ↑ Upstream = iterative refinement

### Task Abstraction

**Actions:**
- **Analyze**: Consume (discover/present/enjoy) or Produce (annotate/record/derive)
- **Search**: Lookup (know both) → Locate (know target) → Browse (know location) → Explore (know neither)
- **Query**: Identify (one) → Compare (some) → Summarize (all)

### Marks & Channels
- **Marks**: Points (0D), Lines (1D), Areas (2D), Links
- **Channels**: Position > Length > Angle > Area > Color > Volume
- **Marks as Constraints**: Points = 0 constraints (can size+shape), Lines = 1 (can width), Areas = 2 (fixed)

---

## 9. Feature Engineering

**Definition**: Preprocessing step to transform raw data into useful features for ML models.

### 4 Core Processes
1. **Creation** — New variables from existing (e.g., BMI = Weight/Height², DTI = Debt/Income)
2. **Transformation** — Scale/encode to same range
3. **Extraction** — Reduce dimensions (PCA, clustering)
4. **Selection** — Remove redundant/noisy features (reduce overfitting)

### Techniques
| Technique | What it Does |
|-----------|-------------|
| **Imputation** | Fill missing values (Categorical→mode, Numerical→mean/median) |
| **Discretization** | Group values into bins/buckets |
| **Integer Encoding** | Categories → digits 1-n (for ordinal data) |
| **One-Hot Encoding** | Binary dummy variables (for nominal data) |
| **Feature Splitting** | Date → year, month, day |

---

## 10. Data Scaling

| Method | Range | Formula | Outlier Safe? | Best Use |
|--------|-------|---------|--------------|----------|
| **Absolute Max** | −1 to 1 | $v/\max(\|v\|)$ | ✗ | Quick scaling |
| **Min-Max** | 0 to 1 | $(v-\min)/(\max-\min)$ | ✗ | Viz, neural nets |
| **Standardization** | μ=0, σ=1 | $(v-\bar{A})/\sigma_A$ | Partial | PCA, clustering |
| **Robust** | IQR-based | $(v-\text{median})/\text{IQR}$ | ✓ | Outlier-heavy data |
| **Decimal** | < 1 | $v/10^j$ | ✗ | Magnitude reduction |

**Why scale?** Different units/magnitudes dominate plots → scale makes features comparable.

**Quick Examples:**
- Min-Max: [20,40,60,80,100] → [0, 0.25, 0.5, 0.75, 1.0]
- Z-score: [40,50,60] (μ=50, σ=10) → [−1, 0, 1]

**Rule**: Understand distribution → Choose method → Apply *before* modeling.

---

## 🔥 PYQ-Targeted Quick Recall

| Mid Sem Topic | Likely Question Area |
|---------------|---------------------|
| Data Visualization Framework & Components | Q1: List 10 components |
| Data Attributes (NOIR) | Q2: Types with examples, operations |
| Anscombe's Quartet | Q3: What it is, why it matters |
| 5 Guidelines for Better Viz | Q4: List + explain each |
| Chart Types (Comparison + Time) | Q5: Properties, advantages, disadvantages |
| Munzner's Nested Model | Framework: 4 levels, 3 questions |
| Perceptual Ranking | Channel effectiveness ranking |
| Visual Analytics | Definition, process, pathways |
| Feature Engineering | 4 processes + techniques |
| Data Scaling | Methods, formulas, when to use |
