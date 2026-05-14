

# SBM[¶](#sbm "Permanent link")

The JustLend DAO Supply and Borrow Market (SBM) is a decentralized liquidity pool where users can participate as suppliers, borrowers or liquidators. Suppliers provide liquidity to a market and can earn interest on the assets provided, where borrowers are able to borrow in a collateralize assets way.

The SBM contract is the main user-facing contract. Most user interactions with the JustLend DAO Protocol occur via the Ctoken contract. It exposes the liquidity management methods that can be invoked using either Solidity or Web3 libraries.

`Ctoken.sol:` allows users to:

* Supply
* Borrow
* Withdraw
* Reapy
* Liquidation

The source code is available on [Github](https://github.com/justlend/justlend-protocol/blob/main/contracts/CToken.sol).

## **Query Interface**[¶](#query-interface "Permanent link")

### **ExchangeRate**[¶](#exchangerate "Permanent link")

Calling this method accrues interest and returns the up-to-date exchange rate.

```
function exchangeRateCurrent() public nonReentrant returns (uint)
```

* **Parameter description:** N/A
* **Returns:** calculated exchange rate scaled by 1e18.

### **Get Cash**[¶](#get-cash "Permanent link")

Calling this method gets the total amount of underlying balance currently available to this market.

```
function getCash() public view returns (uint)
```

* **Parameter description:** N/A
* **Returns:** The quantity of underlying assets owned by this contract.

### **Total Borrows**[¶](#total-borrows "Permanent link")

Calling this method gets the sum of the currently loaned-outs and the accrued interests.

```
function totalBorrowsCurrent() external nonReentrant returns (uint)
```

* **Parameter description:** N/A
* **Returns:** The total borrows with interest.

### **Borrow Balance**[¶](#borrow-balance "Permanent link")

Calling this method accrues interest to the updated borrowIndex and then calculates the account's borrow balance using the updated borrowIndex.

```
function borrowBalanceCurrent(address account) external nonReentrant returns (uint)
```

* **Parameter description:**
  + `account:` the address whose balance should be calculated after updating borrowIndex.
* **Returns:** The total borrows with interest.

### **Borrow Rate**[¶](#borrow-rate "Permanent link")

Calling this method gets the current per-block borrow interest rate for this jToken.

```
function borrowRatePerBlock() external view returns (uint)
```

* **Parameter description:** N/A
* **Returns:** The borrow interest rate per block, scaled by 1e18.

### **Total Supply**[¶](#total-supply "Permanent link")

Calling this method gets the total number of tokens in circulation.

```
function totalSupply() external view returns (uint256)
```

* **Parameter description:** N/A
* **Returns:** The supply of tokens.

### **Underlying Balance**[¶](#underlying-balance "Permanent link")

Calling this method gets the underlying balance of the owner.

```
function balanceOfUnderlying(address owner) external returns (uint)
```

* **Parameter description:**
  + `owner:` the address of the account.
* **Returns:** The amount of underlying owned by owner.

### **Supply Rate**[¶](#supply-rate "Permanent link")

Calling this method gets the current per-block supply interest rate for this jToken.

```
function supplyRatePerBlock() external view returns (uint)
```

* **Parameter description:** N/A
* **Returns:** The supply interest rate per block, scaled by 1e18.

### **Total Reserves**[¶](#total-reserves "Permanent link")

Calling this method gets the reserves. Reserve represents a portion of historical interest set aside as cash which can be withdrawn or transferred through the protocol's governance.

```
function totalReserves() returns (uint)
```

* **Parameter description:** N/A
* **Returns:** The total amount of reserves.

### **Reserve Factor**[¶](#reserve-factor "Permanent link")

Calling this method gets the current reserve factor.

```
function reserveFactorMantissa() returns (uint)
```

* **Parameter description:** N/A
* **Returns:** The current reserve factor.

## **Write Interface**[¶](#write-interface "Permanent link")

### **Borrow**[¶](#borrow "Permanent link")

Calling this method borrows assets from JustLend DAO protocol to the sender's owner address.

```
function borrow(uint borrowAmount) external returns (uint)
```

* **Parameter description:**
  + `borrowAmount:` the amount of the underlying asset to borrow.
* **Returns:** None, reverts on error.

#### **Event**[¶](#event "Permanent link")

```
Borrow(address borrower, uint borrowAmount, uint accountBorrows, uint totalBorrows, uint borrowIndex)
```

* Emits when user successfully borrow.
  + `borrower:` address of borrow assets account;
  + `borrowAmount:` the amount of borrowed assets;
  + `accountBorrows:` the account borrow the assets;
  + `totalBorrows:` total borrow assets form the account;
  + `borrowIndex:` the index of this borrow order.

### **repayBorrow**[¶](#repayborrow "Permanent link")

Calling this method repays their own borrow.

```
function repayBorrow(uint amount) external payable
```

* **Parameter description:**
  + `amount:` the amount of the asset to repay.
* **Returns:** None, reverts on error.

#### **Event**[¶](#event_1 "Permanent link")

```
RepayBorrow(address payer, address borrower, uint repayAmount, uint accountBorrows, uint totalBorrows, uint borrowIndex)
```

* Emits when user successfully repay borrow.
  + `payer:` operate repay borrow;
  + `borrower:` address of borrow assets account;
  + `repayAmount:` the amount of repaid assets;
  + `accountBorrows:` the account borrow the assets;
  + `totalBorrows:` total borrow assets form the account;
  + `borrowIndex:` the index of this borrow order.

### **repayBorrowBehalf**[¶](#repayborrowbehalf "Permanent link")

Calling this method repays their own borrow.

```
function repayBorrow(uint amount) external payable
```

* **Parameter description:**
  + `borrower:` the account with the debt being paid off.
  + `msg.value:` the amount to repay.
* **Returns:** None, reverts on error.

### **Mint**[¶](#mint "Permanent link")

Calling this method supplies assets into the market and receives jTokens in exchange.

```
function mint() external payable
```

* **Parameter description:**
  + `msg.value:` the amount of TRX to supply.
* **Returns:** None, reverts on error.

#### **Event**[¶](#event_2 "Permanent link")

```
Mint(address minter, uint mintAmount, uint mintTokens)
```

* Emits when user successfully mint.
  + `minter:` operate supply assets into the market;
  + `mintAmount:` the amount of supplied assets;
  + `mintTokens:` the tokens need to mint.

### **Redeem**[¶](#redeem "Permanent link")

Calling this method redeems jTokens in exchange for the underlying asset and accrues interest whether or not the operation succeeds.

```
function redeem(uint redeemTokens) external returns (uint)
```

* **Parameter description:**
  + `redeemTokens:` the number of jTokens to redeem into underlying.
* **Returns:** 0 for success, reverts on error.

#### **Event**[¶](#event_3 "Permanent link")

```
Redeem(address redeemer, uint redeemAmount, uint redeemTokens)
```

* Emits when user successfully redeem.
  + `redeemer:` operate redeem jTokens;
  + `redeemAmount:` the amount of redeem assets;
  + `redeemTokens:` the tokens need to redeem.

### **RedeemUnderlying**[¶](#redeemunderlying "Permanent link")

Calling this method redeems jTokens in exchange for a specified amount of underlying asset.

```
function redeemUnderlying(uint redeemAmount) external returns (uint)
```

* **Parameter description:**
  + `redeemAmount:` the amount of underlying to redeem.
* **Returns:** 0 for success, reverts on error.

### **Transfer**[¶](#transfer "Permanent link")

Calling this method transfers a specified amount of jtokens to the destination. This action will fail if the account's liquidity become negative due to the transfer.

```
function transfer(address dst, uint256 amount) external nonReentrant returns (bool)
```

* **Parameter description:**
  + `dst:` the receiver's address.
  + `amount:` amount of token to be transferred.
* **Returns:** A boolean value indicating whether or not the transfer succeeded.

## **Liquidation Process**[¶](#liquidation-process "Permanent link")

To enable developers to determine if a user is eligible for liquidation and to facilitate the liquidation process through contract calls, the following steps outline the specific operations to be executed:

1. **Query Liquidation Incentive:** Before proceeding, check the reward of the liquidation. This represents the "bonus" collateral a liquidator receives.

   * **Action:** Call `liquidationIncentiveMantissa()` on the **Unitroller** contract.
   * **Purpose:** To calculate the potential profit from the liquidation.
2. **Assess Account Liquidity:** Identify whether an account's collateral is insufficient to cover its debt.

   * **Action:** Call `getAccountLiquidity(address account)` on the **Unitroller** contract.
   * **Evaluation:** This function returns three values. You are looking for the shortfall.
     + If **shortfall > 0:** The account is underwater and eligible for liquidation.
     + If **liquidity > 0:** The account is healthy and cannot be liquidated.
3. **Execute Liquidation:** Once a target is confirmed, call the specific entry point based on the asset type being repaid.

   * **For jTRC20:** Call `liquidateBorrow(address borrower, uint repayAmount, address jTokenCollateral)` on the respective jTrc20 contract.
   * **For jTRX:** Call `liquidateBorrow(address borrower, address jTokenCollateral)` on the jTRX contract.

In addition, JustLend DAO will continuously monitor relevant data and provide an interface for querying high-risk liquidation users. You can **Identify High-Risk Users** by navigating to the [APIs](https://docs.justlend.org/developers/apis/) page and calling the **/justlend/liquidate/highRiskAccountList** endpoint.

**Please note** that there may be a certain delay in the availability of backend data and is for reference only.

### **Liquidation Incentive**[¶](#liquidation-incentive "Permanent link")

By calling the liquidationIncentiveMantissa function of the Unitroller contract, liquidation incentives can be inquired. Liquidators will be given a proportion of the borrower's collateral as an incentive, which is defined as liquidation incentive. This is to encourage liquidators to perform liquidation of underwater accounts.

```
function liquidationIncentiveMantissa() view returns (uint)
```

* **Parameter description:** N/A
* **Returns:** The liquidationIncentive, scaled by 1e18, is multiplied by the closed borrow amount from the liquidator to determine how much collateral can be seized.

### **Get Account Liquidity**[¶](#get-account-liquidity "Permanent link")

By calling the getAccountLiquidity function of the Unitroller contract, account information can be accessed through an account's address to determine whether the account should be liquidated or not.

```
getAccountLiquidity(address account) view returns (uint, uint, uint)
```

* **Parameter description:**
  + `account:` user address.
* **Returns:** The amount of underlying owned by owner.
  + `error:` error code, 0 means success.
  + `liquidity:` liquidity.
  + `shortfall:` When the value is bigger than 0, the current account does not meet the market requirement for collateralization and needs to be liquidated.

Note: There should be at most one non-zero value between liquidity and shortfall.

### **Liquidate Borrow（jTrc20）**[¶](#liquidate-borrowjtrc20 "Permanent link")

By calling liquidateBorrow function of the corresponding jTrc20 contract (e.g. jUSDT), accounts whose liquidity does not meet the market requirement for collateralization will be liquidated by other users to restore the account liquidity to a normal level (i.e. higher than the market requirement for collateralization). In the event of liquidation, liquidators may repay part or 50% of the loan for the borrower. Liquidators will be given a proportion of the borrower's collateral as an incentive.

```
function liquidateBorrow(address borrower, uint repayAmount, address jTokenCollateral) returns (uint)
```

* **Parameter description:**
  + `borrower:` address of a liquidated account.
  + `repayAmount:` amount of token to be repaid in the event of liquidation (measured in the borrowed asset).
  + `jTokenCollateral:` address of the jTOKEN contract to set aside the collateralized asset of a borrower.
* **Returns:** 0 on success, otherwise an Error code.

### **Liquidate Borrow（jTRX）**[¶](#liquidate-borrowjtrx "Permanent link")

By calling the liquidateBorrow function of the jTRX contract, accounts whose liquidity does not meet the market requirement for collateralization will be liquidated by other users to restore the account liquidity to a normal level (i.e., higher than the market requirement for collateralization). In the event of liquidation, liquidators may repay part or 50% of the loan for the borrower. Liquidators will be given a proportion of the borrower's collateral as an incentive.

```
function liquidateBorrow(address borrower, address jTokenCollateral) payable
```

* **Parameter description:**
  + `borrower:` address of a liquidated account.
  + `jTokenCollateral:` address of the jTRX contract to set aside the collateralized asset of a borrower.
  + `msg.value:` amount of TRX to be repaid in the event of liquidation.
* **Returns:** No return. If any error occurs, the transaction will be reverted.

#### **Event**[¶](#event_4 "Permanent link")

```
LiquidateBorrow(address liquidator, address borrower, uint repayAmount, address cTokenCollateral, uint seizeTokens)
```

* Emits when user successfully liquidate borrow order.
  + `liquidator:` operate liquidation;
  + `borrower:` address of a liquidated account;
  + `repayAmount:` the amount of repaid assets;
  + `cTokenCollateral:` address of the jTRX contract to set aside the collateralized asset of a borrower；
  + `seizeTokens:` the tokens need to be liquidated.

## **Error Code And Failure info**[¶](#error-code-and-failure-info "Permanent link")

### **Error code**[¶](#error-code "Permanent link")

| Code | Name | Description |
| --- | --- | --- |
| 0 | NO\_ERROR | Not a failure. |
| 1 | UNAUTHORIZED | The sender is not authorized to perform this action. |
| 2 | BAD\_INPUT | An invalid argument was supplied by the caller. |
| 3 | COMPTROLLER\_REJECTION | The action would violate the comptroller policy. |
| 4 | COMPTROLLER\_CALCULATION\_ERROR | An internal calculation has failed in the comptroller. |
| 5 | INTEREST\_RATE\_MODEL\_ERROR | The interest rate model returned an invalid value. |
| 6 | INVALID\_ACCOUNT\_PAIR | The specified combination of accounts is invalid. |
| 7 | INVALID\_CLOSE\_AMOUNT\_REQUESTED | The amount to liquidate is invalid. |
| 8 | INVALID\_COLLATERAL\_FACTOR | The collateral factor is invalid. |
| 9 | MATH\_ERROR | A math calculation error occurred. |
| 10 | MARKET\_NOT\_FRESH | Interest has not been properly accrued. |
| 11 | MARKET\_NOT\_LISTED | The market is not currently listed by its comptroller. |
| 12 | TOKEN\_INSUFFICIENT\_ALLOWANCE | ERC-20 contract must allow Money Market contract to call transferFrom. The current allowance is either 0 or less than the requested supply, repayBorrow or liquidate amount. |
| 13 | TOKEN\_INSUFFICIENT\_BALANCE | Caller does not have sufficient balance in the ERC-20 contract to complete the desired action. |
| 14 | TOKEN\_INSUFFICIENT\_CASH | The market does not have a sufficient cash balance to complete the transaction. You may attempt this transaction again later. |
| 15 | TOKEN\_TRANSFER\_IN\_FAILED | Failure in ERC-20 when transfering token into the market. |
| 16 | TOKEN\_TRANSFER\_OUT\_FAILED | Failure in ERC-20 when transfering token out of the market. |

### **Failure info**[¶](#failure-info "Permanent link")

| Code | Name |
| --- | --- |
| 0 | ACCEPT\_ADMIN\_PENDING\_ADMIN\_CHECK |
| 1 | ACCRUE\_INTEREST\_ACCUMULATED\_INTEREST\_CALCULATION\_FAILED |
| 2 | ACCRUE\_INTEREST\_BORROW\_RATE\_CALCULATION\_FAILED |
| 3 | ACCRUE\_INTEREST\_NEW\_BORROW\_INDEX\_CALCULATION\_FAILED |
| 4 | ACCRUE\_INTEREST\_NEW\_TOTAL\_BORROWS\_CALCULATION\_FAILED |
| 5 | ACCRUE\_INTEREST\_NEW\_TOTAL\_RESERVES\_CALCULATION\_FAILED |
| 6 | ACCRUE\_INTEREST\_SIMPLE\_INTEREST\_FACTOR\_CALCULATION\_FAILED |
| 7 | BORROW\_ACCUMULATED\_BALANCE\_CALCULATION\_FAILED |
| 8 | BORROW\_ACCRUE\_INTEREST\_FAILED |
| 9 | BORROW\_CASH\_NOT\_AVAILABLE |
| 10 | BORROW\_FRESHNESS\_CHECK |
| 11 | BORROW\_NEW\_TOTAL\_BALANCE\_CALCULATION\_FAILED |
| 12 | BORROW\_NEW\_ACCOUNT\_BORROW\_BALANCE\_CALCULATION\_FAILED |
| 13 | BORROW\_MARKET\_NOT\_LISTED |
| 14 | BORROW\_COMPTROLLER\_REJECTION |
| 15 | LIQUIDATE\_ACCRUE\_BORROW\_INTEREST\_FAILED |
| 16 | LIQUIDATE\_ACCRUE\_COLLATERAL\_INTEREST\_FAILED |
| 17 | LIQUIDATE\_COLLATERAL\_FRESHNESS\_CHECK |
| 18 | LIQUIDATE\_COMPTROLLER\_REJECTION |
| 19 | LIQUIDATE\_COMPTROLLER\_CALCULATE\_AMOUNT\_SEIZE\_FAILED |
| 20 | LIQUIDATE\_CLOSE\_AMOUNT\_IS\_UINT\_MAX |
| 21 | LIQUIDATE\_CLOSE\_AMOUNT\_IS\_ZERO |
| 22 | LIQUIDATE\_FRESHNESS\_CHECK |
| 23 | LIQUIDATE\_LIQUIDATOR\_IS\_BORROWER |
| 24 | LIQUIDATE\_REPAY\_BORROW\_FRESH\_FAILED |
| 25 | LIQUIDATE\_SEIZE\_BALANCE\_INCREMENT\_FAILED |
| 26 | LIQUIDATE\_SEIZE\_BALANCE\_DECREMENT\_FAILED |
| 27 | LIQUIDATE\_SEIZE\_COMPTROLLER\_REJECTION |
| 28 | LIQUIDATE\_SEIZE\_LIQUIDATOR\_IS\_BORROWER |
| 29 | LIQUIDATE\_SEIZE\_TOO\_MUCH |
| 30 | MINT\_ACCRUE\_INTEREST\_FAILED |
| 31 | MINT\_COMPTROLLER\_REJECTION |
| 32 | MINT\_EXCHANGE\_CALCULATION\_FAILED |
| 33 | MINT\_EXCHANGE\_RATE\_READ\_FAILED |
| 34 | MINT\_FRESHNESS\_CHECK |
| 35 | MINT\_NEW\_ACCOUNT\_BALANCE\_CALCULATION\_FAILED |
| 36 | AMINT\_NEW\_TOTAL\_SUPPLY\_CALCULATION\_FAILED |
| 37 | MINT\_TRANSFER\_IN\_FAILED |
| 38 | MINT\_TRANSFER\_IN\_NOT\_POSSIBLE |
| 39 | REDEEM\_ACCRUE\_INTEREST\_FAILED |
| 40 | REDEEM\_COMPTROLLER\_REJECTION |
| 41 | REDEEM\_EXCHANGE\_TOKENS\_CALCULATION\_FAILED |
| 42 | REDEEM\_EXCHANGE\_AMOUNT\_CALCULATION\_FAILED |
| 43 | REDEEM\_EXCHANGE\_RATE\_READ\_FAILED |
| 44 | REDEEM\_FRESHNESS\_CHECK |
| 45 | REDEEM\_NEW\_ACCOUNT\_BALANCE\_CALCULATION\_FAILED |
| 46 | REDEEM\_NEW\_TOTAL\_SUPPLY\_CALCULATION\_FAILED |
| 47 | REDEEM\_TRANSFER\_OUT\_NOT\_POSSIBLE |
| 48 | REDUCE\_RESERVES\_ACCRUE\_INTEREST\_FAILED |
| 49 | REDUCE\_RESERVES\_ADMIN\_CHECK |
| 50 | REDUCE\_RESERVES\_CASH\_NOT\_AVAILABLE |
| 51 | REDUCE\_RESERVES\_FRESH\_CHECK |
| 52 | REDUCE\_RESERVES\_VALIDATION |
| 53 | REPAY\_BEHALF\_ACCRUE\_INTEREST\_FAILED |
| 54 | REPAY\_BORROW\_ACCRUE\_INTEREST\_FAILED |
| 55 | REPAY\_BORROW\_ACCUMULATED\_BALANCE\_CALCULATION\_FAILED |
| 56 | REPAY\_BORROW\_COMPTROLLER\_REJECTION |
| 57 | REPAY\_BORROW\_FRESHNESS\_CHECK |
| 58 | REPAY\_BORROW\_NEW\_ACCOUNT\_BORROW\_BALANCE\_CALCULATION\_FAILED |
| 59 | REPAY\_BORROW\_NEW\_TOTAL\_BALANCE\_CALCULATION\_FAILED |
| 60 | REPAY\_BORROW\_TRANSFER\_IN\_NOT\_POSSIBLE |
| 61 | SET\_COLLATERAL\_FACTOR\_OWNER\_CHECK |
| 62 | SET\_COLLATERAL\_FACTOR\_VALIDATION |
| 63 | SET\_COMPTROLLER\_OWNER\_CHECK |
| 64 | SET\_INTEREST\_RATE\_MODEL\_ACCRUE\_INTEREST\_FAILED |
| 65 | SET\_INTEREST\_RATE\_MODEL\_FRESH\_CHECK |
| 66 | SET\_INTEREST\_RATE\_MODEL\_OWNER\_CHECK |
| 67 | SET\_MAX\_ASSETS\_OWNER\_CHECK |
| 68 | SET\_ORACLE\_MARKET\_NOT\_LISTED |
| 69 | SET\_PENDING\_ADMIN\_OWNER\_CHECK |
| 70 | SET\_RESERVE\_FACTOR\_ACCRUE\_INTEREST\_FAILED |
| 71 | SET\_RESERVE\_FACTOR\_ADMIN\_CHECK |
| 72 | SET\_RESERVE\_FACTOR\_FRESH\_CHECK |
| 73 | SET\_RESERVE\_FACTOR\_BOUNDS\_CHECK |
| 74 | TRANSFER\_COMPTROLLER\_REJECTION |
| 75 | TRANSFER\_NOT\_ALLOWED |
| 76 | TRANSFER\_NOT\_ENOUGH |
| 77 | TRANSFER\_TOO\_MUCH |

---