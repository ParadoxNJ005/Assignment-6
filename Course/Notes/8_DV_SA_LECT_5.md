# DV_SA_LECT_5: Visualization Frameworks & Feature Engineering

## Part 1: Analysis Framework - Four Levels, Three Questions
Based on Tamara Munzner’s Nested Model of Visualization Design and Validation.

### 1. Domain Situation (Who)
- **Target Users:** Understand the specific group of users and their target domain.
- **Goal:** Break down complex domain questions and problems into simpler abstract tasks.

### 2. Abstraction (What & Why)
- **Data Abstraction (What):** Identify the data types needed to support the tasks. Transform or derive data if necessary.
- **Task Abstraction (Why):** Translate domain-specific actions into generalized analytical tasks.

### 3. Idiom (How)
- **Visual Encoding Idiom:** How to draw the data (Marks and Channels).
- **Interaction Idiom:** How to manipulate the visual elements.

### 4. Algorithm
- **Focus:** Efficient computation and processing data.

*Note: The nested model implies downstream cascading effects and upstream iterative refinement. Validation is difficult because errors can occur at each level.*

---

## Part 2: Task Abstraction (Actions and Targets)

### Actions
- **Analyze:** Consume (discover vs. present/explore vs. explain, enjoy) or Produce (annotate, record, derive).
- **Search:** Depends on what the user knows (target and location).
  - **Lookup:** Know both target and location (e.g., word in a dictionary).
  - **Locate:** Know target, do not know location (e.g., node in a network).
  - **Browse:** Do not know target, know location (e.g., books in a bookstore).
  - **Explore:** Do not know target or location (e.g., cool neighborhood in a new city).
- **Query:** How much data matters?
  - **Identify:** One item.
  - **Compare:** Some items.
  - **Summarize:** All items.

### Targets
- What is being acted on (distributions, trends, outliers, topology).

---

## Part 3: Visual Encoding (Marks and Channels)
Idiom structure is the combination of Marks and Channels, explaining how raw data becomes a visualization.

### Marks
Geometric primitives that represent individual items or links.
- **Points (0D):** Represent individual data items (e.g., scatter plots).
- **Lines (1D):** Represent connections or trends (e.g., time series).
- **Bars/Areas (2D/Interlocking):** Represent quantities (e.g., bar charts).
- **Links:** Represent relationships (e.g., network graphs).

### Channels
Control the appearance of marks based on attributes (also called visual variables or retinal channels).
- **Position (Most Important):** Shows numerical values.
- **Color:** Represents category or magnitude.
- **Size:** Represents quantity.
- **Shape:** Differentiates categories.
- **Orientation:** Direction of marks (e.g., slope).

### Channel Rankings
- **Expressiveness**: Match channel type to data type (magnitude for ordered, identity for categorical).
- **Effectiveness**: Channels differ in the accuracy of human perception (Spatial position ranks highest for both).

### Marks as Constraints
- **Points (0D)**: 0 constraints on size → can encode more attributes with size & shape.
- **Lines (1D)**: 1 constraint (length fixed) → can still encode width.
- **Interlocking Areas (2D)**: 2 constraints (length/width) → cannot size or shape code further.
- **Quick Check**: Can you size-code another attribute, or is size/shape already in use?

### Grouping Channels
Four ways to encode group membership:
1. **Containment** — Enclosing related marks.
2. **Connection** — Lines linking related items.
3. **Proximity** — Same spatial region.
4. **Similarity** — Same values in categorical channels.

---

## Part 4: Feature Engineering
The pre-processing step to transform raw data into useful predictor variables, significantly improving exploratory data analysis (EDA) and visualizations.

### 1. Feature Creation
Crafting new variables from existing sources using mathematical operations or domain knowledge.

**Real-World Examples:**
| Domain | Raw Features | Engineered Feature | Impact |
|--------|-------------|-------------------|--------|
| Education | Study Hours, Marks | Performance Score = Marks / Study Hours | Reveals learning efficiency |
| Finance | Income, Debt, Expenses | Debt-to-Income Ratio = Debt / Income; Savings = Income − Expenses | Normalizes individual scale differences |
| Healthcare | Weight (kg), Height (m) | BMI = Weight / Height² | Transforms raw biometrics into a globally recognized health indicator |

### 2. Feature Transformation
Scaling, encoding, and changing data to ensure variables are on the same scale, reducing skewness, and making visualizations clearer.

### 3. Feature Extraction
Reducing dimensionality and summarizing data natively using algorithms like PCA (Principal Component Analysis). Example: Converting many features into Principal Components (PC1, PC2) for a simpler 2D scatter plot visualization.

### 4. Feature Selection
Selecting the most relevant subset of features by removing redundant, irrelevant, or noisy features to reduce overfitting.

### Additional Techniques
- **Imputation:** Handling missing values.
  - *Categorical Imputation:* Replacing with the mode.
  - *Numerical Imputation:* Replacing with the mean/median.
- **Discretization (Binning):** Grouping continuous sets of values into logical bins.
- **Categorical Encoding:**
  - *Integer/Label Encoding:* Assigning ordinal digits (1 to n) to unique categories.
  - *One-Hot Encoding (OHE):* Creating binary dummy variables for non-ordinal categories.
- **Feature Splitting:** Separating features (e.g., splitting a timestamp into hour, day, month, year).

---

## Part 5: Data Scaling
Critical for data visualization to make varying units comparable, improve visual clarity, and prevent scale dominance in multivariate analysis (PCA, Clustering, Heatmaps).

### 1. Absolute Maximum Scaling
- **Concept:** Divides every observation by the maximum absolute value.
- **Range:** -1 to 1 (or 0 to 1).
- **Drawback:** Sensitive to outliers.

### 2. Min-Max Scaling (Normalization)
- **Concept:** Subtracts the minimum value and divides by the dataset's range (max - min).
- **Range:** Exactly 0 to 1.
- **Drawback:** Prone to extreme outliers.

### 3. Normalization (Mean-based)
- **Concept:** Similar to Min-Max, but subtracts the average value instead of the minimum.

### 4. Standardization (Z-score Normalization)
- **Concept:** Subtracts the mean (centering data at 0) and divides by standard deviation (variance = 1).
- **Range:** Centers around 0, equal spread.
- **Best Use:** When data has outliers, or for PCA, clustering, and distance-based ML models.

### 5. Robust Scaling
- **Concept:** Subtracts the median and divides by the Inter Quartile Range (IQR).
- **Advantage:** Highly robust to outliers.

### 6. Decimal Scaling
- **Concept:** Shifts the decimal point by a power of 10 based on the maximum absolute value.
- **Range:** less than 1.

### Scaling Method Comparison & Practical Guidelines

| Method | Range | Formula | Outlier Robust? | Best Use |
|--------|-------|---------|-----------------|----------|
| Absolute Max | −1 to 1 | $v' = v / \max(|v|)$ | ❌ | Quick scaling |
| Min-Max | 0 to 1 | $v' = (v - \min) / (\max - \min)$ | ❌ | Visualization, neural networks |
| Standardization | Mean=0, Std=1 | $v' = (v - \bar{A}) / \sigma_A$ | Partially | PCA, clustering, ML models |
| Robust | Median-centered | $v' = (v - \text{median}) / \text{IQR}$ | ✅ | Data with significant outliers |
| Decimal | < 1 | $v' = v / 10^j$ (j = digits in max) | ❌ | Simple magnitude reduction |

**Worked Example — Min-Max Scaling:**
Scores = [20, 40, 60, 80, 100]. Min = 20, Max = 100.
- 20 → $(20−20)/(100−20) = 0.0$
- 40 → $(40−20)/(100−20) = 0.25$
- 60 → $0.5$, 80 → $0.75$, 100 → $1.0$

**Worked Example — Z-score Standardization:**
Marks = [40, 50, 60]. Mean = 50, Std = 10.
- 40 → $(40−50)/10 = -1$
- 50 → $(50−50)/10 = 0$
- 60 → $(60−50)/10 = 1$
→ Data becomes centered at 0 with equal spread.

**Best Practice Workflow:** Understand data distribution → Choose scaling method → Apply before modeling.
- *"Choose scaling based on data and task."*
