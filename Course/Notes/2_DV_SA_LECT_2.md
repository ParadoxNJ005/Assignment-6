# Lecture 2: Exploratory Data Analytics (EDA) & Descriptive Statistics

## The Big Picture of Statistics
EDA sits within a broader 4-step statistical process:
1. **Producing Data** — Choosing a sample from the population and collecting data.
2. **Exploratory Data Analysis (EDA)** — Summarizing and visualizing the collected data *(Descriptive Statistics)*.
3. **Probability** — Building probability models.
4. **Inference** — Drawing conclusions about the entire population based on sample data.

## What is Exploratory Data Analysis (EDA)?
An approach for summarizing, visualizing, and becoming familiar with the important characteristics of a dataset. It is an iterative process with no strict structure.

**Objectives of EDA:**
- Discover Patterns
- Spot Anomalies
- Frame Hypotheses
- Check Assumptions

*EDA vs Confirmatory Data Analysis (CDA):* EDA is like detective work (gathering evidence), while CDA is like a court trial (evaluating evidence).

**EDA can help answer:** What data types am I dealing with? What is a typical value? What uncertainty surrounds this estimate? What variation/covariation occurs within/between variables? Are there outliers?

## A Typical EDA Process (8 Steps)
*(Important for End Sem Q2a)*
- **Step 1: Look at the structure of the data:** Number of data points, number of features, feature names, and data types.
- **Step 2: Check for consistency** across datasets when dealing with multiple data sources.
- **Step 3:** Identify what data signifies (measures).
- **Step 4: Calculate key metrics (Summary Analysis):**
  - Measures of central tendency (Mean, Median, Mode)
  - Measures of dispersion/variability (Range, Quartile Deviation, Mean Deviation, Standard Deviation)
  - Measures of skewness and kurtosis
- **Step 5: Investigate visuals:** Histogram for each variable, Scatterplot to correlate variables. *(Addresses End Sem Q2c for continuous variables)*
- **Step 6:** Calculate metrics and visuals per category for categorical variables.
- **Step 7:** Identify and handle outliers.
- **Step 8:** Estimate missing points using data imputation techniques.

## EDA Methods
EDA is majorly performed using these methods:
1. **Descriptive Statistics** — Summarize data features (central tendency, variability, shape).
2. **Univariate Analysis** — Analyze one variable at a time (histograms, box plots).
3. **Bivariate Analysis** — Explore relationships between two variables (scatter plots, correlation).
4. **Multivariate Analysis** — Analyze three or more variables simultaneously.
5. **Dimensionality Reduction** — Techniques like PCA to reduce number of features while preserving information.

## Data Types Used in EDA
1. **Nominal:** Qualitative, unordered categories (e.g., Religious Preference, Type of chocolate). No mathematical operations except equality.
2. **Ordinal:** Categorical but with an inherent order or rank (e.g., Low/Medium/High, Levels of agreement). Differences between ranks are not consistent.
3. **Interval:** Numerical data where differences are meaningful but there is **no true zero** (e.g., Temperature in Celsius/Fahrenheit). You can Add and Subtract.
4. **Ratio:** Numerical data with a clear definition of 0.0 (e.g., Weight, Age).

## Descriptive Statistics
*(Important for End Sem Q1)*
They provide simple summaries about the sample and measures. Three main types:
1. **Distribution**: Frequency of each value.
2. **Central Tendency**: Averages of the values.
3. **Variability / Dispersion**: How spread out the values are.

### Measures of Central Tendency
*(Important for End Sem Q2b)*
- **Mean**: Arithmetic average. Only for interval/ratio data. Sensitive to outliers.
- **Median**: Middle value when ordered. Used for ordinal, interval, ratio data. **Best for skewed distributions** as it is unaffected by extreme outliers.
  - Odd set: $(n+1)/2$ position.
  - Even set: Average of $n/2$ and $(n/2)+1$ positions.
- **Mode**: Most frequent value. Meaningful for nominal/ordinal data.

*When to use which?* 
- Nominal -> Mode
- Ordinal -> Mode, Median
- Interval/Ratio -> Mode, Median, Mean

### Measures of Variability
Reveals consistency and reliability. Two datasets can have the same mean but vastly different spreads.
- **Range**: Max - Min.
- **Variance**: Average of squared deviations from the mean.
- **Standard Deviation**: Square root of variance; average distance from mean.
- **Skewness**: Degree of asymmetry.
- **Kurtosis**: Measure of peakedness or tail heaviness.

### Skewness
*(Important for End Sem Q1 MCQ)*
- **Normal Distribution**: Symmetrical. Mean = Median = Mode. Skewness = 0.
- **Positively Skewed (Right Skewed)**: Long tail on the right. Clustered lower scores. **Mode < Median < Mean**.
- **Negatively Skewed (Left Skewed)**: Long tail on the left. Clustered higher scores. **Mean < Median < Mode**.
- *Pearson’s Coefficient of Skewness*: $3 \times (\text{Mean} - \text{Median}) / \text{Standard Deviation}$

### Kurtosis
*(Important for End Sem Q1 MCQ)*
- **Mesokurtic**: Kurtosis is zero. Normal distribution-like.
- **Leptokurtic**: Heavy tail (**outliers present**). More peaked than normal.
- **Platykurtic**: Light tail (**no outliers**). Flatter than normal.
