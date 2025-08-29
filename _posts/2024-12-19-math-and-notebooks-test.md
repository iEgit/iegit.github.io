---
layout: post
title: "Testing Math Expressions and Jupyter Notebooks"
date: 2024-12-19 16:00:00 +0000
categories: test math jupyter
author: iEgit
excerpt: "A test post to demonstrate KaTeX mathematical expressions and Jupyter notebook support in our Jekyll blog."
---

# Testing Math Expressions and Jupyter Notebooks

This post demonstrates the new mathematical expression and Jupyter notebook capabilities of our blog.

## Mathematical Expressions with KaTeX

### Inline Math

Here's an inline mathematical expression: $E = mc^2$

The quadratic formula is $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$

### Block Math

Here's a block mathematical expression:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

### Complex Equations

The Schrödinger equation:

$$
i\hbar\frac{\partial}{\partial t}\Psi(\mathbf{r},t) = \hat{H}\Psi(\mathbf{r},t)
$$

Matrix notation:

$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix} =
\begin{pmatrix}
ax + by \\
cx + dy
\end{pmatrix}
$$

## Test Content

This is regular content to ensure our math rendering doesn't interfere with normal text processing.

### Code Blocks

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

The math should render properly alongside code blocks and other content.