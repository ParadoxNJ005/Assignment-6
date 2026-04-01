# Exploratory Data Analytics (EDA) & Descriptive Statistics - Mind Map (Lecture 2)

```
                    EXPLORATORY DATA ANALYTICS (EDA)
                               |
                ________________|________________
               |                |                |
           DEFINITION       OBJECTIVES       EDA PROCESS
               |                |                |
         - Summarize       - Discover         8 Steps
         - Visualize         Patterns        Process
         - Understand      - Spot             |
           important         Anomalies      Structure
           characteristics - Frame          Consistency
         - Iterative,       Hypotheses      Signification
           no strict       - Check           Metrics
           structure        Assumptions    Visuals
                                          Category Analysis
         EDA vs CDA              |        Outliers
         - EDA = Detective     (Look  & Check framework)
         - CDA = Court trial   data
           (Evaluate)          Discover Patterns
```

---

## MAIN BRANCHES

### 1. DEFINITION & PURPOSE
```
EDA Foundation
│
├── What is EDA?
│   ├── Summarize datasets
│   ├── Visualize characteristics
│   └── Become familiar with data
│
├── Approach
│   └── Iterative process with no strict structure
│
├── EDA vs CDA Comparison
│   ├── EDA = Detective work (gathering evidence)
│   └── CDA = Court trial (evaluating evidence)
│
└── Why EDA?
    └── Understand data before formal analysis
```

### 2. OBJECTIVES OF EDA
```
Core Goals
│
├── DISCOVER PATTERNS
│   ├── Trends
│   ├── Relationships
│   └── Clustering
│
├── SPOT ANOMALIES
│   ├── Outliers
│   ├── Inconsistencies
│   └── Unusual values
│
├── FRAME HYPOTHESES
│   ├── Formulate questions
│   └── Generate research directions
│
└── CHECK ASSUMPTIONS
    ├── Validate distributions
    ├── Check normality
    └── Test independence
```

### 3. 8-STEP EDA PROCESS
```
Typical EDA Workflow
│
├── STEP 1: STRUCTURE
│   ├── Count data points
│   ├── Count features
│   ├── List feature names
│   └── Identify data types
│
├── STEP 2: CONSISTENCY
│   ├── Compare across sources
│   ├── Check for duplicates
│   └── Validate data integrity
│
├── STEP 3: SIGNIFICATION
│   └── Identify what data represents
│
├── STEP 4: KEY METRICS (SUMMARY ANALYSIS)
│   ├── Central Tendency
│   │   ├── Mean
│   │   ├── Median
│   │   └── Mode
│   └── Variability
│       ├── Range
│       ├── Quartile Deviation
│       ├── Mean Deviation
│       ├── Standard Deviation
│       ├── Skewness
│       └── Kurtosis
│
├── STEP 5: INVESTIGATE VISUALS
│   ├── Histogram (each variable)
│   └── Scatterplot (variable correlations)
│
├── STEP 6: CATEGORY ANALYSIS
│   ├── Metrics per category
│   └── Visuals per category
│       └── For categorical variables
│
├── STEP 7: OUTLIER HANDLING
│   ├── Identify outliers
│   └── Handle outliers
│
└── STEP 8: MISSING DATA
    ├── Estimate missing points
    └── Data imputation techniques
```

### 4. DATA TYPES
```
Data Type Classification
│
├── NOMINAL
│   ├── Qualitative
│   ├── Unordered categories
│   ├── Examples: Religious preference, Chocolate type
│   ├── Operations: Equality only
│   └── Statistics: Mode
│
├── ORDINAL
│   ├── Categorical with order/rank
│   ├── Examples: Low/Medium/High, Likert scale
│   ├── Property: Inconsistent differences
│   └── Statistics: Mode, Median
│
├── INTERVAL
│   ├── Numerical
│   ├── Meaningful differences
│   ├── NO TRUE ZERO
│   ├── Examples: Temperature (C/F)
│   ├── Operations: Add, Subtract
│   └── Statistics: Mode, Median, Mean
│
└── RATIO
    ├── Numerical
    ├── Clear zero definition
    ├── Examples: Weight, Age, Height
    └── Statistics: Mode, Median, Mean
```

### 5. DESCRIPTIVE STATISTICS
```
Overview & Summaries
│
├── THREE MAIN TYPES
│   │
│   ├── 1. DISTRIBUTION
│   │   └── Frequency of each value
│   │
│   ├── 2. CENTRAL TENDENCY
│   │   ├── Mean (average)
│   │   ├── Median (middle)
│   │   └── Mode (most frequent)
│   │
│   └── 3. VARIABILITY / DISPERSION
│       └── Spread of values
│
└── Purpose
    └── Provide simple summaries about sample & measures
```

### 6. MEASURES OF CENTRAL TENDENCY
```
Averages & Typical Values
│
├── MEAN (Arithmetic Average)
│   ├── Formula: Sum of values / Count
│   ├── Data types: Interval, Ratio only
│   ├── Pros: Uses all data points
│   ├── Cons: Sensitive to outliers
│   └── Use when: Normal distribution, no outliers
│
├── MEDIAN (Middle Value)
│   ├── Calculation:
│   │   ├── Odd set: position (n+1)/2
│   │   └── Even set: average of n/2 and (n/2)+1
│   ├── Data types: Ordinal, Interval, Ratio
│   ├── Pros: Unaffected by extreme outliers
│   ├── Best for: SKEWED DISTRIBUTIONS
│   └── Use when: Outliers present, skewed data
│
└── MODE (Most Frequent)
    ├── Data types: Nominal, Ordinal, Interval, Ratio
    ├── Pros: No outlier sensitivity
    ├── Cons: May not be unique
    └── Use when: Categorical data
```

### 7. CHOOSING THE RIGHT CENTRAL TENDENCY
```
Data Type → Appropriate Measures
│
├── NOMINAL
│   └── Mode ✓
│
├── ORDINAL
│   ├── Mode ✓
│   └── Median ✓
│
└── INTERVAL / RATIO
    ├── Mode ✓
    ├── Median ✓
    └── Mean ✓
```

### 8. MEASURES OF VARIABILITY
```
Spread & Consistency
│
├── RANGE
│   ├── Formula: Max - Min
│   └── Simple measure of spread
│
├── VARIANCE
│   ├── Average of squared deviations
│   └── Measures dispersion from mean
│
├── STANDARD DEVIATION
│   ├── Formula: √Variance
│   ├── Average distance from mean
│   └── Most commonly used
│
├── SKEWNESS
│   ├── Degree of asymmetry
│   └── (See detailed section)
│
└── KURTOSIS
    ├── Peakedness / Tail heaviness
    └── (See detailed section)
```

### 9. SKEWNESS DETAILS
```
Asymmetry of Distribution

SYMMETRICAL (NORMAL)
├── Shape: Bell curve
├── Mean = Median = Mode
├── Skewness = 0
└── No tail direction

POSITIVELY SKEWED (RIGHT SKEWED)
├── Shape: Long tail on RIGHT
├── Scores: Clustered lower
├── Order: Mode < Median < Mean
├── Tail pulls mean right
└── Common in: Income data

NEGATIVELY SKEWED (LEFT SKEWED)
├── Shape: Long tail on LEFT
├── Scores: Clustered higher
├── Order: Mean < Median < Mode
├── Tail pulls mean left
└── Common in: Test scores (ceiling effect)

CALCULATION
├── Pearson's Coefficient
└── = 3 × (Mean − Median) / Std Dev
```

### 10. KURTOSIS DETAILS
```
Peakedness / Tail Behavior

MESOKURTIC
├── Kurtosis = 0
├── Normal distribution-like
└── Standard peakedness

LEPTOKURTIC
├── Heavy tails
├── OUTLIERS PRESENT
├── More peaked than normal
├── Sharp peak, fat tails
└── Extreme values likely

PLATYKURTIC
├── Light tails
├── NO OUTLIERS
├── Flatter than normal
├── Broad peak, thin tails
└── Extreme values unlikely
```

---

## CRITICAL RELATIONSHIPS

### Data Type → Central Tendency Mapping
```
┌─────────────────┬──────────┬────────┬──────┐
│ Data Type       │ Mode     │ Median │ Mean │
├─────────────────┼──────────┼────────┼──────┤
│ Nominal         │ ✓        │ ✗      │ ✗    │
│ Ordinal         │ ✓        │ ✓      │ ✗    │
│ Interval/Ratio  │ ✓        │ ✓      │ ✓    │
└─────────────────┴──────────┴────────┴──────┘
```

### Distribution Shape → Appropriate Measure
```
Normal Distribution
├── Use: Mean (most accurate)
├── Mean = Median = Mode
└── No skew

Skewed Distribution
├── Use: Median (robust)
├── Outliers present
└── Mean distorted by tails

Categorical Data
├── Use: Mode (only option)
└── Non-numerical values
```

### Skewness Indicators
```
Relationship Check
│
├── If Mean > Median → RIGHT SKEWED (positive)
├── If Mean ≈ Median → NORMAL (symmetric)
└── If Mean < Median → LEFT SKEWED (negative)
```

---

## SUMMARY TABLE: DESCRIPTIVE STATISTICS AT A GLANCE

| Measure | Type | What it Shows | When to Use | Pros | Cons |
|---------|------|---------------|------------|------|------|
| **Mean** | Central Tendency | Average value | Normal dist., no outliers | Uses all data | Sensitive to outliers |
| **Median** | Central Tendency | Middle value | Skewed data, outliers | Robust | Ignores magnitudes |
| **Mode** | Central Tendency | Most common | Categorical data | Simple | May not be unique |
| **Range** | Variability | Max-Min spread | Quick overview | Easy to calculate | Only 2 data points |
| **Std Dev** | Variability | Avg distance from mean | Compare datasets | Intuitive | Units-dependent |
| **Skewness** | Shape | Asymmetry | Understand distribution | Identifies bias | Requires both mean & median |
| **Kurtosis** | Shape | Tail behavior | Detect outliers | Practical | Complex interpretation |

---

## KEY DECISION TREE: WHICH MEASURE TO USE?

```
Start with your data
│
├─ CATEGORICAL (Nominal)?
│  └─ USE MODE
│
├─ ORDINAL (Ranked)?
│  ├─ USE MODE or MEDIAN
│  └─ Avoid mean
│
└─ NUMERICAL (Interval/Ratio)?
   │
   ├─ OUTLIERS PRESENT?
   │  ├─ YES → USE MEDIAN
   │  │        CHECK SKEWNESS
   │  │        CHECK KURTOSIS (Leptokurtic)
   │  │
   │  └─ NO → USE MEAN
   │           CHECK SKEWNESS
   │           CHECK KURTOSIS
   │
   └─ SKEWED DISTRIBUTION?
      ├─ YES → USE MEDIAN (robust)
      └─ NO → USE MEAN (efficient)
```

---

## KEY TAKEAWAYS
1. **EDA is iterative** - No fixed formula, explore systematically via 8 steps
2. **Data type matters** - Determines which statistics are valid
3. **Central tendency alone is insufficient** - Must assess variability/spread too
4. **Median > Mean for skewed data** - More robust to outliers
5. **Skewness & Kurtosis diagnose distribution** - Identify outliers and asymmetry
6. **Always visualize** - Histograms & scatterplots reveal patterns missed by numbers
7. **Handle outliers & missing data** - Steps 7-8 are crucial for data quality
