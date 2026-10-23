# Canadian mortgage compounding

After this lesson you can convert a quoted mortgage rate with semi-annual compounding into the monthly, biweekly or weekly rate that a payment schedule needs, and explain why the payment differs from the one you get by dividing the quoted rate by 12.

Before this: [mortgage amortization schedules](03-mortgage-amortization-schedules.md), [APR, APY and the effective annual rate](../02-interest-and-growth/03-apr-apy-and-effective-annual-rate.md) and [the loan amortization formula](../03-time-value-of-money/03-loan-amortization-formula.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A rate of 5% compounded semi-annually pays 2.5% every half year. What is the effective annual rate?
2. A rate of 5% compounded monthly pays $\frac{0.05}{12}$ each month. What is its effective annual rate?
3. Which interest rate per month grows a balance by exactly 2.5% over 6 months?

<details class="solution" markdown>
<summary>Answers</summary>

1. $1.025^2 - 1 = 0.050625$, so 5.0625%.
2. $(1 + 0.05/12)^{12} - 1 = 0.051162$, so about 5.1162%.
3. The monthly growth factor $g$ satisfies $g^6 = 1.025$, so $g = 1.025^{1/6} = 1.0041239$, which is a monthly rate of 0.41239%.

</details>

## The idea

A lender quotes you a mortgage rate of 5.00%. That number alone does not say how much interest you will pay, because it does not say how often interest is added to the balance. Interest added twice a year at 2.5% grows a balance more slowly than interest added every month at one twelfth of 5%, even though both are "5% a year". The missing piece is the compounding frequency.

The payment schedule needs a rate per payment: how much the balance grows between one payment and the next. To get it from the quoted rate you need the compounding rule. This lesson states the Canadian rule for fixed-rate mortgages, shows how to turn the quoted rate into a rate per payment, and measures how much the choice of rule matters. The conversion is a small piece of algebra with exponents, the same one that powers the [APR and APY lesson](../02-interest-and-growth/03-apr-apy-and-effective-annual-rate.md).

## Definitions

A **nominal annual rate** $j$ **compounded $m$ times a year** means that interest of $\frac{j}{m}$ of the balance is added $m$ times a year. A quoted rate of 5% compounded semi-annually ($m = 2$) adds 2.5% twice a year. A quoted rate is also called a nominal rate.

The **effective annual rate** (EAR) is the rate that, applied once a year, gives the same growth in a year. For a nominal rate $j$ compounded $m$ times a year,

$$
\text{EAR} = \Bigl(1 + \frac{j}{m}\Bigr)^m - 1.
$$

In plain words, the EAR is what the balance actually grows by in a year, as a fraction of the starting balance. The EAR of 5% compounded semi-annually is 5.0625%.

The **periodic rate** $i_p$ for $p$ payments a year is the rate of growth between two payments. Two rates are **equivalent** if they give the same growth over a year. So the periodic rate $i_p$ must satisfy $(1 + i_p)^p = 1 + \text{EAR}$.

## Compounding in Canadian mortgage law

The Interest Act is a federal law. Its section 6 covers mortgages on real property whose payments blend principal and interest, which describes an ordinary amortized mortgage. It reads ([Interest Act, R.S.C. 1985, c. I-15](https://laws-lois.justice.gc.ca/eng/acts/i-15/FullText.html)):

> Whenever any principal money or interest secured by mortgage on real property or hypothec on immovables is, by the mortgage or hypothec, made payable on a sinking fund plan, on any plan under which the payments of principal money and interest are blended or on any plan that involves an allowance of interest on stipulated repayments, no interest whatever shall be chargeable, payable or recoverable on any part of the principal money advanced, unless the mortgage or hypothec contains a statement showing the amount of the principal money and the rate of interest chargeable on that money, calculated yearly or half-yearly, not in advance.

In plain words: the mortgage contract must state the rate "calculated yearly or half-yearly, not in advance", or the lender cannot collect interest. "Not in advance" means interest is charged on the balance owed, at the end of each period, and not deducted up front. The Act does not say anything about monthly compounding, so a fixed-rate mortgage contract is written with a rate that compounds half-yearly (or yearly).

In practice, Canadian fixed-rate mortgages are quoted with semi-annual compounding. That is the usual convention, and the Act's wording is its legal basis. Your contract states the rule it uses, so check it. Section 4 of the Act, which deals with rates stated for periods shorter than a year, begins "Except as to mortgages on real property", so it does not apply to these mortgages.

Variable-rate mortgages are a different case. As common practice, many lenders quote and compound a variable rate monthly, but this lesson did not find a rule or an official page that says so, so treat it as something to look up in your own contract. What the math below shows is how much the difference matters.

<div class="note" markdown>

The Interest Act is federal law and is amended from time to time. Check the linked text before relying on it for a real decision. This lesson is explanation and is not legal advice.

</div>

## How to do it

### From the quoted rate to the rate per payment

For a quoted rate $j$ compounded semi-annually and $p$ payments a year, the periodic rate is

$$
i_p = \Bigl(1 + \frac{j}{2}\Bigr)^{2/p} - 1.
$$

For monthly payments, $p = 12$ and $i_{12} = (1 + j/2)^{1/6} - 1$. For biweekly payments ($p = 26$) it is $(1 + j/2)^{1/13} - 1$, and for weekly ($p = 52$) it is $(1 + j/2)^{1/26} - 1$.

*Theorem.* Let $j$ be a quoted annual rate compounded semi-annually, and let $p$ be a positive integer. The periodic rate $i_p$ with the same effective annual rate is $i_p = (1 + j/2)^{2/p} - 1$.

*What we know.* One year of semi-annual compounding multiplies a balance by $(1 + j/2)^2$. One year of $p$ periods at rate $i_p$ multiplies it by $(1 + i_p)^p$.

*What we want.* A rate $i_p$ with $(1 + i_p)^p = (1 + j/2)^2$.

*Plan.* Take the $p$-th root of both sides and subtract 1.

*Proof.* Since $1 + i_p > 0$, taking the $p$-th root of $(1 + i_p)^p = (1 + j/2)^2$ gives $1 + i_p = (1 + j/2)^{2/p}$ by the exponent rule $(x^a)^b = x^{ab}$. Subtracting 1 gives the formula. $\blacksquare$

*Look back.* The formula never divides the quoted rate by the number of payments. It finds the growth factor per payment whose repeated product reproduces the annual factor, and that is why the balance after a year is the same whatever the payment frequency.

The steps to a payment are:

1. Write the quoted rate $j$ and note that it compounds semi-annually.
2. Compute the growth factor per payment, $(1 + j/2)^{2/p}$, and subtract 1 to get $i_p$. Keep all the digits.
3. Compute the number of payments, $n = p \times \text{years}$.
4. Compute the payment, $\text{PMT} = L \cdot \frac{i_p}{1 - (1 + i_p)^{-n}}$.
5. Check: $(1 + i_p)^p$ should equal $(1 + j/2)^2$, and $n \cdot \text{PMT}$ should exceed $L$ by the total interest.

### How much the rule matters

This table shows the \$560,000 loan over 25 years at a quoted 5% (made up), with different compounding frequencies. The monthly rate is $(1 + 0.05/m)^{m/12} - 1$ for $m$ compounding periods a year:

| Compounding | Monthly rate | Effective annual rate | Monthly payment | Total interest |
|---|---|---|---|---|
| annual | 0.407412% | 5.0000% | \$3,237.57 | \$411,272.16 |
| semi-annual (Canadian fixed) | 0.412392% | 5.0625% | \$3,256.99 | \$417,096.37 |
| quarterly | 0.414943% | 5.0945% | \$3,266.96 | \$420,087.19 |
| monthly | 0.416667% | 5.1162% | \$3,273.70 | \$422,111.27 |

All four are "5%". The more often interest compounds, the higher the effective rate, the payment and the interest. Semi-annual compounding is a little cheaper than monthly at the same quoted rate: \$16.72 a month, which is $16.7163 \times 300 = 5014.89$, about \$5,015, over 25 years.

For comparing two offers, the effective annual rate is the honest number. A fixed 5.00% compounded semi-annually (EAR 5.0625%) is a slightly lower cost than a 5.00% compounded monthly (EAR 5.1162%). To find the quoted semi-annual rate that matches a monthly-compounded rate $r$, convert through the EAR: $j = 2\bigl((1 + r/12)^6 - 1\bigr)$. For 5% compounded monthly, $j = 5.0524\%$.

## Worked examples

<div class="example" markdown>

### Example 1: a full payment calculation

Find the monthly payment on a \$560,000 mortgage, quoted at 5.00% compounded semi-annually, amortized over 25 years. (The rate is a made-up example.)

Step 1: $j = 0.05$, compounded semi-annually, so the half-year rate is $0.05 \div 2 = 0.025$.

Step 2: the monthly rate is $i = 1.025^{1/6} - 1$. Taking the sixth root of 1.025 gives $1.0041239155$, so $i = 0.0041239155$ (about 0.41239%).

Step 3: $n = 25 \times 12 = 300$.

Step 4: first, $(1 + i)^{-300} = 1.025^{-50} = 0.29094$. The payment is

$$
\text{PMT} = 560000 \times \frac{0.0041239155}{1 - 0.29094} = 560000 \times 0.00581605 = 3256.99.
$$

The payment is \$3,256.99 a month, to the cent. Rounding can move the last cent depending on how many digits you keep, so keep several until the end.

Step 5: check. First, $(1 + i)^{12} = 1.0041239155^{12} = 1.050625$, which equals $1.025^2$. Second, 300 payments total $300 \times 3256.99 = 977097$, so the interest is $977097 - 560000 = 417097$, matching the schedule's \$417,096.37 up to rounding the payment.

Using $0.05 \div 12$ instead would give \$3,273.70, which does not match the Canadian rule.

</div>

<div class="example" markdown>

### Example 2: monthly, biweekly and weekly equivalents

Find the rate per payment for monthly, biweekly and weekly payments at a quoted 5% compounded semi-annually.

Use $i_p = 1.025^{2/p} - 1$ (Step 2).

| Payments | $p$ | Exponent | Rate per payment |
|---|---|---|---|
| monthly | 12 | $\frac{1}{6}$ | 0.412392% |
| biweekly | 26 | $\frac{1}{13}$ | 0.190124% |
| weekly | 52 | $\frac{1}{26}$ | 0.095017% |

Check: all three compound to the same year, $(1.0041239)^{12} = (1.0019012)^{26} = (1.0009502)^{52} = 1.050625$. The rates are not in proportion to the number of periods: $0.412392\% \times \frac{12}{26} = 0.1903\%$, which is close to the biweekly rate, 0.190124%, but not equal to it.

</div>

<div class="example" markdown>

### Example 3: monthly compounding costs more

A lender offers 4.50% compounded semi-annually on a fixed rate. Another offers 4.50% compounded monthly. How do the payments on a \$400,000 loan over 25 years compare? (Both rates are made up.)

For the semi-annual offer, $i = 1.0225^{1/6} - 1 = 0.0037153$, and the payment is \$2,213.89.

For the monthly offer, $i = 0.045 \div 12 = 0.00375$. The payment is $400000 \times \frac{0.00375}{1 - 1.00375^{-300}} = 2223.33$.

The monthly-compounding loan costs \$9.44 more each month, so about $9.44 \times 300 = 2832$ dollars over 25 years.

Check: the effective annual rates are $1.0225^2 - 1 = 4.5506\%$ and $1.00375^{12} - 1 = 4.5940\%$. The second is higher, so its payment is higher.

</div>

<div class="example" markdown>

### Example 4: a 4% mortgage (finish it yourself)

A \$300,000 mortgage is quoted at 4% compounded semi-annually (made up), amortized over 25 years with monthly payments. Find the monthly rate and the payment.

Step 1: the half-year rate is $0.04 \div 2 = 0.02$, so the monthly rate is $i = 1.02^{1/6} - 1$.

Now compute $i$ and the payment, and compare it with the payment you get by using $0.04 \div 12$.

<details class="solution" markdown>
<summary>Finish</summary>

$i = 0.0033058903$. With $n = 300$ the payment is $300000 \times \frac{0.0033058903}{1 - 1.0033058903^{-300}} = 1578.06$, so \$1,578.06.

With $0.04 \div 12 = 0.0033333$ the payment would be \$1,583.51, which is \$5.45 too high.

Check: $(1.0033058903)^{12} = 1.0404$, which equals $1.02^2$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: dividing the quoted rate by 12. For a fixed-rate Canadian mortgage, the monthly rate is $(1 + j/2)^{1/6} - 1$, not $\frac{j}{12}$. The second gives a payment about \$16.72 too high on the \$560,000 loan. Check which rule an online calculator uses before trusting its payment.

</div>

<div class="warning" markdown>

Watch out: dividing the semi-annual rate by 6. Half of 5% is 2.5%, and $\frac{2.5\%}{6} = 0.41667\%$ is the same wrong number as $\frac{5\%}{12}$. The semi-annual rate is 2.5% over six months as a compound factor, not as a sum of six equal pieces.

</div>

<div class="warning" markdown>

Watch out: rounding the monthly rate too early. Rounding 0.0041239155 to 0.0041 changes the payment from \$3,256.99 to \$3,247.66, about \$9 off. Keep at least seven significant digits and round only the final payment.

</div>

Variable-rate mortgages need their own check. If a variable rate compounds monthly, use $i = \frac{j}{12}$ for that mortgage, and read the contract to find out. When the rate changes in the middle of the term, the schedule uses the new rate from that payment on.

The Canadian rule changes only the rate per payment. The formulas for the payment and the balance are exactly the same as in [mortgage amortization schedules](03-mortgage-amortization-schedules.md).

## Tricks and shortcuts

To estimate the monthly rate for a semi-annual rate $j$, divide by 12 and subtract about 1% of the result: $\frac{5\%}{12} = 0.41667\%$ and $0.41667\% \times 0.99 = 0.4125\%$, close to 0.41239%.

To compare any two quotes, convert both to the EAR with $(1 + j/m)^m - 1$. A lower EAR is the lower-cost loan when the term and fees are the same.

## In code

This code converts a quoted semi-annual rate to a rate per payment, checks that every frequency gives the same effective annual rate, and compares the payment with the naive $\frac{j}{12}$.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def periodic_rate(quoted, per_year):
    """Rate per payment, from a quoted rate compounded semi-annually."""
    return (1 + quoted / 2) ** (2 / per_year) - 1

def payment(loan, i, n):
    return loan * i / (1 - (1 + i) ** -n)

j = 0.05
for p in (12, 26, 52):
    i = periodic_rate(j, p)
    print(p, f"{i:.8f}", round((1 + i) ** p - 1, 6))
# 12 0.00412392 0.050625
# 26 0.00190124 0.050625
# 52 0.00095017 0.050625

i = periodic_rate(j, 12)
canadian = payment(560_000, i, 300)
naive = payment(560_000, j / 12, 300)
print(round(canadian, 2), round(naive, 2), round(naive - canadian, 2))  # 3256.99 3273.7 16.72
print(round((naive - canadian) * 300, 2))                               # 5014.89

# Example 3: 4.50% semi-annual against 4.50% monthly, 400,000 over 25 years
print(round(payment(400_000, periodic_rate(0.045, 12), 300), 2))        # 2213.89
print(round(payment(400_000, 0.045 / 12, 300), 2))                      # 2223.33

# Effective annual rate for m compounding periods a year
for m in (1, 2, 4, 12):
    print(m, round((1 + j / m) ** m - 1, 6))
# 1 0.05
# 2 0.050625
# 4 0.050945
# 12 0.051162

# Number of payments for a given payment (a log, see exponential equations)
i = periodic_rate(0.04, 12)
n = -math.log(1 - 200_000 * i / 1_200) / math.log(1 + i)
print(round(n, 1))                                                      # 242.6
```

The function `periodic_rate` is the whole lesson in one line. Everything else is the payment formula from before.

</details>

## FAQ

### Why does the law say "half-yearly" and not "monthly"?

The Interest Act says that the mortgage must state a rate calculated yearly or half-yearly. This lesson does not cover the history behind the wording. What the section requires is a statement of the rate on that basis, and fixed-rate Canadian mortgages follow it with semi-annual compounding.

### Does semi-annual compounding make my mortgage cheaper than a monthly-compounded one?

At the same quoted rate, yes: semi-annual compounding has a lower effective rate. But a lender's quoted rate is not the same across products, so compare the EAR, the term and the fees, not the quoted rates alone.

### Do I pay interest twice a year, then?

No. You pay every month (or biweekly or weekly). The compounding rule only decides how the rate per payment is computed. The interest in each payment is the rate per payment times the balance.

### Why not let the formula take the quoted rate directly?

The payment formula wants the rate per payment. Writing $j/12$ is correct only if the quoted rate compounds monthly. If you make the conversion by exponent, the formula works for every compounding rule and every payment frequency.

## Practice

### Warm-up

1\. Find the effective annual rate of 4% compounded semi-annually.

<details class="solution" markdown>
<summary>Solution</summary>

The half-year rate is 2%, and the EAR is $1.02^2 - 1 = 0.0404$, so 4.04%.

Check: it is a little above 4%, as it should be, because the second half-year's interest earns interest on the first.

</details>

2\. Find the monthly rate equivalent to 6% compounded semi-annually.

<details class="solution" markdown>
<summary>Solution</summary>

The half-year rate is 3%, and the monthly rate is $1.03^{1/6} - 1 = 0.0049386$, so 0.49386%.

Check: $(1.0049386)^6 = 1.03$, and $0.06 \div 12 = 0.5\%$ is a little higher, as expected.

</details>

3\. Find the biweekly rate equivalent to 4% compounded semi-annually.

<details class="solution" markdown>
<summary>Solution</summary>

The half-year rate is 2%. There are 26 biweekly periods in a year, so $\frac{2}{26} = \frac{1}{13}$ of a half-year factor each: $1.02^{1/13} - 1 = 0.0015244$, so 0.15244%.

Check: $(1.0015244)^{26} = 1.0404 = 1.02^2$.

</details>

### Standard

4\. Find the monthly payment on \$300,000 at 4% compounded semi-annually over 25 years. By how much does the payment with the naive rate $0.04 \div 12$ differ?

<details class="solution" markdown>
<summary>Solution</summary>

The monthly rate is 0.0033058903 and $n = 300$, so the payment is \$1,578.06. With $0.04 \div 12 = 0.0033333$, the payment is \$1,583.51, which is \$5.45 higher.

Check: the Canadian rate is slightly lower than the naive one, so its payment must be lower.

</details>

5\. Which costs more, 5% compounded monthly or 5% compounded semi-annually? Find the quoted semi-annual rate that has the same cost as 5% compounded monthly.

<details class="solution" markdown>
<summary>Solution</summary>

Compare effective annual rates: monthly is $(1 + 0.05/12)^{12} - 1 = 5.1162\%$ and semi-annual is $1.025^2 - 1 = 5.0625\%$. The monthly rate costs more.

The matching semi-annual rate $j$ has $(1 + j/2)^2 = 1.051162$, so $j = 2(1.051162^{1/2} - 1) = 5.0524\%$. In the form $2\bigl((1 + 0.05/12)^6 - 1\bigr)$ it is the same number.

Check: $(1 + 0.050524/2)^2 = 1.051162$.

</details>

6\. A mortgage has a monthly rate of 0.4%. What quoted rate, compounded semi-annually, matches it?

<details class="solution" markdown>
<summary>Solution</summary>

Over 6 months the balance grows by $1.004^6 = 1.02424$, which is the half-year growth factor. So the half-year rate is 2.424% and the quoted rate is $2 \times 2.424\% = 4.848\%$.

Check: with $j = 0.04848$, $1 + j/2 = 1.02424$ and $1.02424^{1/6} = 1.004$.

</details>

### Challenge

7\. A borrower owes \$200,000 at 4% compounded semi-annually and pays \$1,200 a month. How many months does it take to pay off the loan? Compare with the payment for a 25-year amortization.

<details class="solution" markdown>
<summary>Solution</summary>

The monthly rate is $i = 1.02^{1/6} - 1 = 0.0033059$. Solving the payment formula for $n$ gives $n = -\frac{\ln(1 - L i / \text{PMT})}{\ln(1 + i)}$. Here $L i = 661.18$, and

$$
n = -\frac{\ln(1 - 661.18 \div 1200)}{\ln 1.0033059} = -\frac{\ln 0.44902}{0.0033004} = 242.6.
$$

It takes 243 payments, about 20.2 years, with the last one smaller. The payment for a 25-year amortization is \$1,052.04, so paying \$1,200 is \$147.96 more a month and saves almost five years.

Check: the formula with $\text{PMT} = 1052.04$ gives $n = 300$.

</details>

8\. (Reviews [exponent rules](../../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md).) Show that compounding the monthly rate $1.025^{1/6} - 1$ for six months gives exactly 2.5%.

<details class="solution" markdown>
<summary>Solution</summary>

The growth factor per month is $1.025^{1/6}$. After six months it is $\bigl(1.025^{1/6}\bigr)^6 = 1.025^{6/6} = 1.025$, by the rule $(x^a)^b = x^{ab}$. So the balance grows by 2.5% in six months.

Check: numerically, $1.0041239155^6 = 1.0250000$.

</details>

## Where this shows up

- The [APR, APY and effective annual rate](../02-interest-and-growth/03-apr-apy-and-effective-annual-rate.md) lesson explains the same conversion for savings accounts and credit cards.
- In the chapter on borrowing, car loans and credit cards use the same payment formula with monthly or daily rates.
- The conversion $(1 + r)^{1/k}$ appears again in [growth rates and CAGR](../../07-economics-math/01-measuring-the-economy/03-growth-rates-and-cagr.md), where a yearly growth rate is turned into a monthly one.
