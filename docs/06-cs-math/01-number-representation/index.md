# Number representation

How computers store numbers and information: bases, bits, integers, floating point, bit operations and the logic gates that do the arithmetic.

1. [Number bases and conversions](01-number-bases-and-conversions.md)
2. [Bits and information](02-bits-and-information.md)
3. [Binary arithmetic and two's complement](03-binary-arithmetic-and-twos-complement.md)
4. [Floating point basics](04-floating-point-basics.md)
5. [Bitwise operations and masks](05-bitwise-operations-and-masks.md)
6. [Boolean algebra and logic gates](06-boolean-algebra-and-logic-gates.md)

## Cheat sheet

### Number bases and conversions

A string of digits $d_k \dots d_0$ in base $b$ means $\sum d_i b^i$, with each digit from 0 to $b - 1$.

| Task | Method | Example |
|---|---|---|
| base $b$ to decimal | Horner: multiply the total by $b$, add the next digit | $\mathrm{A91}_{16} = (10 \cdot 16 + 9) \cdot 16 + 1 = 2{,}705$ |
| decimal to base $b$ | divide by $b$ until the quotient is 0, read the remainders bottom up | $45 = 101101_2$ |
| binary to hex or octal | group bits in 4s (hex) or 3s (octal) from the right | $1101\,0110_2 = \mathrm{D6}_{16}$ |

- $n$ bits hold $2^n$ values, from 0 to $2^n - 1$. A byte holds 0 to 255.
- Powers of 2 to know: $2^{10} = 1{,}024 \approx 10^3$, $2^{16} = 65{,}536$, $2^{32} \approx 4.3 \times 10^9$.

Main mistakes: reading remainders top down, grouping bits from the left, dropping zeros at the right end, and taking $2^n$ as the top of the $n$-bit range.

### Bits and information

| Quantity | Formula | Example |
|---|---|---|
| bits to label $N$ values | $\lceil \log_2 N \rceil$, or `(N - 1).bit_length()` | 365 days need 9 bits |
| information in an outcome | $-\log_2 p$ | $p = \frac{1}{1024}$ carries 10 bits |
| entropy | $H = -\sum p_i \log_2 p_i$ | coin with $p = 0.9$: 0.469 bits |
| bound | $0 \le H \le \log_2 N$, equal to $\log_2 N$ only for the uniform case | fair die: 2.585 bits |

- Units: kB $= 10^3$ bytes and KiB $= 2^{10}$, MB and MiB, GB and GiB, TB and TiB. A "1 TB" drive is 931 GiB. Network speeds are in bits per second, so 100 Mbit/s is at most 12.5 MB/s.
- Pigeonhole: there are $2^n$ strings of $n$ bits and only $2^n - 1$ shorter ones, so no lossless compressor shrinks every file. Fewer than 1 file in 128 can shrink by a byte or more.
- When all probabilities are powers of $\frac{1}{2}$, a prefix code reaches the entropy: $\frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \frac{1}{8}$ gives $H = 1.75$ with the codes 0, 10, 110, 111.

Main mistakes: using `math.ceil(math.log2(N))` for large $N$, weighting every surprisal equally, computing $\log_2 0$, and treating a bit of storage as a bit of information.

### Binary arithmetic and two's complement

Add column by column with carries ($1 + 1 = 10_2$). In $n$ bits, a carry out of the top is lost, so results wrap modulo $2^n$.

| Fact | Statement |
|---|---|
| unsigned range | 0 to $2^n - 1$ |
| two's complement value | $-b_{n-1} 2^{n-1} + \sum_{i<n-1} b_i 2^i$ |
| signed range | $-2^{n-1}$ to $2^{n-1} - 1$: 8 bits $-128$ to 127, 32 bits $-2{,}147{,}483{,}648$ to $2{,}147{,}483{,}647$ |
| pattern of $x$ | the binary form of $x \bmod 2^n$, so $-37$ is $256 - 37 = 219 = \mathrm{DB}_{16}$ |
| negate | flip every bit and add 1; the smallest number negates to itself |
| subtract | $a - b = a + \mathrm{NOT}(b) + 1$ |
| sign extension | copy the sign bit to widen a signed value; widen unsigned values with zeros |

- Signed overflow happens exactly when both inputs have the same sign and the result has the other sign. In hardware, it is the carry into the sign bit XOR the carry out of it.
- Unsigned overflow is a carry out of the top bit. The two kinds are independent: $\mathrm{FF}_{16} + 01_{16}$ overflows unsigned only.
- In Python, `x & (2**n - 1)` keeps $n$ bits, and `u - 2**n if u >> (n - 1) else u` reads an $n$-bit pattern as signed.
- In hex, a first digit of 8 to F means negative: `0xFF` is $-1$ and `0x80` is $-128$ in 8 bits.

Main mistakes: flipping without adding 1, negating the smallest number, confusing signed and unsigned overflow, and zero-extending a signed value.

### Floating point basics

A normal float is $(-1)^s \times 1.f \times 2^{E - \text{bias}}$.

| | Sign, exponent, fraction | Bias | Epsilon $2^{-m}$ | Largest finite value |
|---|---|---|---|---|
| binary32 | 1, 8, 23 | 127 | $2^{-23} \approx 1.19 \times 10^{-7}$ | $\approx 3.4 \times 10^{38}$ |
| binary64 | 1, 11, 52 | 1,023 | $2^{-52} \approx 2.22 \times 10^{-16}$ | $\approx 1.8 \times 10^{308}$ |

- Exponent field all 0s: zero and subnormals. All 1s: infinity (fraction 0) or NaN (fraction not 0). NaN is not equal to itself.
- The spacing of doubles in $[2^e, 2^{e+1})$ is $2^{e-52}$, so the relative rounding error is at most $2^{-53}$. Integers are exact up to $2^{53}$.
- Rounding is to nearest, ties to even. A fraction $\frac{a}{b}$ in lowest terms is exact only when $b$ is a power of 2, so 0.1 is not exact and $0.1 + 0.2 = 0.30000000000000004$.
- Compare with `math.isclose(a, b)`, and add `abs_tol` when one side may be 0. Use integer cents or `Decimal` for money.
- Cancellation: avoid subtracting nearly equal numbers. Use $1 - \cos x = 2\sin^2 \frac{x}{2}$ and $\sqrt{x+1} - \sqrt{x} = \frac{1}{\sqrt{x+1} + \sqrt{x}}$, or `math.expm1` and `math.log1p`.

Main mistakes: testing floats with `==`, reading the exponent field without subtracting the bias, expecting `x + 1 != x` above $2^{53}$, and giving `isclose` no absolute tolerance near 0.

### Bitwise operations and masks

| Task | Expression |
|---|---|
| test bit $i$ | `(x >> i) & 1` |
| set bit $i$ | OR `x` with `1 << i` |
| clear bit $i$ | `x & ~(1 << i)` |
| toggle bit $i$ | `x ^ (1 << i)` |
| lowest $w$ bits | `x & ((1 << w) - 1)`, which is $x \bmod 2^w$ |
| field of width $w$ at $s$ | `(x >> s) & ((1 << w) - 1)` |

- `x << k` is $x \cdot 2^k$, and `x >> k` is $\lfloor x / 2^k \rfloor$, rounding toward $-\infty$ for negatives: `-5 >> 1` is $-3$.
- `x & (x - 1)` clears the lowest 1 bit, `x & -x` isolates it, and a positive $x$ is a power of 2 exactly when `x & (x - 1) == 0`. Popcount takes one pass per 1 bit.
- XOR rules: commutative, associative, $a \oplus 0 = a$, $a \oplus a = 0$. They make XOR swap work and cancel pairs in a list.
- Sets of $\{0, \dots, n-1\}$ as masks: union is OR, intersection is `&`, difference is `s & ~t`, complement is `U ^ s`, subset is `s & t == s`, and size is popcount.
- Python precedence differs from C: `x & 1 == 0` is `(x & 1) == 0` in Python and `x & (1 == 0)` in C. Use brackets.

Main mistakes: `x & m` for clearing, `~x` read as an 8-bit flip (in Python `~5` is $-6$), expecting a logical shift on a negative Python integer, and `x & (x - 1) == 0` without `x > 0`.

### Boolean algebra and logic gates

The laws of logical equivalence hold for 0 and 1, and swapping $\wedge$ with $\vee$ and 0 with 1 in a law gives another law (duality).

| Gate | Outputs for 00, 01, 10, 11 |
|---|---|
| AND | 0, 0, 0, 1 |
| OR | 0, 1, 1, 1 |
| NAND | 1, 1, 1, 0 |
| NOR | 1, 0, 0, 0 |
| XOR | 0, 1, 1, 0 |

- A function of $n$ variables is a truth table with $2^n$ rows, and there are $2^{2^n}$ of them.
- DNF: OR the minterms of the 1-rows. CNF: AND the maxterms of the 0-rows, with each variable negated where the row has a 1.
- NAND is universal: $\neg P = P \uparrow P$, $P \wedge Q = (P \uparrow Q) \uparrow (P \uparrow Q)$, $P \vee Q = (P \uparrow P) \uparrow (Q \uparrow Q)$. NOR is universal by duality.
- Half adder: sum $a \oplus b$, carry $a \wedge b$. Full adder: sum $a \oplus b \oplus c$, carry-out is the majority of $a$, $b$, $c$. Two half adders and an OR make a full adder.
- A ripple-carry adder chains $n$ full adders. Its output is the sum modulo $2^n$ plus the carry out, and its delay grows with $n$.
- K-map for 3 variables: columns in Gray code order $00, 01, 11, 10$, groups of 1, 2, 4 or 8 cells, edges wrap, largest groups, every 1 covered. Each group is the AND of the variables that stay constant in it.

Main mistakes: using the DNF literal rule for a CNF, cancelling in Boolean algebra, using binary order on a K-map, and grouping in threes or L shapes.
