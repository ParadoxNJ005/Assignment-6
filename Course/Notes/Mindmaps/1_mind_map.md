# Data Visualization - Mind Map (Lecture 1)

```
                        DATA VISUALIZATION
                               |
                ________________|________________
               |                |                |
          DEFINITION        COMPONENTS      HISTORY
               |                |                |
         - Process of      1. Data           - Prehistoric
           describing     2. Visual             (Cave paintings)
           information      Elements         - 366-335 BC
           through visual 3. Techniques        (Roman Maps)
           rendering      4. Interactivity   - 17th Century
         - Visual info    5. Color/Design      (Van Langren - Line graph)
           processed      6. Context/         - 18th Century
           60,000x          Annotations        (Playfair - Bar/Line/Pie)
           faster than    7. Tools/           - 1850s
           text             Platforms          (Nightingale - Coxcomb)
         - Pattern         8. Data             - 19th Century
           recognition      Preparation        (John Snow - Dot maps)
           in 13ms        9. Exploration      - Information Age
         - Bridge gap     10. Dashboarding     (BI, AI-driven)
           between raw
           data & insight
```

---

## MAIN BRANCHES

### 1. DEFINITION & PURPOSE
```
Definition
├── Visual rendering of information
├── Transform complex datasets into clear narratives
├── Bridge raw numbers to actionable insights
│
Power of Visualization
├── Visual processing: 60,000x faster than text
├── Brain processes images in ~13 milliseconds
├── Enables instantaneous pattern recognition
└── Outlier detection at a glance
```

### 2. 10 COMPONENTS FRAMEWORK
```
10 Components of Effective Visualization
│
├── 1. DATA
│   └── Numerical, text, or geospatial
│
├── 2. VISUAL ELEMENTS
│   └── Graphics, charts, overlays, diagrams, maps, tables
│
├── 3. VISUALIZATION TECHNIQUES
│   └── Transforming, scaling data, selecting chart type
│
├── 4. INTERACTIVITY
│   └── Zooming, hovering (tooltips), rotating, filtering
│
├── 5. COLOR PALETTE & DESIGN
│   └── Font, positioning, styling for usability & aesthetics
│
├── 6. CONTEXT & ANNOTATIONS
│   └── Titles, subtitles, captions, legends
│
├── 7. TOOLS & PLATFORMS
│   └── Tableau, Power BI, D3.js, Matplotlib, Seaborn
│
├── 8. DATA PREPARATION
│   └── Cleaning, processing, aggregating, reshaping
│
├── 9. DATA EXPLORATION
│   └── Patterns, trends, noise, correlations
│
└── 10. DASHBOARDING
    └── Multi-view displays for monitoring KPIs
```

### 3. HISTORY TIMELINE
```
Historical Evolution
│
├── PREHISTORIC
│   └── Lascaux cave paintings (hunting, storytelling)
│
├── 366-335 BC
│   └── Roman maps (schematic, connectivity-focused, not geographic)
│
├── 17th CENTURY
│   └── Michael Florent Van Langren
│       └── First known line graph (showing longitude uncertainty)
│
├── 18th CENTURY
│   └── William Playfair
│       ├── Bar charts
│       ├── Line charts
│       └── Pie charts (economic data over time)
│
├── 1850s
│   └── Florence Nightingale
│       └── Coxcomb/Rose chart (military death prevention)
│
├── 19th CENTURY
│   └── John Snow
│       └── Dot maps (cholera source tracing)
│
└── INFORMATION AGE
    ├── Computers & GUIs
    ├── BI Dashboards
    ├── Interactivity
    └── Future: AI-driven analytics, multimodal views
```

### 4. VISUAL MAPPING ELEMENTS
```
Visual Elements & Encoding
│
├── LINE
│   ├── Defines boundaries & connections
│   └── Use horizontal gridlines; avoid heavy lines
│
├── SHAPE (MARKS)
│   ├── Bars → Compare categories (length = most accurate)
│   ├── Lines → Show trends over time
│   └── Scatter/Points → Explore relationships & outliers
│
├── COLOR
│   ├── Hue → Categorical identity (max 6-8)
│   ├── Saturation → Emphasis & attention
│   ├── Lightness/Value → Ordered magnitude
│   └── Avoid: Rainbow gradients, red/green combos
│
├── SIZE & SCALE
│   ├── Bars start at zero (length = magnitude)
│   └── Bubbles scaled by area (not radius)
│
├── WHITE SPACE
│   ├── Improves legibility
│   ├── Groups items
│   └── Creates rhythm
│
├── TEXTURE & PATTERN
│   ├── Differentiates without color
│   ├── Good for grayscale/colorblindness
│   └── Keep simple & low-frequency
│
├── VALUE & CONTRAST
│   ├── High (data/focus)
│   ├── Medium (context)
│   └── Low (background/grids)
│
├── FORM & DEPTH
│   ├── Foreground: labels/callouts
│   ├── Midground: data
│   ├── Background: grids/shading
│   └── Avoid: 3D distortion
│
└── MOTION
    ├── Strategic animation (200-500ms)
    ├── Explain change over time
    └── Don't distract
```

### 5. GESTALT THEORY & VISUAL HIERARCHY
```
Gestalt Principles
"The whole is greater than the sum of its parts"
│
├── PROXIMITY
│   └── Objects close together = perceived as group
│
├── SIMILARITY
│   └── Shared visual properties (color, shape) = grouped
│
├── CONTINUITY
│   └── Eye prefers smooth, continuous lines
│
├── CLOSURE
│   └── Mentally fill in missing parts of shapes
│
├── FIGURE & GROUND
│   └── Separate main object from background
│
└── COMMON FATE
    └── Objects moving together = related (animation)
```

### 6. DESIGN METHODOLOGY
```
Basic Framework for Visualization Design
│
└── 7 Steps
    ├── 1. IDENTIFY PURPOSE
    │   └── Intended use of visualization
    │
    ├── 2. CONSIDER AUDIENCE
    │   ├── Operational vs Strategic
    │   └── Informative vs Persuasive
    │
    ├── 3. RESEARCH
    │   ├── Available data
    │   ├── Visual elements
    │   └── Benchmark designs
    │
    ├── 4. DESIGN
    │   ├── Sketch
    │   ├── Iterate
    │   └── Collect feedback
    │
    ├── 5. EXECUTE DESIGN
    │   └── Build in Tableau, Code, etc.
    │
    ├── 6. DOCUMENT & DEPLOY
    │   └── Documentation & release
    │
    └── 7. SUSTAIN
        └── Maintain & monitor
```

### 7. ELEMENTS OF DESIGN
```
Design Principles
│
├── UNITY
│   └── Consistency in color, font, shape
│
├── HIERARCHY
│   ├── Indicate importance
│   ├── Indicate flow direction
│   └── Use size & placement
│
├── COLOR
│   └── Provide contrast & draw attention
│
├── BALANCE & ALIGNMENT
│   ├── Harmonious structure
│   └── Without distraction
│
└── GROUPING & SPACING
    ├── Visual flow
    └── Narrate a story
```

---

## SUMMARY CONNECTIONS

| Concept | Purpose | Key Takeaway |
|---------|---------|--------------|
| **What is DV?** | Define field & power | Visual > Text (60,000x faster) |
| **10 Components** | Framework for design | All elements matter for effectiveness |
| **History** | Evolution & context | DV evolved from simple to interactive |
| **Visual Mapping** | Encoding techniques | Choose right mark, color, size for data |
| **Gestalt Theory** | Cognitive principles | Brain groups & interprets visually |
| **Methodology** | Process guidance | 7-step design workflow |
| **Design Elements** | Visual principles | Consistency, hierarchy, balance matter |

---

## KEY TAKEAWAYS
1. **Visual perception is powerful** - 60,000x faster processing than text
2. **Framework matters** - 10 components ensure comprehensive visualization
3. **Choose wisely** - Mark, color, and size encode meaning
4. **Respect Gestalt principles** - Brain naturally groups similar elements
5. **Follow methodology** - Structured 7-step approach improves outcomes
6. **Design consistency** - Unity, hierarchy, and balance create effective visuals
