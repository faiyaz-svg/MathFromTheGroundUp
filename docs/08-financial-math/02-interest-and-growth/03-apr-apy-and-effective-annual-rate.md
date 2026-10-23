# APR, APY and the effective annual rate

After this lesson you can turn a quoted rate with any compounding into the effective annual rate, compare offers fairly, convert a rate from one compounding frequency to an equivalent one, and explain what an APR on a loan is meant to show.

Before this: [compound interest](02-compound-interest.md) and [exponential and logarithmic equations](../../03-high-school/07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. What yearly growth does a nominal 6% compounded monthly give?
2. Which pays more: a nominal 4.9% compounded monthly, or a nominal 5% compounded semi-annually?
3. A nominal 5% compounded quarterly has an effective annual rate of 5.09%. What does that number say about \$1,000 after one year?

<details class="solution" markdown>
<summary>Answers</summary>

1. $\left(1 + \frac{0.06}{12}\right)^{12} - 1 = 0.061678\ldots$, so 6.17% a year.
2. The first has $1.00408\overline{3}^{12} - 1 = 5.012\%$ and the second has $1.025^2 - 1 = 5.0625\%$. The second pays more, although the difference is small.
3. It grows to $1000 \times 1.050945 = 1050.945$, about \$1,050.95. That is the same as if 5.0945% were paid once, at the end of the year.

</details>

## The idea

Two banks advertise savings rates. Bank A says 4.80% compounded monthly, and Bank B says 4.85% compounded annually. Bank B's number is bigger, but Bank A pays interest twelve times a year, and each payment starts earning interest at once. After a year, \$1,000 grows to \$1,049.07 at Bank A and to \$1,048.50 at Bank B. The smaller quoted rate wins.

A quoted rate has two parts that need to be read together: the rate and how often it is compounded. To compare, we convert each offer into one number with the same compounding, and the natural choice is a year. The **effective annual rate** says how much \$1 really grows in a year, with the compounding already included. Loans have a similar problem with fees, and the idea of the annual percentage rate is an attempt to put both the interest and some fees into one yearly number.

## Definitions

The **nominal annual rate** $r$ is the yearly rate as quoted, before the effect of compounding. When it is compounded $n$ times a year, each period earns $\frac{r}{n}$.

The **effective annual rate** (EAR) is the single yearly rate with annual compounding that gives the same growth over a year. It is written $r_{\text{eff}}$ here, and

$$
r_{\text{eff}} = \left(1 + \frac{r}{n}\right)^n - 1.
$$

In plain words, compute the growth factor for one year, which is $\left(1 + \frac{r}{n}\right)^n$, and subtract the 1 you started with. The result is the percent \$1 gains in a year, so it is the number to compare. For a nominal 6% compounded monthly, $r_{\text{eff}} = 1.005^{12} - 1 = 0.061678$, that is, 6.1678%.

The **annual percentage yield** (APY) is the name used for the effective annual rate on deposits, mainly in the United States. It is the same number as the EAR. Some Canadian banks use the term too, and others only quote a rate. If an advertisement does not say which one it shows, look for the compounding period.

The **annual percentage rate** (APR) is a yearly rate that is meant to express the cost of a loan. In its everyday meaning, it is the interest rate plus some of the fees, expressed per year. The details depend on the rules for the product, so they are described below rather than by one formula.

## How to do it

### From a nominal rate to the EAR

1. Write the nominal rate $r$ as a decimal and the number of compounding periods per year, $n$.
2. Compute the periodic rate $\frac{r}{n}$ and add 1.
3. Raise it to the power $n$.
4. Subtract 1 and write the result as a percent.

For a nominal 5%, the EAR rises with $n$ but only a little:

| Compounded | $n$ | Effective annual rate |
|---|---|---|
| annually | 1 | 5.0000% |
| semi-annually | 2 | 5.0625% |
| quarterly | 4 | 5.0945% |
| monthly | 12 | 5.1162% |
| weekly | 52 | 5.1246% |
| daily | 365 | 5.1267% |
| continuously | | 5.1271% |

When $n = 1$, the nominal and effective rates are equal. For any $n > 1$ the EAR is higher, and it has an upper limit, which the [next lesson](04-continuous-compounding-and-e.md) finds.
### Comparing offers

Convert every offer to its EAR, then pick the highest EAR for a deposit or the lowest for a loan. Two offers with the same compounding can be compared by their nominal rates, and that is the only case where the shortcut is safe.

### Equivalent rates

Two rates with different compounding are **equivalent** if they have the same EAR, so that they give the same growth over any whole number of years. Setting the yearly growth factors equal gives

$$
\left(1 + \frac{r_1}{n_1}\right)^{n_1} = \left(1 + \frac{r_2}{n_2}\right)^{n_2}.
$$

Solve for the unknown nominal rate $r_2$ by taking the $n_2$-th root:

$$
r_2 = n_2\left(\left(1 + \frac{r_1}{n_1}\right)^{n_1/n_2} - 1\right).
$$

In plain words, find the growth factor for a year, take the root that gives the growth factor for one period of the new compounding, subtract 1 and multiply by the number of periods. For an effective annual rate $r_{\text{eff}}$ the same formula starts from $n_1 = 1$ and $r_1 = r_{\text{eff}}$.

### The APR on a loan

A loan has costs beyond the rate: an application fee, an administration fee, insurance that is required to get the loan. The idea of an annual percentage rate is to turn the interest and some of these fees into a single rate per year, so that two loans with different fee structures can be compared.

Suppose you borrow \$2,000 for one year at 6% simple interest and pay a \$40 fee, which is taken out of the loan so that you receive \$1,960. You pay back \$2,120. Your cost is \$160 on money you actually had of \$1,960, and $\frac{160}{1960} = 8.16\%$. The loan is worth about 8.16% a year to the lender, not 6%.

That shows the general idea: fees raise the true yearly cost above the interest rate. This is the idea, and not the formula in the law. Which fees count, and how the calculation is set up, depends on the type of loan and on the regulations that apply, so use the lender's disclosure and not your own arithmetic when the two differ. The Financial Consumer Agency of Canada (FCAC) says that federally regulated lenders, such as banks, must give you the loan amount, the interest rate (fixed or variable), the term, the payment amount and other fees and service charges when you take a personal loan, and that lenders under provincial or territorial regulation may not have to ([FCAC, personal loans](https://www.canada.ca/en/financial-consumer-agency/services/loans/personal-loans.html), page dated 2025-10-14). The same page says that by law lenders may not charge more than 35% interest annually, and that this includes all fees, costs and interest paid to get the loan.

### Mortgages

Fixed-rate mortgages in Canada are usually quoted with semi-annual compounding. Section 6 of the federal [Interest Act](https://laws-lois.justice.gc.ca/eng/acts/i-15/FullText.html) requires a mortgage to state its rate "calculated yearly or half-yearly, not in advance", which is the legal background of that convention. A mortgage quoted at 5% has $n = 2$, so its EAR is $1.025^2 - 1 = 5.0625\%$, and its monthly payments are based on an equivalent monthly rate. The equivalent nominal rate compounded monthly is $12\left(1.025^{1/6} - 1\right) = 4.9487\%$, which is a monthly rate of 0.4124%. The lesson on [Canadian mortgage compounding](../05-housing/04-canadian-mortgage-compounding.md) works this out in full.

<div class="note" markdown>

The 35% limit is a changing figure. The Criminal Code (section 347) defines the criminal rate as an annual percentage rate of interest, calculated in accordance with generally accepted actuarial practices and principles, above 35% on the credit advanced ([Justice Laws](https://laws-lois.justice.gc.ca/eng/acts/c-46/section-347.html)). The 35% level has been in force since January 1, 2025, and it replaced a higher limit. Some loans have their own rules: payday loans in provinces that regulate them have a separate cap, which Example 4 of the simple interest lesson mentions. Rules change, so check the linked pages before using these figures for a real decision.

</div>

## Worked examples

<div class="example" markdown>

### Example 1: choosing between three savings offers

Three accounts advertise: A pays a nominal 4.80% compounded monthly, B pays 4.85% compounded annually and C pays 4.82% compounded semi-annually. The rates are made up. Which pays the most?

Step 1: the nominal rates are 0.0480, 0.0485 and 0.0482, with $n = 12$, $1$ and $2$.

Steps 2 and 3: the one-year growth factors are

$$
\left(1 + \tfrac{0.048}{12}\right)^{12} = 1.049070, \qquad 1.0485, \qquad \left(1 + \tfrac{0.0482}{2}\right)^2 = 1.048781.
$$

Step 4: subtract 1. The EARs are 4.9070% for A, 4.8500% for B and 4.8781% for C.

Account A pays the most, although it has the lowest nominal rate. The order of the nominal rates is B, C, A and the order of the EARs is A, C, B, which is the reverse.

Check: on \$10,000 for a year, A pays \$490.70, C pays \$487.81 and B pays \$485.00.

</div>

<div class="example" markdown>

### Example 2: converting a rate

(a) A savings account pays an effective annual rate of 5%. What nominal rate compounded monthly is equivalent? (b) A nominal 6% compounded monthly is equivalent to what nominal rate compounded semi-annually?

(a) Start from $n_1 = 1$ and $r_1 = 0.05$ and go to $n_2 = 12$:

$$
r_2 = 12\left(1.05^{1/12} - 1\right) = 12 \times 0.004074 = 0.048889.
$$

The nominal rate is 4.889% compounded monthly, a monthly rate of 0.4074%. It is less than 5% because monthly compounding does some of the work. Check: $1.004074^{12} = 1.05$.

(b) The yearly growth factor of 6% monthly is $1.005^{12} = 1.061678$, and the factor for half a year is $1.005^6 = 1.030378$. So the semi-annual periodic rate is 3.0378%, and the nominal rate is $2 \times 3.0378\% = 6.0755\%$. Check: $1.030378^2 = 1.061678$, the same yearly factor.

</div>

<div class="example" markdown>

### Example 3: a fee turns into a rate

You borrow \$5,000 for one year at 7% simple interest, and the lender takes a \$100 fee out of the amount, so you receive \$4,900. What yearly rate is the cost on the money you receive?

The interest is $5000 \times 0.07 = 350$. The cost is $350 + 100 = 450$ dollars, on \$4,900 received, so the rate is $\frac{450}{4900} = 0.0918$, or 9.18%. Without the fee it would be 7%. The fee adds 2.18 percentage points.

Check: $4900 \times 0.0918 = 449.82$, close to 450 (the rate was rounded). This is the general idea of an APR. A lender's disclosed APR follows the rules for that product.

</div>

<div class="example" markdown>

### Example 4: a short loan, two ways (finish it yourself)

Example 4 of the [simple interest lesson](01-simple-interest.md) found that a \$14 fee per \$100 for 14 days is 365% a year as a simple rate. As an effective annual rate, treat each 14 days as one compounding period with a 14% rate. There are $\frac{365}{14}$ periods in a year.

Step 1: the growth factor per period is 1.14, and the number of periods per year is $\frac{365}{14} = 26.07$.

Step 2: the yearly factor is $1.14^{26.07}$.

Finish: compute the EAR.

<details class="solution" markdown>
<summary>Finish</summary>

$1.14^{26.0714} = 30.45$, so the EAR is $30.45 - 1 = 29.45$, that is, 2,945% a year.

Check: $\ln 1.14 = 0.131028$ and $26.0714 \times 0.131028 = 3.4162$, and $e^{3.4162} = 30.45$. The simple rate (365%) and the compounded rate (2,945%) differ because they answer different questions: one adds up the fees of 26 loans, the other assumes each new loan is the whole balance rolled over.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: comparing nominal rates with different compounding. A quoted 4.85% annually is not better than 4.80% monthly, as Example 1 showed. Convert both to EAR first.

</div>

<div class="warning" markdown>

Watch out: halving the EAR to get a semi-annual rate. An effective rate of 5% is not "2.5% twice a year": that would give $1.025^2 = 1.050625$, an EAR of 5.0625%. The equivalent semi-annual nominal rate is $2 \times (1.05^{1/2} - 1) = 4.939\%$.

</div>

<div class="warning" markdown>

Watch out: reading an APR as the whole cost. A loan's APR does not include every charge. Late fees and prepayment penalties usually appear separately, and so does optional insurance. Read the loan's own disclosure.

</div>

When $n$ is 1 the EAR equals the nominal rate, and when the rate is 0% it is 0% for every $n$. For a loan, the opposite side of the table applies: the lender prefers more frequent compounding, so a loan quoted at 12% compounded monthly costs 12.68% a year, not 12%.

## Tricks and shortcuts

For small rates, the EAR is close to $r + \frac{r^2}{2}\left(1 - \frac{1}{n}\right)$. At 5% compounded monthly, that is $0.05 + 0.00125 \times \frac{11}{12} = 0.05115$, against the exact 5.1162%. So compounding adds about half of $r^2$ to the rate, at most. At 5% that is at most 0.125 percentage points.

A quick check on any EAR: it must lie between the nominal rate and $e^r - 1$, the continuous limit. For 6% monthly, $0.06 < 0.061678 < 0.061837$.

## In code

The code computes an EAR, converts between compounding frequencies, and finds the APR-like rate of a loan with an up-front fee.

<details class="code" markdown>
<summary>In code</summary>

```python
def ear(r, n):
    return (1 + r / n) ** n - 1

def convert(r1, n1, n2):
    """Nominal rate compounded n2 times a year with the same EAR as r1 at n1."""
    return n2 * ((1 + r1 / n1) ** (n1 / n2) - 1)

print(round(100 * ear(0.06, 12), 4))             # 6.1678
for r, n in [(0.048, 12), (0.0485, 1), (0.0482, 2)]:
    print(n, round(100 * ear(r, n), 4))          # 12 4.907, then 1 4.85, then 2 4.8781
print(round(100 * convert(0.05, 1, 12), 4))      # 4.8889
print(round(100 * convert(0.06, 12, 2), 4))      # 6.0755
print(round(100 * convert(0.05, 2, 12), 4))      # 4.9487, a 5% mortgage as a monthly rate

print(round(100 * 450 / 4900, 2))                # 9.18, Example 3
print(round(100 * (1.14 ** (365 / 14) - 1)))     # 2945, Example 4
```

</details>

## FAQ

### Is the APY the same as the EAR?

Yes. Both are the yearly growth of \$1 with compounding included. "APY" is the usual word for a deposit and mainly an American one, and "effective annual rate" is the general term. The APR is a different thing: it is for loans, and it adds fees.

### Why do banks quote the nominal rate and not the EAR?

The nominal rate is the number that goes into the payment formulas, and for a loan it is the smaller of the two numbers, so it looks better in an advertisement. Disclosure rules require lenders to show certain information, and the exact rules depend on the product. The EAR is the number that lets you check the quote yourself.

### Why does a mortgage use a nominal rate with half-yearly compounding when the payments are monthly?

The quote follows the convention described above. The payment schedule then uses the equivalent monthly rate, $1.025^{1/6} - 1$ for a 5% quote, so that the balance grows by the same yearly factor as a half-yearly quote would give. The EAR of 5.0625% is what the borrower really pays on an unpaid balance for a year.

## Practice

### Warm-up

1\. Find the EAR of a nominal 6% compounded quarterly.

<details class="solution" markdown>
<summary>Solution</summary>

$n = 4$, so $\left(1 + \frac{0.06}{4}\right)^4 - 1 = 1.015^4 - 1 = 0.061364$, that is, 6.1364%.

Check: it is between 6% and the continuous limit $e^{0.06} - 1 = 6.1837\%$.

</details>

2\. Find the EAR of a nominal 3% compounded daily, with 365 days a year.

<details class="solution" markdown>
<summary>Solution</summary>

$\left(1 + \frac{0.03}{365}\right)^{365} - 1 = 0.030453$, so 3.0453%.

Check: the continuous limit is $e^{0.03} - 1 = 3.0455\%$, just above.

</details>

3\. A credit account charges 1.5% per month. What is its effective annual rate?

<details class="solution" markdown>
<summary>Solution</summary>

The monthly rate is 0.015 and there are 12 months: $1.015^{12} - 1 = 0.195618$, so 19.56%. The nominal rate is $12 \times 1.5\% = 18\%$.

Check: $1.015^{12} = 1.1956$, and the EAR is above the nominal 18% as it must be.

</details>

### Standard

4\. Rank three deposits by EAR: 4.5% compounded monthly, 4.6% compounded semi-annually and 4.55% compounded annually.

<details class="solution" markdown>
<summary>Solution</summary>

Monthly: $\left(1 + \frac{0.045}{12}\right)^{12} - 1 = 4.594\%$. Semi-annual: $1.023^2 - 1 = 4.6529\%$. Annual: 4.55%. The ranking is 4.6% semi-annual (4.6529%), then 4.5% monthly (4.594%), then 4.55% annual (4.55%).

Check: the semi-annual one also has the highest nominal rate, so it should rank first.

</details>

5\. What nominal rate compounded monthly is equivalent to an effective annual rate of 7%?

<details class="solution" markdown>
<summary>Solution</summary>

$r = 12\left(1.07^{1/12} - 1\right) = 12 \times 0.005654 = 0.06785$, that is, 6.785% compounded monthly.

Check: $\left(1 + \frac{0.06785}{12}\right)^{12} = 1.07000$.

</details>

6\. Deposit A pays a nominal 3.90% compounded semi-annually. Deposit B pays 3.85% compounded monthly. Which pays more on \$10,000 over a year, and by how much?

<details class="solution" markdown>
<summary>Solution</summary>

A: $1.0195^2 - 1 = 3.938\%$, which is \$393.80 on \$10,000. B: $\left(1 + \frac{0.0385}{12}\right)^{12} - 1 = 3.919\%$, which is \$391.87. A pays about \$1.94 more.

Check: B compounds more often, but the 0.05 percentage point gap in the quoted rates is larger than what monthly compounding adds over semi-annual at these rates, so A comes out ahead.

</details>

### Challenge

7\. A lender offers \$8,000 for one year at 6% simple interest, with a \$160 fee deducted from the loan. (a) What yearly rate is the cost on the money you receive? (b) By how many percentage points does the fee raise the cost above the quoted 6%?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The interest is $8000 \times 0.06 = 480$. The cost is $480 + 160 = 640$ on $8000 - 160 = 7840$ received: $\frac{640}{7840} = 0.08163$, which is 8.16%.

(b) $8.16 - 6 = 2.16$, so the fee adds about 2.16 percentage points. A \$160 fee on \$8,000 looks like 2%, but it is paid on a loan that is \$160 smaller, and it is charged once while the money is borrowed for a year.

Check: $7840 \times 0.0816 = 639.74$, close to 640.

</details>

8\. (Reviews [compound interest](02-compound-interest.md).) A nominal 5% compounded monthly is used for 3 years on \$1,000. Show that the amount equals $1000 \times (1 + r_{\text{eff}})^3$ and give both numbers.

<details class="solution" markdown>
<summary>Solution</summary>

Directly, $1000\left(1 + \frac{0.05}{12}\right)^{36} = 1161.47$. The EAR is $r_{\text{eff}} = 0.051162$, and $1000 \times 1.051162^3 = 1161.47$.

They agree because $\left(\left(1 + \frac{r}{n}\right)^n\right)^t = \left(1 + \frac{r}{n}\right)^{nt}$: the EAR packs a year of monthly steps into one factor.

Check: both values equal $1161.4722\ldots$.

</details>

## Where this shows up

- The [continuous compounding lesson](04-continuous-compounding-and-e.md) takes $n \to \infty$, and [inflation and real returns](06-inflation-and-real-returns.md) uses the EAR to compare a rate with the rise in prices. Mortgages, student loans and credit cards use these conversions each time a monthly payment is figured from a yearly rate.
- Economics: effective annual rates are the form in which interest rates are compared across assets, and the growth-rate lessons in [growth rates and CAGR](../../07-economics-math/01-measuring-the-economy/03-growth-rates-and-cagr.md) use the same conversion between periods.
- Everyday money: a credit card with a monthly rate and a savings account with daily interest both need the EAR before you can compare them with anything else.
