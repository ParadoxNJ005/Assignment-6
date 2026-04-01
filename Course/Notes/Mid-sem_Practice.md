# 📝 Data Visualization — Probable Mid-Sem Practice Questions

> Based on PYQ pattern analysis (Mid Sem 2025 + End Sem 2025), lecture PDFs, and existing MCQ banks.
> Format: Questions with detailed tutor-mode answers.

---

## Section A: Short Answer / Theory Questions

---

### Q1. List and briefly explain the 10 main components of a Data Visualization framework.
**[High Probability — appeared in Mid Sem 2025 Q1]**

**Answer:**
1. **Data** — The raw input: numerical, text, or geospatial data.
2. **Visual Elements** — Graphics, charts, overlays, diagrams, maps, tables.
3. **Visualization Techniques** — Methods for transforming, scaling data, and selecting the right chart type.
4. **Interactivity** — Features like zooming, hovering (tooltips), rotating, filtering.
5. **Color Palette & Design** — Font selection, element positioning, styling for usability and aesthetics.
6. **Context & Annotations** — Titles, subtitles, captions, legends that give meaning.
7. **Tools & Platforms** — Tableau, Power BI, Python (Matplotlib, Seaborn, D3.js).
8. **Data Preparation** — Cleaning, processing, aggregating, reshaping raw data.
9. **Data Exploration** — Searching for patterns, trends, noise, correlations.
10. **Dashboarding** — Aggregate displays combining multiple views for monitoring KPIs.

---

### Q2. What is Anscombe's Quartet? What is its fundamental implication for data analysis?
**[High Probability — appeared in Mid Sem 2025 Q3]**

**Answer:**
Anscombe's Quartet is a set of **four datasets** that possess **identical simple descriptive statistics**:
- Same mean (for both x and y)
- Same variance
- Same correlation coefficient
- Same linear regression line

However, when plotted graphically, their structures are **completely different** — one is linear, one is curved, one has an outlier, and one is a vertical cluster with one extreme point.

**Fundamental Implication:** Relying purely on summary statistics can be dangerously misleading. A single summary often oversimplifies and hides the true nature of the data. **You must always visualize your data** to understand its actual structure, distribution, and outliers.

---

### Q3. Explain the five guidelines for better data visualizations with examples.
**[High Probability — appeared in Mid Sem 2025 Q4]**

**Answer:**

1. **Show the Data**: The data should be the primary visual element. Remove unnecessary borders, backgrounds, and decorations.
   - *Example*: A dot density map of the US population using only dots — no state borders, roads, or labels — where the data itself reveals clusters via the Gestalt principle of similarity.

2. **Reduce the Clutter**: Eliminate distracting visual elements that don't encode data.
   - *Remove*: Heavy gridlines, unnecessary 3D effects, textured fills, excessive data markers.
   - *Example*: A 3D pie chart distorts proportions — replace with a flat bar chart.

3. **Integrate Graphics and Text**: Text and visuals should work together.
   - **Label directly** instead of using legends (forces eye movement back and forth).
   - Write **headline-style titles** that state the takeaway, not just a description (e.g., "US health spending grew 40% in 15 years" vs. "Health spending data").
   - Add **explainer annotations** to call out peaks, anomalies, or context.

4. **Avoid the Spaghetti Chart**: Don't pack too many series into one chart.
   - Use **Small Multiples** (panel/trellis/facet charts): Break one dense chart into multiple smaller charts sharing the same scale, axes, and layout.
   - *Example*: Brexit voting data shown as 6 separate scatterplots by demographic variable instead of one overlapping mess.

5. **Start with Gray**: Begin every visualization with all data elements in gray. Then intentionally add color only where needed.
   - Forces purposeful, strategic use of color to highlight specific data points.
   - *Example*: In a multi-country line chart, show all countries in gray and only highlight USA and Germany in color.

---

### Q4. Describe Munzner's Nested Model of Visualization Design. What are the four levels and three questions?
**[High Probability — referenced in Mid Sem 2025 Q1, End Sem Q4]**

**Answer:**
Munzner's Nested Model provides a systematic framework for visualization design with **four levels**, each answering a core question:

| Level | Question | Focus |
|-------|----------|-------|
| 1. **Domain Situation** | **Who?** | Understand the target users, their domain, their questions & data |
| 2. **Abstraction** | **What & Why?** | Translate domain specifics into generalized vis vocabulary — Data Abstraction (what is shown?) + Task Abstraction (why is user looking?) |
| 3. **Idiom** | **How?** | Visual encoding idiom (how to draw) + Interaction idiom (how to manipulate) |
| 4. **Algorithm** | **How efficiently?** | Efficient computation for rendering and processing |

**Key Properties:**
- **Downstream cascading effects**: A wrong decision at an upper level cascades errors to all lower levels (e.g., wrong data abstraction → wrong idiom choice → useless visualization).
- **Upstream iterative refinement**: Insights at lower levels may require revisiting upper-level decisions.
- **Validation differs at each level**: Each level has different ways to get it wrong and different methods to validate.

---

### Q5. Differentiate between EDA and CDA. List the objectives of EDA.
**[Medium-High Probability — appeared in End Sem Q2]**

**Answer:**

| Aspect | EDA (Exploratory Data Analysis) | CDA (Confirmatory Data Analysis) |
|--------|-------------------------------|----------------------------------|
| Analogy | Like **detective work** (gathering evidence) | Like a **court trial** (evaluating evidence) |
| Purpose | Discover patterns, generate hypotheses | Test and confirm pre-defined hypotheses |
| Approach | Open-ended, iterative, visual | Structured, statistical testing |
| Example | Exploring a new dataset to find trends | Clinical research trials |

**Objectives of EDA:**
1. **Discover Patterns** — Identify trends, clusters, relationships.
2. **Spot Anomalies** — Find outliers or unexpected values.
3. **Frame Hypotheses** — Generate testable questions from data exploration.
4. **Check Assumptions** — Validate whether assumptions for modeling are met.

**EDA helps answer:** What data types am I dealing with? What is a typical value? What uncertainty surrounds it? What variation/covariation exists? Are there outliers? Which features have the most business impact?

---

### Q6. Explain the four data types (NOIR) used in EDA with examples and allowed operations.
**[High Probability — appeared in Mid Sem 2025 Q2]**

**Answer:**

| Type | Nature | True Zero? | Allowed Operations | Example |
|------|--------|-----------|-------------------|---------|
| **Nominal** | Qualitative, unordered categories | ✗ | Equality (=, ≠), set membership only | Religion, Color, Type of Chocolate |
| **Ordinal** | Categorical with inherent order/rank | ✗ | Equality + Ordering (>, <) | Low/Med/High, Satisfaction (Poor→Excellent) |
| **Interval** | Numerical, equal intervals meaningful | ✗ | Equality + Order + Addition/Subtraction | Temperature (°C/°F), Credit scores, GMAT |
| **Ratio** | Numerical with absolute zero | ✓ | All arithmetic (+ − × ÷) | Weight, Age, Height, Income |

**Key Distinctions:**
- **Interval vs Ratio**: 0°C does NOT mean "no temperature" (interval — no true zero). 0 kg DOES mean "no weight" (ratio — true zero).
- **Nominal vs Ordinal**: Both are categorical, but ordinal has a meaningful rank/order (e.g., "Excellent > Good > Poor").

---

### Q7. Explain measures of Central Tendency. When should you use Mean, Median, or Mode?
**[High Probability — appeared in End Sem Q1, Q2b]**

**Answer:**

| Measure | Definition | Formula/Method | Sensitive to Outliers? |
|---------|-----------|---------------|----------------------|
| **Mean** | Arithmetic average of all values | $\bar{x} = \sum x_i / n$ | ✓ Yes |
| **Median** | Middle value when data is sorted | Odd: $(n+1)/2$ position; Even: avg of $n/2$ and $(n/2)+1$ | ✗ No |
| **Mode** | Most frequently occurring value | Count frequencies | ✗ No |

**When to use which:**

| Data Level | Use |
|-----------|-----|
| Nominal | Mode only |
| Ordinal | Mode, Median |
| Interval / Ratio | Mode, Median, Mean |

**Critical Rule:** In skewed distributions, **Median is the best measure** because it is unaffected by extreme outliers.

- **Normal distribution**: Mean = Median = Mode → all three work.
- **Positively skewed (right)**: Mode < Median < Mean → use Median.
- **Negatively skewed (left)**: Mean < Median < Mode → use Median.

---

### Q8. Explain Skewness and Kurtosis with types and their implications.
**[High Probability — appeared in both Mid Sem and End Sem MCQs]**

**Answer:**

**Skewness** measures the asymmetry of a probability distribution:

| Type | Tail Direction | Central Tendency Order | Skewness Value |
|------|---------------|----------------------|----------------|
| Normal (Symmetric) | None | Mean = Median = Mode | 0 |
| Positive Skew (Right) | Long right tail | **Mode < Median < Mean** | > 0 |
| Negative Skew (Left) | Long left tail | **Mean < Median < Mode** | < 0 |

**Pearson's Coefficient of Skewness**: $S_k = 3(\text{Mean} - \text{Median}) / \sigma$ (used when mode is unknown).

**Kurtosis** measures tail heaviness (presence of outliers) compared to a Normal distribution:

| Type | Tail | Kurtosis | Outliers? | Example |
|------|------|----------|-----------|---------|
| **Mesokurtic** | Normal | ≈ 0 | Normal | Standard bell curve |
| **Leptokurtic** | Heavy (peaked) | > 0 | ✓ Present | Stock market returns |
| **Platykurtic** | Light (flat) | < 0 | ✗ Absent | Uniform-like distributions |

**Practical Implication:** Kurtosis helps with outlier detection and determining proper sample sizes.

---

## Section B: Chart-Specific Questions

---

### Q9. Describe any 5 chart types used for visualizing comparison of data. For each, state its properties, advantages, disadvantages, and a potential narrative.
**[High Probability — Mid Sem 2025 Q5]**

**Answer:**

#### 1. Bar Chart
- **Properties**: Rectangles along vertical (column) or horizontal (bar) axis. Length/height represents value.
- **Advantages**: Sits at the **top of the perceptual ranking scale** — most accurately perceived comparison. Familiar, easy to read.
- **Disadvantages**: Can appear boring; too many bars = clutter.
- **Narrative**: Comparing populations across countries, ranking sales by region.
- **Rules**: Start axis at zero. Don't break the bar. Use gridlines judiciously.

#### 2. Dot Plot (Dumbbell Chart)
- **Properties**: Circles at data values connected by a line or arrow. Developed by William Cleveland.
- **Advantages**: Uses less ink than bars (lighter visual), great for showing range/difference between two points.
- **Disadvantages**: Summary chart — hides all intermediate data variations between the two points.
- **Narrative**: Comparing math vs reading test scores across countries; showing change between 2015 and 2020.

#### 3. Heatmap
- **Properties**: A table with color-coded cells. Color saturation represents data values.
- **Advantages**: Excellent for high-frequency data and spotting patterns quickly (e.g., higher fatalities on Fridays). Can show data across two categorical dimensions.
- **Disadvantages**: Cannot determine exact values easily (color perception is low on the perceptual ranking scale).
- **Narrative**: Visualizing measles infection rates across all US states over 80 years.

#### 4. Sankey Diagram
- **Properties**: Arrows/lines showing transitions between states. Width of lines = magnitude of flow.
- **Advantages**: Shows flow and category splitting beautifully. Named after Matthew Henry Phineas Riall Sankey (1898).
- **Disadvantages**: Too many series makes it "spaghetti-like" and unreadable.
- **Narrative**: Showing how students tried to spell "camouflage" — branching from correct to incorrect paths.

#### 5. Waterfall Chart
- **Properties**: A modified bar chart where each subsequent bar starts where the previous one ended.
- **Advantages**: Clearly shows running totals and the additive/subtractive components.
- **Disadvantages**: Can be confusing without connecting guide lines and color differentiation for positive vs negative.
- **Narrative**: Revenue → Expenses → Adjustments → Final Profit, showing how each component contributes.

---

### Q10. Describe any 5 chart types used for visualizing changes over time.
**[High Probability — Mid Sem 2025 Q5]**

**Answer:**

#### 1. Line Chart
- **Properties**: Data values connected by lines over a continuous period. Near the top of the perceptual ranking scale.
- **Rule**: Axis does NOT need to start at zero (unlike bar charts), but **delineate the zero baseline** when crossing positive/negative.
- **Caution**: Line-width illusion — we misjudge the vertical gap between two curves.
- **Missing Data**: Use dashed lines or dots — never pretend the series is continuous.

#### 2. Sparklines
- **Properties**: Tiny, word-sized line graphics embedded in tables (invented by Edward Tufte).
- **Use Case**: Track general patterns, not specific values. Shows trends inline with data-rich tables.

#### 3. Bump Chart
- **Properties**: Plots **rank changes** (not values) over time.
- **Advantage**: Abstracts from magnitude differences — shows relative positions clearly.
- **Ribbon Effect**: Width scaled to actual data values, bringing magnitude back.

#### 4. Stacked Area Chart
- **Properties**: Multiple series stacked, summing to a total/percentage. The area gives visual weight.
- **Three Disadvantages**:
  1. Line-width illusion (steep changes look bigger).
  2. Only bottom series has a flat baseline — other series are hard to compare.
  3. Ordering the series changes where the reader's attention goes.

#### 5. Connected Scatterplot
- **Properties**: Two variables plotted on x and y axes, connected chronologically by a line.
- **Use Case**: Alternative to dual-axis charts. Shows trajectory of the relationship between two time series (e.g., life expectancy vs GDP growth over decades).

---

### Q11. Why should you avoid Dual Axis Line Charts? What are the alternatives?
**[Medium Probability]**

**Answer:**

**Problems with Dual Axis Charts:**
1. **Confusing**: Hard to determine which line corresponds to which axis.
2. **Misleading**: By arbitrarily choosing axis ranges, the creator can make lines cross anywhere and imply false correlations.
3. **Gridline mismatch**: Horizontal gridlines typically align with only one axis, leaving the other floating.
4. **False focal points**: The intersection of two lines becomes a focal point, even if it has no real meaning.

**Example**: Tyler Vigen's "Spurious Correlations" collection shows how dual-axis charts can make completely unrelated variables (like US cheese consumption and bedsheet tangling deaths) appear correlated.

**Alternatives:**
- Two **side-by-side charts** (small multiples).
- **Vertically stacked** charts with aligned horizontal time axes.
- A **connected scatterplot** if the relationship between the two variables is the focus.

---

## Section C: Visual Analytics & Feature Engineering

---

### Q12. What is Visual Analytics? Explain the Visual Analytics process.
**[Medium-High Probability — referenced in Mid Sem Q1 scope]**

**Answer:**
**Visual Analytics** is a field that combines **automatic analysis methods** (data mining, algorithms) with **interactive visual interfaces** and **human interaction** to gain knowledge from data through continuous refinement and verification.

**The Process:**
1. **Data Transformation** — Clean, normalize, and integrate heterogeneous data sources.
2. **Two Analysis Pathways:**
   - **Automatic Analysis First**: Data mining → Model generation → Visual evaluation → Parameter tuning.
   - **Visual Exploration First**: Interactive visual exploration → Hypothesis generation → Automated confirmation.
3. **The Power of Alternation**: Alternating between visual and automatic methods leads to continuous refinement, early error detection, and higher confidence.
4. **Human Interaction (Key Component)**: Analyst controls parameters and selects algorithms based on visual feedback.

**Knowledge Sources**: Visualization ⊕ Automatic Analysis ⊕ Human Interactions.

---

### Q13. Explain Feature Engineering. What are its four core processes? Give techniques with examples.
**[Medium-High Probability — appeared in End Sem Q3, MCQs]**

**Answer:**
**Feature Engineering** is the preprocessing step that transforms raw data into useful features (predictor variables) for ML models. It is often called the *"secret sauce"* behind successful predictive models.

**Four Core Processes:**

| Process | What it Does | Example |
|---------|-------------|---------|
| **1. Feature Creation** | Derive new variables from existing ones using math/domain knowledge | BMI = Weight/Height²; Debt-to-Income = Debt/Income |
| **2. Feature Transformation** | Scale/encode variables to the same range | Min-Max scaling, Log transform, Standardization |
| **3. Feature Extraction** | Reduce dimensionality using algorithms | PCA converts many features → 2 principal components for 2D scatter |
| **4. Feature Selection** | Remove redundant/noisy features | Keeping Study Hours, Marks, Attendance; removing Student ID |

**Specific Techniques:**

| Technique | Description |
|-----------|-------------|
| **Imputation** | Fill missing values: Categorical → mode, Numerical → mean/median |
| **Discretization** | Group continuous values into bins/buckets |
| **Integer/Label Encoding** | Assign ordinal digits (1 to n) for ordered categories |
| **One-Hot Encoding (OHE)** | Create binary dummy variables for unordered categories (e.g., color → color_red, color_blue) |
| **Feature Splitting** | Separate features (e.g., timestamp → year, month, day, hour) |

---

### Q14. Explain Data Scaling methods. When should you use each?
**[Medium Probability — End Sem scope, MCQs on scaling]**

**Answer:**

**Why Scale?** Variables with different units (e.g., Age: 20–60, Salary: 20K–100K) cause salary to dominate plots and distance calculations. Scaling makes features comparable.

| Method | Formula | Range | Outlier Robust? | Best Use |
|--------|---------|-------|-----------------|----------|
| **Absolute Max** | $v' = v / \max(\|v\|)$ | −1 to 1 | ✗ | Quick scaling |
| **Min-Max** | $v' = (v - \min) / (\max - \min)$ | 0 to 1 | ✗ | Visualization, Neural networks |
| **Standardization (Z-score)** | $v' = (v - \bar{A}) / \sigma_A$ | μ=0, σ=1 | Partial | PCA, Clustering, ML models |
| **Robust** | $v' = (v - \text{median}) / \text{IQR}$ | Median-centered | ✓ | Outlier-heavy data |
| **Decimal** | $v' = v / 10^j$ | < 1 | ✗ | Simple magnitude reduction |

**Worked Example — Min-Max:**
Scores = [20, 40, 60, 80, 100]. Min = 20, Max = 100.
- 20 → $(20-20)/(100-20) = 0.0$
- 40 → $(40-20)/(100-20) = 0.25$
- 60 → 0.5, 80 → 0.75, 100 → 1.0

**Worked Example — Z-score:**
Marks = [40, 50, 60]. Mean = 50, Std = 10.
- 40 → $(40-50)/10 = -1$, 50 → $0$, 60 → $1$

**Best Practice:** Understand distribution → Choose method → Apply *before* modeling.

---

## Section D: MCQ Practice (Pattern-Based)

---

**Q15.** Gestalt principle where our brain fills in missing parts of incomplete shapes is called:
- (a) Proximity
- (b) Similarity
- (c) **Closure** ✓
- (d) Continuity

**Q16.** In a positively skewed distribution, which order holds?
- (a) Mean < Median < Mode
- (b) **Mode < Median < Mean** ✓
- (c) Mean = Median = Mode
- (d) Mode < Mean < Median

**Q17.** A Marimekko chart differs from a standard bar chart because:
- (a) Bars are circular
- (b) **Width of each bar is scaled to another variable** ✓
- (c) Bars are stacked to 100%
- (d) It uses color only

**Q18.** Kurtosis type where the tails are heavy and outliers are present:
- (a) Mesokurtic
- (b) **Leptokurtic** ✓
- (c) Platykurtic
- (d) Isokurtic

**Q19.** Which of the following sits HIGHEST on the perceptual ranking scale for ordered data?
- (a) Color saturation
- (b) Area/Size
- (c) **Position on common scale** ✓
- (d) Tilt/Angle

**Q20.** The "Start with Gray" guideline means:
- (a) Use only grayscale charts
- (b) **Start all data elements in gray, then add color purposefully** ✓
- (c) Print charts in grayscale for testing
- (d) Use gray backgrounds

**Q21.** Which chart type was invented by Stephen Few as a compact alternative to gauge charts?
- (a) Dot Plot
- (b) Sparkline
- (c) **Bullet Chart** ✓
- (d) Waterfall Chart

**Q22.** Shneiderman's mantra for interactive data visualization is:
- (a) "Show the data, reduce the clutter"
- (b) **"Overview first, zoom and filter, then details-on-demand"** ✓
- (c) "Start with gray"
- (d) "Choose the right chart type"

**Q23.** One-Hot Encoding is used when:
- (a) There is an ordinal relationship between categories
- (b) **There is NO ordinal relationship between categories** ✓
- (c) The data is numerical
- (d) Missing values need to be imputed

**Q24.** A Waffle Chart is a:
- (a) Circular chart showing proportions
- (b) **10×10 grid where each cell represents 1 percentage point** ✓
- (c) A stacked bar chart variant
- (d) A type of heatmap

**Q25.** In a Bump Chart, the primary data plotted is:
- (a) Raw values over time
- (b) Percentage change
- (c) **Ranks over time** ✓
- (d) Cumulative totals

**Q26.** Which data type has a true zero and supports all arithmetic operations?
- (a) Nominal
- (b) Ordinal
- (c) Interval
- (d) **Ratio** ✓

**Q27.** A Streamgraph differs from a Stacked Area chart because:
- (a) It uses lines instead of areas
- (b) **Data can be positive on both sides of the central axis, creating an organic shape** ✓
- (c) It only shows one data series
- (d) It requires interactive controls

**Q28.** Marks in Munzner's framework include all EXCEPT:
- (a) Points
- (b) Lines
- (c) Areas
- (d) **Color** ✓ (Color is a *channel*, not a mark)

**Q29.** Which scaling method is most robust to outliers?
- (a) Min-Max Scaling
- (b) Absolute Maximum Scaling
- (c) Standardization
- (d) **Robust Scaling (IQR-based)** ✓

**Q30.** In Munzner's Search taxonomy, when you know the target but NOT the location, you are:
- (a) Looking up
- (b) **Locating** ✓
- (c) Browsing
- (d) Exploring

**Q31.** The bar chart axis should always:
- (a) Start at the median value
- (b) **Start at zero** ✓
- (c) Start at the minimum data value
- (d) Use a logarithmic scale

**Q32.** A Connected Scatterplot is primarily used to:
- (a) Show categories
- (b) **Show the relationship between two time series without dual axes** ✓
- (c) Display rankings
- (d) Show part-to-whole relationships

**Q33.** Sparklines were invented by:
- (a) William Playfair
- (b) Stephen Few
- (c) **Edward Tufte** ✓
- (d) Florence Nightingale

**Q34.** Feature Extraction in Feature Engineering primarily aims to:
- (a) Create new features manually
- (b) **Reduce dimensionality while preserving important information** ✓
- (c) Handle missing values
- (d) Encode categorical variables

**Q35.** The "Line-Width Illusion" means:
- (a) Thicker lines appear more important
- (b) **We assess the distance between curves at the closest point rather than the vertical distance** ✓
- (c) Lines in 3D appear wider
- (d) Dashed lines appear shorter

---

## 🎯 Topic Probability Matrix

| Topic | Probability | Expected Format |
|-------|------------|-----------------|
| 10 Components of DV Framework | 🔴 High | Short Answer / List |
| Anscombe's Quartet | 🔴 High | Explain + Implication |
| 5 Guidelines for Better Viz | 🔴 High | Explain with Examples |
| NOIR Data Types | 🔴 High | Table / Explain |
| Comparison Charts (5+) | 🔴 High | Props, Adv, Disadv, Narrative |
| Time Charts (5+) | 🔴 High | Props, Adv, Disadv, Narrative |
| Central Tendency + When to Use | 🔴 High | Table + Skewed Rule |
| Skewness & Kurtosis | 🔴 High | Types + Order + Examples |
| Munzner's Nested Model | 🟡 Medium-High | 4 Levels, 3 Questions |
| Visual Analytics Process | 🟡 Medium-High | Definition + Steps |
| Feature Engineering | 🟡 Medium-High | 4 Processes + Techniques |
| EDA vs CDA | 🟡 Medium | Compare + Objectives |
| Data Scaling Methods | 🟡 Medium | Formulas + When to Use |
| Marks & Channels | 🟡 Medium | Definitions + Rankings |
| Gestalt Principles | 🟢 Medium-Low | MCQ / Short |
| Shneiderman's Mantra | 🟢 Medium-Low | MCQ recall |
| Perceptual Ranking Scale | 🟡 Medium | Channel rankings table |
