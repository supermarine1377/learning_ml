## Data description

https://www.kaggle.com/datasets/jsphyg/tipping

Predict the tips amount for each diner using the column tip as the target.

There are no n/a values so we don't have to do filling.

### total_bill

bill in dollars

### tip

tip in dollars

### sex (str)

sex of the bill payer

### smoker (bool)

whether there were smokers in the party

### day (str)

day of the week

- Sun
- Sat
- Thur
- Fri

### time (str)

time of day

- Dinner
- Lunch

### size

size of the party

## Coefficient values

```
total_bill           0.675734
tip                  1.000000
size                 0.489299
is_billpayer_male    0.088862
has_smoker           0.005929
is_sat              -0.002790
is_sun               0.125114
is_thur             -0.095879
is_lunch            -0.121629
Name: tip, dtype: float64
```

## Dependent values selection

- total_bill
- size

```
Name: total_bill, dtype: float64
count    244.000000
mean      19.785943
std        8.902412
min        3.070000
25%       13.347500
50%       17.795000
75%       24.127500
max       50.810000

Name: size, dtype: float64
count    244.000000
mean       2.569672
std        0.951100
min        1.000000
25%        2.000000
50%        2.000000
75%        3.000000
max        6.000000
```

The total_bill has a linear relationship with the size
```
total_bill           1.000000
tip                  0.675734
size                 0.598315
is_billpayer_male    0.144877
has_smoker           0.085721
is_fri              -0.086168
is_sat               0.054919
is_sun               0.122953
is_thur             -0.138174
is_lunch            -0.183118
```