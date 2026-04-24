# DATA 271 Final Project Rubric

**Total: 100 points**

| Section | Points |
|---|---|
| Introduction | 12 |
| Libraries Required | 8 |
| Data Preparation | 22 |
| Exploratory Data Analysis | 28 |
| Summary | 18 |
| Formatting and Other Requirements | 7 |
| Works Cited | 5 |

---

## 1. Introduction — 12 points

- **1.1** Provide an introduction that explains the problem statement you are addressing.
- **1.2** Why should we be interested in this?
- **1.3** Provide a short explanation of how you plan to address this problem statement (the data used and the methodology employed).
- **1.4** Discuss your proposed approach that you think will address this problem.
- **1.5** Explain how your analysis could help the consumer of your analysis.
- **1.6** Motivate the problem with references to credible outside sources (e.g., news articles, academic papers, government reports). In-text citations must be included where claims or context draw on outside work, and all sources must appear in the Works Cited section.

---

## 2. Libraries Required — 8 points

- **2.1** All libraries used are loaded upfront so the reader knows which are required to replicate the analysis.
- **2.2** An explicit explanation is provided regarding the purpose of each library.

---

## 3. Data Preparation — 22 points

- **3.1** Original source where the data was obtained is cited and, if possible, hyperlinked.
- **3.2** Source data is thoroughly explained (i.e., what was the original purpose of the data, when was it collected, how many variables did the original have, explain any peculiarities of the source data such as how missing values are recorded, or how data was imputed, etc.). Refer to the dataset's metadata / data dictionary and use it to define any jargon, abbreviations, or coded values that appear in the feature column names (e.g., what does `HIC_ES_TOT` mean? what units is it in? what do the category codes stand for?) so a reader unfamiliar with the source can follow your analysis.
- **3.3** All data importing and cleaning steps are explained in text (markdown cells should explain *why* you are doing the data cleaning activities that you perform) and follow a logical process.
- **3.4** Once your data is clean, show what the final data set looks like. However, do not print off a data frame with 200+ rows; show the data in the most condensed form possible.
- **3.5** Provide summary statistics about the variables of concern in your cleaned data set. Provide a consolidated explanation, either with a table that provides summary information for each variable or a nicely written summary paragraph with inline code. Explain any insights gained from summary statistics.

---

## 4. Exploratory Data Analysis — 28 points

- **4.1** Uncover new information in the data that is not self-evident (i.e., do not just plot the data as it is; rather, slice and dice the data in different ways, create new variables, or join separate data frames to create new summary information).
- **4.2** Provide findings in the form of plots and tables.
- **4.3** Graphs are carefully tuned for desired purpose. Each graph should illustrate one primary point and is appropriately formatted (plot and axis titles, legend if necessary, scales are appropriate, etc.).
- **4.4** Table(s) are included to make it easy to perform important comparisons.
- **4.5** Insights obtained from the analysis are thoroughly, yet succinctly, explained. Make it easy to see and understand the interesting findings that you uncovered.
- **4.6** At least one **interactive plot** is included (e.g., built with Plotly, Bokeh, Altair, or ipywidgets) that meaningfully supports exploration of the data — for example, hover tooltips, linked views, dropdowns, or sliders that let the reader probe the data beyond what a static plot shows.

---

## 5. Summary — 18 points

- **5.1** Summarize the problem statement you addressed.
- **5.2** Summarize how you addressed this problem statement (the data used and the methodology employed).
- **5.3** Summarize the interesting insights that your analysis provided.
- **5.4** Describe any additional questions that came up during your analysis that could lead to new future projects or follow-on investigations.
- **5.5** Discuss the limitations of your analysis and how you, or someone else, could improve or build on it.

---

## 6. Formatting and Other Requirements — 7 points

- **6.1** Proper coding style is followed and code is well commented.
- **6.2** Coding is systematic — a complicated problem is broken down into subproblems that are individually much simpler. Code is efficient, correct, and minimal. Code uses appropriate data structure (list, data frames, arrays). Code checks for common errors.
- **6.3** There is approximately one markdown cell between every code cell to provide context and explanations.
- **6.4** Achievement, mastery, cleverness, creativity: Tools and techniques from the course are applied competently and, perhaps, somewhat creatively.
- **6.5** Project is posted on GitHub to start building a portfolio.

---

## 7. Works Cited — 5 points

- **7.1** A dedicated Works Cited section is included at the end of the notebook listing every outside source referenced in the project (including in the Introduction and Data Preparation sections).
- **7.2** Citations follow a consistent style (e.g., APA, MLA, or Chicago) — author, title, publisher/outlet, date, and a hyperlink/DOI where available.
- **7.3** Every source listed is cited in-text at least once; every in-text citation appears in this section.
