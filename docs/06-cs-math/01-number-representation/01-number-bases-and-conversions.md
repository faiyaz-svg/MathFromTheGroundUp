# Number bases and conversions

After this lesson you can convert whole numbers between decimal, binary, octal and hexadecimal by hand, and say how many values a given number of bits can hold.

Before this: [place value](../../01-elementary/01-place-value-and-rounding.md), [exponents](../../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md) and [long division](../../01-elementary/07-long-division.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Convert $110101_2$ to decimal.
2. Write 77 in binary and in hex.
3. How many different values can 12 bits hold? Write the largest one in decimal, binary and hex.

<details class="solution" markdown>
<summary>Answers</summary>

1. The 1s are in the places 32, 16, 4 and 1, so $110101_2 = 32 + 16 + 4 + 1 = 53$.
2. Since $77 = 64 + 8 + 4 + 1$, it is $1001101_2$. Grouping the bits in 4s from the right gives $0100\,1101_2 = \mathrm{4D}_{16}$.
3. There are $2^{12} = 4{,}096$ values, from 0 up to $4{,}095 = 1111\,1111\,1111_2 = \mathrm{FFF}_{16}$.

</details>

## The idea

When you read 2,705, you are reading instructions: take 2 thousands, 7 hundreds, no tens and 5 ones.

$$
2{,}705 = 2 \cdot 1000 + 7 \cdot 100 + 0 \cdot 10 + 5 \cdot 1
$$

Each place is worth 10 times the place to its right, so the digits only need to go up to 9: ten of one place make one of the next, which is what carrying does. The 0 matters too. Leave it out and you get 275.

Nothing here depends on ten. Build the same system on two, with places worth 1, 2, 4, 8, 16 and so on, and only the digits 0 and 1. Then 1011 means one 8, no 4, one 2 and one 1, which is eleven.

| Place value | 8 | 4 | 2 | 1 |
|---|---|---|---|---|
| Digit | 1 | 0 | 1 | 1 |

Changing the base changes how a number is written, not the number. Eleven pebbles are eleven pebbles whether you bundle them as one ten and one one, or as one eight, one two and one one. Computers store numbers in base 2, and programmers also use bases 8 and 16, which convert to base 2 one digit at a time.

## Definitions

### Base and place value

Let $b \ge 2$ be an integer. In **positional notation** with **base** $b$ (also called the radix), each **digit** is one of the integers $0, 1, \dots, b - 1$. A string of digits $d_k d_{k-1} \dots d_1 d_0$ stands for the number

$$
\begin{aligned}
(d_k d_{k-1} \dots d_1 d_0)_b &= d_k b^k + d_{k-1} b^{k-1} + \dots + d_1 b^1 + d_0 b^0 \\
&= \sum_{i=0}^{k} d_i b^i.
\end{aligned}
$$

The digit $d_i$ sits in position $i$, counting from 0 at the right, and $b^i$ is the **place value** of that position. The symbol $\Sigma$, a capital Greek sigma, means "add up": $\sum_{i=0}^{k} d_i b^i$ says to work out $d_i b^i$ for each $i$ from 0 to $k$ and add the results. [Summation notation](../../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md) covers it properly.

In plain words, the base says how much bigger each place is than the one to its right, and each digit says how many of that place you have. Positions start at 0 so that the exponent matches the position, and the rightmost digit counts ones because $b^0 = 1$. For example, $(1011)_2 = 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0 = 11$.

Zeros at the left end of a number are **leading zeros**. They don't change the value, since each adds $0 \cdot b^i = 0$, so $0011_2 = 11_2 = 3$. For each base $b \ge 2$, every positive integer has exactly one representation that doesn't start with 0; [repeated division](#decimal-to-another-base) shows why.

### Binary, octal and hexadecimal

Base 10 is **decimal**, base 2 is **binary**, base 8 is **octal** and base 16 is **hexadecimal**, or hex for short. Hex needs sixteen digits, so the letters A to F stand for 10 to 15, written as capitals or small letters. A binary digit is a **bit**. The leftmost bit of a number has the largest place value and is the **most significant bit**; the rightmost, the ones place, is the **least significant bit**.

In plain words, each base is a bundle size: binary place values are 1, 2, 4, 8, ..., and hex place values are 1, 16, 256, .... The table lists 0 to 15 in all four bases, with the binary padded to 4 bits for the grouping method below.

| Decimal | Binary | Octal | Hex |
|---|---|---|---|
| 0 | 0000 | 0 | 0 |
| 1 | 0001 | 1 | 1 |
| 2 | 0010 | 2 | 2 |
| 3 | 0011 | 3 | 3 |
| 4 | 0100 | 4 | 4 |
| 5 | 0101 | 5 | 5 |
| 6 | 0110 | 6 | 6 |
| 7 | 0111 | 7 | 7 |
| 8 | 1000 | 10 | 8 |
| 9 | 1001 | 11 | 9 |
| 10 | 1010 | 12 | A |
| 11 | 1011 | 13 | B |
| 12 | 1100 | 14 | C |
| 13 | 1101 | 15 | D |
| 14 | 1110 | 16 | E |
| 15 | 1111 | 17 | F |

### Writing the base

When bases are mixed, write the base as a subscript, in decimal: $1011_2$, $13_8$, $\mathrm{B}_{16}$ and $11_{10}$ are all eleven. A number with no subscript is decimal. Code uses a prefix instead, and Python writes eleven as `0b1011`, `0o13` or `0xB`.

### Powers of 2

The place values in binary are the powers of 2. Learn at least the ones up to $2^{10}$.

| $n$ | $2^n$ | $n$ | $2^n$ | $n$ | $2^n$ |
|---|---|---|---|---|---|
| 0 | 1 | 6 | 64 | 12 | 4,096 |
| 1 | 2 | 7 | 128 | 13 | 8,192 |
| 2 | 4 | 8 | 256 | 14 | 16,384 |
| 3 | 8 | 9 | 512 | 15 | 32,768 |
| 4 | 16 | 10 | 1,024 | 16 | 65,536 |
| 5 | 32 | 11 | 2,048 | | |

Since $2^{10} = 1{,}024$, we have $2^{10} \approx 10^3$, where $\approx$ means "is about". So $2^{20}$ is about a million and $2^{30}$ is about a billion. This near miss is why "kilo" in computing sometimes means 1,024; [scientific notation](../../02-middle-school/04-powers-roots-and-real-numbers/02-scientific-notation.md) sorts out the prefixes.

## How to do it

### Another base to decimal

The expanded form comes straight from the definition: multiply each digit by its place value and add. **Horner's method** gets the same answer without a table of place values:

1. Start with the leftmost digit as the running total.
2. Multiply the running total by the base $b$ and add the next digit.
3. Repeat step 2 until you have added the last digit. The running total is the value.
4. Check with the expanded form.

You already do this when you read 2,705 from the left: 2, then 27, then 270, then 2,705, multiplying by 10 and adding each time. Multiplying out the brackets shows why it works:

$$
((d_3 b + d_2) b + d_1) b + d_0 = d_3 b^3 + d_2 b^2 + d_1 b + d_0.
$$

### Decimal to another base

Repeated division takes off the digits one at a time, ones digit first.

1. Divide the number by $b$. Write down the quotient and the remainder.
2. Divide the quotient by $b$ the same way.
3. Repeat step 2 until the quotient is 0.
4. Read the remainders from the last one up to the first. In hex, write the remainders 10 to 15 as A to F.
5. Check by converting back.

<div class="warning" markdown>

Watch out at step 4: the first remainder is the ones digit, so it goes on the right. Dividing 6 by 2 again and again gives the remainders 0, 1, 1. Read from the bottom up they make $110_2 = 6$; read from the top down they make $011_2 = 3$.

</div>

Why it works: in [long division](../../01-elementary/07-long-division.md), a number equals the quotient times the divisor plus a remainder smaller than the divisor, and only one such pair fits. Positional notation has exactly that shape, with $b$ as the divisor:

$$
\underbrace{(d_k \dots d_1 d_0)_b}_{\text{number}} = \underbrace{(d_k \dots d_1)_b}_{\text{quotient}} \cdot \underbrace{b}_{\text{divisor}} + \underbrace{d_0}_{\text{remainder}}
$$

So dividing by $b$ gives the last digit $d_0$ (at most $b - 1$) as the remainder and chops it off the quotient, just as 2,705 divided by 10 is 270 remainder 5. Dividing again gives $d_1$, and so on. Each division has only one quotient and remainder, so the digits are forced and the representation is unique.

For binary, subtracting powers of 2 is often quicker for small numbers:

1. Find the largest power of 2 that is at most the number, and write 1 in its place.
2. Subtract that power.
3. Go to the next smaller power. If it is at most what is left, write 1 and subtract it; if not, write 0.
4. Repeat step 3 down to the ones place, even after nothing is left.
5. Check by adding the powers that got a 1.

<div class="warning" markdown>

Watch out at step 4: stopping as soon as nothing is left drops the zeros at the right end. The 4s, 2s and 1s places of 8 still need digits, so $8 = 1000_2$, not $1_2$.

</div>

### Between binary and hex or octal

Since $16 = 2^4$ and $8 = 2^3$, each hex digit is exactly 4 bits and each octal digit is exactly 3 bits.

1. Starting at the right end, split the bits into groups of 4 for hex, or 3 for octal.
2. If the leftmost group is short, pad it with zeros on the left.
3. Replace each group with its digit from the table above.

To go back, write each hex digit as 4 bits (each octal digit as 3), keeping the zeros inside a group: $3_{16}$ becomes 0011, not 11.

<div class="warning" markdown>

Watch out at step 1: group from the right, where the ones place is. Grouped from the left, $1101011_2$ splits into 1101 and 011, which reads as $\mathrm{D3}_{16} = 211$. Grouped from the right it splits into 110 and 1011, padded to 0110 and 1011, which gives $\mathrm{6B}_{16} = 107$, the correct value.

</div>

Why it works: in $1101\,0110_2$ the left four bits have the place values 16, 32, 64 and 128, which are 16 times 1, 2, 4 and 8. So the left group counts 16s:

$$
1101\,0110_2 = 1101_2 \cdot 16 + 0110_2 = 13 \cdot 16 + 6 = \mathrm{D6}_{16}.
$$

A third group would count 256s, since $16^2 = 256$, and so on. Base 10 is not a power of 2, so decimal digits never line up with bits; that is why decimal conversions take arithmetic.

### Counting in binary

Counting in binary works like a car odometer whose wheels show only 0 and 1: 0, 1, 10, 11, 100, 101, 110, 111, 1000. To add 1, change the rightmost 0 to 1 and every 1 to its right to 0, so $1011_2 + 1 = 1100_2$. With no 0 at all, put a 1 in front: $111_2 + 1 = 1000_2$, just as $999 + 1 = 1{,}000$.

The picture fails at the left end: an odometer has a fixed number of wheels and rolls over to zeros, while on paper you can always add a digit. Computers, though, do store numbers in a fixed number of bits.

### How many values fit in a fixed number of bits

*Theorem.* For each integer $n \ge 1$, there are exactly $2^n$ strings of $n$ bits, and read as binary numbers they give each integer from 0 to $2^n - 1$ exactly once.

We know each position holds 0 or 1, and we want the number of strings and their values. The plan: count the strings, find the largest value, then match strings to numbers.

*Proof.* Each of the $n$ positions has 2 choices, whatever the others hold, so there are $2 \cdot 2 \cdots 2 = 2^n$ strings (the product rule from [counting rules](../03-counting-and-discrete-probability/01-counting-rules.md)). The all-zeros string is 0. The all-ones string plus 1 is a 1 followed by $n$ zeros, which is $2^n$, so the largest value is $2^n - 1$. Different strings give different numbers, since representations are unique once leading zeros are dropped. So $2^n$ strings give $2^n$ different values in a range of exactly $2^n$ integers, and each integer is used once.

Look back: three decimal digits hold $10^3$ values, 000 to 999, and in general $n$ digits in base $b$ hold $b^n$ values, from 0 to $b^n - 1$. A byte (8 bits) holds 256 values, from 0 to $255 = \mathrm{FF}_{16}$.

<div class="warning" markdown>

Watch out: with $n$ bits the largest value is $2^n - 1$, not $2^n$, because 0 takes up one of the $2^n$ values. A byte goes up to 255.

</div>

## Worked examples

<div class="example" markdown>

### Example 1: 45 in binary by repeated division

We want base 2, so every division is by 2.

Step 1: divide 45 by 2. Since $22 \cdot 2 = 44$, the quotient is 22 and the remainder is 1. That remainder is the ones digit.

Steps 2 and 3: keep dividing each quotient by 2 until the quotient is 0. Every remainder is 0 or 1; a remainder of 2 or more would mean the quotient was too small.

| Division | Quotient | Remainder |
|---|---|---|
| $45 \div 2$ | 22 | 1 (ones digit) |
| $22 \div 2$ | 11 | 0 |
| $11 \div 2$ | 5 | 1 |
| $5 \div 2$ | 2 | 1 |
| $2 \div 2$ | 1 | 0 |
| $1 \div 2$ | 0 | 1 (leftmost digit) |

Don't skip the last row: stopping at quotient 1 instead of 0 loses the leading 1.

Step 4: from the bottom up the remainders read 1, 0, 1, 1, 0, 1, so $45 = 101101_2$.

Step 5, the check: the 1s are in the places 32, 8, 4 and 1, and $32 + 8 + 4 + 1 = 45$. The length fits too, since $32 \le 45 < 64$ means 6 bits.

</div>

<div class="example" markdown>

### Example 2: hex to decimal with Horner's method

Convert $\mathrm{A91}_{16}$ to decimal. Step 1 starts the total at A, which is 10. Step 2 multiplies by 16 and adds the 9 to get 169, and the repeat in step 3 multiplies by 16 and adds the 1:

$$
169 \cdot 16 + 1 = 2{,}705.
$$

So $\mathrm{A91}_{16} = 2{,}705$, the number from the start of the lesson.

Check by repeated division by 16: $2{,}705 = 169 \cdot 16 + 1$, then $169 = 10 \cdot 16 + 9$, then $10 = 0 \cdot 16 + 10$. From the bottom up the remainders are 10, 9 and 1, and 10 is the single digit A.

</div>

<div class="example" markdown>

### Example 3: 200 in binary, with zeros at the end

Subtract powers of 2. In steps 1 and 2, the largest power of 2 that is at most 200 is 128, which leaves 72. In step 3, 64 fits and leaves 8, then 32 and 16 don't fit, then 8 fits and leaves 0. By step 4 the 4s, 2s and 1s places still get digits, all 0:

| Place value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|
| Digit | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 |

So $200 = 1100\,1000_2$.

Check: $128 + 64 + 8 = 200$. As a second check, group the bits in 4s: 1100 is C and 1000 is 8, and $\mathrm{C8}_{16} = 12 \cdot 16 + 8 = 200$.

</div>

<div class="example" markdown>

### Example 4: finish it yourself

Write 1,000 in octal by repeated division by 8. The first two divisions are done:

| Division | Quotient | Remainder |
|---|---|---|
| $1{,}000 \div 8$ | 125 | 0 |
| $125 \div 8$ | 15 | 5 |

Finish steps 3 to 5: divide until the quotient is 0, read the remainders and check.

<details class="solution" markdown>
<summary>Finish</summary>

Dividing 15 by 8 gives 1 remainder 7, and dividing 1 by 8 gives 0 remainder 1. From the bottom up the remainders read 1, 7, 5, 0, so $1{,}000 = 1750_8$. The 0 on the right is the first remainder and has to stay.

Check: $1 \cdot 512 + 7 \cdot 64 + 5 \cdot 8 + 0 = 512 + 448 + 40 = 1{,}000$.

</details>

</div>

## Edge cases and common mistakes

Four common mistakes are flagged above at their steps: reading remainders from the top down, dropping zeros at the right end, grouping from the left, and taking $2^n$ as the top of the $n$-bit range. These are the remaining cases.

<div class="note" markdown>

Zero is 0 in every base: step 1 of repeated division gives quotient 0 and remainder 0. Code with `while num > 0` skips its loop and returns an empty string, so the function in [In code](#in-code) handles 0 separately.

Leading zeros never change the value ($00101_2 = 101_2 = 5$), and they pad a number to a fixed width, as in the byte $0000\,0101_2$. Zeros inside a number or at its right end are real digits.

</div>

<div class="warning" markdown>

Watch out: every digit must be less than the base. There is no 2 in binary, no 8 or 9 in octal and no G in hex, so $1021_2$ is not a number, and Python's `int("1021", 2)` raises an error.

In hex, a remainder from 10 to 15 is one digit, written as a letter. Converting 255 gives the remainders 15 and 15, so $255 = \mathrm{FF}_{16}$; writing 1515 would mean $1515_{16} = 5{,}397$. Letter case doesn't matter, and `0xff`, `0xFF` and `0xFf` are all 255.

</div>

<div class="note" markdown>

Negative numbers get a minus sign, as in decimal: $-13 = -1101_2$. Inside a computer they are stored with two's complement<!-- link: 03-binary-arithmetic-and-twos-complement.md -->, the lesson after next. Digits after the point have place values $b^{-1}, b^{-2}, \dots$, so $0.1_2 = \frac{1}{2}$, but a decimal fraction as plain as 0.1 never ends in binary, which is where floating point basics<!-- link: 04-floating-point-basics.md --> starts.

</div>

## Tricks and shortcuts

- To turn a hex digit into bits, split its value into 8, 4, 2 and 1: B is $11 = 8 + 2 + 1$, so B is 1011.
- Estimate with $2^{10} \approx 10^3$: $2^{32} = 2^2 \cdot 2^{30} \approx 4 \times 10^9$ (exactly 4,294,967,296). It also means about 10 bits per 3 decimal digits, so a 3-digit number needs at most 10 bits. If yours has 14, recheck.
- A binary number is odd exactly when its last bit is 1, because every other place value is even.
- Writing a 0 on the right multiplies by the base: $101_2 = 5$ and $1010_2 = 10$. Dropping the last bit halves the number and throws away the remainder. These are the shifts of bitwise operations and masks<!-- link: 05-bitwise-operations-and-masks.md -->.
- A string of $n$ ones is $2^n - 1$: $1111_2 = 15 = \mathrm{F}_{16}$.

## In code

The two functions are repeated division and Horner's method written out; the last three lines are Python's built-in versions.

<details class="code" markdown>
<summary>In code</summary>

```python
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_base(num, b):
    """Repeated division: write num >= 0 in base b (2 to 36)."""
    if num == 0:
        return "0"                  # the loop would return "" for 0
    out = ""
    while num > 0:
        num, r = divmod(num, b)     # quotient and remainder
        out = DIGITS[r] + out       # later remainders go on the left
    return out

def from_base(s, b):
    """Horner's method: multiply by the base, add the next digit."""
    total = 0
    for ch in s.upper():
        d = DIGITS.index(ch)
        if d >= b:
            raise ValueError(f"{ch} is not a digit in base {b}")
        total = total * b + d
    return total

print(to_base(45, 2), to_base(2705, 16), to_base(0, 2))  # 101101 A91 0
print(from_base("101101", 2), from_base("a91", 16))      # 45 2705
print(int("A91", 16), int("00101", 2))                   # 2705 5
print(bin(45), oct(1000), hex(2705))       # 0b101101 0o1750 0xa91
print(format(45, 'b'), format(5, '08b'))   # 101101 00000101
```

</details>

## FAQ

### Why do computers use binary?

Each digit is stored as a physical state, such as a voltage on a wire. Telling two states apart (high or low) is far more reliable under electrical noise than telling ten levels apart. Binary also matches logic, with 1 and 0 for true and false, which boolean algebra and logic gates<!-- link: 06-boolean-algebra-and-logic-gates.md --> builds on.

### Why do programmers write hex instead of binary?

One hex digit is exactly 4 bits, so a byte (8 bits) is 2 hex digits and a 32-bit value is 8 hex digits instead of 32 bits. Converting between hex and binary is a lookup. Decimal is compact too, but its digits don't line up with bits: 255 hides its bit pattern, while 0xFF shows eight 1s at once.

### What does the 0x in front of a number mean?

It is a prefix saying the digits are hex, so 0x1F is $\mathrm{1F}_{16} = 31$. The leading 0 makes the language read a number and not a variable named x1F. Python uses 0b and 0o for binary and octal. C marks octal with a bare leading 0, so 0755 in C is $755_8 = 493$; Python 3 rejects 0755 and asks for 0o755.

### Can a base be larger than 16?

Yes. Every integer $b \ge 2$ works, given $b$ digit symbols. Base 36 uses 0 to 9 and A to Z, and Python's `int()` accepts every base from 2 to 36, so `int("ZZ", 36)` is 1,295. Base64, which carries binary data such as email attachments as text, has 64 symbols (A to Z, a to z, 0 to 9, + and /), one per 6 bits, since $64 = 2^6$. It encodes a run of bytes, not one number, so it groups from the left.

### Is there a base 1?

Not as positional notation: the only digit would be 0, and every place value would be $1^i = 1$. What people call base 1, or unary, is a tally, where 5 is written 11111 and each mark is worth 1 wherever it sits. It shows up as an input format for Turing machines<!-- link: ../06-theory-of-computation/04-turing-machines-and-church-turing-thesis.md -->.

## Practice

### Warm-up

1\. Convert $11010_2$ to decimal.

<details class="solution" markdown>
<summary>Solution</summary>

The 1s sit in the places 16, 8 and 2, so $11010_2 = 16 + 8 + 2 = 26$.

Check with Horner's method: 1, then $1 \cdot 2 + 1 = 3$, $3 \cdot 2 + 0 = 6$, $6 \cdot 2 + 1 = 13$ and $13 \cdot 2 + 0 = 26$.

</details>

2\. Convert 41 to binary.

<details class="solution" markdown>
<summary>Solution</summary>

Dividing by 2 until the quotient is 0 gives the quotients 20, 10, 5, 2, 1, 0 and the remainders 1, 0, 0, 1, 0, 1. From the bottom up: $41 = 101001_2$. The zeros in the middle are real digits.

Check: $32 + 8 + 1 = 41$.

</details>

3\. Which of these are valid numbers in the base shown? Give the decimal value of each valid one: $1201_2$, $00101_2$, $\mathrm{7G}_{16}$, $\mathrm{ff}_{16}$ and $0078_8$.

<details class="solution" markdown>
<summary>Solution</summary>

- $1201_2$ is not valid, because binary has no digit 2.
- $00101_2$ is valid. Leading zeros change nothing, so it is $101_2 = 5$.
- $\mathrm{7G}_{16}$ is not valid, because hex digits stop at F.
- $\mathrm{ff}_{16}$ is valid, since case doesn't matter: $15 \cdot 16 + 15 = 255$.
- $0078_8$ is not valid. The leading zeros are fine, but octal digits stop at 7.

Check: `int("00101", 2)` gives 5 and `int("ff", 16)` gives 255, while the other three raise errors in Python.

</details>

### Standard

4\. Convert 500 to hex.

<details class="solution" markdown>
<summary>Solution</summary>

Since $31 \cdot 16 = 496$, dividing 500 by 16 gives 31 remainder 4. Then 31 divided by 16 is 1 remainder 15, written F, and 1 divided by 16 is 0 remainder 1. From the bottom up: $500 = \mathrm{1F4}_{16}$.

Check: $1 \cdot 256 + 15 \cdot 16 + 4 = 256 + 240 + 4 = 500$.

</details>

5\. Convert $1110100111_2$ to hex and to octal.

<details class="solution" markdown>
<summary>Solution</summary>

For hex, group in 4s from the right: 11, 1010, 0111. Padding the left group to 0011 gives the digits 3, A and 7, so the number is $\mathrm{3A7}_{16}$.

For octal, group in 3s from the right: 1, 110, 100, 111. Padding the left group to 001 gives the digits 1, 6, 4 and 7, so the number is $1647_8$.

Check: both answers must be the same number.

$$
\begin{aligned}
\mathrm{3A7}_{16} &= 3 \cdot 256 + 10 \cdot 16 + 7 = 935 \\
1647_8 &= 1 \cdot 512 + 6 \cdot 64 + 4 \cdot 8 + 7 = 935
\end{aligned}
$$

</details>

6\. A university wants to give each of its 5,000 students a different ID made of bits, all of the same length. What is the smallest length that works, and what range of IDs does it allow?

<details class="solution" markdown>
<summary>Solution</summary>

With $n$ bits there are $2^n$ IDs, so we need the smallest $n$ with $2^n \ge 5{,}000$. From the table, $2^{12} = 4{,}096$ is too small and $2^{13} = 8{,}192$ is enough. So the IDs need 13 bits, and they run from 0 to $2^{13} - 1 = 8{,}191$. Some IDs go unused, which is fine.

Check: 12 bits give only 4,096 IDs, which leaves 904 students without one.

</details>

### Challenge

7\. Unix file permissions are written in octal, as in `chmod 755`. (a) Write $755_8$ in binary. (b) Convert it to hex without going through decimal. (c) Explain why you can't turn each octal digit straight into one hex digit.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Each octal digit becomes 3 bits, 7 as 111 and 5 as 101, so $755_8 = 111\,101\,101_2$. Each group holds the read, write and execute bits for one class of user.

(b) Regroup the same 9 bits into 4s from the right: 1, 1110, 1101. Padding the left group to 0001 gives the digits 1, E and D, so the number is $\mathrm{1ED}_{16}$.

(c) An octal digit is 3 bits and a hex digit is 4, so the boundaries between octal digits fall in the middle of hex digits. Copying the digits across would give $755_{16}$, which is 1,877, not 493.

Check: $755_8 = 7 \cdot 64 + 5 \cdot 8 + 5 = 493$ and $\mathrm{1ED}_{16} = 256 + 14 \cdot 16 + 13 = 493$.

</details>

8\. This one reviews place value and long division. (a) Divide 2,705 by 10 again and again, writing down each remainder. What do the remainders spell, and why? (b) Convert 2,705 to base 7, doing each division by long division.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The remainders are 5, 0, 7 and 2, which from the bottom up spell 2705, the number you started with. Each division by 10 chops off the ones digit, which is why repeated division by a base gives the digits in that base.

(b) Start with the long division of 2,705 by 7. Seven goes into 27 three times with 6 left. Bring down the 0 to make 60, which 7 goes into 8 times with 4 left. Bring down the 5 to make 45, which 7 goes into 6 times with 3 left. So $2{,}705 = 386 \cdot 7 + 3$. The same way, $386 = 55 \cdot 7 + 1$. The rest are short:

$$
\begin{aligned}
55 &= 7 \cdot 7 + 6 \\
7 &= 1 \cdot 7 + 0 \\
1 &= 0 \cdot 7 + 1
\end{aligned}
$$

The remainders were 3, 1, 6, 0, 1, so from the bottom up $2{,}705 = 10613_7$. The 0 says there are no 343s.

Check: the place values in base 7 are 1, 7, 49, 343 and 2,401, and $2{,}401 + 0 + 6 \cdot 49 + 7 + 3 = 2{,}401 + 294 + 10 = 2{,}705$.

</details>

## Where this shows up

- Programmers read raw data in hex: memory addresses, bytes in a file, and web colours, where #FF8800 is red 255, green 136 and blue 0 (orange). Octal lives on in Unix permissions such as `chmod 755`.
- The next lesson, bits and information<!-- link: 02-bits-and-information.md -->, measures information in bits. Later in this chapter binary is the base for two's complement<!-- link: 03-binary-arithmetic-and-twos-complement.md -->, floating point<!-- link: 04-floating-point-basics.md --> and bit masks<!-- link: 05-bitwise-operations-and-masks.md -->.
- Questions like Practice 6 are base-2 logarithms in disguise, and [logarithms](../../03-high-school/07-exponentials-and-logarithms/02-logarithms.md) turns the table lookup into a formula.
