# 7. Visual Analytics & Feature Engineering

## What is Visual Analytics?
- **Definition**: Combining automatic and visual analysis methods with human interaction to gain knowledge from data through continuous refinement and verification.
- Forms a tight coupling between human interaction and computational methods for deeper insights.
- It is an **iterative process** (Continuous cycle of analysis, visualization, and refinement leading to better results and knowledge discovery).

## The Visual Analytics Process
1. **Step 1: Data Transformation**: Preprocessing and transforming heterogeneous data sources.
   - **Data Cleaning**: Remove inconsistencies and errors.
   - **Normalization**: Standardize data formats and scales.
   - **Integration**: Combine data into unified representations.
2. **Analysis Pathways** (The Power of Alternation):
   - **The Automatic Analysis Path**: Apply data mining methods > Model Evaluation via visualization > Parameter Tuning.
   - **The Visual Exploration Path**: Interactive visual exploration > Hypothesis Generation > Automated Confirmation.
3. **Benefits of Alternating Methods**:
   - Continuous Refinement (better results).
   - Error Detection (misleading results discovered early).
   - Higher Confidence (verification through multiple methods increases trust).
4. **Human Interaction**: The key component. Allows parameter control and algorithm selection based on visual feedback.

### Knowledge Sources in Visual Analytics
Knowledge emerges from three complementary sources:
1. **Visualization** — Direct insights from visual data representations.
2. **Automatic Analysis** — Computational models and algorithmic discoveries.
3. **Human Interactions** — Knowledge gained from the interplay between methods and human insight.

## Data Types in Big Data Applications
Real-world datasets extend beyond basic tables (e.g., Time series, Geospatial, Sensor, Video, Scientific measurements). Three major complex typologies highlighted:
1. **Network**: Models relationships (General graphs, cycles allowed, multiple paths, no root required).
2. **Tree**: Models hierarchies (Special graphs, no cycles, single paths, one root required).
3. **Spatial**: Models fields where every position in space has a value (e.g., Grid grids mapping `f(x, y) -> value`).

## Data Analytics Actions & Targets
- Discover distribution
- Compare trends
- Locate outliers
- Browse topology

## Feature Engineering
- **Definition**: The pre-processing step of machine learning used to transform raw data into features (measurable properties/attributes) for predictive modeling.
- **Goal**: Select/create the most useful predictor variables to improve model accuracy and performance.

### Four Main Processes:
1. **Feature Creation**: Deriving new features from existing ones via mathematical operations (addition, ratios, aggregations, etc.). Requires human creativity.
2. **Transformation**: Adjusting predictor variables to ensure they are on the same scale and within acceptable computational ranges.
3. **Feature Extraction**: Automated process to generate new variables and reduce data volume (e.g., PCA, cluster analysis, text analytics).
4. **Feature Selection**: Selecting the most relevant subset of original features by removing redundant, irrelevant, or noisy data (reduces overfitting).

### Specific Feature Engineering Techniques
1. **Imputation**: Handling missing values without deleting entire rows.
   - *Categorical Imputation*: Replace missing categorical values with the mode (most common value).
   - *Numerical Imputation*: Replace missing numerical values with the mean or median.
2. **Discretization (Binning)**: Grouping sets of values in a logical fashion into bins/buckets (applies to both numerical and categorical values).
3. **Categorical Encoding**: Converting categorical features into algorithms-readable numerical values.
   - *Integer Encoding (Label Encoding)*: Categories replaced by digits $from \ 1 \ to \ n$. Used when an **ordinal relationship** exists.
   - *One-Hot Encoding (OHE)*: Used when **no ordinal relationship** exists. Creates a new binary dummy/indicator variable for each unique category (e.g., `color` becomes `color_red`, `color_blue`, `color_green` with boolean 0/1 values).
4. **Feature Splitting**: Separating features into two or more parts (e.g., splitting a Sale Date or Timestamp into year, month, day, hour).
