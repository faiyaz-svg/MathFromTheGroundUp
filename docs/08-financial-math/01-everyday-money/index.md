# Everyday money

Percent and rate arithmetic for the till, the grocery shelf and the paycheque, with Ontario's 2026 rules.

1. [Tips, discounts and HST](01-tips-discounts-and-hst.md)
2. [Unit price and comparison shopping](02-unit-price-and-comparison-shopping.md)
3. [Paycheques and budgeting](03-paycheques-and-budgeting.md)

## Cheat sheet

### Tips, discounts and HST

Turn every step into a multiplier and multiply. Ontario's HST is 13%, made of 5% federal and 8% provincial, and it is charged on the pre-tax price.

| Task | Method | Example |
|---|---|---|
| add HST | multiply by 1.13 | \$24.99 becomes \$28.24 |
| remove HST | divide by 1.13 | \$67.80 becomes \$60.00 |
| percent discount $d$ | multiply by $1 - d$ | 20% off is $\times 0.80$ |
| two discounts $a$, $b$ | single discount $a + b - ab$ | 20% then 10% is 28% off |
| discounts, then tax | multiply all the multipliers | $80 \times 0.80 \times 0.90 \times 1.13 = 65.09$ |
| dollar coupon | subtract before tax, then multiply by 1.13 | $(200 \times 0.85 - 20) \times 1.13 = 169.50$ |
| tip on the total | tip rate times 1.13, as a rate of the pre-tax bill | 18% on the total is 20.34% of the pre-tax bill |

- Percent discounts and tax can go in any order. A dollar coupon cannot: taken off before tax it also saves 13% of its value.
- In your head: 10% is one place left, 13% is $10\% + 3 \times 1\%$, a 15% tip is 10% plus half of it, and removing HST is multiplying by 0.885.
- Round once, at the end. Rounding tax item by item can differ from rounding the subtotal's tax by a cent.

Main mistakes:

- Adding discounts: 20% then 10% is 28%, not 30%.
- Removing tax by taking 13% off the total. Divide by 1.13.
- Tipping on the total and thinking it is a tip on the food.
- Rounding in the middle of the calculation.

### Unit price and comparison shopping

Unit price is price divided by quantity, in one common unit. The lower unit price is the cheaper product.

| Task | Method | Example |
|---|---|---|
| unit price | price divided by quantity, same unit | \$4.49 for 500 g is \$0.898 per 100 g |
| convert first | 1 kg = 1000 g, 1 L = 1000 mL, 1 lb = 0.45359237 kg | \$3.49/lb is \$7.69/kg |
| buy $n$ get $m$ free | discount $\frac{m}{n+m}$ | buy 2 get 1 free is 33.3% off |
| buy 1 get 1 half off | 25% off each | two \$6 shirts cost \$9 |
| shrinkflation | unit price factor is price factor divided by quantity factor | 450 g to 400 g, same price: $\times 1.125$ |
| bulk vs waste | big pack wins only if you use more than $\frac{U_{\text{big}}}{U_{\text{small}}}$ of it | 1 kg at \$4.99 vs 400 g at \$2.49: use over 80% |
| membership break-even | fee divided by saving rate | \$65 at 9% needs \$722.22 a year |

- In a spreadsheet the price per 100 g is `=B2/(C2/100)`, copied down the column.
- A "2 for" deal is a discount only if the pair costs less than twice the single price.
- A lower unit price saves money only on what you use and only on what you would have bought anyway.

Main mistakes:

- Comparing \$1.29 per 100 g with \$12.20 per kg without converting.
- Dividing quantity by price and then picking the smaller number.
- Counting a deal on something you don't need as a saving.
- Counting the club discount on goods you would not have bought without the club.

### Paycheques and budgeting

Net pay is gross pay minus deductions. A full-time year is $40 \times 52 = 2080$ hours.

| Pay period | Paycheques a year | \$62,400 gross per paycheque |
|---|---|---|
| weekly | 52 | \$1,200.00 |
| biweekly | 26 | \$2,400.00 |
| semi-monthly | 24 | \$2,600.00 |
| monthly | 12 | \$5,200.00 |

2026 payroll figures (CRA): CPP 5.95%, basic exemption \$3,500, YMPE \$74,600, maximum \$4,230.45. CPP2 4% between \$74,600 and \$85,000, maximum \$416. EI 1.63% up to \$68,900, maximum \$1,123.07. Ontario minimum wage \$17.95 (October 1, 2026 to September 30, 2027).

$$
\text{CPP} = 0.0595 \times \left(g - \frac{3500}{n}\right), \qquad \text{EI} = 0.0163 \times g, \qquad \text{net} = g - \text{CPP} - \text{EI} - \text{income tax}.
$$

- Biweekly example (\$62,400): CPP \$134.79, EI \$39.12, estimated income tax \$366.49, net \$1,859.60, which is about \$4,029.13 a month.
- CPP and EI stop at their yearly maximums, so a high earner's take-home rises late in the year.
- Income tax withholding is an estimate. The full method is in the tax brackets lesson.
- 50/30/20: 50% needs, 30% wants, 20% saving and extra debt payments. It is a starting draft, not a rule.
- Emergency fund in months is savings divided by monthly essentials. Three to six months is a common rule of thumb.

Main mistakes:

- Budgeting from gross pay.
- Treating biweekly as 24 paycheques a year. It is 26.
- Charging CPP on the first \$3,500 a year.
- Following 50/30/20 when rent alone is over half of net pay, without adjusting the split.
