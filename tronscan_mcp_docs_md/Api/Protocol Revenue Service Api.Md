

# Protocol Revenue Service API

## Get TRON total protocol revenue

Returns a full breakdown of TRON protocol revenue — burn income, staking income, energy/bandwidth splits, closing TRX price, and period-over-period comparison rates — at configurable time granularity.

```
GET https://apilist.tronscanapi.com/api/turnover/new?size=1000&start=1575129600000&end=1725846158880&timeType=0
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/turnover/new?size=1000&start=1575129600000&end=1725846158880&timeType=0) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `size` | Number of items per page. Default and max: `2000` |
| `start` | Start time, accurate to milliseconds |
| `end` | End time, accurate to milliseconds |
| `timeType` | Query granularity. `0`: Day · `1`: Month · `2`: Quarter · `3`: Year |
| `format` | Download format. Set to `csv` to download the statistic data as a CSV file |

### Response

```
{
    "total": 1,
    "data": [
        {
            "day": "2024-09-08",
            "trxClosePrice": "0.1531909239",
            "totalIncome": 5619413.042217823529562,
            "burnIncome": 1124467.409354824102680,
            "burnIncomePercent": "0.2001",
            "stakeIncome": 4494945.632862999426882,
            "stakeIncomePercent": "0.7999",
            "energyIncome": 5339887.246792556266662,
            "netIncome": 279525.7954252672629,
            "energyBurnIncome": 1054296.594447472672380,
            "energyBurnIncomePercent": "0.9376",
            "energyBurnIncomePercentInTotal": "0.1876",
            "energyStakeIncome": 4285590.652345083594282,
            "energyStakeIncomePercent": "0.9534",
            "energyStakeIncomePercentInTotal": "0.7626",
            "netBurnIncome": 70170.8149073514303,
            "netBurnIncomePercent": "0.0624",
            "netBurnIncomePercentInTotal": "0.0125",
            "netStakeIncome": 209354.9805179158326,
            "netStakeIncomePercent": "0.0466",
            "netStakeIncomePercentInTotal": "0.0373"
        }
    ],
    "totalIncomeYester": 5619413.042217823529562,
    "totalIncomeYesterRate": -0.049,
    "totalIncomeMonth": "229708957.488249488240826",
    "totalIncomeMonthRate": 0.5024,
    "totalIncome3Month": "524743928.187377907224572",
    "totalIncome3MonthRate": 0.3363,
    "totalIncomeYear": "1575565290.6602948302878386299322",
    "totalIncomeYearRate": 1.1513
}
```

**`data[]` field reference**

| Field | Description |
| --- | --- |
| `day` | Statistic day |
| `trxClosePrice` | TRX closing price for the day |
| `totalIncome` | Total income |
| `burnIncome` | Total burn income |
| `burnIncomePercent` | Proportion of total burn income to total income |
| `stakeIncome` | Total stake income |
| `stakeIncomePercent` | Proportion of total staking income to total income |
| `energyIncome` | Total energy income |
| `netIncome` | Total bandwidth income |
| `energyBurnIncome` | Energy burn income |
| `energyBurnIncomePercent` | Proportion of energy burn income to total burn income |
| `energyBurnIncomePercentInTotal` | Proportion of energy burn income to total income |
| `energyStakeIncome` | Energy stake income |
| `energyStakeIncomePercent` | Proportion of energy staking income to total staking income |
| `energyStakeIncomePercentInTotal` | Proportion of energy staking income to total income |
| `netBurnIncome` | Bandwidth burn income |
| `netBurnIncomePercent` | Proportion of bandwidth burn income to total burn income |
| `netBurnIncomePercentInTotal` | Proportion of bandwidth burn income to total income |
| `netStakeIncome` | Bandwidth staking income |
| `netStakeIncomePercent` | Proportion of bandwidth staking income to total staking income |
| `netStakeIncomePercentInTotal` | Proportion of bandwidth staking income to total income |

**Top-level summary fields**

| Field | Description |
| --- | --- |
| `totalIncomeYester` | Last day total income |
| `totalIncomeYesterRate` | Day-over-day total income change rate |
| `totalIncomeMonth` | Last month total income |
| `totalIncomeMonthRate` | Month-over-month total income change rate |
| `totalIncome3Month` | Last quarter total income |
| `totalIncome3MonthRate` | Quarter-over-quarter total income change rate |
| `totalIncomeYear` | Last year total income |
| `totalIncomeYearRate` | Year-over-year total income change rate |

---

## Retrieve burn income / staking income on TRON

Returns detailed burn **or** staking income statistics — energy/bandwidth splits, period aggregates (day / month / quarter / year), income proportions, and period-over-period change ratios — for the selected income type.

```
GET https://apilist.tronscanapi.com/api/consumption/statistic?size=1000&start=1575129600000&end=1725847289598&timeType=0&type=burn
```

> Try this endpoint in your [**browser**](https://apilist.tronscanapi.com/api/consumption/statistic?size=1000&start=1575129600000&end=1725847289598&timeType=0&type=burn) ↗ 🔗

RequestResponse

### Request

| Parameter | Description |
| --- | --- |
| `size` | Number of items per page. Default and max: `2000` |
| `start` | Start time, accurate to milliseconds |
| `end` | End time, accurate to milliseconds |
| `timeType` | Query granularity. `0`: Day · `1`: Month · `2`: Quarter · `3`: Year |
| `format` | Download format. Set to `csv` to download the statistic data as a CSV file |
| `type` | Income type to retrieve. `burn`: Burn income · `stake`: Staking income |

### Response

```
{
    "total": 1,
    "data": [
        {
            "day": "2024-09-08",
            "trxPriceInUsd": 0.1531909239,
            "totalIncome": 5619413.042218,
            "burnIncome": 1124467.409354,
            "stakeIncome": 4494945.632863,
            "energyIncome": 5339887.246793,
            "netIncome": 279525.795425,
            "energyBurnIncome": 1054296.594447,
            "energyStakeIncome": 4285590.652345,
            "netBurnIncome": 70170.814907,
            "netStakeIncome": 209354.980518
        }
    ],
    "totalIncomeYester": 1124467.409354,
    "totalIncomeMonth": 60428021.151735,
    "totalIncome3Month": 135831107.601129,
    "totalIncomeYear": 492478932.604666,
    "totalNetIncomeYester": 70170.814907,
    "totalNetIncomeMonth": 2750197.858982,
    "totalNetIncome3Month": 6343358.549405,
    "totalNetIncomeYear": 19628143.501117,
    "totalEnergyIncomeYester": 1054296.594447,
    "totalEnergyIncomeMonth": 57677823.292753,
    "totalEnergyIncome3Month": 129487749.051724,
    "totalEnergyIncomeYear": 472850789.103549,
    "totalNetIncomeYesterRate": 0.062404,
    "totalNetIncomeMonthRate": 0.045512,
    "totalNetIncome3MonthRate": 0.0467,
    "totalNetIncomeYearRate": 0.039856,
    "totalEnergyIncomeYesterRate": 0.937596,
    "totalEnergyIncomeMonthRate": 0.954488,
    "totalEnergyIncome3MonthRate": 0.9533,
    "totalEnergyIncomeYearRate": 0.960144,
    "totalIncomeYesterRatio": -0.164912,
    "totalIncomeMonthRatio": 0.682368,
    "totalIncome3MonthRatio": 0.164025,
    "totalIncomeYearRatio": 0.427393,
    "totalNetIncomeYesterRatio": -0.046008,
    "totalNetIncomeMonthRatio": 0.540702,
    "totalNetIncome3MonthRatio": 0.435015,
    "totalNetIncomeYearRatio": 0.422052,
    "totalEnergyIncomeYesterRatio": -0.171783,
    "totalEnergyIncomeMonthRatio": 0.689776,
    "totalEnergyIncome3MonthRatio": 0.153355,
    "totalEnergyIncomeYearRatio": 0.427615
}
```

**`data[]` field reference**

| Field | Description |
| --- | --- |
| `day` | Statistic day |
| `trxPriceInUsd` | TRX price in USD on the statistic day |
| `totalIncome` | Total income |
| `burnIncome` | Total burn income |
| `stakeIncome` | Total stake income |
| `energyIncome` | Total energy income |
| `netIncome` | Total bandwidth income |
| `energyBurnIncome` | Energy burn income |
| `energyStakeIncome` | Energy stake income |
| `netBurnIncome` | Bandwidth burn income |
| `netStakeIncome` | Bandwidth stake income |

**Period aggregate fields** — all values are for the selected income `type` (burn or stake)

| Field | Description |
| --- | --- |
| `totalIncomeYester` | Yesterday total income |
| `totalIncomeMonth` | Last month total income |
| `totalIncome3Month` | Last quarter total income |
| `totalIncomeYear` | Last year total income |
| `totalNetIncomeYester` | Yesterday bandwidth income |
| `totalNetIncomeMonth` | Last month bandwidth income |
| `totalNetIncome3Month` | Last quarter bandwidth income |
| `totalNetIncomeYear` | Last year bandwidth income |
| `totalEnergyIncomeYester` | Yesterday energy income |
| `totalEnergyIncomeMonth` | Last month energy income |
| `totalEnergyIncome3Month` | Last quarter energy income |
| `totalEnergyIncomeYear` | Last year energy income |

**Income proportion fields** — ratio of bandwidth or energy income within the period total

| Field | Description |
| --- | --- |
| `totalNetIncomeYesterRate` | Bandwidth income proportion for the previous day |
| `totalNetIncomeMonthRate` | Bandwidth income proportion for the month |
| `totalNetIncome3MonthRate` | Bandwidth income proportion for the quarter |
| `totalNetIncomeYearRate` | Bandwidth income proportion for the year |
| `totalEnergyIncomeYesterRate` | Energy income proportion for the previous day |
| `totalEnergyIncomeMonthRate` | Energy income proportion for the month |
| `totalEnergyIncome3MonthRate` | Energy income proportion for the quarter |
| `totalEnergyIncomeYearRate` | Energy income proportion for the year |

**Period-over-period change ratio fields** — positive values indicate growth; negative values indicate decline

| Field | Description |
| --- | --- |
| `totalIncomeYesterRatio` | Day-over-day total income change |
| `totalIncomeMonthRatio` | Month-over-month total income change |
| `totalIncome3MonthRatio` | Quarter-over-quarter total income change |
| `totalIncomeYearRatio` | Year-over-year total income change |
| `totalNetIncomeYesterRatio` | Day-over-day bandwidth income change |
| `totalNetIncomeMonthRatio` | Month-over-month bandwidth income change |
| `totalNetIncome3MonthRatio` | Quarter-over-quarter bandwidth income change |
| `totalNetIncomeYearRatio` | Year-over-year bandwidth income change |
| `totalEnergyIncomeYesterRatio` | Day-over-day energy income change |
| `totalEnergyIncomeMonthRatio` | Month-over-month energy income change |
| `totalEnergyIncome3MonthRatio` | Quarter-over-quarter energy income change |
| `totalEnergyIncomeYearRatio` | Year-over-year energy income change |