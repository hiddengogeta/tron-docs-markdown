

# Staked TRX[¶](#staked-trx "Permanent link")

Based on Stake 2.0, with TRX Liquid Staking, users can stake TRX to get sTRX tokens and gain high rewards. Compared to traditional staking, TRX Liquid Staking is easier to use and more profitable. Staked TRX will be used automatically for voting and governance, and gain rewards via Energy Rental.
The contract [StakedTRX](https://tronscan.org/#/token20/TU3kjFuhtEo42tsCBtfYUAZxoqQ4yuSLQ5) used to set up the staked TRX service.

## **Query Interface**[¶](#query-interface "Permanent link")

### **Exchange Rate**[¶](#exchange-rate "Permanent link")

Query the exchange rate between sTRX and TRX.

```
function exchangeRate() public view returns (uint256)
```

* **Parameter description:** N/A.
* **Returns:** exchange rate, 1 sTRX / 1 TRX exchange rate, scaled by 1e18.

### **Total TRX Assets**[¶](#total-trx-assets "Permanent link")

Query the total TRX assets managed by contract.

```
function totalUnderlying() public view returns (uint256)
```

* **Parameter description:** N/A.
* **Returns:** the total assets of TRX managed by contract, the minimum unit.

### **User Balance in TRX**[¶](#user-balance-in-trx "Permanent link")

Query the amount of TRX corresponding to the sTRX held by user.

```
function balanceInTrx(address _account) public view returns (uint256)
```

* **Parameter description:**
  + `_account:` the user address.
* **Returns:** the amount of TRX corresponding to the sTRX held by user, the minimum unit.

### **Current Unfreezing Round**[¶](#current-unfreezing-round "Permanent link")

Query the current unfreezing round of the contract. The initial value is 1.

```
function round() view external returns (uint256)
```

* **Parameter description:** N/A.
* **Returns:** current unfreezing round.

### **Claimable Amount in TRX**[¶](#claimable-amount-in-trx "Permanent link")

The amount of TRX that can be withdrawn after the unfreezing period has expired.

```
function claimable() external returns (uint256)
```

* **Parameter description:** N/A.
* **Returns:** the amount of TRX that can be claimed.

### **Withdrawal Amount in TRX**[¶](#withdrawal-amount-in-trx "Permanent link")

The amount of TRX being withdrawn. This value is increased when the user withdraws.

```
function withdrawal() external returns (uint256)
```

* **Parameter description:** N/A.
* **Returns:** the amount of TRX being withdrawn.

### **Unfreeze Balance in TRX**[¶](#unfreeze-balance-in-trx "Permanent link")

The total amount to be unfrozen. If the user withdraws but has not completed the round, it will enter the unfreezing queue.

```
function balanceToUnfreeze() external returns (uint256)
```

* **Parameter description:** N/A.
* **Returns:** the amount of TRX to be unfrozen, minimum unit.

### **Freeze Balance in TRX**[¶](#freeze-balance-in-trx "Permanent link")

The amount to be frozen. As long as the value is greater than 1 TRX, the freezing operation will be performed.

```
function balanceToFreeze() external returns (uint256)
```

* **Parameter description:** N/A.
* **Returns:** the amount of TRX to be frozen, minimum unit.

## **Write Interface**[¶](#write-interface "Permanent link")

### **Deposit TRX**[¶](#deposit-trx "Permanent link")

Deposit TRX assets and receive sTRX.

```
function deposit() external payable returns (uint256)
```

* **Parameter description:**
  + `msg.value:` the amount of TRX to deposit.
* **Returns:** the amount of sTRX received by user through exchange, the minimum unit.

#### **Event**[¶](#event "Permanent link")

```
Deposit(address user, uint256 trxAmount, uint256 strx, uint256 userHoldStrx)
```

* Emits when user successfully deposits TRX.
  + `trxAmount:` the amount of TRX user deposits;
  + `strx:` the amount of sTRX user gets;
  + `userHoldStrx:` the total amount of sTRX held by user after the deposit.

### **Withdraw sTRX**[¶](#withdraw-strx "Permanent link")

Specify the amount of sTRX to withdraw, the minimum unit.

```
function withdraw(uint256 tokenAmount) external returns (uint256)
```

* **Parameter description:**
  + `tokenAmount:` the amount of sTRX to withdraw.
* **Returns:** the amount of TRX to be unfrozen when user withdraws, the minimum unit.

#### **Event**[¶](#event_1 "Permanent link")

```
Withdraw(address user, uint256 strx, uint256 trxAmount, uint256 userHoldStrx)
```

* Emits when user successfully withdraws sTRX.
  + `strx:` the amount of sTRX user withdraws;
  + `trxAmount:` the amount of TRX user gets;
  + `userHoldStrx:` the total amount of sTRX held by user after the withdrawal.

### **Withdraw sTRX (with the amount of TRX specified)**[¶](#withdraw-strx-with-the-amount-of-trx-specified "Permanent link")

Specify the amount of TRX user hopes to obtain through withdrawal, the minimum unit.

```
function withdrawExact(uint256 trxAmount) external returns (uint256)
```

* **Parameter description:**
  + `trxAmount:` the specific amount of TRX.
* **Returns:** the amount of sTRX withdrawn by user, the minimum unit.

### **Claim TRX**[¶](#claim-trx "Permanent link")

Claim the ready-to-be-withdrawn TRX unfrozen in the earliest round.

```
function claim() external returns (uint256)
```

* **Parameter description:** N/A.
* **Returns:** the amount of TRX claimed by user in the earliest unfreezing round, the minimum unit.

#### **Event**[¶](#event_2 "Permanent link")

```
Claim(address user, uint256 trxAmount)
```

* Emits when user successfully claims TRX.
  + `trxAmount:` the amount of TRX user claims.

### **Claim all unfrozen TRX**[¶](#claim-all-unfrozen-trx "Permanent link")

Claim all ready-to-be-withdrawn, unfrozen TRX

```
function claimAll() external returns (uint256)
```

* **Parameter description:** N/A.
* **Returns:** the amount of TRX claimed by the user for all expired unfreezing rounds, the minimum unit.

---