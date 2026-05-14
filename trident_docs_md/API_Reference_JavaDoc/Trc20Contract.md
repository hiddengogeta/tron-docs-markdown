

org.tron.trident.core.contract

## Class Trc20Contract

* java.lang.Object
* + [org.tron.trident.core.contract.Contract](../../../../../org/tron/trident/core/contract/Contract.html "class in org.tron.trident.core.contract")
  + - org.tron.trident.core.contract.Trc20Contract

* ---

    

  ```
  public class Trc20Contract
  extends Contract
  ```

  The `Trc20Contract` is a wrapper class of a standard TRC-20 smart contract.

  A `Trc20Contract` object includes standard TRC-20 functions defined
  in TIP-20. Each `Trc20Contract` binds a [`ApiWrapper`](../../../../../org/tron/trident/core/ApiWrapper.html "class in org.tron.trident.core") with specific
  caller's private key and address.

  Since:
  :   jdk 1.8.0\_231

  See Also:
  :   [`ApiWrapper`](../../../../../org/tron/trident/core/ApiWrapper.html "class in org.tron.trident.core"),
      [`Function`](../../../../../org/tron/trident/abi/datatypes/Function.html "class in org.tron.trident.abi.datatypes")

* + ### Nested Class Summary

    - ### Nested classes/interfaces inherited from class org.tron.trident.core.contract.[Contract](../../../../../org/tron/trident/core/contract/Contract.html "class in org.tron.trident.core.contract")

      `Contract.Builder`
  + ### Field Summary

    - ### Fields inherited from class org.tron.trident.core.contract.[Contract](../../../../../org/tron/trident/core/contract/Contract.html "class in org.tron.trident.core.contract")

      `abi, bytecode, callValue, cntrAddr, codeHash, constructor, consumeUserResourcePercent, functions, name, originAddr, originEnergyLimit, ownerAddr, trxHash, version, wrapper`
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `Trc20Contract(Contract cntr, java.lang.String ownerAddr, ApiWrapper wrapper)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `java.math.BigInteger` | `allowance(java.lang.String owner, java.lang.String spender)` Call function allowance(address \_owner, address \_spender) public view returns (uint256 remaining). |
    | `java.lang.String` | `approve(java.lang.String spender, long amount, int power, java.lang.String memo, long feeLimit)` Call function approve(address \_spender, uint256 \_value) public returns (bool success) Allows \_spender to withdraw from your account multiple times, up to the \_value amount. |
    | `java.math.BigInteger` | `balanceOf(java.lang.String accountAddr)` Call function balanceOf(address \_owner) public view returns (uint256 balance). |
    | `java.math.BigInteger` | `decimals()` Call function decimals() public view returns (uint8). |
    | `java.lang.String` | `name()` Call function name() public view returns (string). |
    | `java.lang.String` | `symbol()` Call function symbol() public view returns (string). |
    | `java.math.BigInteger` | `totalSupply()` Call function totalSupply() public view returns (uint256). |
    | `java.lang.String` | `transfer(java.lang.String destAddr, long amount, int power, java.lang.String memo, long feeLimit)` Call function transfer(address \_to, uint256 \_value) public returns (bool success). |
    | `java.lang.String` | `transferFrom(java.lang.String fromAddr, java.lang.String destAddr, long amount, int power, java.lang.String memo, long feeLimit)` call function transferFrom(address \_from, address \_to, uint256 \_value) public returns (bool success) The transferFrom method is used for a withdraw workflow, allowing contracts to transfer tokens on your behalf. |

    - ### Methods inherited from class org.tron.trident.core.contract.[Contract](../../../../../org/tron/trident/core/contract/Contract.html "class in org.tron.trident.core.contract")

      `abiToFunctions, collectParams, createSmartContract, deploy, deploy, loadAbiFromJson, loadConstructor, setAbi, toProto`
    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### Trc20Contract

      ```
      public Trc20Contract(Contract cntr,
                           java.lang.String ownerAddr,
                           ApiWrapper wrapper)
      ```
  + ### Method Detail

    - #### name

      ```
      public java.lang.String name()
      ```

      Call function name() public view returns (string).
      Returns the name of the token - e.g. "MyToken".

      Returns:
      :   the name of the token
    - #### symbol

      ```
      public java.lang.String symbol()
      ```

      Call function symbol() public view returns (string).
      Returns the symbol of the token. E.g. "HIX".

      Returns:
      :   the symbol of the token
    - #### decimals

      ```
      public java.math.BigInteger decimals()
      ```

      Call function decimals() public view returns (uint8).
      Returns the number of decimals the token uses - e.g. 8,
      means to divide the token amount by 100000000 to get its user representation

      Returns:
      :   the number of decimals the token uses
    - #### totalSupply

      ```
      public java.math.BigInteger totalSupply()
      ```

      Call function totalSupply() public view returns (uint256).
      Returns the total token supply.

      Returns:
      :   the total token supply
    - #### balanceOf

      ```
      public java.math.BigInteger balanceOf(java.lang.String accountAddr)
      ```

      Call function balanceOf(address \_owner) public view returns (uint256 balance).
      Returns the account balance of another account with address \_owner.

      Parameters:
      :   `accountAddr` - The token owner's address

      Returns:
      :   the account balance of another account with address \_owner
    - #### transfer

      ```
      public java.lang.String transfer(java.lang.String destAddr,
                                       long amount,
                                       int power,
                                       java.lang.String memo,
                                       long feeLimit)
      ```

      Call function transfer(address \_to, uint256 \_value) public returns (bool success).
      Transfers \_value amount of tokens to address \_to.

      Parameters:
      :   `destAddr` - The address to receive the token
      :   `amount` - The transfer amount
      :   `power` - The power number of 10 that the transfer amount multiplied by
      :   `memo` - The transaction memo
      :   `feeLimit` - The energy fee limit

      Returns:
      :   Transaction hash
    - #### transferFrom

      ```
      public java.lang.String transferFrom(java.lang.String fromAddr,
                                           java.lang.String destAddr,
                                           long amount,
                                           int power,
                                           java.lang.String memo,
                                           long feeLimit)
      ```

      call function transferFrom(address \_from, address \_to, uint256 \_value) public returns (bool success)
      The transferFrom method is used for a withdraw workflow,
      allowing contracts to transfer tokens on your behalf. This can only be called
      when someone has allowed you some amount.

      Parameters:
      :   `fromAddr` - The address who sends tokens (or the address to withdraw from)
      :   `destAddr` - The address to receive the token
      :   `amount` - The transfer amount
      :   `power` - The power number of 10 that the transfer amount multiplied by
      :   `memo` - The transaction memo
      :   `feeLimit` - The energy fee limit

      Returns:
      :   Transaction hash
    - #### approve

      ```
      public java.lang.String approve(java.lang.String spender,
                                      long amount,
                                      int power,
                                      java.lang.String memo,
                                      long feeLimit)
      ```

      Call function approve(address \_spender, uint256 \_value) public returns (bool success)
      Allows \_spender to withdraw from your account multiple times, up to the \_value amount.
      If this function is called again it overwrites the current allowance with \_value.

      Parameters:
      :   `spender` - The address who is allowed to withdraw.
      :   `amount` - The amount allowed to withdraw.
      :   `power` - The power number of 10 that the transfer amount multiplied by
      :   `memo` - The transaction memo
      :   `feeLimit` - The energy fee limit

      Returns:
      :   Transaction hash
    - #### allowance

      ```
      public java.math.BigInteger allowance(java.lang.String owner,
                                            java.lang.String spender)
      ```

      Call function allowance(address \_owner, address \_spender) public view returns (uint256 remaining).
      Returns the amount which \_spender is still allowed to withdraw from \_owner.

      Parameters:
      :   `owner` - The address to be withdrew from.
      :   `spender` - The address of the withdrawer.

      Returns:
      :   the amount which \_spender is still allowed to withdraw from \_owner