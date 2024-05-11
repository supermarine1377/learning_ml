## Data description

欠損値の個数

```
id              0
age             0
job             0
marital         0
education       0
default         0
amount          0
housing         0
loan            0
contact         0
day             0
month           0
duration     7044
campaign        0
previous        0
y               0
dtype: int64
```

### 特徴量の候補

#### id (int)

顧客ID

#### age (int)

年齢

```
     count       mean        std   min   25%   50%   75%   max
y
0  18445.0  40.267877  10.454893  18.0  32.0  38.0  48.0  95.0
1   8683.0  42.402165  10.785727  18.0  34.0  41.0  50.0  93.0
```

特徴量として扱わない

#### job

職種

- 'blue-collar'
- 'entrepreneur'
- 'management'
- 'retired'
- 'services'
- 'technician' 
- 'admin.' 
- 'self-employed' 
- 'housemaid' 
- 'unemployed' 
- 'unknown'
- 'student'

jobごとのyの平均

```
job
admin.           0.306969
blue-collar      0.355080
entrepreneur     0.379650
housemaid        0.282353
management       0.306050
retired          0.366643
self-employed    0.302646
services         0.331205
student          0.159785
technician       0.311067
unemployed       0.251899
unknown          0.292135
Name: y, dtype: float64
```

jobごとのyの平均のdescription

```
count    12.000000
mean      0.303790
std       0.058140
min       0.159785
25%       0.289689
50%       0.306510
75%       0.337174
max       0.379650
Name: y, dtype: float64
```

studentは\mu+2\sigmaの範囲外だが\mu+3\sigmaの範囲内

特徴量とする

#### education

最終学歴

- 'secondary' 
- 'primary' 
- 'tertiary' 
- 'unknown'

educationごとのyの平均のdescription

```
education
primary      0.351566
secondary    0.319623
tertiary     0.299661
unknown      0.353562
```

```
Name: y, dtype: float64
count    4.000000
mean     0.331103
std      0.026100
min      0.299661
25%      0.314632
50%      0.335594
75%      0.352065
max      0.353562
Name: y, dtype: float64
```

どれも\mu+2\sigmaの範囲内に収まるので特徴量としない

#### marital

既婚/未婚/離別など

- 'married'
- 'single'
- 'divorced'

martialでgroup_byしたデータの統計量

```
marital
divorced    0.334534
married     0.341478
single      0.268468
Name: y, dtype: float64
count    3.000000
mean     0.314827
std      0.040298
min      0.268468
25%      0.301501
50%      0.334534
75%      0.338006
max      0.341478
Name: y, dtype: float64
```

single が明らかに特徴的なので特徴量とする

#### loan

個人ローンの有無

- no
- yes

```
loan
no     0.301167
yes    0.419355
Name: y, dtype: float64
count    2.000000
mean     0.360261
std      0.083571
min      0.301167
25%      0.330714
50%      0.360261
75%      0.389808
max      0.419355
Name: y, dtype: float64
```

特徴量にした方がよさそう

#### housing

住宅ローンの有無

- no
- yes
　
```
housing
no     0.217196
yes    0.401719
Name: y, dtype: float64
count    2.000000
mean     0.309457
std      0.130478
min      0.217196
25%      0.263327
50%      0.309457
75%      0.355588
max      0.401719
Name: y, dtype: float64
```

特徴量にした方がよさそう

#### amount(int)

年間キャンペーン終了時点での、総投資信託購入額

```
     count         mean          std     min   25%    50%     75%       max
y
0  18445.0  1365.713364  3090.119923 -6847.0  75.0  449.0  1396.0  102127.0
1   8683.0  1303.063918  2771.807666 -3313.0  76.0  449.0  1426.0   57435.0
```

あまりyに差がないように見えるし、負のamountがあったりと謎なので特徴量としない

#### default

債務不履行の有無

- no
- yes

```
          count      mean       std  min  25%  50%  75%  max
default
no       26644.0  0.321386  0.467017  0.0  0.0  0.0  1.0  1.0
yes        484.0  0.247934  0.432260  0.0  0.0  0.0  0.0  1.0
```

特徴量とする

#### previous(int)

キャンペーン前に接触した回数

```
     count      mean       std  min  25%  50%  75%    max
y
0  18445.0  0.540634  2.621198  0.0  0.0  0.0  0.0  275.0
1   8683.0  0.662789  2.231392  0.0  0.0  0.0  0.0   55.0
```

特徴量とする

#### campaign(int)

現キャンペーン内での接触回数

```
     count      mean       std  min  25%  50%  75%   max
y
0  18445.0  2.438655  2.851526  1.0  1.0  2.0  2.0  63.0
1   8683.0  3.416907  3.552366  1.0  1.0  3.0  4.0  44.0
```

特徴量とする

#### day(int)

最終接触日

特徴量としない

#### month

最終接触月

- 'apr' 
- 'feb'
- 'jan' 
- 'jun' 
- 'sep' 
- 'may' 
- 'aug'
- 'mar' 
- 'jul' 
- 'nov' 
- 'oct'
- 'dec'

特徴量としない

#### duration

接触時の平均時間（秒）

欠損値があるので穴埋めする

```
y    mean
0    301.424731
1    348.601032
```

特徴量とする

#### contact

連絡方法

- 'cellular'
- 'sending _document'
- 'telephone'

```
                     count      mean       std  min  25%  50%  75%  max
contact
cellular           17580.0  0.276906  0.447482  0.0  0.0  0.0  1.0  1.0
sending _document   7861.0  0.417759  0.493221  0.0  0.0  0.0  1.0  1.0
telephone           1687.0  0.314760  0.464558  0.0  0.0  0.0  1.0  1.0
```

sending _document が一番yが高そうなので特徴量にする

### 目的変数

y

今回のキャンペーンの結果

- 1: 購入
- 2: 未購入

## 結果

```
training score: 0.8307252482696359
model validation score: 0.8334210988239424
model test score: 0.8201253225211943
```