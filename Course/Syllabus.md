# 📚 Data Visualisation — Syllabus Covered Till Date

> **Note:** This syllabus represents the topics covered to date, organized logically based on the course lecture materials (Lectures 1–5, Comparison, and Time).

---

## Module 1: Introduction & Fundamentals of Data Visualization
* **What is Data Visualization?** Definition, goals, and cognitive benefits (human processing vs. data).
* **The 10 Components of DV Framework:** From Data and Visual Elements to Tools and Dashboarding.
* **Visual Mapping Elements:** Use of lines, shapes, color (hue, saturation, lightness), size, white space, texture, contrast, and motion.
* **Gestalt Principles of Perception:** Proximity, Similarity, Continuity, Closure, Figure & Ground, Common Fate.
* **Elements of Design:** Unity, Hierarchy, Color, Balance & Alignment, Grouping/Spacing.
* **Historical Pioneers:** William Playfair, Florence Nightingale, John Snow, Otto Neurath, Edward Tufte, Stephen Few.

## Module 2: Exploratory Data Analytics (EDA) & Descriptive Statistics
* **EDA vs. Confirmatory Data Analysis (CDA):** Objectives, iterative processes, detective vs. court trial analogy.
* **The 8-Step EDA Process:** From structure analysis to missing point estimation.
* **Data Types (NOIR):** Nominal, Ordinal, Interval, and Ratio — definitions and allowed mathematical operations.
* **Central Tendency:** Mean, Median, Mode, and when to use which (handling normal vs. skewed distributions).
* **Variability & Dispersion:** Range, Variance, and Standard Deviation.
* **Distribution Shapes:** 
  * Normal, Positive Skew, Negative Skew.
  * Formula for Pearson's Coefficient of Skewness.
  * **Kurtosis:** Mesokurtic, Leptokurtic, Platykurtic.

## Module 3: Visualization Guidelines & Frameworks
* **The 5 Guidelines for Better Visualization:** 
  1. Show the Data
  2. Reduce Clutter
  3. Integrate Graphics & Text
  4. Avoid Spaghetti Charts (use Small Multiples)
  5. Start with Gray
* **Anscombe's Quartet:** The pitfall of relying solely on summary statistics and the necessity of visualization.
* **Form × Function Quadrants:** Static/Interactive vs. Explanatory/Exploratory visualizations.
* **Shneiderman's Mantra:** "Overview first, zoom and filter, then details-on-demand."
* **Munzner's Nested Model of Visualization Design:** 
  * 4 Levels: Domain Situation, Abstraction, Idiom, Algorithm.
  * Task Abstraction: Actions (Analyze, Search, Query) and Targets.
  * Marks (Points, Lines, Areas) vs. Channels (Position, Color, Size, Shape).

## Module 4: Perceptual Science & Chart Selection
* **The Perceptual Ranking Scale:** Munzner's channel effectiveness rankings for ordered/quantitative data (Position > Length > Angle > Area > Color).
* **Visualizing Comparison (16 Chart Types):**
  * *High Precision (Tier 1):* Bar Chart, Paired Bar, Diverging Bar, Dot Plot, Bullet Chart, Waterfall, Unit/Isotype.
  * *Medium Precision (Tier 2):* Stacked Bar, Marimekko, Waffle, Mosaic, Sankey Diagram.
  * *Low Precision / Pattern-Focused (Tier 3):* Bubble Chart, Heatmap, Radial Bar, Gauge Chart.
* **Visualizing Time (13 Chart Types):**
  * Line Chart, Sparklines, Slope Chart, Bump Chart, Cycle Chart.
  * Area Chart, Stacked Area, Streamgraph, Horizon Chart.
  * Gantt Chart, Connected Scatterplot.
  * *Critiques & Pitfalls:* Line-width illusion, avoiding Dual Axis Line Charts.

## Module 5: Visual Analytics
* **What is Visual Analytics?** The interaction between visualization, automated analysis, and human analysts.
* **The Visual Analytics Process:** Data Transformation → Automated/Visual Pathways → Refinement.
* **Knowledge Sources:** Visualization ⊕ Automatic Analysis ⊕ Human Interactions.
* **Complex Data Types:** Spatial data, Network graphs, and Tree/Hierarchical structures.

## Module 6: Data Scaling & Feature Engineering
* **Feature Engineering Pipeline:** 
  1. Feature Creation (e.g., BMI, Debt-to-Income)
  2. Feature Transformation (Scaling and Encoding)
  3. Feature Extraction (PCA)
  4. Feature Selection (Reducing noise)
* **Categorical Encoding:** One-Hot Encoding (Nominal) vs. Integer/Label Encoding (Ordinal).
* **Data Scaling / Normalization Techniques:** 
  * Absolute Max Scaling
  * Min-Max Scaling
  * Standardization (Z-score)
  * Robust Scaling (using IQR and Median)
  * Decimal Scaling
* Understand the formulas, behaviors with outliers, and best-use scenarios for each method.
