# Bits and information

After this lesson you can work out how many bits a set of values needs, do storage arithmetic in bytes with both decimal and binary units, compute the information in an outcome and the entropy of a distribution, and explain why no lossless compressor can shrink every file.

Before this: [number bases and conversions](01-number-bases-and-conversions.md), [logarithms](../../03-high-school/07-exponentials-and-logarithms/02-logarithms.md) and [scientific notation](../../02-middle-school/04-powers-roots-and-real-numbers/02-scientific-notation.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. How many bits are needed to give each day of a non-leap year its own label?
2. A coin lands heads with probability 0.9. How many bits of information does one flip carry on average? Give the answer to three decimal places.
3. A programmer claims their compressor makes every file at least one bit shorter. What goes wrong?

<details class="solution" markdown>
<summary>Answers</summary>

1. There are 365 days. Since $2^8 = 256$ is too small and $2^9 = 512$ is enough, the answer is 9 bits.
2. The entropy is $0.9 \log_2 \frac{1}{0.9} + 0.1 \log_2 \frac{1}{0.1} \approx 0.9 \cdot 0.152 + 0.1 \cdot 3.322 \approx 0.469$ bits. A fair coin would carry 1 bit.
3. There are $2^n$ files of $n$ bits but only $2^n - 1$ strings that are shorter, so two different files would have to compress to the same output, and no decompressor could tell them apart.

</details>

## The idea

A friend picks a whole number from 1 to 1,000 and you may ask yes/no questions. The best plan is to halve the possibilities each time: "Is it above 500?", then "Is it above 250?" or "above 750?", and so on. After 10 questions at most one number is left, because $2^{10} = 1{,}024 \ge 1{,}000$. Nine questions can't be enough, since $2^9 = 512 < 1{,}000$. Each yes/no answer is one bit, so naming one of 1,000 equally likely numbers takes 10 bits.

Now change the game. The friend flips a coin that lands heads 99% of the time and tells you the result. Hearing "heads" barely surprises you; it tells you almost nothing. Hearing "tails" is a shock. This suggests that information is surprise: the less likely an outcome, the more you learn when it happens. A lossless compressor uses the same fact. It gives short codes to common patterns, and long codes to rare ones.

This lesson makes both ideas exact. The first becomes a counting rule for bits. The second becomes a formula, $-\log_2 p$, and its average over a distribution, called entropy. Counting also gives a limit that no program can beat.

## Definitions

### Bits, bytes and words

A **bit** is a variable with two possible values, written 0 and 1. A **byte** is a group of 8 bits, so it has $2^8 = 256$ possible values. A **word** is the group of bits a processor handles as one unit, such as the size of a register. On most current desktop and phone processors it is 64 bits, but the term depends on the design, and x86 assembly manuals still call 16 bits a word. Say the number of bits when it matters.

In plain words, a bit is the smallest unit of storage, a byte is the smallest unit most computers can address, and a word is the natural chunk the processor works on. A byte is two hex digits, and a 64-bit word is 16 hex digits ([number bases and conversions](01-number-bases-and-conversions.md)).

The prefixes for sizes come in two families. The decimal (SI) ones are kB $= 10^3$ bytes, MB $= 10^6$, GB $= 10^9$ and TB $= 10^{12}$. The binary (IEC) ones have an "i" in the symbol: KiB $= 2^{10}$ bytes, MiB $= 2^{20}$, GiB $= 2^{30}$ and TiB $= 2^{40}$. The two differ by 2.4% at the kilo level and by 10% at the tera level; the table is in [scientific notation](../../02-middle-school/04-powers-roots-and-real-numbers/02-scientific-notation.md#kb-or-kib). Network speeds are in bits per second, and file sizes in bytes, so 100 Mbit/s is at most $\frac{10^8}{8} = 12.5$ MB per second.

### Information content

Let an outcome have probability $p$, where $0 < p \le 1$. Its **information content**, also called its surprisal, is

$$
I(p) = \log_2 \frac{1}{p} = -\log_2 p \text{ bits.}
$$

In plain words, an outcome with probability $\frac{1}{2}$ carries 1 bit (a fair coin flip), one with probability $\frac{1}{1024}$ carries 10 bits, and a certain outcome ($p = 1$) carries 0 bits. There are three reasons for the logarithm. A certain outcome should carry nothing, and $\log_2 1 = 0$. A rarer outcome should carry more, and $\frac{1}{p}$ grows as $p$ shrinks. And information from independent events should add: the probability of both is the product $pq$, and $-\log_2(pq) = -\log_2 p - \log_2 q$. For $N$ equally likely outcomes each has $p = \frac{1}{N}$, so each carries $\log_2 N$ bits, the same number as the bits needed to label them.

### Entropy

A **discrete probability distribution** on $N$ outcomes is a list of probabilities $p_1, p_2, \dots, p_N$, each at least 0, that add up to 1. Its **entropy** is the average information content of an outcome:

$$
H = \sum_{i=1}^{N} p_i \log_2 \frac{1}{p_i} = -\sum_{i=1}^{N} p_i \log_2 p_i,
$$

where a term with $p_i = 0$ counts as 0. This is the expected value ([discrete random variables](../../05-university-core/07-probability/03-discrete-random-variables.md)) of the surprisal, weighted by how often each outcome occurs. The convention $0 \cdot \log_2 0 = 0$ matches the limit of $p \log_2 p$ as $p \to 0$, and it says that an outcome that never happens adds nothing.

In plain words, entropy measures how unpredictable the source is, in bits per outcome. The table gives some values; the 0.9 coin and the four-outcome source are worked in the examples.

| Distribution | Probabilities | $H$ in bits |
|---|---|---|
| fair coin | $\frac{1}{2}, \frac{1}{2}$ | 1 |
| coin with $P(\text{heads}) = 0.9$ | 0.9, 0.1 | 0.469 |
| coin with $P(\text{heads}) = 0.99$ | 0.99, 0.01 | 0.081 |
| fair 8-sided die | eight times $\frac{1}{8}$ | 3 |
| fair 6-sided die | six times $\frac{1}{6}$ | 2.585 |
| always the same outcome | 1, 0, 0 | 0 |
| four outcomes | $\frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \frac{1}{8}$ | 1.75 |

Claude Shannon introduced this quantity in "A Mathematical Theory of Communication" (*Bell System Technical Journal*, 1948). His source coding theorem says that no lossless code can use fewer than $H$ bits per outcome on average, and that codes exist within one bit of $H$. This lesson uses the first half only as motivation and proves a simpler limit below.

### Lossless compression

A **lossless compressor** is a function $C$ from bit strings to bit strings together with a decompressor $D$ such that $D(C(x)) = x$ for every string $x$. In plain words, you get back exactly what you put in. This forces $C$ to be injective: different inputs give different outputs, since otherwise $D$ would have to return two different answers for one input ([injective, surjective and bijective](../../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md)). A lossy compressor, such as JPEG or MP3, throws information away on purpose, so it is not injective and the limits below don't apply to it.

## How to do it

### How many bits for $N$ values

1. Count the values $N$, including every value that could occur.
2. Find the smallest integer $n$ with $2^n \ge N$. Use the powers of 2 table from [number bases and conversions](01-number-bases-and-conversions.md), or compute $\lceil \log_2 N \rceil$.
3. Check the neighbours: $2^{n-1}$ must be less than $N$ and $2^n$ at least $N$.

*Theorem 1.* For each integer $N \ge 1$, the smallest number of bits $n$ that can give $N$ different values each its own bit string is $n = \lceil \log_2 N \rceil$.

What we know: $n$ bits give exactly $2^n$ different strings (from the last lesson). What we want: the smallest $n$ for which $N$ values can get distinct strings. The plan is to show that this is possible exactly when $2^n \ge N$, and then solve the inequality.

*Proof.* If $2^n \ge N$, give the $N$ values $N$ different strings out of the $2^n$ available. If $2^n < N$, there are more values than strings, so two values share a string, which the pigeonhole principle (below) forbids. So labels exist exactly when $2^n \ge N$. Because $\log_2$ is increasing, $2^n \ge N$ is the same as $n \ge \log_2 N$. The smallest integer that is at least $\log_2 N$ is $\lceil \log_2 N \rceil$. $\blacksquare$

Look back: a power of 2 fits exactly, since $N = 2^k$ gives $k$ bits. One more value costs a whole extra bit, so $2^k + 1$ values need $k + 1$ bits. Python's `(N - 1).bit_length()` gives the same number, because the largest label is $N - 1$ and `bit_length` counts the bits in it.

### Storage arithmetic

1. Turn the quantity into bits or bytes. One byte is 8 bits, and a pixel with 3 colour channels of 8 bits each is 3 bytes.
2. Multiply out the total. Keep the unit with every number.
3. Choose the unit for the answer. Divide by $10^3, 10^6, 10^9$ for kB, MB, GB, or by $2^{10}, 2^{20}, 2^{30}$ for KiB, MiB, GiB. State which family you used.
4. Check the size: $2^{10} \approx 10^3$ means the two families differ by a few percent at the kilo and mega levels, so a result that is far off has a mistake.

### Entropy of a distribution

1. List the probabilities. Check that they add up to 1.
2. For each outcome with $p_i > 0$, compute the surprisal $\log_2 \frac{1}{p_i}$. Powers of $\frac{1}{2}$ give whole numbers; others need a calculator or $\log_2 x = \frac{\ln x}{\ln 2}$.
3. Multiply each surprisal by its probability and add. Outcomes with $p_i = 0$ add 0.
4. Check against the bounds below: $0 \le H \le \log_2 N$.

*Theorem 2.* For a distribution on $N$ outcomes, $0 \le H \le \log_2 N$, and $H = \log_2 N$ exactly when all $N$ outcomes have probability $\frac{1}{N}$.

What we know: $H = \sum p_i \log_2 \frac{1}{p_i}$, and each $p_i \le 1$, so every term is at least 0, which gives $H \ge 0$. What we want: the upper bound. The plan is to compare $H$ with $\log_2 N$ term by term, using the inequality $\ln y \le y - 1$ for $y > 0$, with equality only at $y = 1$. That inequality holds because $f(y) = y - 1 - \ln y$ has derivative $1 - \frac{1}{y}$, which is negative for $y < 1$ and positive for $y > 1$, so $f$ has its minimum value $f(1) = 0$.

*Proof.* Sum only over the outcomes with $p_i > 0$; the others add 0 to everything. These probabilities still add to 1, so $\log_2 N = \sum p_i \log_2 N$, and

$$
H - \log_2 N = \sum p_i \log_2 \frac{1}{p_i} - \sum p_i \log_2 N = \sum p_i \log_2 \frac{1}{N p_i}.
$$

Write $\log_2 y = \frac{\ln y}{\ln 2}$ and apply $\ln y \le y - 1$ with $y = \frac{1}{N p_i}$:

$$
H - \log_2 N \le \frac{1}{\ln 2} \sum p_i \left( \frac{1}{N p_i} - 1 \right) = \frac{1}{\ln 2} \left( \sum \frac{1}{N} - \sum p_i \right).
$$

The sum of $\frac{1}{N}$ has at most $N$ terms, so it is at most 1, and $\sum p_i = 1$. So the right side is at most 0, and $H \le \log_2 N$. Equality needs $\frac{1}{N p_i} = 1$ for every $i$ in the sum, so $p_i = \frac{1}{N}$, and all $N$ outcomes must be in the sum. $\blacksquare$

Look back: the uniform distribution is the hardest to predict, so it has the most entropy, and it matches Theorem 1: $N$ equally likely values need $\log_2 N$ bits, rounded up to a whole number when you must store them. Any skew in the probabilities lowers the average, which is the room a compressor uses.

### Why compression has a limit

*Theorem 3 (pigeonhole).* Let $n \ge 1$. No lossless compressor maps every $n$-bit string to a strictly shorter string.

What we know: the compressor is injective. What we want: a contradiction from the assumption that all $2^n$ strings of length $n$ shrink. The plan is proof by contradiction, using a count.

*Proof.* The strings shorter than $n$ bits have lengths $0, 1, \dots, n - 1$, and there are $2^k$ strings of length $k$. Counting them (the empty string is the one string of length 0) gives

$$
1 + 2 + 4 + \dots + 2^{n-1} = 2^n - 1.
$$

Suppose each of the $2^n$ strings of length $n$ were mapped to one of these $2^n - 1$ shorter strings. By the **pigeonhole principle**, if more than $m$ objects go into $m$ boxes, some box holds at least two objects, so two different inputs would give the same output. That contradicts injectivity. $\blacksquare$

Look back: the same count says more. Among the $n$-bit strings, at most $2^{n-k+1} - 1$ can map to outputs of length $n - k$ or less, because there are only that many such outputs. So fewer than a fraction $2^{1-k}$ of all files can shrink by $k$ bits or more. For $k = 8$ that is fewer than 1 file in 128 shrinking by a byte or more. Real compressors work because real files are far from random: text, code and images have patterns, which means low entropy, and the few files that do shrink are exactly those.

## Worked examples

<div class="example" markdown>

### Example 1: entropy of a biased coin

A coin lands heads with probability 0.9 and tails with probability 0.1. Find the entropy of one flip.

Step 1: the probabilities 0.9 and 0.1 add up to 1.

Step 2: the surprisal of heads is $\log_2 \frac{1}{0.9} = \log_2 1.111\ldots \approx 0.152$ bits, and the surprisal of tails is $\log_2 10 \approx 3.322$ bits. The rarer outcome carries far more information.

Step 3: weight each by its probability and add:

$$
H = 0.9 \cdot 0.152 + 0.1 \cdot 3.322 \approx 0.137 + 0.332 = 0.469 \text{ bits.}
$$

Step 4, the check: $0 \le 0.469 \le \log_2 2 = 1$. It is less than the 1 bit of a fair coin, as expected, because a biased coin is easier to predict. By Shannon's source coding theorem, 1,000 such flips can be stored in about 469 bits on average, not 1,000, by a code designed for long runs of flips.

<div class="warning" markdown>

Watch out at step 3: weigh each surprisal by its own probability. Averaging 0.152 and 3.322 with equal weights gives 1.737, which is more than the maximum possible entropy of 1.

</div>

</div>

<div class="example" markdown>

### Example 2: storage for uncompressed video

A 4K frame has $3840 \times 2160$ pixels, and each pixel stores 3 bytes (one byte each for red, green and blue). How big is one frame, how much is 1 second at 60 frames per second, and how many seconds fit on a 1 TB drive?

One frame is $3840 \cdot 2160 \cdot 3 = 24{,}883{,}200$ bytes. In decimal units that is 24.9 MB. In binary units, divide by $2^{20} = 1{,}048{,}576$ to get 23.73 MiB.

One second is $60 \cdot 24{,}883{,}200 = 1{,}492{,}992{,}000$ bytes, about 1.49 GB. A 1 TB drive holds $10^{12}$ bytes, so it fits $\frac{10^{12}}{1.492992 \times 10^9} \approx 669.8$ seconds, a little under 11 minutes.

Check by rounding: $4000 \cdot 2000 \cdot 3 = 24$ million bytes per frame, times 60 is about 1.4 billion per second, and $10^{12}$ divided by that is about 700. Real video is compressed by a factor of hundreds, which is why a film fits on a drive at all.

</div>

<div class="example" markdown>

### Example 3: a distribution with a code that reaches the entropy

A sensor reports one of four levels with probabilities $\frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \frac{1}{8}$. Find $H$ and compare it with a code that gives shorter strings to likelier levels.

The surprisals are 1, 2, 3 and 3 bits, so

$$
H = \frac{1}{2} \cdot 1 + \frac{1}{4} \cdot 2 + \frac{1}{8} \cdot 3 + \frac{1}{8} \cdot 3 = 1.75 \text{ bits.}
$$

A fixed code needs $\lceil \log_2 4 \rceil = 2$ bits per report. Now use the codes $0$, $10$, $110$ and $111$. No code is the start of another, so a stream of them can be read without separators. The average length is the same sum, $\frac{1}{2} \cdot 1 + \frac{1}{4} \cdot 2 + \frac{1}{8} \cdot 3 + \frac{1}{8} \cdot 3 = 1.75$ bits, which equals $H$. This works because every probability is a power of $\frac{1}{2}$. For other probabilities the best whole-number code lengths can't match $H$ exactly.

Check: $1.75 \le \log_2 4 = 2$, as Theorem 2 requires.

</div>

<div class="example" markdown>

### Example 4: a six-letter password (finish it yourself)

A password is 6 lowercase letters chosen uniformly at random. There are $26^6 = 308{,}915{,}776$ passwords. How many bits of entropy does it have, and how many bits does it take to store it as one number?

The entropy of a uniform choice among $N$ outcomes is $\log_2 N$, and the storage is $\lceil \log_2 N \rceil$ by Theorem 1. Since $\log_2 26^6 = 6 \log_2 26$ and $\log_2 26 \approx 4.700$, finish the arithmetic for both numbers and check that they fit Theorem 2.

<details class="solution" markdown>
<summary>Finish</summary>

The entropy is $6 \cdot 4.7004 \approx 28.2$ bits. Storing it as a number needs $\lceil 28.2 \rceil = 29$ bits.

Check: $2^{28} = 268{,}435{,}456$ is below $308{,}915{,}776$ and $2^{29} = 536{,}870{,}912$ is above it, so 28 bits are not enough and 29 are. The entropy 28.2 is at most the storage 29, as it must be, and it is less than the 29 only because the count $26^6$ is not a power of 2.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: a bit of storage is not always a bit of information. An error flag that is 1 with probability 0.01 takes up a full bit of storage, but each read carries only 0.081 bits of information. The two are equal only when the bit is 0 or 1 with probability $\frac{1}{2}$ each.

</div>

<div class="warning" markdown>

Watch out: don't compute $\log_2 0$. An outcome with probability 0 contributes $0 \cdot \log_2 0 = 0$ to the entropy, by convention. In code, skip those terms, or `math.log2(0)` raises a `ValueError`.

</div>

<div class="warning" markdown>

Watch out: `math.ceil(math.log2(N))` can be wrong for large $N$. The float `math.log2(2**50 + 1)` is exactly `50.0`, because 51 digits of precision don't fit, so the formula says 50 bits when 51 are needed. Use `(N - 1).bit_length()`, which works on exact integers.

</div>

<div class="warning" markdown>

Watch out for the units. A "1 TB" drive holds $10^{12}$ bytes, which is 931 GiB, and "100 Mbps" is megabits, not megabytes, per second. Write the unit with every number, and decide between the decimal and binary family before dividing.

</div>

Entropy depends on the probabilities, not on what the outcomes mean. A random string of letters has more entropy per character than English text, even though only the text says anything. Entropy measures the surprise of the source and nothing about its meaning.

The zero case of Theorem 1 is easy to miss: $N = 1$ needs 0 bits, since a variable with one possible value carries no information. This is also why `bits_needed(1)` returns 0 in the code below.

## Tricks and shortcuts

- Each doubling of the number of values costs one bit: 1,000 values need 10 bits, 2,000 need 11, and 4,000 need 12. A million needs 20 and a billion needs 30.
- To estimate the bits for a count with $d$ decimal digits, multiply: $\log_2 10 \approx 3.32$, so $d$ digits need about $3.32\,d$ bits. A 9-digit ID, with up to $10^9$ values, needs 30 bits.
- For entropy, picture 20 questions. A fair choice among 8 things is 3 questions, among 1,000 about 10. A skewed choice needs fewer on average because you can ask about the likely things first.
- When all the probabilities are powers of $\frac{1}{2}$, the entropy is a plain sum of fractions, as in Example 3. No calculator is needed.
- To estimate whether a file can be compressed, ask whether it has repeated or predictable parts. Random bytes, and files that were already compressed, can't be squeezed further.

## In code

The functions turn the definitions into code. The `zlib` lines show Theorem 3 at work: random data does not shrink, and patterned data does. Every number in the comments is real output.

<details class="code" markdown>
<summary>In code</summary>

```python
import math
import random
import zlib
from itertools import product

def bits_needed(n):
    """Smallest number of bits that can label n distinct values (n >= 1)."""
    return (n - 1).bit_length()

def surprisal(p):
    """Information content of an outcome with probability p, in bits."""
    return math.log2(1 / p)

def entropy(probs):
    """Shannon entropy in bits; terms with p = 0 count as 0."""
    return sum(p * surprisal(p) for p in probs if p > 0)

print([bits_needed(n) for n in (1, 2, 3, 365, 1000, 5000)])  # [0, 1, 2, 9, 10, 13]

n = 2**50 + 1                                                # one more than a power of 2
print(bits_needed(n), math.ceil(math.log2(n)))               # 51 50

print(surprisal(0.5), surprisal(1 / 1024))                   # 1.0 10.0
print(round(entropy([0.5, 0.5]), 4))                         # 1.0
print(round(entropy([0.9, 0.1]), 4))                         # 0.469
print(round(entropy([1 / 6] * 6), 4), round(math.log2(6), 4))  # 2.585 2.585
print(entropy([0.5, 0.25, 0.125, 0.125]))                    # 1.75
print(entropy([1.0, 0.0]))                                   # 0.0

# H never exceeds log2(N): try 1000 random distributions on 7 outcomes
rng = random.Random(1)
worst = 0.0
for _ in range(1000):
    w = [rng.random() for _ in range(7)]
    total = sum(w)
    worst = max(worst, entropy([x / total for x in w]))
print(worst < math.log2(7))                                  # True

# Pigeonhole: strings of 3 bits against all shorter strings
strings = lambda k: ["".join(b) for b in product("01", repeat=k)]
print(len(strings(3)), sum(len(strings(k)) for k in range(3)))  # 8 7

# Real compressors: random bytes against repetitive bytes
data = rng.randbytes(10_000)
print(len(zlib.compress(data, 9)))                           # 10011
print(len(zlib.compress(b"abc" * 3000, 9)))                  # 35

# Storage arithmetic: one uncompressed 4K frame, 3 bytes per pixel
frame = 3840 * 2160 * 3
print(frame, round(frame / 2**20, 2), round(frame / 1e6, 1))  # 24883200 23.73 24.9
print(round(1e12 / (frame * 60), 1))                         # 669.8 (seconds of 60 fps video per 1 TB)
```

The first two prints show the float trap: `bits_needed` is exact where `math.ceil(math.log2(n))` is off by one. Random bytes grow by 11 bytes under `zlib`, from its headers and block structure, while 9,000 repeated bytes shrink to 35. The 1,000-distribution loop is a test, not a proof; Theorem 2 is the proof.

</details>

## FAQ

### Why does entropy use a logarithm?

Because information from independent events should add, while probabilities multiply. A logarithm turns products into sums. The base only sets the unit: base 2 gives bits, and base $e$ gives nats (natural units), used in machine learning. One nat is $\frac{1}{\ln 2} \approx 1.44$ bits.

### If compression can't shrink every file, why does zip work?

Because it doesn't shrink every file. It shrinks the files people actually have, such as text and code, which are a tiny corner of all possible strings, and it makes everything else a little longer. Theorem 3 says the average over all files can't be improved, and the "few files that matter" are the ones with low entropy. This is also why compressing a compressed file or a random file gains nothing.

### What is the difference between a bit and a shannon?

A bit is a storage cell with two states. A shannon (symbol Sh) is the unit of information, the same $-\log_2 p$ scale used here, and one shannon is the information in one fair coin flip. In everyday computing both are called bits. The distinction matters only when a bit is biased, as in the first warning above.

### Is entropy the same as the entropy in physics?

The formulas have the same shape, $-\sum p \ln p$, and the physical version (Gibbs entropy) is multiplied by Boltzmann's constant. In this book, entropy always means the information measure above.

## Practice

### Warm-up

1\. How many bits does each need? (a) 100 different values, (b) 1,000,000,000 values, (c) $2^{20} + 1$ values, (d) 1 value.

<details class="solution" markdown>
<summary>Solution</summary>

Find the smallest $n$ with $2^n \ge N$.

- (a) $2^6 = 64 < 100 \le 128 = 2^7$, so 7 bits.
- (b) $2^{29} = 536{,}870{,}912 < 10^9 \le 1{,}073{,}741{,}824 = 2^{30}$, so 30 bits.
- (c) $2^{20}$ values fit exactly in 20 bits, so one more value needs 21 bits.
- (d) $2^0 = 1 \ge 1$, so 0 bits.

Check with Python: `(N - 1).bit_length()` gives 7, 30, 21 and 0.

</details>

2\. A file is 5,000,000 bytes. Give its size in MB and in MiB.

<details class="solution" markdown>
<summary>Solution</summary>

In decimal units, $\frac{5{,}000{,}000}{10^6} = 5$ MB. In binary units, $\frac{5{,}000{,}000}{2^{20}} = \frac{5{,}000{,}000}{1{,}048{,}576} \approx 4.77$ MiB.

Check: the binary unit is bigger, so the same bytes make a smaller number, and $4.77 \cdot 1.048576 \approx 5.0$.

</details>

3\. Find the entropy of (a) a fair 4-sided die, and (b) a source with probabilities $\frac{1}{4}, \frac{1}{4}, \frac{1}{2}$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Four equally likely outcomes give $H = \log_2 4 = 2$ bits.

(b) The surprisals are 2, 2 and 1 bits, so $H = \frac{1}{4} \cdot 2 + \frac{1}{4} \cdot 2 + \frac{1}{2} \cdot 1 = 1.5$ bits.

Check (b) with Theorem 2: $1.5 \le \log_2 3 \approx 1.585$.

</details>

### Standard

4\. A sensor reports four levels with probabilities 0.7, 0.1, 0.1 and 0.1. Find the entropy to three decimal places and compare it with the 2 bits of a fixed-length code.

<details class="solution" markdown>
<summary>Solution</summary>

The surprisal of 0.7 is $\log_2 \frac{1}{0.7} \approx 0.515$ bits, and the surprisal of 0.1 is $\log_2 10 \approx 3.322$ bits. So

$$
H = 0.7 \cdot 0.515 + 3 \cdot 0.1 \cdot 3.322 \approx 0.360 + 0.997 = 1.357 \text{ bits.}
$$

A fixed code uses 2 bits per report, so a good variable-length code could save up to about $2 - 1.357 = 0.643$ bits per report, roughly a third.

Check: $1.357 \le \log_2 4 = 2$, and the four outcomes are not equally likely, so the inequality is strict.

</details>

5\. Compare two password schemes. Scheme A uses 8 characters from the 62 characters a to z, A to Z and 0 to 9. Scheme B uses 8 digits. Each is chosen uniformly at random. Find the number of passwords and the entropy of each, and the whole number of bits needed to store each.

<details class="solution" markdown>
<summary>Solution</summary>

Scheme A has $62^8 = 218{,}340{,}105{,}584{,}896$ passwords, so its entropy is $8 \log_2 62 \approx 8 \cdot 5.954 = 47.6$ bits, and storing one needs $\lceil 47.6 \rceil = 48$ bits.

Scheme B has $10^8$ passwords, so its entropy is $8 \log_2 10 \approx 26.6$ bits, and storing one needs 27 bits.

Check: $2^{26} = 67{,}108{,}864 < 10^8 \le 134{,}217{,}728 = 2^{27}$, so 27 bits is right for B. Scheme A has about $2.2 \times 10^6$ times as many passwords, since $2.18 \times 10^{14} \div 10^8$.

</details>

6\. (a) How many bit strings of length at most 15 are there, counting the empty string? (b) Use that to show that a lossless compressor can't shrink every 16-bit string. (c) At most how many 16-bit strings can be compressed to 8 bits or fewer?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The count is $1 + 2 + 4 + \dots + 2^{15} = 2^{16} - 1 = 65{,}535$.

(b) There are $2^{16} = 65{,}536$ strings of 16 bits, one more than there are shorter strings. If each were mapped to a shorter string, two would share an output, and the compressor wouldn't be injective.

(c) There are $2^9 - 1 = 511$ strings of at most 8 bits, and an injective compressor needs a different output for each input. So at most 511 of the 65,536 strings, which is under 0.8%.

Check: the fraction is $\frac{511}{65{,}536} \approx 0.0078$, which is below $2^{1-8} = \frac{1}{128} \approx 0.0078125$, the bound from the look back.

</details>

### Challenge

7\. Two independent sources have distributions $p_1, \dots, p_a$ and $q_1, \dots, q_b$. The pair $(i, j)$ has probability $p_i q_j$. Show that the entropy of the pair is the sum of the two entropies. Use it to find the entropy of rolling two fair 6-sided dice and check it against $\log_2 36$.

<details class="solution" markdown>
<summary>Solution</summary>

What we want: $H_{\text{pair}} = H_p + H_q$. The plan is to split the logarithm of a product into a sum of logarithms and sum over each index separately.

$$
\begin{aligned}
H_{\text{pair}} &= \sum_{i,j} p_i q_j \log_2 \frac{1}{p_i q_j} = \sum_{i,j} p_i q_j \left( \log_2 \frac{1}{p_i} + \log_2 \frac{1}{q_j} \right) \\
&= \sum_i p_i \log_2 \frac{1}{p_i} \sum_j q_j + \sum_j q_j \log_2 \frac{1}{q_j} \sum_i p_i = H_p \cdot 1 + H_q \cdot 1.
\end{aligned}
$$

For two fair dice, $H = 2 \log_2 6 \approx 5.170$ bits. The 36 outcomes are equally likely, so Theorem 2 gives $\log_2 36 = \log_2 6^2 = 2 \log_2 6$, the same number.

Check: $2 \cdot 2.585 = 5.170$, and $2^{5.170} \approx 36$.

</details>

8\. (Reviews [logarithms](../../03-high-school/07-exponentials-and-logarithms/02-logarithms.md).) A database has $8 \times 10^9$ users. (a) How many bits does a user ID need so every user gets a different one? (b) How many decimal digits? (c) Explain why the ratio of the two answers is close to $\log_2 10$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $\log_2 (8 \times 10^9) = 3 + 9 \log_2 10 \approx 3 + 29.897 = 32.897$, so $\lceil 32.897 \rceil = 33$ bits.

(b) The number of decimal digits of the largest ID, $8 \times 10^9 - 1$, is $\lfloor \log_{10}(8 \times 10^9) \rfloor + 1 = \lfloor 9.903 \rfloor + 1 = 10$ digits.

(c) A digit carries $\log_2 10 \approx 3.32$ bits of choice, so $d$ digits carry about $3.32\,d$ bits. Here $\frac{33}{10} = 3.3$, close to 3.32; the gap comes from rounding each count up to a whole number.

Check: $2^{32} = 4{,}294{,}967{,}296 < 8 \times 10^9 \le 2^{33} = 8{,}589{,}934{,}592$, so 33 bits is right.

</details>

## Where this shows up

- The next lesson, [binary arithmetic and two's complement](03-binary-arithmetic-and-twos-complement.md), uses fixed numbers of bits and what happens at the ends of the range. [Floating point basics](04-floating-point-basics.md) spends a fixed bit budget on a number's size and its precision.
- Compression, coding and machine learning all use entropy. Huffman coding builds prefix codes like the one in Example 3, decision trees pick splits by information gain, and the cross-entropy loss of a classifier is a surprisal averaged over the data. Password strength is measured in bits of entropy, as in Example 4.
- The pigeonhole principle ([inclusion-exclusion and the pigeonhole principle](../03-counting-and-discrete-probability/04-inclusion-exclusion-and-pigeonhole.md)) is behind Theorem 3, and also behind hash collisions: a hash function from long strings to short ones must map some strings to the same value ([hash collisions](../../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md#hash-collisions)).
