---
layout: notebook
title: "Data Analysis with Python - Sample Notebook"
date: 2024-12-19 17:00:00 +0000
categories: data-science python jupyter
author: iEgit
excerpt: "A sample notebook-style post demonstrating data analysis with Python, showcasing our new Jupyter notebook support."
notebook_url: "https://github.com/example/notebook.ipynb"
---

# Data Analysis with Python - Sample Notebook

This is a demonstration of our new Jupyter notebook support, showing how notebook content can be displayed in blog posts.

## Importing Libraries

<div class="cell code-cell">
<div class="cell-input">
<div class="prompt in-prompt" data-count="1"></div>
<pre><code class="language-python">import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")</code></pre>
</div>
</div>

## Loading and Exploring Data

<div class="cell code-cell">
<div class="cell-input">
<div class="prompt in-prompt" data-count="2"></div>
<pre><code class="language-python"># Create sample data
np.random.seed(42)
data = {
    'x': np.random.randn(100),
    'y': np.random.randn(100),
    'category': np.random.choice(['A', 'B', 'C'], 100)
}
df = pd.DataFrame(data)

# Display basic info
print(f"Dataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
df.head()</code></pre>
</div>
<div class="cell-output text-output">
<div class="prompt out-prompt" data-count="2"></div>
<pre>Dataset shape: (100, 3)
Columns: ['x', 'y', 'category']</pre>
</div>
</div>

<div class="cell code-cell">
<div class="cell-output html-output">
<table class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>x</th>
      <th>y</th>
      <th>category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.496714</td>
      <td>-0.469474</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.138264</td>
      <td>0.542560</td>
      <td>B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.647689</td>
      <td>1.579213</td>
      <td>C</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.523030</td>
      <td>-0.469474</td>
      <td>A</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.234153</td>
      <td>0.542560</td>
      <td>B</td>
    </tr>
  </tbody>
</table>
</div>
</div>

## Statistical Analysis

Let's perform some basic statistical analysis on our data:

<div class="cell code-cell">
<div class="cell-input">
<div class="prompt in-prompt" data-count="3"></div>
<pre><code class="language-python"># Calculate correlation
correlation = df[['x', 'y']].corr()
print("Correlation matrix:")
print(correlation)

# Basic statistics
print("\nBasic statistics:")
print(df.describe())</code></pre>
</div>
<div class="cell-output text-output">
<div class="prompt out-prompt" data-count="3"></div>
<pre>Correlation matrix:
          x         y
x  1.000000 -0.085586
y -0.085586  1.000000

Basic statistics:
               x           y
count  100.000000  100.000000
mean     0.026844   -0.014467
std      1.014906    0.988796
min     -2.318372   -2.552990
25%     -0.635634   -0.615572
50%      0.064820   -0.099501
75%      0.705805    0.656659
max      3.578396    2.269755</pre>
</div>
</div>

## Mathematical Formulations

We can also include mathematical expressions in our notebook posts. For example, the correlation coefficient is calculated as:

$$r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2\sum_{i=1}^{n}(y_i - \bar{y})^2}}$$

## Visualization

<div class="cell code-cell">
<div class="cell-input">
<div class="prompt in-prompt" data-count="4"></div>
<pre><code class="language-python"># Create a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='x', y='y', hue='category', s=60, alpha=0.7)
plt.title('Scatter Plot of X vs Y by Category')
plt.grid(True, alpha=0.3)
plt.show()</code></pre>
</div>
</div>

<div class="cell-output image-output">
<div class="plot-container">
<img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxyZWN0IHdpZHRoPSI0MDAiIGhlaWdodD0iMzAwIiBmaWxsPSIjZjhmOWZhIi8+CiAgICA8dGV4dCB4PSIyMDAiIHk9IjE1MCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1mYW1pbHk9IkFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjE2IiBmaWxsPSIjNjY2Ij5QbG90IFBsYWNlaG9sZGVyPC90ZXh0Pgo8L3N2Zz4K" alt="Scatter plot of X vs Y by Category" />
</div>
</div>

## Conclusion

This notebook demonstrates how we can now display Jupyter notebook content in our Jekyll blog, including:

- Code cells with syntax highlighting
- Output cells with various formats (text, HTML, images)
- Mathematical expressions using KaTeX
- Proper styling that matches notebook aesthetics

The integration allows for seamless sharing of data science work and analysis directly in blog format.

## Code Summary

<div class="cell markdown-cell">
<div class="cell-input">
Key takeaways from this analysis:
<ul>
<li>Data correlation: Low negative correlation between x and y (-0.086)</li>
<li>Distribution: Both variables follow approximately normal distributions</li>
<li>Categories: Data is evenly distributed across three categories A, B, C</li>
</ul>
</div>
</div>