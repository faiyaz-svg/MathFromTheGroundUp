# Mortgage basics

After this lesson you can tell a mortgage's term from its amortization, compute the minimum down payment and the mortgage insurance premium for a price, apply the stress test, and check a purchase against the GDS and TDS limits.

Before this: [renting vs buying a home](01-renting-vs-buying-a-home.md), [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md) and [the loan amortization formula](../03-time-value-of-money/03-loan-amortization-formula.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. For a \$650,000 home, the minimum down payment is 5% of the first \$500,000 and 10% of the rest. Find it.
2. A buyer puts 10% down on a \$500,000 home. The mortgage insurance premium for that loan-to-value is 3.10% of the loan. Find the premium and the total loan once the premium is added.
3. The qualifying rate is the greater of the contract rate plus 2 percentage points and 5.25%. What is it for a contract rate of 4.25%, and for 2.9%?

<details class="solution" markdown>
<summary>Answers</summary>

1. $0.05 \times 500000 + 0.10 \times 150000 = 25000 + 15000 = 40000$, so \$40,000.
2. The loan is $500000 - 50000 = 450000$. The premium is $0.031 \times 450000 = 13950$, and the total loan is $450000 + 13950 = 463950$, so \$463,950.
3. For 4.25% the sum is $4.25 + 2 = 6.25\%$, which is greater than 5.25%, so the rate is 6.25%. For 2.9% the sum is 4.9%, below 5.25%, so the rate is 5.25%.

</details>

## The idea

A mortgage is a loan used to buy property, where the property itself is the lender's protection: if you stop paying, the lender can take the home and sell it. Almost nobody pays the full price of a home in cash, so the mortgage is usually the largest debt a person takes on, and the lender's rules decide who can borrow and how much.

Those rules answer three questions. How much of your own money must go in first (the down payment)? Is the lender protected if the loan is large compared with the home's value (mortgage insurance)? Could you still make the payments if rates rose (the stress test and the debt ratios)? Each question has a number attached, and each number is a small calculation, so this lesson is mostly percent arithmetic with a few Canadian rules.

The mortgage also has two different lengths, which beginners often mix up. The loan is calculated as if it would be paid off over 25 years, but the contract with the lender, and its interest rate, lasts only 5 years in a typical case. After the 5 years you renew at whatever rate is offered then. The next lesson, [mortgage amortization schedules](03-mortgage-amortization-schedules.md), follows one mortgage through a renewal.

## Definitions

A **mortgage** is a loan secured by real property: the lender holds a legal claim on the property until the loan is repaid. The **principal** is the amount borrowed that is still owed.

The **mortgage term** is the length of time the contract is in effect, including its interest rate. The **amortization period** is the length of time it would take to pay off the whole loan with the regular payments. In plain words, the amortization sets the size of the payment, and the term is how long that deal lasts before you renegotiate. The Financial Consumer Agency of Canada (FCAC) describes both in its page on [choosing a mortgage](https://www.canada.ca/en/financial-consumer-agency/services/mortgages/choose-mortgage.html).

The **down payment** is the part of the price you pay from your own money. The **loan-to-value ratio** (LTV) is the loan divided by the price (or the home's value):

$$
\text{LTV} = \frac{\text{loan}}{\text{price}}.
$$

In plain words, an LTV of 90% means the lender is financing 90 cents of each dollar of the price. A mortgage with an LTV above 80% is called **high-ratio**, and in Canada it has to be covered by mortgage loan insurance.

**Mortgage loan insurance** is a policy that protects the lender, not the borrower, if the borrower defaults. The borrower pays the premium. In Canada the insurer can be CMHC (the Canada Mortgage and Housing Corporation) or a private company.

The **stress test** is a rule that you must qualify for the mortgage at a **qualifying rate** higher than your contract rate. The **gross debt service ratio** (GDS) is the monthly housing cost divided by gross (before-tax) monthly income. The **total debt service ratio** (TDS) is the monthly housing cost plus all other monthly debt payments, divided by gross monthly income.

A **fixed-rate** mortgage keeps the same interest rate for the whole term. A **variable-rate** mortgage has a rate that can go up and down during the term.

A **prepayment privilege** is the amount you may pay on top of your regular payments each year without a penalty.

## How to do it

### The minimum down payment

The rule on the FCAC's [down payment page](https://www.canada.ca/en/financial-consumer-agency/services/mortgages/down-payment.html) has three cases:

| Purchase price | Minimum down payment |
|---|---|
| up to \$500,000 | 5% of the price |
| over \$500,000 and under \$1,500,000 | 5% of the first \$500,000, plus 10% of the part above \$500,000 |
| \$1,500,000 or more | 20% of the price |

CMHC's [purchase page](https://www.cmhc-schl.gc.ca/professionals/project-funding-and-mortgage-financing/mortgage-loan-insurance/mortgage-loan-insurance-homeownership-programs/purchase) says the same for one- and two-unit homes, and that insured loans must have a purchase price below \$1,500,000. The \$1.5 million cap took effect on December 15, 2024, and replaced the old \$1 million cap ([Finance Canada](https://www.canada.ca/en/department-finance/news/2024/12/boldest-mortgage-reforms-in-decades-come-into-force-today.html)). So for a price of \$1.5 million or more, the buyer needs at least 20% down, and no insured mortgage is available.

Here are the minimums for six made-up prices:

| Price | Minimum down | As a percent of the price |
|---|---|---|
| \$300,000 | \$15,000 | 5.0% |
| \$500,000 | \$25,000 | 5.0% |
| \$600,000 | \$35,000 | 5.8% |
| \$1,000,000 | \$75,000 | 7.5% |
| \$1,400,000 | \$115,000 | 8.2% |
| \$1,500,000 | \$300,000 | 20.0% |

At \$1,400,000 the minimum is $25000 + 0.10 \times 900000 = 115000$, and at \$1,500,000 it jumps to \$300,000. The jump is an edge in the rule: at a price just under \$1,500,000 the minimum is about \$125,000, and at \$1,500,000 it is \$300,000, a jump of about \$175,000.

<div class="note" markdown>

These figures are for 2026 and change from time to time. Check the linked pages before using them for real decisions.

</div>

### Mortgage insurance premiums

When the down payment is under 20% of the price, the loan is high-ratio and has to be insured. The premium is a percent of the loan, set by the LTV. CMHC publishes the table on its [premium page](https://www.cmhc-schl.gc.ca/professionals/project-funding-and-mortgage-financing/mortgage-loan-insurance/mortgage-loan-insurance-homeownership-programs/premium-information-for-homeowner-and-small-rental-loans). This is CMHC's current table for owner-occupied homes:

| Loan-to-value | Premium, as a percent of the loan |
|---|---|
| up to 65% | 0.60% |
| over 65% to 75% | 1.70% |
| over 75% to 80% | 2.40% |
| over 80% to 85% | 2.80% |
| over 85% to 90% | 3.10% |
| over 90% to 95% | 4.00% |

CMHC's table has one more row, for the 90% to 95% range when the down payment is not from traditional sources, at 4.50%. The premium is usually added to the loan, so you pay interest on it for the whole amortization. The LTV that sets the premium rate is the one before the premium is added.

CMHC's page also says that premiums in Quebec, Ontario and Saskatchewan are subject to provincial sales tax, and that this tax cannot be added to the loan amount. The page does not give the rate, so this lesson does not either. In Ontario the sales tax on the premium is paid in cash at closing, which belongs in your closing-cost budget.

The steps are:

1. Find the minimum or chosen down payment, using the table above.
2. The loan is the price minus the down payment. The LTV is the loan divided by the price.
3. If the LTV is 80% or less, no insurance is needed. Otherwise find the LTV's row in the premium table.
4. The premium is that percent of the loan. The total loan is the loan plus the premium.
5. Check that the LTV is at most 95%, because a down payment under 5% is not allowed.

### The stress test

Lenders must make sure you could keep paying if rates rose. The test uses a qualifying rate, which, according to the FCAC page on [preparing for a mortgage](https://www.canada.ca/en/financial-consumer-agency/services/mortgages/preparing-mortgage.html), is the higher of 5.25% and your negotiated rate plus 2%. The FCAC says this applies to both insured and uninsured mortgages. The Office of the Superintendent of Financial Institutions (OSFI) states the same rule for [uninsured mortgages](https://www.osfi-bsif.gc.ca/en/supervision/financial-institutions/banks/minimum-qualifying-rate-uninsured-mortgages): "the greater of the mortgage contract rate plus 2% or 5.25%".

You compute the payment at the qualifying rate, over the amortization period, and use that payment (not the real one) in the debt ratios below. Your real payment is lower than the one used in the test, so the test is a safety margin.

### The GDS and TDS ratios

The FCAC page above gives the guideline limits: housing costs should be at most 39% of gross household income (GDS), and total debts at most 44% (TDS). The page adds that you may still qualify with a ratio slightly above these limits. CMHC's [Home Start page](https://www.cmhc-schl.gc.ca/professionals/project-funding-and-mortgage-financing/mortgage-loan-insurance/mortgage-loan-insurance-homeownership-programs/home-start) uses the same limits, calculated at the qualifying rate, for its insured 30-year loans.

Housing costs, according to the FCAC, are the mortgage payment, property taxes, heating, and 50% of condo fees if you have any. In symbols, with monthly amounts:

$$
\text{GDS} = \frac{\text{mortgage payment} + \text{property tax} + \text{heating} + 0.5 \times \text{condo fees}}{\text{gross monthly income}},
$$

$$
\text{TDS} = \frac{\text{housing costs} + \text{other debt payments}}{\text{gross monthly income}}.
$$

Other debt payments include car loans, minimum credit card payments, lines of credit and student loan payments.

To find the largest mortgage a lender would approve:

1. Find the gross monthly income and multiply by 0.39 and by 0.44.
2. Subtract from the 39% amount the property tax and heating (and half the condo fee). Subtract from the 44% amount the same housing costs and the other debt payments.
3. The smaller of the two results is the most you can spend on the mortgage payment.
4. Turn that payment into a loan size, by solving the payment formula for the loan at the qualifying rate: $L = \text{payment} \cdot \frac{1 - (1+i)^{-n}}{i}$, where $i$ is the monthly rate and $n$ the number of payments.

### Fixed or variable

With a fixed rate the payment is known for the whole term, so the cost of the mortgage in the term is known in advance. With a variable rate, the rate can change, and so can the cost. The FCAC notes that fixed rates are usually higher than variable rates for a similar term at the time you sign.

This lesson does not predict which will cost less, because nobody knows. What the math can say is how much a change matters. This table uses a made-up \$500,000 balance amortized over 25 years, with payments computed as in [Canadian mortgage compounding](04-canadian-mortgage-compounding.md):

| Quoted rate (made up) | Monthly payment |
|---|---|
| 4% | \$2,630.10 |
| 5% | \$2,908.02 |
| 6% | \$3,199.03 |

Each extra percentage point adds about \$280 to \$290 a month. A buyer with a variable rate should ask whether the budget survives a rise of that size.

### Amortization limits

The standard maximum amortization for an insured mortgage is 25 years. Since December 15, 2024, 30-year amortizations are allowed for all first-time buyers and for all buyers of newly built homes (Finance Canada release above). CMHC's Home Start page lists the conditions: at least one borrower is a first-time buyer, or the home is newly built; the home is owner-occupied; the mortgage is high-ratio; at least one borrower has a credit score of 600; the price is under \$1,500,000; and GDS and TDS are at most 39% and 44% at the qualifying rate. The premium for a 30-year amortization is 0.20 percentage points higher than the standard table. For the 90% to 95% LTV row it is 4.20%.

A longer amortization lowers the payment but raises the total interest, which Example 1 and Practice 7 show.

### Prepayment privileges

Most mortgages limit how much extra you can pay without a penalty. The FCAC describes the prepayment privilege as the amount you can put toward the mortgage on top of the regular payments, and says that privileges vary by lender and that you should check the contract for minimums and maximums ([FCAC on prepayment penalties](https://www.canada.ca/en/financial-consumer-agency/services/mortgages/reduce-prepayment-penalties.html)). Typical privileges include a yearly lump sum up to some percent of the original loan, or raising the regular payment by some percent. An open mortgage allows any prepayment without a penalty.

Going over the limit, or breaking the contract before the end of the term, can trigger a penalty. The FCAC says lenders typically charge the higher of three months' interest on what you still owe and the interest rate differential (IRD), and that the calculation differs by lender. For a \$495,642.04 balance, three months of interest at a quoted 5% is about $3 \times 2043.99 = 6131.96$, so about \$6,132. The IRD can be larger, and you should ask your lender how theirs works.

## Worked examples

<div class="example" markdown>

### Example 1: a \$600,000 home with the minimum down payment

A first-time buyer wants to buy a \$600,000 home with the smallest legal down payment. Find the down payment, the premium, the total loan and the monthly payment at a quoted 5% over 25 years. (The 5% is a made-up example rate.)

Step 1: the minimum down payment is $0.05 \times 500000 + 0.10 \times 100000 = 25000 + 10000 = 35000$, so \$35,000.

Step 2: the loan is $600000 - 35000 = 565000$, and the LTV is $565000 \div 600000 = 0.9417$, or 94.17%.

Step 3: the LTV is above 80%, so the loan must be insured. It falls in the "over 90% to 95%" row, which is 4.00%.

Step 4: the premium is $0.04 \times 565000 = 22600$, so the total loan is $565000 + 22600 = 587600$, that is, \$587,600.

The payment uses the loan formula with the Canadian monthly rate from the [next lessons](04-canadian-mortgage-compounding.md): $i = (1.025)^{1/6} - 1 = 0.0041239$ and $n = 300$:

$$
\text{payment} = 587600 \times \frac{i}{1 - (1+i)^{-300}} = 3417.51.
$$

Check: 300 payments of \$3,417.51 total \$1,025,253, and subtracting the \$587,600 loan leaves \$437,653 of interest. The monthly payment is more than the interest of the first month ($587600 \times i = 2423.1$), as it must be.

If the buyer qualifies for a 30-year amortization, the premium row is 4.20%, so the premium is \$23,730 and the loan is \$588,730. The payment falls to \$3,141.997, which is \$3,142.00 rounded, \$275.51 less per month, but the total paid over 30 years is \$1,131,119, and the interest is \$542,389, which is \$104,736 more than in the 25-year case.

</div>

<div class="example" markdown>

### Example 2: the stress test and the ratios

A buyer is buying a \$700,000 home with 20% down. The loan is \$560,000 at a contract rate of 5% (made up), over 25 years. Property tax is \$5,600 a year and heating is \$150 a month. Gross household income is \$150,000, and there is a \$600 monthly car payment. Does the buyer pass the GDS and TDS limits?

The qualifying rate is the greater of $5 + 2 = 7\%$ and 5.25%, so 7%. The payment at 7% over 25 years is \$3,922.33, compared with \$3,256.99 at the contract rate.

Housing costs: $3922.33 + 5600 \div 12 + 150 = 3922.33 + 466.67 + 150 = 4538.99$. Monthly income: $150000 \div 12 = 12500$.

GDS: $4538.99 \div 12500 = 0.3631$, which is 36.3%, under 39%.

TDS: $(4538.99 + 600) \div 12500 = 0.4111$, which is 41.1%, under 44%.

Both limits pass. Check: 39% of \$12,500 is \$4,875, and the housing costs of \$4,538.99 are below that. The income that makes GDS exactly 39% is $4538.99 \div 0.39 \times 12 = 139661.38$, which is below \$150,000.

</div>

<div class="example" markdown>

### Example 3: the most you can borrow

A household earns \$120,000 a year. Property tax is \$5,600 a year (\$466.67 a month), heating is \$150 a month, and there is \$800 a month of other debt payments. The qualifying rate is 7%. What is the largest mortgage, over 25 years, that passes both limits?

Monthly income is \$10,000. The 39% limit is \$3,900 and the 44% limit is \$4,400.

The GDS room for the mortgage payment is $3900 - 466.67 - 150 = 3283.33$. The TDS room is $4400 - 800 - 466.67 - 150 = 2983.33$.

The TDS room is smaller, so it decides: the payment at the qualifying rate can be at most \$2,983.33. With $i = 1.035^{1/6} - 1$ and $n = 300$:

$$
L = 2983.33 \times \frac{1 - (1+i)^{-300}}{i} = 425937.
$$

So the largest mortgage is about \$425,937. Without the \$800 debts, the GDS room of \$3,283.33 would allow about \$468,769, so the debts cost the household about \$42,800 of borrowing room.

Check: the payment on \$425,937 at 7% over 25 years is \$2,983.33, and the TDS is $(2983.33 + 466.67 + 150 + 800) \div 10000 = 0.44$.

</div>

<div class="example" markdown>

### Example 4: premium on a 5% down payment (finish it yourself)

A buyer puts the minimum 5% down on a \$500,000 home. Find the loan, the LTV, the premium and the total loan, then the monthly payment at a quoted 5% over 25 years.

Step 1: the down payment is $0.05 \times 500000 = 25000$ and the loan is \$475,000. The LTV is $475000 \div 500000 = 95\%$, in the "over 90% to 95%" row.

Now find the premium and the total loan, and compute the payment with $i = 1.025^{1/6} - 1$.

<details class="solution" markdown>
<summary>Finish</summary>

The premium is $0.04 \times 475000 = 19000$, so the total loan is \$494,000. The payment is $494000 \times \frac{i}{1 - (1+i)^{-300}} = 2873.13$, so \$2,873.13 a month.

Check: the payment is $494000 \div 587600 = 0.8407$ times the one in Example 1 on a \$587,600 loan, and $0.8407 \times 3417.51 = 2873.1$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: the premium rate comes from the loan before the premium is added. In Example 1 the LTV is 94.17%, not $587600 \div 600000 = 97.9\%$. Using the larger number would put you above the 95% limit and mislead you.

</div>

<div class="warning" markdown>

Watch out: the minimum down payment is not 5% of the whole price above \$500,000. For \$600,000 the minimum is \$35,000, not \$30,000. The 5% applies to the first \$500,000 and 10% to the rest.

</div>

<div class="warning" markdown>

Watch out: the amortization is not the term. A 5-year term with a 25-year amortization does not mean the mortgage is paid off in 5 years. After the term you renew, and the balance is still large (about \$495,642 on the \$560,000 mortgage from the last lesson).

</div>

<div class="warning" markdown>

Watch out: the ratios use the qualifying-rate payment. Testing GDS with the real \$3,256.99 payment in Example 2 gives $(3256.99 + 466.67 + 150) \div 12500 = 31.0\%$, instead of the lender's 36.3%.

</div>

The insurance premium protects the lender, not you. The borrower's benefit is access to a mortgage with less than 20% down.

The minimum down payment jumps at \$1.5 million, so a buyer just below the cap may do better to compare the insured mortgage with a smaller home.

## Tricks and shortcuts

Over \$500,000, the minimum down payment is $25000 + 0.10 \times (\text{price} - 500000)$. Equivalently, it is 10% of the price minus \$25,000: \$600,000 gives \$60,000 minus \$25,000, which is \$35,000. Try \$800,000: $80000 - 25000 = 55000$.

To estimate the effect of a rate change on a 25-year payment, remember that around these rates each percentage point adds about 10% to the payment: \$3,199.03 at 6% against \$2,908.02 at 5% is a ratio of $3199.03 \div 2908.02 = 1.10$.

## In code

This code computes the down payment, premium, payment and the largest loan under the two limits.

<details class="code" markdown>
<summary>In code</summary>

```python
def monthly_rate(quoted):
    return (1 + quoted / 2) ** (1 / 6) - 1

def payment(loan, quoted, years):
    i, n = monthly_rate(quoted), 12 * years
    return loan * i / (1 - (1 + i) ** -n)

def min_down(price):
    if price >= 1_500_000:
        return 0.20 * price
    return 0.05 * price if price <= 500_000 else 25_000 + 0.10 * (price - 500_000)

def premium_rate(ltv):
    for top, rate in [(0.65, 0.006), (0.75, 0.017), (0.80, 0.024),
                      (0.85, 0.028), (0.90, 0.031), (0.95, 0.040)]:
        if ltv <= top:
            return rate
    raise ValueError("LTV above 95%")

def insured_loan(price, down):
    loan = price - down
    ltv = loan / price
    return loan * (1 + premium_rate(ltv)) if ltv > 0.80 else loan

def qualifying_rate(contract):
    return max(contract + 0.02, 0.0525)

def max_loan(income, tax, heat, debts, contract, years=25):
    m = income / 12
    room = min(0.39 * m - tax / 12 - heat, 0.44 * m - debts - tax / 12 - heat)
    i, n = monthly_rate(qualifying_rate(contract)), 12 * years
    return room * (1 - (1 + i) ** -n) / i

print(min_down(650_000), min_down(1_400_000))               # 40000.0 115000.0
print(insured_loan(600_000, min_down(600_000)))             # 587600.0
print(round(payment(587_600, 0.05, 25), 2))                 # 3417.51
print(round(payment(494_000, 0.05, 25), 2))                 # 2873.13
print(qualifying_rate(0.0425), qualifying_rate(0.029))      # 0.0625 0.0525
print(round(max_loan(120_000, 5_600, 150, 800, 0.05)))      # 425937
print(round(max_loan(120_000, 5_600, 150, 0, 0.05)))        # 468769
```

Each rule is a few lines, and the edge of each rule shows up as a comparison.

</details>

## FAQ

### Why does the premium depend on the loan-to-value and not on my income?

The insurer is protecting the lender from a loss if the home sells for less than the loan. The smaller your down payment, the smaller the cushion, so the premium rises as the LTV rises. Income is checked separately, through the stress test and the ratios.

### Why can a longer amortization cost so much more?

Interest is charged on the balance, and a slower payoff leaves a high balance for longer. In Example 1 the 30-year loan saves \$275.51 a month but adds \$104,736 of interest over its life. The payment drops by about 8%, but the number of payments rises by 20%.

### What if my GDS is 40%?

The FCAC says the 39% is a guideline and that you may still qualify with a slightly higher ratio. The CMHC Home Start requirements, which the lesson cites, state 39% and 44% as maximums. Lenders and insurers apply their own rules, so ask a lender about your case.

### Why is the stress test rate the same for every lender?

For banks and other federally regulated lenders the rule comes from the regulator, OSFI. Other lenders may use different rules, and the FCAC says some of them also require a stress test.

## Practice

### Warm-up

1\. Find the minimum down payment for a \$450,000 home and for a \$950,000 home.

<details class="solution" markdown>
<summary>Solution</summary>

For \$450,000 the price is at most \$500,000, so the minimum is $0.05 \times 450000 = 22500$, so \$22,500.

For \$950,000 it is $25000 + 0.10 \times 450000 = 25000 + 45000 = 70000$, so \$70,000.

Check: $70000 \div 950000 \approx 7.4\%$, between 5% and 10%.

</details>

2\. Can a buyer get an insured mortgage on a \$1,500,000 home? What is the smallest down payment?

<details class="solution" markdown>
<summary>Solution</summary>

No. Insured mortgages need a price below \$1,500,000. At \$1,500,000 the minimum down payment is 20%: $0.20 \times 1500000 = 300000$, so \$300,000, which leaves an LTV of 80%, so no insurance is needed.

Check: $1200000 \div 1500000 = 0.8$, which is the 80% limit.

</details>

3\. Find the qualifying rate for contract rates of 3.49% and 2.99%.

<details class="solution" markdown>
<summary>Solution</summary>

For 3.49%: $3.49 + 2 = 5.49\%$, which is above 5.25%, so the qualifying rate is 5.49%.

For 2.99%: $2.99 + 2 = 4.99\%$, which is below 5.25%, so the qualifying rate is 5.25%.

Check: in both cases the answer is the larger of the two numbers.

</details>

### Standard

4\. A buyer buys an \$800,000 home with a \$120,000 down payment. Find the LTV, the premium and the total loan.

<details class="solution" markdown>
<summary>Solution</summary>

The loan is $800000 - 120000 = 680000$, and the LTV is $680000 \div 800000 = 0.85$, or 85%. The loan is over 80%, so it must be insured. An LTV of exactly 85% is in the "over 80% to 85%" row, which is 2.80%.

The premium is $0.028 \times 680000 = 19040$, so the total loan is $680000 + 19040 = 699040$, that is, \$699,040.

Check: an extra dollar of down payment would not change the row, but a dollar less would put the LTV above 85% and into the 3.10% row.

</details>

5\. A household earns \$96,000 a year. Its qualifying mortgage payment is \$2,500 a month, property tax is \$400 a month and heating is \$120 a month. It also pays \$400 a month on a car loan and \$150 a month on a credit card. Find the GDS and TDS, and say whether each is within 39% and 44%.

<details class="solution" markdown>
<summary>Solution</summary>

Monthly income is $96000 \div 12 = 8000$. Housing costs are $2500 + 400 + 120 = 3020$, so GDS $= 3020 \div 8000 = 0.3775$, or 37.75%, within 39%.

Total debts are $3020 + 400 + 150 = 3570$, so TDS $= 3570 \div 8000 = 0.44625$, or 44.6%, which is above 44%.

The household passes the GDS but not the TDS.

Check: 44% of \$8,000 is \$3,520, and \$3,570 is \$50 over.

</details>

6\. A buyer borrows \$400,000 over 25 years. Compare the monthly payment at a made-up quoted rate of 5% with a rate of 6%.

<details class="solution" markdown>
<summary>Solution</summary>

The payment at 5% is \$2,326.42 and at 6% it is \$2,559.23, using the loan formula with the Canadian monthly rate. The difference is $2559.23 - 2326.42 = 232.81$, so \$232.81 a month more.

Check: the \$500,000 loan in the table has a payment difference of $3199.03 - 2908.02 = 291.01$, and $0.8 \times 291.01 = 232.81$, matching the answer. The loan is 0.8 times as big and the payment is proportional to the loan.

</details>

### Challenge

7\. Compare a 25-year and a 30-year amortization for the loan in Example 1 (premiums 4.00% and 4.20%, quoted rate 5%): the monthly payments, the total paid over the life of each, and the total interest.

<details class="solution" markdown>
<summary>Solution</summary>

For 25 years the total loan is \$587,600 and the payment is \$3,417.51. Over 300 payments the total paid is $3417.5109 \times 300 = 1025253.27$, so the interest is $1025253.27 - 587600 = 437653.27$.

For 30 years the premium is $0.042 \times 565000 = 23730$, the total loan is \$588,730, and the payment is \$3,142.00. Over 360 payments the total paid is $3141.9971 \times 360 = 1131118.97$, and the interest is $1131118.97 - 588730 = 542388.97$.

The monthly payment falls by \$275.51 and the total interest rises by $542388.97 - 437653.27 = 104735.70$, about \$104,736.

Check: the 30-year payments add up to $1131118.97 - 1025253.27 = 105865.70$ more than the 25-year ones, and the loan is \$1,130 larger; $105865.70 - 1130 = 104735.70$.

</details>

8\. (Reviews [renting vs buying a home](01-renting-vs-buying-a-home.md).) A first-time buyer buys a \$600,000 home with the minimum down payment. Closing costs are the land transfer tax after the \$4,000 refund, plus \$2,000 of legal fees (made up). How much cash is needed on closing day, not counting the sales tax on the premium?

<details class="solution" markdown>
<summary>Solution</summary>

The down payment is \$35,000. The land transfer tax is $275 + 1950 + 2250 + 0.02 \times 200000 = 275 + 1950 + 2250 + 4000 = 8475$. After the refund of \$4,000 it is \$4,475.

The cash needed is $35000 + 4475 + 2000 = 41475$, so \$41,475.

Check: it is about 6.9% of the price, which makes sense next to the 5.8% minimum down payment plus fees of a bit over 1%.

</details>

## Where this shows up

- The next lesson, [mortgage amortization schedules](03-mortgage-amortization-schedules.md), builds the full schedule for the \$560,000 mortgage and follows it through a renewal.
- In the chapter on borrowing, the same payment formula appears for [car loans and total cost](../04-borrowing/02-car-loans-and-total-cost.md).
- In economics, the stress test is a small example of a safety margin against a risk the borrower cannot control: a rise in rates.
