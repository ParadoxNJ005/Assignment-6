# Lecture 1: Introduction to Data Visualization

## What is Data Visualization?
- The process of describing information through visual rendering.
- **Power of Visual Perception**: Our brains process visual information 60,000 times faster than text. The human brain can process entire images in as little as 13 milliseconds. Visualizations make pattern recognition and outlier detection instantaneous compared to staring at raw spreadsheets.
- **Goal**: Transform complex datasets into clear, compelling visual narratives that drive understanding and informed decision-making. Bridge the gap between raw numbers and actionable insights.

## Main Components of Data Visualization (Essential Framework)
*(Important for Mid Sem Q1)*
An effective data visualization framework consists of these 10 components:
1. **Data**: Numerical, text, or geospatial.
2. **Visual Elements**: Graphics, charts, overlays, diagrams, maps, tables.
3. **Visualization Techniques**: Transforming, scaling data, and selecting the right chart type.
4. **Interactivity**: Zooming, hovering (tooltips), rotating, filtering categories.
5. **Color Palette and Design**: Font selection, element positioning, styling for usability and aesthetics.
6. **Context and Annotations**: Titles, subtitles, captions, legends.
7. **Tools and Platforms**: Software like Tableau, Power BI, Python libraries (D3.js, Matplotlib, Seaborn).
8. **Data Preparation**: Cleaning, processing, aggregating, reshaping.
9. **Data Exploration**: Searching for patterns, trends, noise, and correlations.
10. **Dashboarding**: Aggregate displays combining multiple views for monitoring KPIs.

## History of Data Visualization
- **Pre-historic**: Lascaux cave paintings (hunting guidance, storytelling).
- **366-335 BC (Roman Maps)**: Early schematic network maps (like modern subway maps) focusing on connectivity for military and trade, not geography.
- **17th Century (Michael Florent Van Langren)**: Created the **first known line graph** showing variations in longitude estimates, making uncertainty visible.
- **18th Century (William Playfair)**: Introduced **Bar charts, Line charts, and Pie charts** to show economic data over time.
- **1850s (Florence Nightingale)**: Used the **"Coxcomb" / Rose chart** to visualize preventable military deaths, driving sanitary reform.
- **19th Century (John Snow)**: Used dot map plotting cholera cases in London to trace the source to the Broad Street pump.
- **Information Age**: Computers, GUIs, BI Dashboards, interactivity. Future: AI-driven analytics, multimodal views.

## Visual Mapping: Elements of Information Visualization
- **Line**: Defines boundaries and connections. Use horizontal gridlines and avoid heavy lines.
- **Shape (Marks)**: 
  - *Bars* (compare categories - length is most accurate)
  - *Lines* (show trends over time)
  - *Scatter/Points* (explore relationships and outliers).
- **Colours**: 
  - *Hue* (categorical identity, max 6-8 categories)
  - *Saturation* (emphasis and attention)
  - *Lightness/Value* (ordered magnitude). 
  - *Avoid:* Rainbow gradients, red/green combos (colorblind constraint).
- **Size and Scale**: Start bars at zero (length encodes magnitude), scale bubbles by area (not radius).
- **White Space**: Improves legibility, groups items, creates rhythm. Keep consistent margins and small multiples.
- **Texture & Pattern**: Differentiates areas without relying on colour (good for grayscale/colorblindness). Keep it low-frequency and simple.
- **Value & Contrast**: Creates visual hierarchy. High contrast (data/focus), Medium (context), Low (background/grids).
- **Form & Depth**: Meaningful layering (Foreground: labels/callouts; Midground: data; Background: grids/shading) rather than 3D distortion.
- **Motion**: Strategic animation (200-500ms transitions) to explain change over time, not to distract.

## Visual Hierarchy & Gestalt Theory
**Gestalt Theory**: "The whole is greater than the sum of its parts" (Brain sees patterns, not individual dots). We automatically group and interpret visual elements.
1. **Proximity**: Objects close to each other are seen as a group.
2. **Similarity**: Objects sharing visual properties (color, shape) are grouped.
3. **Continuity**: The eye prefers smooth, continuous lines.
4. **Closure**: Mentally filling in missing parts of incomplete shapes.
5. **Figure and Ground**: Separating main object from background.
6. **Common Fate**: Objects moving together are related (animation).

## A Basic Framework Methodology
1. **Identify Purpose** (Intended Use)
2. **Consider Audience** (Operational vs Strategic, informative vs persuasive)
3. **Research** (Available data, elements, benchmark designs)
4. **Design** (Sketch, Iterate, Collect feedback)
5. **Execute Design** (Build in tools like Tableau or Code)
6. **Document - Deploy**
7. **Sustain**

## Elements of Design
- **Unity**: Consistency in color, font, and shape.
- **Hierarchy**: Indicating importance and flow (size, placement).
- **Color**: Providing contrast and drawing attention to key points.
- **Balance & Alignment**: Harmonious structure without distraction.
- **Grouping / Spacing**: Visual flow and narrating a story.
