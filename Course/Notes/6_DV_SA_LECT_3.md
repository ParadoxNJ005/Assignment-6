# 6. Exploratory Data Analytics (EDA)
> **Note**: DV_SA_LECT_3 covers the same material as LECT_2. This note is a complementary summary. See also `2_DV_SA_LECT_2.md` for additional details.

## The Big Picture of Statistics
1. **Producing Data**: Choosing a sample and collecting data.
2. **Exploratory Data Analysis (EDA)** *(Descriptive Statistics)*: Summarizing collected data.
3. & 4. **Probability & Inference**: Drawing conclusions about the population.

## What is EDA?
- An approach for summarizing, visualizing, and becoming familiar with the important characteristics of a dataset.
- It is an **iterative process** (no real structured way).
- **Objectives:**
  - Discover Patterns
  - Spot Anomalies
  - Frame Hypothesis
  - Check Assumptions

## A Typical EDA Process
1. Look at data structure (size, features, data types).
2. Check consistency across multiple data sources.
3. Identify what data signifies (measures).
4. **Summary Analysis (Key Metrics)**:
   - Measures of Central Tendency: Mean, Median, Mode
   - Measures of Dispersion/Variability: Range, Quartiles, Mean Deviation, Std Dev.
   - Measures of Shape: Skewness, Kurtosis.
5. **Visualizations**: Histograms (distribution), Scatterplots (correlation).
6. Calculate metrics per category for categorical variables.
7. Identify and handle Outliers.
8. Estimate missing points (Imputation).

## EDA Methods
1. **Descriptive Statistics** — Summarize features (central tendency, spread, shape).
2. **Univariate Analysis** — One variable at a time.
3. **Bivariate Analysis** — Two-variable relationships.
4. **Multivariate Analysis** — Three or more variables.
5. **Dimensionality Reduction** — Techniques like PCA.

## Confirmatory vs Exploratory Analysis
- **Confirmatory Data Analysis (CDA)**: Like a court trial. It is the process of evaluating evidence (e.g., Clinical Trials).
- **Exploratory Data Analysis (EDA)**: Like detective work. Gathering evidence. (Tukey: exploratory and confirmatory analysis should proceed side by side).

## Data Types Used in EDA
1. **Nominal**: Qualitative, categorical data with no inherent order (e.g., Religion, Type of Chocolate). Cannot perform mathematical operations except equality.
2. **Ordinal**: Categorical data with inherent order/rank (e.g., Income Levels, Agreement scales). Difference between ranks is not measurable.
3. **Interval**: Numerical/Quantitative data. Order matters, and intervals (differences) are equal and meaningful. (e.g., Temperature, Credit Scores). **Drawback**: No natural/absolute zero.
4. **Ratio**: Numerical data with all properties of Interval, AND a clear, meaningful **absolute zero**.

### Data Types — Allowed Operations Summary
| Level | Equality | Order | Addition/Subtraction | Multiplication/Division | True Zero |
|-------|----------|-------|---------------------|------------------------|----------|
| Nominal | ✅ | ❌ | ❌ | ❌ | ❌ |
| Ordinal | ✅ | ✅ | ❌ | ❌ | ❌ |
| Interval | ✅ | ✅ | ✅ | ❌ | ❌ |
| Ratio | ✅ | ✅ | ✅ | ✅ | ✅ |

## Descriptive Statistics
- Used to describe the basic features of the data. 
- Three main types:
  1. **Distribution**: Frequency of each value (Normal vs Skewed).
  2. **Central Tendency**: Averages of the values (Mean, Median, Mode).
  3. **Variability/Dispersion**: How spread out the values are (Range, Variance, Standard Deviation, Skewness, Kurtosis).

### 1. Central Tendency
- **Mean**: Arithmetic average (Use for Interval and Ratio data).
- **Median**: Middle value in an ordered dataset (Best for ordinal or skewed data).
- **Mode**: Most frequently occurring value (Best for nominal/categorical data).

### 2. Variability
- **Range**: Difference between Maximum and Minimum.
- **Variance**: Average of squared deviations from the mean.
- **Standard Deviation**: Square root of variance; average distance of points from the mean.
- **Why it matters**: Two datasets can have the same mean but totally different behavior based on spread (e.g., Class A scores are tightly clustered around 75, Class B scores range from 50 to 100).

### 3. Distribution & Shape (Skewness & Kurtosis)
- **Normal Distribution**: Symmetrical. Mean = Median = Mode. Skewness = 0.
- **Positive Skew (Right-skewed)**: Long tail on the right. Mode < Median < Mean.
- **Negative Skew (Left-skewed)**: Long tail on the left. Mean < Median < Mode.
- **Skewness Coefficient (Pearson)**: $3 \times (Mean - Median) / Standard Deviation$.
- **Kurtosis**: Measures if data is heavy-tailed (outliers) or light-tailed vs Normal distribution.
  - **Mesokurtic**: Kurtosis = 0 (Normal distribution shape).
  - **Leptokurtic**: Heavy tail. Kurtosis > 0. Outliers are present (e.g., Stock returns).
  - **Platykurtic**: Light tail. Kurtosis < 0. Values are flatly distributed. No outliers.

### When to Use Mean, Median, or Mode?
| Data Level | Applicable Measures |
|-----------|--------------------|
| Nominal | Mode |
| Ordinal | Mode, Median |
| Interval / Ratio | Mode, Median, Mean |

- For **normal distributions** → all three give the same answer.
- For **skewed distributions** → **median is best** (unaffected by extreme outliers).
