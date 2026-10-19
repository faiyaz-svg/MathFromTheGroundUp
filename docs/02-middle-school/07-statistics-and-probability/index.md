# Statistics and probability

Summarizing data by its centre and spread, measuring chance by counting outcomes, and looking for associations between two variables.

1. [Describing data](01-describing-data.md)
2. [Basic probability](02-basic-probability.md)
3. [Scatter plots and two-way tables](03-scatter-plots-and-two-way-tables.md)

## Cheat sheet

### Describing data

A variable is categorical (groups, such as program or postal code) or numerical (measured or counted). If averaging the values makes no sense, it is categorical, even when the values are digits.

| Measure | How to find it | Example: 2, 4, 9 |
|---|---|---|
| mean $\bar{x}$ | sum divided by count, $\frac{x_1 + \dots + x_n}{n}$ | $\frac{15}{3} = 5$ |
| median | middle of the sorted list, at position $\frac{n + 1}{2}$; mean of the two middle values when $n$ is even | 4 |
| mode | most common value; there may be several or none | none |
| range | largest minus smallest | $9 - 2 = 7$ |
| MAD | mean of the distances $\lvert x_i - \bar{x} \rvert$ | $\frac{3 + 1 + 4}{3} = \frac{8}{3}$ |
| weighted mean | $\frac{w_1 x_1 + \dots + w_n x_n}{w_1 + \dots + w_n}$ | 25%, 25%, 40%, 10% of 88, 71, 62, 95 is 74.05 |

Quartiles, the book's method: sort, split at the median (leaving the median out of both halves when $n$ is odd), and take the median of each half. These are $Q_1$ (lower) and $Q_3$ (upper), and $\text{IQR} = Q_3 - Q_1$. NumPy's default and Excel's `QUARTILE.INC` interpolate and can differ slightly.

- Five-number summary: minimum, $Q_1$, median, $Q_3$, maximum. A box plot draws the box from $Q_1$ to $Q_3$, a line at the median, and whiskers to the most extreme values that are not outliers.
- Outliers: below $Q_1 - 1.5 \times \text{IQR}$ or above $Q_3 + 1.5 \times \text{IQR}$.
- Right skew (a long tail of large values, as with incomes) pulls the mean above the median. Report the median and IQR for skewed data or data with outliers, and the mean and MAD for roughly symmetric data.
- Adding a constant to every value shifts the centre and leaves the spread alone. Multiplying every value by a positive number multiplies both.
- $\text{total} = n \times \bar{x}$ finds a missing value.
- A histogram groups numerical data into equal bins, with touching bars. A value on a boundary goes in the bin that starts there.

Main mistakes:

- Taking the median before sorting, or picking one of the two middle values when $n$ is even.
- Averaging components without their weights: the plain mean of 88, 71, 62 and 95 is 79, not the weighted 74.05.
- Averaging deviations without absolute values. They always add to 0.
- Calling a value an outlier without checking the fences, or deleting a real outlier.
- Reading a long whisker as "more values". Each quarter of a box plot holds about the same number.

### Basic probability

For equally likely outcomes, $P(A) = \frac{\text{number of outcomes in } A}{\text{number of outcomes in } S}$, where the sample space $S$ lists every outcome and the event $A$ is a set of them. Every probability is between 0 (impossible) and 1 (certain).

| Rule | When | Formula |
|---|---|---|
| complement | always | $P(A^c) = 1 - P(A)$ |
| "and": multiply | $A$ and $B$ independent | $P(A \text{ and } B) = P(A) \times P(B)$ |
| "or": add | $A$ and $B$ mutually exclusive | $P(A \text{ or } B) = P(A) + P(B)$ |
| "or" with overlap | always | subtract the overlap once: heart or king is $\frac{13 + 4 - 1}{52} = \frac{4}{13}$ |
| at least one | independent trials | $1 - P(\text{none})$: at least one six in 4 rolls is $1 - \left(\frac{5}{6}\right)^4 \approx 0.518$ |

- Independent: one event doesn't change the probability of the other (separate coin flips). Mutually exclusive: they can't both happen (heart and spade on one draw). Mutually exclusive events with positive probabilities are never independent.
- Two dice have 36 equally likely ordered pairs. The ways to roll the sums 2 to 12 are 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1.
- Trees: multiply along each path, add the leaves in the event, and check that all the leaves add to 1.
- Experimental probability is the share of trials in which the event happened. It moves toward the theoretical probability as the number of trials grows.
- Odds of $a:b$ in favour are a probability of $\frac{a}{a + b}$.

Main mistakes:

- Treating the sums 2 to 12 as equally likely. Count the 36 cells.
- Adding for "at least one": four rolls do not give $\frac{4}{6}$, and seven would give more than 1.
- Adding events that overlap, which counts the overlap twice.
- Multiplying when the events are not independent, such as draws without replacement. Count ordered pairs instead: 2 reds from 2 red and 3 blue is $\frac{2}{20}$, not $\left(\frac{2}{5}\right)^2$.
- The gambler's fallacy: after five heads, the next flip is still $\frac{1}{2}$.
- Listing HH, HT, TT as three equally likely outcomes. HT and TH are different.

### Scatter plots and two-way tables

Describe a scatter plot by direction (positive, negative or none), form (linear or curved, clusters), strength (tight or loose) and outliers. The explanatory variable goes across and the response up.

Line of best fit by eye:

1. Draw a line along the trend with about half the points on each side.
2. Read two points off the line, far apart, and find $m = \frac{y_2 - y_1}{x_2 - x_1}$.
3. Put one point into $y = mx + b$ to find $b$.
4. Interpret the slope with units ("5 points per hour"). Predict by substituting.

| Term | Meaning |
|---|---|
| interpolation | predicting inside the range of the data's $x$ values; fairly safe |
| extrapolation | predicting outside it; risky (20 hours of study predicts 147 out of 100) |
| confounding variable | a third variable that drives both, such as population for libraries and car accidents |

| In a two-way table | Divide by | Answers |
|---|---|---|
| joint relative frequency | grand total | what share of everyone is in this cell |
| marginal relative frequency | grand total, using a margin | what share of everyone is in this row or column |
| row relative frequency | the row total | within this row, what share is in each column |
| column relative frequency | the column total | within this column, what share is in each row |

Two categorical variables are associated when the row percents differ from row to row; if every row splits the same way, there is no association.

Main mistakes:

- Concluding cause from association. Look for a confounder, and compare rates, not totals.
- Extrapolating a line far beyond the data.
- Reading the slope from two data points that sit off the trend instead of from the line.
- Calling a strong curve "no association": always look at the plot.
- Comparing counts instead of percents when the groups have different sizes.
- Mixing up row and column percents: 30% of CS students use Linux, while 94.7% of Linux users are in CS.
