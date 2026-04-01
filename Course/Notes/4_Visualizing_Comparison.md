# 4. Visualizing Comparison of Data

## All 16 Comparison Charts Ranked by Perceptual Accuracy

| Rank | Chart | Primary Channel Used | Perceptual Tier | Precision |
|------|-------|---------------------|-----------------|-----------|
| 1 | **Bar Chart** | Length on common aligned baseline | ★ Position/Length (Rank 1–3) | 🟢 Highest |
| 2 | **Bullet Chart** | Length on common scale + reference lines | ★ Position/Length (Rank 1–3) | 🟢 Highest |
| 3 | **Dot Plot (Dumbbell)** | Position on common scale | ★ Position (Rank 1) | 🟢 Highest |
| 4 | **Waterfall Chart** | Length on common scale (running total) | ★ Position/Length (Rank 1–3) | 🟢 Highest |
| 5 | **Paired Bar Chart** | Length on common scale (grouped) | ★ Position/Length (Rank 1–3) | 🟢 High |
| 6 | **Diverging Bar Chart** | Length from central baseline | ★ Length (Rank 2–3) | 🟢 High |
| 7 | **Unit / Isotype Chart** | Counting discrete marks (position) | ★ Position/Count (Rank 1–3) | 🟢 High |
| 8 | **Waffle Chart** | Counting filled cells in grid (area-ish) | ★–◆ Position/Area (Rank 3–5) | 🟡 Medium-High |
| 9 | **Stacked Bar Chart** | Length (only bottom series aligned) | ◆ Unaligned Length (Rank 2–3) | 🟡 Medium |
| 10 | **Sankey Diagram** | Width of flows (length/area) | ◆ Length/Width (Rank 3–4) | 🟡 Medium |
| 11 | **Marimekko Chart** | Height + Width (two lengths → area) | ◆ Area (Rank 5) | 🟡 Medium |
| 12 | **Mosaic Chart** | Area (both dims = 100%) | ◆ Area (Rank 5) | 🟡 Medium |
| 13 | **Bubble Comparison** | Circle area | ◇ Area (Rank 5) | 🔴 Low |
| 14 | **Heatmap** | Color saturation / luminance | ◇ Color (Rank 6) | 🔴 Low (pattern-rich) |
| 15 | **Gauge Chart** | Angle (speedometer needle) | ◇ Angle (Rank 4) | 🔴 Low |
| 16 | **Radial / Circular Bar** | Distorted length on curved axis | ◇ Distorted (off-scale) | 🔴 Lowest |

> **Reading the table**: Charts at the top (🟢) allow the most accurate value comparisons. Charts at the bottom (🔴) are better for patterns/engagement but poor for extracting exact values.

### Quick Tier Summary
- **Tier 1 — Position/Length** (Ranks 1–7): Bar, Bullet, Dot Plot, Waterfall, Paired Bar, Diverging Bar, Unit/Isotype
- **Tier 2 — Unaligned Length/Area** (Ranks 8–12): Waffle, Stacked Bar, Sankey, Marimekko, Mosaic
- **Tier 3 — Area/Color/Angle** (Ranks 13–16): Bubble, Heatmap, Gauge, Radial Bar

---

## Perceptual Ranking Scale — Channel Effectiveness (Munzner)

| Rank | For **Ordered/Quantitative** Data | For **Categorical** Data |
|------|-----------------------------------|--------------------------|
| 1 (Best) | Position on common scale | Spatial region |
| 2 | Position on unaligned scale | Color hue |
| 3 | Length (aligned baselines) | Motion |
| 4 | Tilt / Angle | Shape |
| 5 | Area / Size | — |
| 6 | Color luminance / Saturation | — |
| 7 (Worst) | Volume / Curvature | — |

### Key Principles
- **Expressiveness**: Match channel type to data type (magnitude channels for ordered data, identity channels for categorical data).
- **Effectiveness**: Some channels are more accurately perceived than others — spatial position is the most effective for both ordered and categorical data.
- **Redundant encoding**: Using multiple channels (e.g., position + color) sends a stronger message but uses up available channels.
- **Trade-off**: Lower-ranked charts (heatmap, radial) may sacrifice precision but gain in aesthetics, engagement, or compact space usage.

---

## Chart Types for Comparison
*(Highly relevant to Mid Sem Q5: properties, advantages, disadvantages, and potential narratives)*

### 1. Bar Charts
- **Properties**: Rectangles arranged vertically (column chart) or horizontally (bar chart). Length/height represents value.
- **Narrative/Use Case**: Comparing categorical data, ranking items from highest to lowest, discovering relationships.
- **Rules / Best Practices**:
  - **Start the axis at zero**: Because we perceive value by length, starting off-zero distorts perception.
  - **Don't break the bar**: Cropping bars with squiggly lines distorts relative values. Use "zoom in/out" multiple graphs instead.
  - **Use gridlines/tick marks judiciously**: White space separates bars well enough. No need for ticks between bars.
  - **Rotate long axis labels**: If horizontal labels are too long, flip the chart into a horizontal bar chart rather than tilting the text.

### 2. Radial / Circular Bar Chart
- **Properties**: Bars radiating outward from the center of a circle.
- **Advantages**: Fits more values in a compact space; good for cyclical/frequent changes.
- **Disadvantages**: Harder to compare heights around a circle. Distorts perception (outer lanes appear longer even if values are equal).
- **Recommendation**: Often best to avoid due to perceptual distortion.

### 3. Paired Bar Chart (Grouped Bar Chart)
- **Properties**: Multiple bars grouped together for each category.
- **Narrative**: Comparing values across AND within categories (e.g., comparing male/female populations within different countries).
- **Disadvantages**: Can become cluttered. Hard to discern if the main comparison is between or within categories if there are too many bars.

### 4. Stacked Bar Chart
- **Properties**: Bars sub-divided into segments. Segments can sum to actual totals, or be normalized to 100%.
- **Narrative**: Showing how different categories sum to a total, or the distribution within a category.
- **Disadvantages**: Interior segments are hard to compare because they don't sit on a shared baseline.
- **Alternative**: Small multiples (breaking the stacks apart into separate graphs).

### 5. Diverging Bar Chart
- **Properties**: Stacks diverge from a central baseline in opposite directions.
- **Narrative**: Excellent for **Likert Scale** survey responses (e.g., Strongly Disagree to Strongly Agree).
- **Tip**: Place the "Neutral" category off to the side rather than splitting it on the center line, as neutral shouldn't mathematically align with agree or disagree sentiments.

### 6. Dot Plot (Dumbbell Chart / Gap Chart)
- **Properties**: Circles corresponding to data values connected by a line or arrow.
- **Advantages**: Uses less ink than bars (reducing clutter). Great for showing differences/ranges between two points (e.g., test scores in 2015 vs 2020).
- **Disadvantages**: Being a summary chart, it hides intermediate variations. If data fluctuated wildly between points, a dot plot masks it.

### 7. Marimekko Chart
- **Properties**: A column chart where the **width** of each column is also scaled according to another variable.
- **Narrative**: Adding a second variable to a standard column chart. 
- **Advantage**: Shows the relationship between two variables simultaneously.

### 8. Mosaic Chart
- **Properties**: A variation of Marimekko where both heights and widths sum to 100%, filling the entire graph space.
- **Narrative**: Part-to-whole perspective along both dimensions.

### 9. Unit Charts & Isotype Charts
- **Unit Chart**: Shows counts of a variable using basic symbols (e.g., 1 square = 10 cars).
- **Isotype Chart**: A subclass of unit charts that uses **icons or images** instead of simple shapes. (Pioneered by Otto Neurath in the 1920s).
- **Caution**: If scaling icons by size, ensure scaling is consistent (area vs height). Scaling just by height disproportionately increases area, misleading the viewer.

### 10. Waffle Chart
- **Properties**: A 10x10 grid (unit chart) where each colored cell represents 1 percentage point.
- **Narrative**: Very effective for part-to-whole relationships and comparing percentages across categories.

### 11. Heatmap
- **Properties**: A table with color-coded cells (color saturation represents data values).
- **Narrative**: Visualizing high-frequency data (like calendar days) or showing general patterns where exact values are less important. Easy to see concentrations (e.g., more fatalities on Fridays).

### 12. Gauge Chart
- **Properties**: Looks like a speedometer (semi-circle with a needle pointing to a range).
- **Narrative**: Showing targets or progress toward a goal (financial planning, fundraising).
- **Disadvantages**: Humans are bad at comparing angles. Not good for discerning exact specific values.

### 13. Bullet Chart
- **Properties**: Created by Stephen Few as a linear, compact alternative to the gauge chart. Contains:
  1. Actual value (bar)
  2. Target value (vertical line)
  3. Background ranges (bands of success: poor, good, excellent).
- **Advantages**: Highly space-efficient and perceptually accurate.

### 14. Bubble Comparison & Nested Bubbles
- **Basic Bubble**: Circles size represents value. Humans are bad at accurately comparing circle areas. Cannot visualize negative values.
- **Nested Bubble**: Layering circles on top of each other. Can mask circles in the back but makes certain comparisons easier.

### 15. Sankey Diagram
- **Properties**: Arrows/lines display transitions from one state to another. Width of lines denotes magnitude of flow.
- **Narrative**: Showing flow, mapping out processes, or comparing categories as they split into sub-categories over time.
- **Disadvantages**: Plotting too many series makes it "spaghetti-like" and impossible to read.

### 16. Waterfall Chart
- **Properties**: A bar chart where each subsequent bar starts where the previous left off. 
- **Narrative**: Visualizing a mathematical equation: adding/subtracting values from an initial value to reach a final amount. (Often used in financial statements: Revenue - Expenses = Profit). Negative/positive values use different colors.
