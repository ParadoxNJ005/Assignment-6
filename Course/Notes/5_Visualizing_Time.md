# 5. Visualizing Changes over Time

## 1. Line Chart
- **Properties**: Data values connected by lines to show values over a continuous period, tracking trends and patterns.
- **Rule of Thumb Exemption - The Zero Baseline**: Unlike bar charts, the vertical axis of a line chart **does not necessarily need to start at zero**.
  - Trying to start at zero for data with minimal percentage variations (e.g., GDP changes) flattens the curve and hides important shifts.
  - However, you should **clear delineate the zero baseline** if the data crosses from positive to negative values.
- **Line Width Illusion**: We tend to misestimate the differences between two curves. We assess the distance between curves at their closest point rather than the vertical distance. Plotting the gap directly (e.g., Trade Balance = Exports - Imports) is often a better choice.
- **Missing Data**: Never ignore missing values to make it appear as a continuous series. Use visual signals (like dashed lines or dots) to indicate missing segments.
- **Preattentive Attributes**: Color and line width are preattentive attributes — our eyes are drawn to thicker/colored lines before thin gray ones. Use the **"Start with Gray"** strategy to highlight key series.
- **Data Markers**: Include markers to flag specific values of interest. Use them sparingly to avoid clutter.
- **Area Between Curves**: The gap between two line series encodes important information (e.g., Trade Balance = Imports - Exports). Plotting the gap as a separate line chart can reveal patterns hidden by the line-width illusion.

## 2. Avoid Dual Axis Line Charts
- **Disadvantages**:
  - Hard to read (which line corresponds to which axis?).
  - Gridlines often don't match up.
  - The intersection point point becomes a focal point even if it has no real meaning.
  - **Manipulation Risk**: By arbitrarily choosing the axis range, the creator can force lines to cross anywhere, creating spurious correlations to mislead readers.
- **Alternative**: Use two **side-by-side charts** (small multiples) or vertically arrange them.

## 3. Circular Line Chart
- **Properties**: Line chart plotted on a polar coordinate system (radial). 
- **Use Case**: Used to improve a visual metaphor (e.g., cyclical seasons, time of day).
- **Disadvantages**: Less perceptually accurate than a standard line chart.

## 4. Slope Chart
- **Properties**: A simplified line chart connecting two (or few) points in time.
- **Use Case**: When it is not necessary to show all data points in a time series, but rather the overall change between a start and end point.
- **Styling**: Excellent for the **"Start with Gray"** strategy to highlight one or two key relationships out of many.

## 5. Sparklines
- **Properties**: "Small, intense, simple, word-sized graphics with typographic resolution" (Edward Tufte).
- **Use Case**: Typically used embedded in data-rich tables (e.g., at the end of a row) to track general patterns/trends rather than finding specific values.

## 6. Bump Chart
- **Properties**: A variation of the line chart used for plotting **changes in ranks over time**.
- **Use Case**: Useful when data has massive outliers and you want to abstract from large differences in magnitude to just show relative positions (1st, 2nd, 3rd...).
- **Trade-off vs Line Chart**: Can't see magnitude differences, but can easily trace ranking changes without lines getting tangled in a clump.
- **Ribbon Effect**: Width of the ribbons can be scaled according to actual data values, bringing magnitude back into the bump chart.

## 7. Cycle Chart
- **Properties**: Compares small units of time (weeks/months) across a multi-year timeframe.
- **Use Case**: Commonly used to display strong **seasonal trends** (e.g., number of births peaking in summer months across a decade). Splits a dense time-series chart into a more readable format.

## 8. Area Charts & Stacked Area Charts
- **Area Chart**: A line graph with the area below the line filled in. Gives the series visual weight. Because of the area, the vertical axis *should* start at zero.
- **Stacked Area Chart**: Shows multiple series summing to a total/percentage.
  - **Disadvantages**:
    1. Line-width illusion.
    2. Only the bottom series sits on a flat horizontal axis; it is extremely hard to accurately compare the volume of floating upper series.
    3. Ordering matters significantly. Reordering the series completely changes where the reader's attention goes.

## 9. Streamgraph
- **Properties**: Stacks data series like an area chart, but the central horizontal axis handles positive variations on both sides, creating a flowing, organic shape.
- **Use Case**: Best for time series where the series themselves have **high volatility** (peaks and troughs). Minimizes the baseline distortion seen in standard stacked area charts. High aesthetic/engagement value, though potentially hard to read for specific values.

## 10. Horizon Chart
- **Properties**: An area chart sliced into horizontal intervals and collapsed into single bands, similar to a heatmap. Darker colors denote higher values.
- **Use Case**: Condensing a dense dataset into a compact space. Makes it easy to spot general trends and extreme values without taking up vertical real estate.

## 11. Gantt Chart
- **Properties**: Horizontal bars showing the start, duration, and end of events.
- **Use Case**: Schedule-tracking (e.g., tracking production schedules, project management, employee shifts). Invented by Henry Laurence Gantt.

## 12. Flow Charts and Timelines
- **Timeline**: Flags dates/events over a chronological sequence.
- **Flow Chart**: Maps a process step-by-step. Does not necessarily map to strict continuous time, but maps chronological or logical sequences.

## 13. Connected Scatterplot
- **Properties**: Projects two variables along horizontal and vertical axes (like a scatterplot) but connects the points chronologically with a line. 
- **Use Case**: Bringing two time series together without using a dual-axis chart. Allows readers to see the relationship/trajectory of two variables over time simultaneously (e.g., Life Expectancy vs Economic Growth through the decades).
- **Tip**: Can use raw values (absolute comparison) or percent growth (relative comparison) — each reveals different patterns.

---

## Key Takeaways for Time Visualizations
- Line and bar charts sit **near the top of the perceptual ranking scale** for time data.
- Always consider whether to show raw values, percentages, ranks, or growth rates — each tells a different story.
- **Small multiples** and the **"Start with Gray"** strategy are powerful techniques across all time charts.
