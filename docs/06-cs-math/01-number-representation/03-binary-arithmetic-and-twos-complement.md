# Binary arithmetic and two's complement

After this lesson you can add and subtract binary numbers by hand, write negative integers in two's complement, say what an $n$-bit integer can hold, detect overflow, extend a value to more bits, and simulate fixed-width integers in Python.

Before this: [number bases and conversions](01-number-bases-and-conversions.md) and [bits and information](02-bits-and-information.md). The proofs use remainders, so [long division](../../01-elementary/07-long-division.md) and [divisibility and modular arithmetic](../02-number-theory/01-divisibility-and-modular-arithmetic.md) help.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Add $0110\,1101_2$ and $0011\,1011_2$ by hand, and check in decimal.
2. Write $-37$ as an 8-bit two's complement number, in binary and in hex.
3. What do the 8 bits $1011\,0110$ mean as an unsigned number, and as a two's complement number?

<details class="solution" markdown>
<summary>Answers</summary>

1. The sum is $1010\,1000_2$. In decimal, $109 + 59 = 168 = 128 + 32 + 8$.
2. Since $37 = 0010\,0101_2$, flip the bits to get $1101\,1010$ and add 1 to get $1101\,1011_2 = \mathrm{DB}_{16}$. Check: $256 - 37 = 219 = \mathrm{DB}_{16}$.
3. Unsigned it is $128 + 32 + 16 + 4 + 2 = 182$. In two's complement the top bit is worth $-128$, so it is $-128 + 54 = -74$.

</details>

## The idea

A car odometer with three wheels shows 000 after 999. Turn it backwards from 000 and it shows 999. Suppose we agree that 999 means $-1$, 998 means $-2$ and so on. Then the odometer can do subtraction by adding: from 005, adding 998 gives 1003, and the odometer drops the thousand and shows 003. We wanted $5 - 2 = 3$, and 998 was our name for $-2$. The wrap-around did the work of the minus sign.

Computers do exactly this with bits. An $n$-bit register is an odometer with $n$ wheels that show only 0 or 1. When it counts past $2^n - 1$ it wraps to 0, and counting down from 0 wraps to $2^n - 1$. If the patterns just below $2^n$ are named as the negative numbers, the same adder circuit works for positive and negative numbers, with no special cases and no separate subtracting circuit. That naming is called two's complement, and nearly every processor uses it for signed integers.

This lesson shows how to add and subtract by hand first, then why the naming works and what it costs. The cost is a fixed range: results that don't fit wrap around, and this is the source of overflow bugs.

## Definitions

### Unsigned integers and carries

An **unsigned integer** of $n$ bits is a bit string $b_{n-1} \dots b_1 b_0$ read as the binary number $\sum_{i=0}^{n-1} b_i 2^i$ ([number bases and conversions](01-number-bases-and-conversions.md)). It can hold each integer from 0 to $2^n - 1$ once. For $n = 8$ the range is 0 to 255, for $n = 16$ it is 0 to 65,535, and for $n = 32$ it is 0 to 4,294,967,295.

When you add two bits in a column, the column sum can be 0, 1, 2 or 3 (two bits and a **carry**, the 0 or 1 that comes in from the column to the right). A sum of 2 is written $10_2$ and a sum of 3 is $11_2$, so the column writes the last bit and carries the other one left. In plain words, this is carrying in decimal addition, with ten replaced by two.

When the sum of two $n$-bit numbers is $2^n$ or more, it needs $n + 1$ bits. The extra bit is the carry out of the top column. A fixed-width register has no room for it, so the register keeps the lowest $n$ bits. This is **unsigned overflow**, and it wraps the result around: in 8 bits, $255 + 1 = 0$ and $200 + 100 = 44$.

### Sign-magnitude

In **sign-magnitude** the top bit is a sign (0 for plus, 1 for minus) and the other $n - 1$ bits are the size. In 4 bits, $0011$ is $+3$ and $1011$ is $-3$. The range is $-(2^{n-1} - 1)$ to $2^{n-1} - 1$.

It is the way people write numbers, but it has two problems for hardware. There are two zeros, $0000$ and $1000$ ($+0$ and $-0$), so one pattern is wasted and equality needs a special case. Adding is also different for different signs. Adding the patterns $0011$ ($+3$) and $1001$ ($-1$) as plain binary gives $1100$, which reads as $-4$, not $+2$. A sign-magnitude adder must compare sizes and choose between adding and subtracting. A simpler scheme avoids all of this.

### Two's complement

In an $n$-bit **two's complement** integer, the top bit has place value $-2^{n-1}$ and the others have their usual place values. The bit string $b_{n-1} b_{n-2} \dots b_0$ has the value

$$
v = -b_{n-1} 2^{n-1} + \sum_{i=0}^{n-2} b_i 2^i.
$$

The top bit is called the sign bit. In plain words, it counts as $-128$ in 8 bits, $-32{,}768$ in 16 bits, and so on. If it is 0, the number is read as usual and is between 0 and $2^{n-1} - 1$. If it is 1, the number is $-2^{n-1}$ plus the value of the other bits, which is between $-2^{n-1}$ and $-1$.

So the range is $-2^{n-1}$ to $2^{n-1} - 1$, and every integer in it has exactly one pattern. The range has one more negative number than positive ones, because zero uses a pattern with the sign bit off.

| Width $n$ | Smallest | Largest |
|---|---|---|
| 8 | $-128$ | 127 |
| 16 | $-32{,}768$ | 32,767 |
| 32 | $-2{,}147{,}483{,}648$ | 2,147,483,647 |
| 64 | $-2^{63}$ | $2^{63} - 1 = 9{,}223{,}372{,}036{,}854{,}775{,}807$ |

The table lists all 16 four-bit patterns in the three readings:

| Bits | Unsigned | Sign-magnitude | Two's complement |
|---|---|---|---|
| 0000 | 0 | 0 | 0 |
| 0001 | 1 | 1 | 1 |
| 0010 | 2 | 2 | 2 |
| 0011 | 3 | 3 | 3 |
| 0100 | 4 | 4 | 4 |
| 0101 | 5 | 5 | 5 |
| 0110 | 6 | 6 | 6 |
| 0111 | 7 | 7 | 7 |
| 1000 | 8 | 0 | $-8$ |
| 1001 | 9 | $-1$ | $-7$ |
| 1010 | 10 | $-2$ | $-6$ |
| 1011 | 11 | $-3$ | $-5$ |
| 1100 | 12 | $-4$ | $-4$ |
| 1101 | 13 | $-5$ | $-3$ |
| 1110 | 14 | $-6$ | $-2$ |
| 1111 | 15 | $-7$ | $-1$ |

Read the two's complement column from the bottom: $1111$ is $-1$, and counting up from there wraps through $0000$ to $0001$, with no gap and no repeated zero.

### Remainders and overflow

Two integers $a$ and $b$ are **congruent modulo $m$**, written $a \equiv b \pmod{m}$, when $m$ divides $a - b$. In plain words, they leave the same remainder when divided by $m$. For example, $-37 \equiv 219 \pmod{256}$, since $219 - (-37) = 256$. Each integer has exactly one congruent value in the range 0 to $m - 1$, its remainder, which Python writes `a % m`.

A signed operation **overflows** when its true result is outside the range of the type, so the stored value is not the true result. In two's complement, the stored value is always congruent to the true result modulo $2^n$ (Theorem 3 below), but it is a different integer.

## How to do it

### Adding in binary by hand

1. Line up the numbers on the right, padding the shorter one with zeros on the left.
2. Work from the rightmost column. Add the two bits and the carry coming in (0 for the first column).
3. Write the last bit of the column sum ($0$, $1$, $0$ or $1$ for sums 0, 1, 2, 3) and carry the other bit to the next column: sums 2 and 3 carry 1.
4. After the leftmost column, a leftover carry becomes a new leading bit. In an $n$-bit register it is lost.
5. Check by converting to decimal.

### Subtracting in binary by hand

1. Line up the numbers, with the number being subtracted underneath.
2. Work from the right. In each column compute top bit $-$ bottom bit $-$ borrow from the column to the right.
3. If the result is 0 or 1, write it. If it is $-1$ or $-2$, add 2 to it, write that, and borrow 1 from the next column.
4. Check by adding the answer to the bottom number, which must give the top number.

Hardware avoids borrowing entirely. It computes $a - b$ as $a + (-b)$, and two's complement makes $-b$ cheap.

### Writing an integer in $n$ bits of two's complement

1. Check that the integer is in the range $-2^{n-1}$ to $2^{n-1} - 1$. If it isn't, it doesn't fit.
2. For a non-negative integer, write it in binary and pad with zeros on the left to $n$ bits.
3. For a negative integer $x$, write $\lvert x \rvert$ in $n$ bits, flip every bit, then add 1 and drop any carry out of the top.
4. Check by reading the result back with the weights, with the top bit worth $-2^{n-1}$. Or compute $x + 2^n$ and write that in binary.

### Reading an $n$-bit two's complement pattern

1. Look at the top bit. If it is 0, read the pattern as an ordinary binary number.
2. If it is 1, read the pattern as an unsigned number $U$ and subtract $2^n$. Or use the weights directly, starting from $-2^{n-1}$.
3. In hex, the top bit is set exactly when the first hex digit is 8 or more.

### Theorems with proofs

*Theorem 1.* For an $n$-bit pattern, let $U$ be its unsigned value and $v$ its two's complement value. Then $v = U$ if the top bit is 0 and $v = U - 2^n$ if the top bit is 1. In both cases $U \equiv v \pmod{2^n}$, and $U$ is the remainder of $v$ divided by $2^n$.

What we know: the two place-value formulas. What we want: how they differ. The plan is to compare the top-bit terms only, since the other bits contribute the same to both.

*Proof.* Let $b_{n-1}$ be the top bit, and let $R = \sum_{i=0}^{n-2} b_i 2^i$ be the rest. Then $U = b_{n-1} 2^{n-1} + R$ and $v = -b_{n-1} 2^{n-1} + R$, so $U - v = 2 b_{n-1} 2^{n-1} = b_{n-1} 2^n$. This is 0 if $b_{n-1} = 0$ and $2^n$ if $b_{n-1} = 1$, which gives the two cases. Either way $U - v$ is a multiple of $2^n$, so $U \equiv v \pmod{2^n}$. And $0 \le U \le 2^n - 1$, so $U$ is the remainder. $\blacksquare$

Look back: the pattern of an integer $x$ in range is the binary form of $x \bmod 2^n$: $x$ itself for $x \ge 0$, and $x + 2^n$ for $x < 0$. For example, $-37 + 256 = 219$.

*Theorem 2 (flip and add one).* Let a pattern have two's complement value $v$ with $v \ne -2^{n-1}$. Flipping all its bits and adding 1 (dropping a carry out of the top) gives the pattern of $-v$. For $v = -2^{n-1}$, the result is the same pattern again.

What we know: Theorem 1. What we want: the unsigned value of the new pattern. The plan is to find it in terms of $U$, and then use Theorem 1 to read off the value.

*Proof.* Flipping turns each bit $b_i$ into $1 - b_i$, so the new unsigned value is

$$
\sum_{i=0}^{n-1} (1 - b_i) 2^i = \sum_{i=0}^{n-1} 2^i - U = (2^n - 1) - U.
$$

Adding 1 gives $2^n - U$, and dropping a carry out of the top is taking the remainder modulo $2^n$. So the new pattern has unsigned value $(2^n - U) \bmod 2^n$, which is congruent to $-U$, and $-U \equiv -v \pmod{2^n}$ by Theorem 1. If $-v$ is in the range, the pattern of $-v$ is its remainder modulo $2^n$ (Theorem 1 again), so the new pattern is the pattern of $-v$. The value $-v$ is out of range exactly when $v = -2^{n-1}$, because $-(-2^{n-1}) = 2^{n-1}$ is too big. In that case the pattern is $1000\ldots0$, and flipping gives $0111\ldots1$, whose increment is $1000\ldots0$ again. $\blacksquare$

Look back: the rule works on $0$ too. Flipping $0000\,0000$ gives $1111\,1111$, adding 1 gives $1\,0000\,0000$, and dropping the carry leaves $0000\,0000$. The exceptional case is why $-(-128) = -128$ in 8 bits.

*Theorem 3 (addition works modulo $2^n$).* Adding two $n$-bit patterns as unsigned numbers and keeping the lowest $n$ bits gives a pattern whose two's complement value is congruent to $x + y$ modulo $2^n$, where $x$ and $y$ are the values of the inputs. If $x + y$ is in the range $-2^{n-1}$ to $2^{n-1} - 1$, the output is exactly the pattern of $x + y$.

*Proof.* Let $U_x$ and $U_y$ be the unsigned values of the inputs. By Theorem 1, $U_x \equiv x$ and $U_y \equiv y$ modulo $2^n$, so $U_x + U_y \equiv x + y$. Keeping the lowest $n$ bits replaces the sum by its remainder modulo $2^n$, which changes it by a multiple of $2^n$ and so keeps the congruence. If $x + y$ is in range, its pattern is its own remainder modulo $2^n$ (Theorem 1), and a congruence class modulo $2^n$ has only one remainder. So the two patterns are the same. $\blacksquare$

Look back: the adder doesn't know about signs. The same circuit adds unsigned and signed numbers, and only the reading of the output differs. Subtraction is $a + (-b)$, with $-b$ from Theorem 2, so $a - b$ is computed as $a + \mathrm{NOT}(b) + 1$.

*Theorem 4 (overflow rule).* Adding two $n$-bit two's complement numbers overflows exactly when the two inputs have the same sign and the output has the opposite sign. Adding numbers of different signs never overflows.

*Proof.* Take $x, y \ge 0$. The true sum $x + y$ is at most $2(2^{n-1} - 1) = 2^n - 2$. If it is at most $2^{n-1} - 1$, it fits, and the output is non-negative. Otherwise it is between $2^{n-1}$ and $2^n - 2$, and the output is $x + y - 2^n$ (Theorem 3), which is between $-2^{n-1}$ and $-2$, so negative. Now take $x, y < 0$. The true sum is between $-2^n$ and $-2$. If it is at least $-2^{n-1}$ it fits, and the output is negative. Otherwise it is below $-2^{n-1}$, and the output $x + y + 2^n$ is between 0 and $2^{n-1} - 1$, so non-negative. Last, if $x \ge 0 > y$, the true sum lies between $y$ and $x$, so it is in range and nothing overflows. $\blacksquare$

Hardware checks the same condition with the carries: the sum overflows exactly when the carry into the sign bit differs from the carry out of it. The code at the end of the lesson checks both rules against all 65,536 pairs of 8-bit numbers.

*Theorem 5 (sign extension).* Copying the sign bit to the left of an $n$-bit two's complement pattern, any number of times, keeps its value.

*Proof.* Put one extra copy $s$ of the sign bit in front. The new top bit has weight $-2^n$, and the old top bit, still equal to $s$, now has weight $+2^{n-1}$. Together they contribute $s(-2^n + 2^{n-1}) = -s \cdot 2^{n-1}$, which is what the old top bit contributed alone. Everything else is unchanged. Repeating the step handles any number of copies. $\blacksquare$

## Worked examples

<div class="example" markdown>

### Example 1: encode and decode $-37$ in 8 bits

We use the steps of writing an integer in two's complement.

Step 1: the range for 8 bits is $-128$ to 127, so $-37$ fits.

Steps 2 and 3: write 37 in 8 bits. Since $37 = 32 + 4 + 1$, it is $0010\,0101$. Flip every bit to get $1101\,1010$, and add 1:

$$
1101\,1010 + 1 = 1101\,1011.
$$

So $-37$ is $1101\,1011_2 = \mathrm{DB}_{16}$.

Step 4, the check: read it with the weights, where the top bit is worth $-128$. The 1s are in the places $-128, 64, 16, 8, 2, 1$, and $-128 + 64 + 16 + 8 + 2 + 1 = -128 + 91 = -37$. As a second check, Theorem 1 says the unsigned value is $-37 + 256 = 219$, and $219 = 128 + 64 + 16 + 8 + 2 + 1 = 1101\,1011_2$.

<div class="warning" markdown>

Watch out at step 3: flipping the bits is not enough. Flipping alone gives $1101\,1010$, which is $-38$. The "add 1" is what turns $255 - 37$ into $256 - 37$.

</div>

</div>

<div class="example" markdown>

### Example 2: adding and subtracting by hand

(a) Add $0110\,1101$ and $0011\,1011$, which are 109 and 59. Write the carries above the columns:

```text
carries   1 1 1 1 1 1 1 0
          0 1 1 0 1 1 0 1
        + 0 0 1 1 1 0 1 1
        -----------------
          1 0 1 0 1 0 0 0
```

From the right: $1 + 1 = 10_2$, so write 0 and carry 1. Next $0 + 1 + 1 = 10_2$, write 0 and carry 1. Next $1 + 0 + 1 = 10_2$. Then $1 + 1 + 1 = 11_2$, so write 1 and carry 1, and so on. The answer is $1010\,1000_2 = 168$, which matches $109 + 59 = 168$.

(b) Subtract $0001\,1011$ (27) from $0010\,1101$ (45). In the rightmost column, $1 - 1 = 0$. In the next, $0 - 1 = -1$, so write $-1 + 2 = 1$ and borrow 1 from the next column. That column is now $1 - 0 - 1 = 0$. The next is $1 - 1 = 0$. The next is $0 - 1 = -1$, so write 1 and borrow again, and the column after is $1 - 0 - 1 = 0$. The remaining columns are 0. The answer is $0001\,0010_2 = 18$.

Check (b): $18 + 27 = 45$.

</div>

<div class="example" markdown>

### Example 3: subtracting by adding, and an overflow

(a) Compute $5 - 7$ in 8 bits as $5 + (-7)$. We have $5 = 0000\,0101$. Writing $-7$: $7 = 0000\,0111$, flipped $1111\,1000$, plus 1 gives $1111\,1001$. Adding,

$$
0000\,0101 + 1111\,1001 = 1111\,1110,
$$

with no carry out. The top bit is 1, so the result is negative, and $1111\,1110$ is $254 - 256 = -2$. Check: $5 - 7 = -2$.

(b) Compute $100 + 50$ in 8 bits. We have $100 = 0110\,0100$ and $50 = 0011\,0010$, and their sum is $1001\,0110$. The top bit is 1, so the result reads as $150 - 256 = -106$. Both inputs are positive and the output is negative, so by Theorem 4 this is an overflow: the true result 150 is above 127. The hardware version of the test agrees: the carry into the sign bit is 1 (the low seven bits add to $100 + 50 = 150 \ge 128$) and the carry out of it is 0.

Check: $-106 \equiv 150 \pmod{256}$, since $150 - (-106) = 256$. The wrapped answer is congruent to the true one, as Theorem 3 says.

</div>

<div class="example" markdown>

### Example 4: finish it yourself

Add $-100 + (-50)$ in 8 bits. The inputs are $1001\,1100$ and $1100\,1110$ (check that they are $256 - 100$ and $256 - 50$). Add them, keep 8 bits, read the result, and decide whether it overflowed.

<details class="solution" markdown>
<summary>Finish</summary>

The 9-bit sum is $1\,0110\,1010$, so dropping the carry gives $0110\,1010 = 64 + 32 + 8 + 2 = 106$. Both inputs are negative and the output is positive, so this is an overflow: the true sum $-150$ is below $-128$.

Check: $-150 + 256 = 106$, so the output is congruent to the true result modulo 256, but it is a different number.

</details>

</div>

## Edge cases and common mistakes

Flipping without adding one is flagged at its step in Example 1. These are the others.

<div class="warning" markdown>

Watch out: the most negative number has no positive partner. In 8 bits, $-128 = 1000\,0000$, and negating it gives $1000\,0000$ again. So `abs` of the smallest integer is still negative, and `-x < 0` can be true for a "positive" input. In C, negating the smallest `int` is undefined behaviour.

</div>

<div class="warning" markdown>

Watch out: unsigned overflow and signed overflow are different events. Take $\mathrm{FF}_{16} + 01_{16}$ in 8 bits. Unsigned, $255 + 1$ carries out of the top and wraps to 0, which is an overflow. Signed, $-1 + 1 = 0$ is correct and there is no overflow. In the other direction, $0111\,1111 + 1 = 1000\,0000$ is $127 + 1 = -128$ in signed arithmetic (overflow), and $127 + 1 = 128$ in unsigned arithmetic (fine). The same bits, the same addition, and two different answers to "did it overflow?".

</div>

<div class="warning" markdown>

Watch out when widening a number. A signed value is extended by copying its sign bit (Theorem 5), and an unsigned value is extended with zeros. The byte $\mathrm{DB}_{16}$ widens to $\mathrm{FFDB}_{16}$ as the signed $-37$, and to $\mathrm{00DB}_{16}$ as the unsigned 219. Using the wrong one changes the value.

</div>

<div class="warning" markdown>

Watch out: the sign bit is not a separate sign. Flipping only the top bit of $0000\,0101$ gives $1000\,0101$, which is $-123$, not $-5$. That would be sign-magnitude. In two's complement, the whole pattern changes when you negate.

</div>

Languages differ in what overflow does. Java wraps signed `int` arithmetic. Unsigned arithmetic in C and C++ wraps by definition, but signed overflow is undefined behaviour, so the compiler may assume it never happens and can remove checks written to detect it. Rust panics on overflow in debug builds and wraps in release builds by default. Python integers never overflow, because they grow as needed, so Python needs masks to imitate a fixed width.

A well-known example is the midpoint of a binary search. With 32-bit `int`s, `(low + high) / 2` can overflow when `low + high` passes 2,147,483,647, and the wrapped sum is negative. Joshua Bloch reported that this bug had sat in the Java library's binary search for years ([Google Research blog, 2 June 2006](https://research.google/blog/extra-extra-read-all-about-it-nearly-all-binary-searches-and-mergesorts-are-broken/)). Writing `low + (high - low) / 2` fixes it. The check is in the code below.

## Tricks and shortcuts

- To negate by hand, copy the bits from the right up to and including the first 1, then flip every bit to the left of it. For $0010\,0101$ the rightmost 1 is the last bit, so flip everything to its left: $1101\,1011$. This is the same as flip and add 1, because adding 1 to the flipped bits carries through exactly the trailing 1s.
- In hex, a first digit of 8 to F means negative. To read a negative hex byte, subtract from $\mathrm{100}_{16}$: for $\mathrm{DB}_{16}$, $256 - 219 = 37$, so it is $-37$.
- Three patterns are worth knowing in every width: all zeros is 0, all ones is $-1$, and a 1 followed by zeros is the smallest number. In 32 bits, these are `0x00000000`, `0xFFFFFFFF` and `0x80000000`, and the largest number is `0x7FFFFFFF`.
- To check a signed addition, ask: did two numbers of the same sign give a result of the other sign? If not, the result is right.
- To size a type, remember $2^{15} = 32{,}768$ and $2^{31} \approx 2.1 \times 10^9$. An `int` counting seconds since 1970 runs out in January 2038, because $2^{31}$ seconds is about 68 years.

## In code

Python integers don't overflow, so a mask imitates a fixed width: `x & (2**n - 1)` keeps the lowest $n$ bits, which is Theorem 1's "remainder modulo $2^n$". The functions turn bit patterns into signed values and back, and the last block tests the theorems on every 8-bit pair.

<details class="code" markdown>
<summary>In code</summary>

```python
def to_unsigned(x, n):
    """The pattern of x in n bits, read as an unsigned number."""
    return x & ((1 << n) - 1)

def to_signed(u, n):
    """Read an n-bit pattern as a two's complement number (Theorem 1)."""
    u &= (1 << n) - 1
    return u - (1 << n) if u >> (n - 1) else u

def bits(x, n):
    return format(to_unsigned(x, n), f"0{n}b")

print(bits(-37, 8), hex(to_unsigned(-37, 8)), to_signed(0xDB, 8))  # 11011011 0xdb -37
print(bits(~37 + 1, 8) == bits(-37, 8))        # True: flip and add one
print(to_signed(100 + 50, 8))                  # -106: 8-bit overflow
print(to_signed(5 - 7, 8), (5 - 7) & 0xFF)     # -2 254
print(to_signed(-(-128), 8))                   # -128: no positive partner
print(bits(-37, 16), hex(to_unsigned(-37, 32)))  # 1111111111011011 0xffffffdb
print(to_signed(0x80000000, 32), to_signed(0x7FFFFFFF, 32))  # -2147483648 2147483647

# the midpoint bug with 32-bit ints
lo, hi = 2_000_000_000, 2_100_000_000
print(to_signed(lo + hi, 32), to_signed(lo + (hi - lo) // 2, 32))  # -194967296 2050000000

# exhaustive check of Theorem 4 and the carry rule on all 65,536 pairs of 8-bit numbers
n, bad = 8, 0
for x in range(-128, 128):
    for y in range(-128, 128):
        overflow = not (-128 <= x + y <= 127)
        r = to_signed(x + y, n)
        by_signs = (x < 0) == (y < 0) and (r < 0) != (x < 0)
        ux, uy = to_unsigned(x, n), to_unsigned(y, n)
        carry_in = ((ux & 0x7F) + (uy & 0x7F)) >> 7
        carry_out = (ux + uy) >> 8
        if overflow != by_signs or overflow != (carry_in != carry_out):
            bad += 1
print(bad)                                     # 0

# Python can also convert between integers and bytes in two's complement
print((-37).to_bytes(1, "big", signed=True).hex())            # db
print(int.from_bytes(bytes.fromhex("db"), "big", signed=True))  # -37
```

</details>

## FAQ

### Why is the range lopsided, $-128$ to 127?

There are $2^n$ patterns, an even number, and 0 uses one of them. That leaves an odd number to split between positive and negative numbers, so one side gets an extra. In two's complement the extra pattern, $1000\ldots0$, goes to the negative side. That is why the sign bit tells you the sign with no exceptions: it is 1 for each negative number and 0 for zero and the positive numbers.

### Why can the adder ignore the carry out of the top?

Because the answer is only supposed to be right modulo $2^n$ (Theorem 3), and the carry out is worth exactly $2^n$. Keeping it would change the answer by a multiple of $2^n$, which is the same number in the congruence. Dropping it is what makes the result land back in range when the true sum is in range.

### How does the processor know if my numbers are signed?

It doesn't. The bits are the same. Instructions and types decide how to read them. A processor adds with one instruction and sets flags afterwards: a carry flag (unsigned overflow) and an overflow flag (signed overflow). Comparisons and shifts have separate signed and unsigned versions, and the compiler picks the one that matches the type you declared.

### Why not just flip all the bits to negate, as in one's complement?

One's complement does exactly that, so $-x$ is `NOT x`. It still has two zeros ($0000$ and $1111$), and the adder needs an end-around carry, where the carry out is added back at the bottom. Two's complement adds 1 once and gets one zero, a plain adder, and one more value. That is why it won.

## Practice

### Warm-up

1\. Add $1011\,0101$ and $0100\,1110$ as 8-bit unsigned numbers. Give the 8-bit result and say whether there is a carry out.

<details class="solution" markdown>
<summary>Solution</summary>

The numbers are 181 and 78. Adding column by column gives the 9-bit sum $1\,0000\,0011$. The register keeps $0000\,0011 = 3$, and the carry out is 1, so it is an unsigned overflow.

Check: $181 + 78 = 259 = 256 + 3$, so the register holds $259 \bmod 256 = 3$.

</details>

2\. Write $-1$, $-128$, $127$ and $-5$ in 8-bit two's complement, in binary and in hex.

<details class="solution" markdown>
<summary>Solution</summary>

- $-1$: $1 = 0000\,0001$, flipped $1111\,1110$, plus 1 gives $1111\,1111 = \mathrm{FF}_{16}$.
- $-128$: it is the smallest number, $1000\,0000 = 80_{16}$.
- $127$: $0111\,1111 = \mathrm{7F}_{16}$.
- $-5$: $5 = 0000\,0101$, flipped $1111\,1010$, plus 1 gives $1111\,1011 = \mathrm{FB}_{16}$.

Check with Theorem 1: $256 - 1 = 255 = \mathrm{FF}_{16}$, $256 - 128 = 128 = 80_{16}$, and $256 - 5 = 251 = \mathrm{FB}_{16}$.

</details>

3\. Read the 8-bit two's complement patterns $\mathrm{F3}_{16}$ and $\mathrm{7C}_{16}$ as decimal numbers.

<details class="solution" markdown>
<summary>Solution</summary>

The first hex digit of $\mathrm{F3}$ is F, which is 8 or more, so the sign bit is set and the number is negative: $\mathrm{F3}_{16} = 243$ and $243 - 256 = -13$. The first digit of $\mathrm{7C}$ is 7, so the number is non-negative: $\mathrm{7C}_{16} = 7 \cdot 16 + 12 = 124$.

Check: negating $-13$ should give $0000\,1101$, and $\mathrm{F3} = 1111\,0011$ flipped is $0000\,1100$, plus 1 is $0000\,1101 = 13$.

</details>

### Standard

4\. Compute $23 - 58$ in 8 bits by adding the two's complement of 58, and read the result.

<details class="solution" markdown>
<summary>Solution</summary>

We have $23 = 0001\,0111$ and $58 = 0011\,1010$. Flip 58 to get $1100\,0101$ and add 1 to get $1100\,0110$, which is $-58$. Then

$$
0001\,0111 + 1100\,0110 = 1101\,1101.
$$

There is no carry out. The top bit is 1, so the result is $221 - 256 = -35$.

Check: $23 - 58 = -35$. The signs of the inputs differ, so Theorem 4 says no overflow is possible.

</details>

5\. In 4-bit two's complement, say which of these overflow, and give the 4-bit result of each: (a) $5 + 3$, (b) $-5 + (-4)$, (c) $6 + (-2)$, (d) $-8 + (-1)$.

<details class="solution" markdown>
<summary>Solution</summary>

The range is $-8$ to 7.

- (a) $0101 + 0011 = 1000$, which is $-8$. Both inputs are positive and the output is negative, so it overflows. The true sum, 8, is above 7.
- (b) $1011 + 1100 = 1\,0111$, so the output is $0111 = 7$. Both inputs are negative and the output is positive, so it overflows. The true sum is $-9$.
- (c) $0110 + 1110 = 1\,0100$, so the output is $0100 = 4$, which is correct. The signs differ, so no overflow, even though there is a carry out of the top bit.
- (d) $1000 + 1111 = 1\,0111$, so the output is $0111 = 7$. It overflows, since the true sum is $-9$.

Check: in (a), $8 - 16 = -8$; in (b) and (d), $-9 + 16 = 7$, as Theorem 3 says.

</details>

6\. Extend the 8-bit pattern $\mathrm{9C}_{16}$ to 16 bits as a signed number, and say what value it has before and after. Then extend it as an unsigned number.

<details class="solution" markdown>
<summary>Solution</summary>

We have $\mathrm{9C}_{16} = 1001\,1100$. The sign bit is 1, so the signed value is $156 - 256 = -100$. Sign extension copies the 1 into the new top 8 bits: $1111\,1111\,1001\,1100 = \mathrm{FF9C}_{16}$. As a 16-bit signed number it is $65{,}436 - 65{,}536 = -100$, the same value.

As an unsigned number, $\mathrm{9C}_{16}$ is 156 and the extension uses zeros: $\mathrm{009C}_{16} = 156$.

Check: $-100 + 65{,}536 = 65{,}436 = \mathrm{FF9C}_{16}$.

</details>

### Challenge

7\. Show that $a - b$ can be computed as $a + \mathrm{NOT}(b) + 1$ in $n$ bits, where NOT flips every bit. Then use it for $45 - 27$ in 8 bits, and say how an adder circuit could do this using a carry-in of 1.

<details class="solution" markdown>
<summary>Solution</summary>

By Theorem 2, the pattern $\mathrm{NOT}(b) + 1$ is the pattern of $-b$. Adding $a$ and that pattern gives $a + (-b) = a - b$ by Theorem 3, with the same range condition: the result is right whenever $a - b$ fits in $n$ bits. Since $\mathrm{NOT}(b) + 1$ can carry, it is cleaner to do both in one addition: an adder with a carry-in input adds $a$, $\mathrm{NOT}(b)$ and a carry-in of 1 in the lowest column.

For $45 - 27$: $45 = 0010\,1101$, $27 = 0001\,1011$, and $\mathrm{NOT}(27) = 1110\,0100$. Then

$$
0010\,1101 + 1110\,0100 + 1 = 1\,0001\,0010,
$$

so dropping the carry out gives $0001\,0010 = 18$.

Check: $45 - 27 = 18$. This is the idea behind the subtractor in the adder lesson ([boolean algebra and logic gates](06-boolean-algebra-and-logic-gates.md)): XOR gates in front of $b$ flip its bits when the operation is "subtract", and the same signal drives the carry-in.

</details>

8\. (Reviews [number bases and conversions](01-number-bases-and-conversions.md).) Convert $\mathrm{BEEF}_{16}$ to decimal as an unsigned 16-bit number. Then read it as a signed 16-bit number, using two different methods, and show that they agree.

<details class="solution" markdown>
<summary>Solution</summary>

By Horner's method, $\mathrm{B} = 11$, then $11 \cdot 16 + 14 = 190$, then $190 \cdot 16 + 14 = 3054$, then $3054 \cdot 16 + 15 = 48{,}879$. So unsigned, $\mathrm{BEEF}_{16} = 48{,}879$.

Method 1 (Theorem 1): the first hex digit B is above 8, so the sign bit is set, and the value is $48{,}879 - 65{,}536 = -16{,}657$.

Method 2 (negate): flip and add 1. $\mathrm{BEEF}_{16}$ flipped is $\mathrm{4110}_{16}$, and adding 1 gives $\mathrm{4111}_{16} = 4 \cdot 4096 + 256 + 16 + 1 = 16{,}657$. So the value is $-16{,}657$.

Check: both methods give $-16{,}657$, and $-16{,}657 + 65{,}536 = 48{,}879$.

</details>

## Where this shows up

- The next lesson, [floating point basics](04-floating-point-basics.md), stores a number's exponent with a bias and not in two's complement. [Bitwise operations and masks](05-bitwise-operations-and-masks.md) uses masks like the ones in this lesson's code, and explains `>>` on negative numbers.
- In [boolean algebra and logic gates](06-boolean-algebra-and-logic-gates.md), a ripple-carry adder built from full adders is the circuit behind Theorem 3. Systems courses use two's complement in every integer instruction, in the carry and overflow flags, and in the `int` and `unsigned` types of C.
- Modular arithmetic ([divisibility and modular arithmetic](../02-number-theory/01-divisibility-and-modular-arithmetic.md)) is the general version of the wrap-around here: integer arithmetic in an $n$-bit register is arithmetic modulo $2^n$. Hash functions and checksums often use this on purpose.
