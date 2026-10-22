# Bitwise operations and masks

After this lesson you can apply AND, OR, XOR, NOT and shifts to bit patterns by hand, use masks to test, set, clear and toggle bits, explain shifts as multiplying and dividing by powers of 2, prove and use tricks such as `x & (x - 1)`, and represent small sets as integers.

Before this: [number bases and conversions](01-number-bases-and-conversions.md), [binary arithmetic and two's complement](03-binary-arithmetic-and-twos-complement.md) and [truth tables and logical equivalence](../../04-proofs-and-logic/02-logic-and-sets/03-truth-tables-and-logical-equivalence.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Work out $1100 \,\&\, 1010$, $1100 \mid 1010$ and $1100 \oplus 1010$ on 4-bit patterns.
2. Write Python expressions that set bit 5 of `x`, and that clear bit 2 of `x`.
3. What does `-7 >> 1` give in Python, and why?

<details class="solution" markdown>
<summary>Answers</summary>

1. Column by column: AND is $1000$, OR is $1110$ and XOR is $0110$.
2. `x | (1 << 5)` and `x & ~(1 << 2)`.
3. It gives $-4$. A right shift by 1 divides by 2 and rounds down (toward $-\infty$), and $\lfloor -3.5 \rfloor = -4$.

</details>

## The idea

A Unix file has permissions for its owner, its group and everyone else, and each class can read, write or execute. That is 9 yes/no answers. Instead of 9 separate variables, the system packs them into one number: `chmod 755` is the pattern $111\,101\,101_2$. Asking "can the group write?" is one operation on that number, and so is "take away write permission from everyone".

Operations on whole bit patterns, one position at a time, are the subject of this lesson. They are the fastest operations a processor has, and they are how flags, colours, network addresses, hash functions and compact sets are handled in practice. They are also a second view of two things you already know: the truth tables of AND, OR, XOR and NOT from logic, applied to every position of a binary number at once, and multiplication and division by 2, which are just shifts.

## Definitions

### Bit vectors and bitwise operations

A **bit vector** of width $n$ is a string of $n$ bits $b_{n-1} \dots b_1 b_0$, which is the same thing as the unsigned integer $\sum b_i 2^i$ from 0 to $2^n - 1$ ([number bases and conversions](01-number-bases-and-conversions.md)). Bit $i$ means position $i$, counted from 0 at the right.

A **bitwise operation** combines bit vectors by applying a logical operation to each position separately. With 1 as true and 0 as false, the connectives of [statements and connectives](../../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md) give four of them:

| Operation | Symbol | Result bit is 1 when |
|---|---|---|
| AND | $a \,\&\, b$, or $a \wedge b$ | both bits are 1 |
| OR | $a \mid b$, or $a \vee b$ | at least one bit is 1 |
| XOR | $a \oplus b$ | exactly one bit is 1 |
| NOT | $\sim a$, or $\neg a$ | the bit is 0 |

Python writes them `&`, `|`, `^` and `~`, the same as C and Java. In plain words, AND keeps the bits that are on in both patterns, OR keeps the bits that are on in either, XOR keeps the bits where the patterns differ, and NOT flips every bit. For example, with $a = 1100\,1010$ and $b = 1010\,0110$:

$$
\begin{aligned}
a \,\&\, b &= 1000\,0010 \\
a \mid b &= 1110\,1110 \\
a \oplus b &= 0110\,1100 \\
\sim a &= 0011\,0101 \text{ (in 8 bits)}
\end{aligned}
$$

In a fixed width $n$, NOT turns $a$ into $(2^n - 1) - a$, since each bit $b_i$ becomes $1 - b_i$ ([binary arithmetic and two's complement](03-binary-arithmetic-and-twos-complement.md), Theorem 2). Python integers have no fixed width, so it treats $\sim a$ as $-a - 1$, the infinite two's complement version of the same flip. To get an $n$-bit result, mask it: `~a & 0xFF` for 8 bits.

### Shifts

A **left shift** $a \ll k$ moves every bit $k$ places to the left and fills the $k$ places on the right with 0s. A **right shift** $a \gg k$ moves every bit $k$ places to the right and drops the $k$ lowest bits. In a fixed width, a left shift also drops the bits that leave on the left.

For right shifts there are two versions in a fixed width, depending on what fills the new places on the left. A **logical shift** fills them with 0s, which is right for unsigned numbers. An **arithmetic shift** copies the sign bit, which is right for two's complement numbers. Python's `>>` is arithmetic: it behaves as if the number had infinitely many copies of its sign bit on the left.

In plain words, shifting left by $k$ is multiplying by $2^k$, and shifting right by $k$ is dividing by $2^k$ and rounding down. This is the same as moving the decimal point when you multiply or divide by a power of 10: $0.45 \times 100 = 45$ is a shift of two places.

### Masks

A **mask** is an integer whose 1-bits mark the positions you care about. ANDing with a mask keeps those positions and zeros out the rest. The mask for the single bit $i$ is $1 \ll i$, and the mask for the lowest $w$ bits is $(1 \ll w) - 1$, which is $w$ ones. For example, the mask for bit 3 is $1000_2 = 8$, and the mask for the lowest 4 bits is $1111_2 = 15$.

## How to do it

### Test, set, clear and toggle one bit

Let `x` be the number and `i` the position, and let `m = 1 << i` be the mask.

1. To test bit $i$, compute `x & m`. It is nonzero exactly when bit $i$ is 1. Or compute `(x >> i) & 1`, which gives the bit itself, 0 or 1.
2. To set bit $i$ to 1, compute `x | m`. OR with 1 gives 1 and OR with 0 changes nothing, so only position $i$ is affected.
3. To clear bit $i$ to 0, compute `x & ~m`. The mask `~m` has a 0 at position $i$ and 1s everywhere else, so AND keeps everything but bit $i$.
4. To toggle bit $i$, compute `x ^ m`. XOR with 1 flips a bit and XOR with 0 leaves it.
5. Check by printing `x` in binary before and after: only position $i$ should differ.

### Extract and replace a field

1. For a field of width $w$ whose lowest bit is at position $s$, shift it down with `x >> s`.
2. Keep only its $w$ bits with `& ((1 << w) - 1)`.
3. To put a new value `v` into the field, first clear it with `x & ~(((1 << w) - 1) << s)` and then OR in `v << s`.
4. Check that the value read back is `v` and that the other bits didn't change.

### Theorems with proofs

*Theorem 1 (shifts).* For an integer $x \ge 0$ and $k \ge 0$, $x \ll k = x \cdot 2^k$ and $x \gg k = \lfloor x / 2^k \rfloor$. In two's complement, the arithmetic right shift by 1 of a negative number also gives $\lfloor x / 2 \rfloor$.

What we know: $x = \sum b_i 2^i$. What we want: the value after a shift. The plan is to read the shift off the place values, and then handle the sign bit separately.

*Proof.* Moving the bit $b_i$ to position $i + k$ changes its place value from $2^i$ to $2^{i+k}$, so the new number is $\sum b_i 2^{i+k} = 2^k \sum b_i 2^i = 2^k x$. For the right shift, split $x$ into the high part $q = \sum_{i \ge k} b_i 2^{i-k}$ and the low part $r = \sum_{i<k} b_i 2^i$, so that $x = 2^k q + r$ with $0 \le r < 2^k$ (the low $k$ bits are at most $2^k - 1$). Shifting right keeps exactly $q$. By the division algorithm ([long division](../../01-elementary/07-long-division.md)), the quotient is the only integer with this property, so $q = \lfloor x / 2^k \rfloor$.

For a negative $n$-bit value $v = -b_{n-1} 2^{n-1} + \sum_{i=0}^{n-2} b_i 2^i$, an arithmetic shift by 1 drops $b_0$ and copies the sign bit, so the bit $b_{n-1}$ now has the places $n - 1$ and $n - 2$, with weights $-2^{n-1}$ and $2^{n-2}$ in the new number. Each remaining bit $b_i$ moves from weight $2^i$ to $2^{i-1}$. The new value is $-b_{n-1} 2^{n-1} + b_{n-1} 2^{n-2} + \sum_{i \ge 1} b_i 2^{i-1}$, which is $-b_{n-1} 2^{n-2} + \sum_{i=1}^{n-2} b_i 2^{i-1} = \frac{v - b_0}{2}$. The number $v - b_0$ is even, since $v$ and $b_0$ have the same parity, so $\frac{v - b_0}{2} = \lfloor v / 2 \rfloor$. $\blacksquare$

Look back: shifting right rounds down toward $-\infty$, so $-5 \gg 1 = -3$ and $-1 \gg k = -1$ for every $k$. This is the same as Python's `//` ($-5 \mathbin{/\!/} 2 = -3$), but not the same as C's integer division, which truncates toward zero and gives $-5 / 2 = -2$.

*Theorem 2 (clearing the lowest 1).* For an integer $x > 0$, `x & (x - 1)` is $x$ with its lowest 1-bit changed to 0, and `x & -x` is the number with only that bit.

What we know: $x > 0$ has at least one 1-bit. What we want: the effect of subtracting 1. The plan is to write $x$ by its lowest 1.

*Proof.* Let the lowest 1 of $x$ be at position $k$. Then the bits below it are all 0, so $x = A\,1\,0^k$ in binary, where $A$ stands for the bits above position $k$ and $0^k$ is $k$ zeros. Subtracting 1 borrows from that 1: it becomes 0 and the $k$ zeros below it become 1s, so $x - 1 = A\,0\,1^k$. The two numbers agree in $A$ and differ in every position from $k$ down. ANDing, the positions of $A$ keep their bits, position $k$ gives $1 \wedge 0 = 0$, and the lower positions give $0 \wedge 1 = 0$. So $x \,\&\, (x-1) = A\,0\,0^k$, which is $x$ with its lowest 1 cleared.

For the second claim, $-x$ is $\sim x + 1$ in two's complement (lesson 3, Theorem 2). Now $\sim x = \bar{A}\,0\,1^k$ ($\bar{A}$ is $A$ flipped), and adding 1 carries through the $k$ ones and stops at the 0: $-x = \bar{A}\,1\,0^k$. ANDing with $x = A\,1\,0^k$ gives $0\,1\,0^k$ because $A \wedge \bar{A} = 0$, the one bit at position $k$. $\blacksquare$

Look back: two uses follow at once. A positive number is a power of 2 exactly when it has one 1-bit, which is exactly when `x & (x - 1)` is 0. And counting the 1s of $x$ (its **popcount**) takes one loop pass per 1-bit: repeat `x &= x - 1` until `x` is 0 and count the passes. A 32-bit number with 3 ones takes 3 passes, not 32.

*Theorem 3 (XOR rules).* For bit vectors of the same width, XOR is commutative and associative, $a \oplus 0 = a$ and $a \oplus a = 0$.

*Proof.* Each is true in every bit position, by the truth table of $\oplus$: $P \oplus Q = Q \oplus P$; the parity of the number of 1s among three bits doesn't depend on grouping, which gives associativity; $P \oplus 0 = P$; and $P \oplus P = 0$. Since the operation acts on each position separately, it holds for the whole vectors. $\blacksquare$

Look back: these rules say that XOR is addition mod 2 in each position, so it is reversible: $(a \oplus b) \oplus b = a \oplus (b \oplus b) = a \oplus 0 = a$. XOR with the same value twice undoes itself, which is why it appears in checksums, parity bits and simple ciphers.

*Corollary (XOR swap).* The three statements `a ^= b`, `b ^= a`, `a ^= b` swap two variables that are distinct.

*Proof.* Let the starting values be $a_0$ and $b_0$. After the first, $a = a_0 \oplus b_0$. After the second, $b = b_0 \oplus (a_0 \oplus b_0) = a_0 \oplus (b_0 \oplus b_0) = a_0 \oplus 0 = a_0$. After the third, $a = (a_0 \oplus b_0) \oplus a_0 = b_0 \oplus (a_0 \oplus a_0) = b_0$. $\blacksquare$

If the two names refer to the same variable, the first step sets it to $a_0 \oplus a_0 = 0$ and the value is lost.

### Sets as bit vectors

A set $S \subseteq \{0, 1, \dots, n - 1\}$ is stored as the integer $m_S = \sum_{i \in S} 2^i$, so bit $i$ is 1 exactly when $i \in S$. The set operations of [sets and set operations](../../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md) become bitwise operations, because "$i$ is in $S \cap T$" means "bit $i$ is 1 in both":

| Set operation | Operation on the masks `s` and `t` |
|---|---|
| empty set | the integer `0` |
| universe $\{0, \dots, n-1\}$ | `U = (1 << n) - 1` |
| $i \in S$ | `s >> i & 1` is 1 |
| $S \cup T$ | OR of `s` and `t` |
| $S \cap T$ | `s & t` |
| $S \setminus T$ | `s & ~t` |
| complement of $S$ in the universe | `U ^ s` |
| symmetric difference | `s ^ t` |
| $S \subseteq T$ | `s & t == s` |
| $\lvert S \rvert$ | popcount of `s` |

There are $2^n$ subsets of an $n$-element set, and $2^n$ integers from 0 to $2^n - 1$, and the map from a subset to its mask matches them one to one. So counting from 0 to $2^n - 1$ lists every subset exactly once, which is how programs loop over all subsets. De Morgan's laws carry over unchanged: $\sim(s \mid t) = \sim s \,\&\, \sim t$ is the complement of a union.

## Worked examples

<div class="example" markdown>

### Example 1: flags in a byte

Let `x = 0b0101_1010`, which is 90. Use the steps for one bit.

Step 1, test: bit 3 is `(x >> 3) & 1`. Shifting right by 3 gives $0000\,1011$, whose last bit is 1, so bit 3 is on. The mask way agrees: `x & 0b1000` is 8, which is nonzero.

Step 2, set bit 0: `x | 1` is $0101\,1010 \mid 0000\,0001 = 0101\,1011$.

Step 3, clear bit 3: the mask `~(1 << 3)` is $\ldots1111\,0111$, so `x & ~(1 << 3)` is $0101\,0010$. The bit was on, and now it is off.

Step 4, toggle bit 6: `x ^ (1 << 6)` is $0101\,1010 \oplus 0100\,0000 = 0001\,1010$. Toggling again with the same mask gives back $0101\,1010$.

Step 5, the check: in each result, only the chosen position differs from $0101\,1010$.

<div class="warning" markdown>

Watch out at step 3: write `x & ~m`, not `x & m`. ANDing with the mask itself keeps only bit $i$ and wipes the other seven bits.

</div>

</div>

<div class="example" markdown>

### Example 2: shifts, colours and negative numbers

(a) $13 \ll 3 = 13 \cdot 8 = 104$, and $100 \gg 3 = \lfloor 100 / 8 \rfloor = 12$, where the lost bits $100 = 12 \cdot 8 + 4$ were the remainder 4. Also $45 \,\&\, 3 = 1$, because the mask $3 = 11_2$ keeps the lowest 2 bits, and $45 \bmod 4 = 1$: masking with $2^k - 1$ is the remainder after dividing by $2^k$.

(b) A web colour such as `0xFF8800` packs three bytes. The red byte is `(c >> 16) & 0xFF`, which is 255, the green byte is `(c >> 8) & 0xFF`, which is 136, and the blue byte is `c & 0xFF`, which is 0. Shifting brings a field to the right end, and the mask $\mathrm{FF}_{16}$ throws away the fields above it.

(c) For negatives, $-5 \gg 1 = -3$, not $-2$: the true quotient is $-2.5$, and the shift rounds down (Theorem 1). Likewise $-9 \gg 1 = -5$. And $-5 \ll 1 = -10$, because left shifts multiply by 2.

Check: `-5 // 2` is also $-3$ in Python, and `13 * 8` is 104.

</div>

<div class="example" markdown>

### Example 3: counting bits and an edge case

Count the 1s of $x = 44 = 101100_2$ with `x &= x - 1`. In the first pass, $44 = 101100$ and $43 = 101011$ give $101000 = 40$. In the second, $40 \,\&\, 39 = 101000 \,\&\, 100111 = 100000 = 32$. In the third, $32 \,\&\, 31 = 0$. That is 3 passes, so $44$ has three 1s. Each pass cleared the lowest 1, as Theorem 2 says.

The edge case is $x = 0$. Then `x & (x - 1)` is $0 \,\&\, (-1) = 0$, so the power-of-2 test `x & (x - 1) == 0` wrongly says that 0 is a power of 2. That is why the correct test is `x > 0 and x & (x - 1) == 0`.

Check: `bin(44).count("1")` is 3, and the test is true for 1, 2, 4, 8 and false for 6 and 12.

</div>

<div class="example" markdown>

### Example 4: sets as masks (finish it yourself)

Take the universe $\{0, \dots, 7\}$, with $A = \{1, 3, 4\}$ and $B = \{3, 4, 6\}$. Their masks are $A = 2 + 8 + 16 = 26 = 0001\,1010$ and $B = 8 + 16 + 64 = 88 = 0101\,1000$. The union is $26 \mid 88 = 0101\,1010 = 90$, which is $\{1, 3, 4, 6\}$, and the intersection is $26 \,\&\, 88 = 0001\,1000 = 24$, which is $\{3, 4\}$. Now find the difference $A \setminus B$ and the complement of $A$ in the universe, as masks and as sets.

<details class="solution" markdown>
<summary>Finish</summary>

The difference is `26 & ~88`. Since $\sim 88 = 1010\,0111$ in 8 bits, the AND with $0001\,1010$ is $0000\,0010 = 2$, which is $\{1\}$. The complement is `255 ^ 26`, and $1111\,1111 \oplus 0001\,1010 = 1110\,0101 = 229$, which is $\{0, 2, 5, 6, 7\}$.

Check: $A \setminus B$ is the elements of $A$ not in $B$, which is just 1. The complement has $8 - 3 = 5$ elements, and $229$ has five 1s.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for precedence, which differs between languages. In Python, `&`, `|` and `^` bind tighter than comparisons, so `x & 1 == 0` means `(x & 1) == 0`. In C and Java, `==` binds tighter, so the same text means `x & (1 == 0)`, which is always 0. In both, `+` binds tighter than shifts, so `1 << i + 1` is `1 << (i + 1)`. Put brackets around every bitwise operation that sits next to something else.

</div>

<div class="warning" markdown>

Watch out: `^` in Python is XOR, not a power, and `&` and `|` are not `and` and `or`. The operators `and` and `or` work on whole truth values and return one of their operands, and `&` and `|` work on every bit. So `6 and 3` is `3`, while `6 & 3` is `2`. In C, `&&` is the logical one and `&` the bitwise one.

</div>

<div class="warning" markdown>

Watch out: `~x` in Python is $-x - 1$, not the 8-bit flip. `~5` is `-6`, not `250`. To flip within a width, mask: `~5 & 0xFF` is `250`.

</div>

<div class="warning" markdown>

Watch out when you shift a negative number right and expect a logical shift. Python has no logical shift for negatives: `-1 >> 4` is still `-1`. To get a logical shift of a byte, mask first: `(x & 0xFF) >> 4`. In C, a right shift of a negative signed number is implementation-defined (usually arithmetic), and a shift by the width or more is undefined. Shifting by a negative count is an error in Python.

</div>

In a fixed width, `x << k` loses the bits that move past the top, so it doesn't always equal `x * 2**k`: in 8 bits, $200 \ll 1$ is $144$, not 400, since $400 \bmod 256 = 144$. Python integers never lose bits, so it takes a mask, `(x << k) & 0xFF`, to imitate the machine.

XOR swap is a curiosity. It needs no temporary variable, but in Python `a, b = b, a` is clearer, and compilers use registers anyway. It also fails when both names are the same variable, as shown above.

## Tricks and shortcuts

- A number is odd exactly when `x & 1` is 1, and `x & (2**k - 1)` is $x \bmod 2^k$, even for negative `x` in Python.
- To round up to a multiple of 8, use `(x + 7) & ~7`: $43 \to 48$. This works for each power of 2 in place of 8, and it is how allocators align sizes.
- `x & -x` isolates the lowest 1, and `x | (x + 1)` turns on the lowest 0.
- XOR cancels pairs: the XOR of a list in which every number appears twice, except one, is that one. The XOR of `[4, 9, 4, 7, 9]` is 7.
- Gray code, `n ^ (n >> 1)`, lists the numbers $0, 1, 3, 2, 6, 7, 5, 4$ for $n = 0, \dots, 7$: consecutive entries differ in exactly one bit. This is the row and column order of the Karnaugh maps in [boolean algebra and logic gates](06-boolean-algebra-and-logic-gates.md).
- To loop over all subsets of a mask, start at `sub = mask` and repeat `sub = (sub - 1) & mask` until 0. For `0b1011` it visits 1011, 1010, 1001, 1000, 0011, 0010, 0001, 0000.

## In code

Everything above runs as written. The asserts at the end of the middle block check the three tricks for every number below 5,000, and the last block shows bit sets and subsets.

<details class="code" markdown>
<summary>In code</summary>

```python
a, b = 0b1100_1010, 0b1010_0110
print(format(a & b, "08b"), format(a | b, "08b"), format(a ^ b, "08b"))  # 10000010 11101110 01101100
print(format(~a & 0xFF, "08b"), ~a, ~0, ~-1)                  # 00110101 -203 -1 0
print(format(a << 2 & 0xFF, "08b"), a << 2, a >> 2, 13 << 3, 100 >> 3)  # 00101000 808 50 104 12

# masks on one bit
x = 0b0101_1010
i = 3
print((x >> i) & 1, x & (1 << i) != 0)                         # 1 True
print(format(x | (1 << 0), "08b"))                             # 01011011  set bit 0
print(format(x & ~(1 << i), "08b"))                            # 01010010  clear bit 3
print(format(x ^ (1 << 6), "08b"))                             # 00011010  toggle bit 6

# a field: bits 4 to 6 (width 3, start 4)
print((x >> 4) & ((1 << 3) - 1))                               # 5

# shifts on negatives: >> rounds toward minus infinity, like //
print(-5 >> 1, -5 // 2, int(-5 / 2), -1 >> 10, -8 >> 1)          # -3 -3 -2 -1 -4
print(-5 << 1, -5 * 2)                                          # -10 -10

# tricks
def lowest_clear(n): return n & (n - 1)
def lowest_bit(n): return n & -n
def is_power_of_two(n): return n > 0 and n & (n - 1) == 0
def popcount(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

print(format(lowest_clear(0b101100), "06b"), format(lowest_bit(0b101100), "06b"))  # 101000 000100
print([n for n in range(1, 70) if is_power_of_two(n)])         # [1, 2, 4, 8, 16, 32, 64]
print(popcount(0b1011_0111), (0b1011_0111).bit_count(), bin(0b1011_0111).count("1"))  # 6 6 6
assert all(popcount(n) == n.bit_count() for n in range(5000))
assert all(lowest_clear(n) == n - lowest_bit(n) for n in range(1, 5000))
assert all(is_power_of_two(n) == (n.bit_count() == 1) for n in range(1, 5000))

# xor swap
p, q = 12, 5
p ^= q
q ^= p
p ^= q
print(p, q)                                                    # 5 12
r = [7]
r[0] ^= r[0]
print(r[0])                                                    # 0  (swapping a variable with itself clears it)

# xor cancels pairs
from functools import reduce
print(reduce(lambda u, v: u ^ v, [3, 5, 3, 9, 9]))             # 5

# bit sets
def to_mask(items): return sum(1 << i for i in items)
def to_set(m): return {i for i in range(m.bit_length()) if m >> i & 1}
A, B = to_mask({1, 3, 4}), to_mask({3, 4, 6})
U = (1 << 8) - 1                                               # universe {0, ..., 7}
print(to_set(A | B), to_set(A & B), to_set(A & ~B), to_set(A ^ B), to_set(U ^ A))
# {1, 3, 4, 6} {3, 4} {1} {1, 6} {0, 2, 5, 6, 7}
print((A & B) == A, (A & (A | B)) == A, A.bit_count())         # False True 3
print(~(A | B) & U == (~A & U) & (~B & U))                     # True  (De Morgan)

# all subsets of a 3-element set, then the submasks of a mask
n = 3
print([to_set(m) for m in range(1 << n)])
# [set(), {0}, {1}, {0, 1}, {2}, {0, 2}, {1, 2}, {0, 1, 2}]
mask = 0b1011
sub, subs = mask, []
while True:
    subs.append(sub)
    if sub == 0:
        break
    sub = (sub - 1) & mask
print([format(s, "04b") for s in subs])
# ['1011', '1010', '1001', '1000', '0011', '0010', '0001', '0000']

# colour packing, and permissions
colour = 0xFF8800
print((colour >> 16) & 0xFF, (colour >> 8) & 0xFF, colour & 0xFF)   # 255 136 0
mode = 0o755
print(oct(mode & 0o700), oct(mode & ~0o022), oct(mode | 0o002))      # 0o700 0o755 0o757
```

The method `int.bit_count()` needs Python 3.10 or later. The last line shows the permission bits from the start of the lesson: `mode & 0o700` keeps the owner's bits, `mode & ~0o022` removes write permission for group and others (it was already off for both, so nothing changes), and `mode | 0o002` turns on write for others.

</details>

## FAQ

### What is the difference between `&` and `and`?

`&` works on every bit of two integers and returns an integer. `and` treats each side as true or false, stops early if the left side is false, and returns one of its operands. `6 & 3` is `2` (bits $110 \,\&\, 011 = 010$), but `6 and 3` is `3`. For booleans both agree, but `True & False` doesn't short-circuit.

### Why is `~x` equal to `-x - 1`?

Flipping every bit of $x$ turns it into $(2^n - 1) - x$ in $n$ bits. Reading that pattern in two's complement, where $2^n - 1$ is the pattern of $-1$, gives $-1 - x$. This is the same fact as "flip and add one" in the other direction: $-x = \sim x + 1$.

### Is a shift faster than multiplying by 2?

On modern machines a compiler turns `x * 8` into a shift by itself, so write the multiplication when you mean a product and the shift when you mean bit manipulation. The reason to prefer shifts is clarity, when you are really packing and unpacking fields.

### Why do hash functions and cryptography use XOR and shifts so much?

XOR is reversible and mixes bits without carries, and shifts move bits between positions, so a few of them spread each input bit across the output. They are also the cheapest operations in hardware. Real designs combine them with additions mod $2^{32}$ or $2^{64}$ ([binary arithmetic and two's complement](03-binary-arithmetic-and-twos-complement.md)).

## Practice

### Warm-up

1\. Work out $10110 \,\&\, 01101$, $10110 \mid 01101$ and $10110 \oplus 01101$ on 5-bit patterns.

<details class="solution" markdown>
<summary>Solution</summary>

Going down the columns, AND is $00100$, OR is $11111$ and XOR is $11011$.

Check: in each position, OR is 1 when AND is 1 or XOR is 1, and never both at once. So AND $+$ XOR as plain integers equals the OR: $4 + 27 = 31 = 11111_2$.

</details>

2\. For an 8-bit value `x`, write expressions that (a) set bit 4, (b) clear bit 0, (c) toggle bit 7, and (d) test whether bit 2 is on.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) `x | (1 << 4)`, or `x | 16`.
- (b) `x & ~1`, or `x & 0xFE` in 8 bits.
- (c) `x ^ (1 << 7)`, or `x ^ 0x80`.
- (d) `(x >> 2) & 1`, or `x & 4 != 0`.

Check with `x = 0b1010_0101`: (a) gives `0b1011_0101`, (b) gives `0b1010_0100`, (c) gives `0b0010_0101`, and (d) gives 1 because bit 2 is on.

</details>

3\. Evaluate $13 \ll 2$, $45 \gg 2$, $-9 \gg 1$ and $45 \,\&\, 3$, and say what $45 \bmod 4$ is.

<details class="solution" markdown>
<summary>Solution</summary>

$13 \ll 2 = 13 \cdot 4 = 52$. $45 \gg 2 = \lfloor 45 / 4 \rfloor = 11$. $-9 \gg 1 = \lfloor -4.5 \rfloor = -5$. $45 \,\&\, 3$ keeps the lowest 2 bits of $101101_2$, which are $01$, so it is 1, and $45 \bmod 4 = 1$ as well.

Check: $11 \cdot 4 + 1 = 45$, and in Python `-9 // 2` is $-5$ too.

</details>

### Standard

4\. Trace the popcount loop `x &= x - 1` on $214 = 11010110_2$, writing $x$ before and after each pass, and say how many passes it takes and why.

<details class="solution" markdown>
<summary>Solution</summary>

The passes are $214 \to 212$, $212 \to 208$, $208 \to 192$, $192 \to 128$ and $128 \to 0$. That is $11010110 \to 11010100 \to 11010000 \to 11000000 \to 10000000 \to 0$, and each pass clears the lowest 1. There are 5 passes, so 214 has five 1s.

Check: $11010110_2$ has the ones $1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 = 5$, and `(214).bit_count()` is 5.

</details>

5\. Use masks for the universe $\{0, \dots, 9\}$. Let $A = \{0, 2, 5, 9\}$ and $B = \{2, 3, 9\}$. Find the masks of $A$ and $B$ as integers, and then the masks and sets for $A \cup B$, $A \cap B$, $A \setminus B$ and the complement of $A$.

<details class="solution" markdown>
<summary>Solution</summary>

The masks are $A = 2^0 + 2^2 + 2^5 + 2^9 = 549 = 10\,0010\,0101_2$ and $B = 2^2 + 2^3 + 2^9 = 524 = 10\,0000\,1100_2$.

- $A \cup B$: `549 | 524` is 557, which is $10\,0010\,1101_2$, the set $\{0, 2, 3, 5, 9\}$.
- $A \cap B$: `549 & 524` is 516, which is $10\,0000\,0100_2$, the set $\{2, 9\}$.
- $A \setminus B$: `549 & ~524` is 33, which is $00\,0010\,0001_2$, the set $\{0, 5\}$.
- Complement of $A$: `1023 ^ 549` is 474, which is $01\,1101\,1010_2$, the set $\{1, 3, 4, 6, 7, 8\}$.

Check: the sizes are consistent, since $\lvert A \cup B \rvert = 4 + 3 - 2 = 5$, and the complement has $10 - 4 = 6$ elements.

</details>

6\. A made-up 16-bit date format stores (year $- 2000$) in 7 bits, month in 4 bits and day in 5 bits, in that order from the top. Pack 21 October 2026 into one integer, give it in hex, and unpack it.

<details class="solution" markdown>
<summary>Solution</summary>

The year field is $26$, the month is 10 and the day is 21. The day occupies bits 0 to 4, the month bits 5 to 8 and the year bits 9 to 15. So the packed number is

$$
(26 \ll 9) \mid (10 \ll 5) \mid 21 = 13312 + 320 + 21 = 13653 = \mathrm{3555}_{16}.
$$

To unpack: the year field is `v >> 9`, which is 26, the month is `(v >> 5) & 15`, which is 10, and the day is `v & 31`, which is 21.

Check: $\mathrm{3555}_{16} = 0011\,0101\,0101\,0101_2$. The top 7 bits $0011010$ are 26, the next 4 bits $1010$ are 10 and the last 5 bits $10101$ are 21.

</details>

### Challenge

7\. A list has an odd number of integers. Every value appears exactly twice, except one value that appears once. Prove that the XOR of all the entries is the value that appears once, and say how fast it is.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: Theorem 3 (XOR is commutative and associative, $a \oplus a = 0$, $a \oplus 0 = a$). What we want: the total XOR. The plan is to regroup the terms so that the equal pairs meet.

Because XOR is commutative and associative, the entries can be reordered and regrouped freely. Put each pair of equal values next to each other, with the single value $u$ left over. Each pair gives $v \oplus v = 0$, so the total is $0 \oplus 0 \oplus \dots \oplus 0 \oplus u = u$.

It takes one pass over the list, so the time is proportional to the length and only one integer of extra memory is used. Counting or sorting would need more.

Check: `reduce(xor, [4, 9, 4, 7, 9])` is 7, since $4 \oplus 9 \oplus 4 \oplus 7 \oplus 9 = (4 \oplus 4) \oplus (9 \oplus 9) \oplus 7 = 7$.

</details>

8\. (Reviews [truth tables and logical equivalence](../../04-proofs-and-logic/02-logic-and-sets/03-truth-tables-and-logical-equivalence.md).) Show that $a \oplus b = (a \mid b) \,\&\, \sim(a \,\&\, b)$ for bit vectors, and test it on all pairs of 4-bit numbers in Python.

<details class="solution" markdown>
<summary>Solution</summary>

All operations act position by position, so it is enough to prove it for single bits $P$ and $Q$. The statement is $P \oplus Q \equiv (P \vee Q) \wedge \neg(P \wedge Q)$, which is the table of exercise 4 in that lesson: both sides read 0, 1, 1, 0 on the rows $(0,0), (0,1), (1,0), (1,1)$. Since it holds in every position, it holds for whole vectors.

In Python, `all((a ^ b) == ((a | b) & ~(a & b)) for a in range(16) for b in range(16))` is `True`.

Check one pair by hand: $a = 1100$ and $b = 1010$ give $a \mid b = 1110$, $a \,\&\, b = 1000$, so $1110 \,\&\, \sim 1000 = 0110$, which is $a \oplus b$.

</details>

## Where this shows up

- The next lesson, [boolean algebra and logic gates](06-boolean-algebra-and-logic-gates.md), builds each of these operations from gates, and a processor does a bitwise AND of two words with one row of AND gates.
- Systems code is full of masks: permission flags, network masks and IP addresses, page tables, register fields, bit-packed data structures, and bitmask dynamic programming over subsets, which uses the subset loop above ([counting rules](../03-counting-and-discrete-probability/01-counting-rules.md) explains the $2^n$ count).
- Hashing, checksums, random number generators and cryptography are built from XOR, shifts and addition mod $2^n$. Parity and error-correcting codes are XOR over bit positions.
