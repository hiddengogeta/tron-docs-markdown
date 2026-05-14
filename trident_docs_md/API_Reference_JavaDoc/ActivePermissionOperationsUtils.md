

org.tron.trident.core.account

## Class ActivePermissionOperationsUtils

* java.lang.Object
* + org.tron.trident.core.account.ActivePermissionOperationsUtils

* ---

    

  ```
  public class ActivePermissionOperationsUtils
  extends java.lang.Object
  ```

  Utility class for encoding and decoding operations for Account Active permissions

  Each bit in the 32-byte operations field corresponds to a [`Chain.Transaction.Contract.ContractType`](../../../../../org/tron/trident/proto/Chain.Transaction.Contract.ContractType.html "enum in org.tron.trident.proto"),
  allowing up to 256 different contract types to be represented.

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static java.lang.String` | `NONE_OPERATIONS` |
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `ActivePermissionOperationsUtils()` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static com.google.protobuf.ByteString` | `buildOperations(com.google.protobuf.ByteString currentOperations, boolean enable, Chain.Transaction.Contract.ContractType... contractTypes)` Build a new operations ByteString by enabling or disabling specified contract types. |
    | `static Chain.Transaction.Contract.ContractType[]` | `decodeOperations(com.google.protobuf.ByteString operations)` Decode operations to list of contract types |
    | `static Chain.Transaction.Contract.ContractType[]` | `decodeOperations(java.lang.String hexOperations)` Decode operations hex string to list of contract type names |
    | `static java.lang.String` | `encodeOperations(Chain.Transaction.Contract.ContractType[] contractTypes)` Encode contract types to operations hex string |
    | `static java.lang.String` | `encodeOperations(int[] contractIds)` Encode contract types to operations hex string using contract IDs. |
    | `static java.lang.String` | `encodeOperations(java.lang.String[] contractNames)` Encode contract types to operations hex string using contract names |
    | `static Chain.Transaction.Contract.ContractType` | `getContractTypeById(int contractId)` Get contractType by ID |
    | `static Chain.Transaction.Contract.ContractType` | `getContractTypeByName(java.lang.String contractName)` Get contractType by name |
    | `static boolean` | `isValidOperations(com.google.protobuf.ByteString operations)` Validate if operations string is valid |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Field Detail

    - #### NONE\_OPERATIONS

      ```
      public static final java.lang.String NONE_OPERATIONS
      ```

      See Also:
      :   [Constant Field Values](../../../../../constant-values.html#org.tron.trident.core.account.ActivePermissionOperationsUtils.NONE_OPERATIONS)
  + ### Constructor Detail

    - #### ActivePermissionOperationsUtils

      ```
      public ActivePermissionOperationsUtils()
      ```
  + ### Method Detail

    - #### encodeOperations

      ```
      public static java.lang.String encodeOperations(Chain.Transaction.Contract.ContractType[] contractTypes)
      ```

      Encode contract types to operations hex string

      Parameters:
      :   `contractTypes` - Array of contract types to encode

      Returns:
      :   Hex string representation of operations
    - #### encodeOperations

      ```
      public static java.lang.String encodeOperations(int[] contractIds)
      ```

      Encode contract types to operations hex string using contract IDs.

      Each bit in the 32-byte operations array represents a [`Chain.Transaction.Contract.ContractType`](../../../../../org/tron/trident/proto/Chain.Transaction.Contract.ContractType.html "enum in org.tron.trident.proto").
      Up to 256 different contract types are supported (8 bits × 32 bytes).

      Parameters:
      :   `contractIds` - Array of contract IDs to encode

      Returns:
      :   Hex string representation of operations
    - #### encodeOperations

      ```
      public static java.lang.String encodeOperations(java.lang.String[] contractNames)
      ```

      Encode contract types to operations hex string using contract names

      Parameters:
      :   `contractNames` - Array of contract names to encode

      Returns:
      :   Hex string representation of operations
    - #### decodeOperations

      ```
      public static Chain.Transaction.Contract.ContractType[] decodeOperations(com.google.protobuf.ByteString operations)
      ```

      Decode operations to list of contract types

      Parameters:
      :   `operations` - ByteString representation of operations

      Returns:
      :   Array of contractType
    - #### decodeOperations

      ```
      public static Chain.Transaction.Contract.ContractType[] decodeOperations(java.lang.String hexOperations)
      ```

      Decode operations hex string to list of contract type names

      Parameters:
      :   `hexOperations` - Hex string representation of operations

      Returns:
      :   Array of contractType
    - #### isValidOperations

      ```
      public static boolean isValidOperations(com.google.protobuf.ByteString operations)
      ```

      Validate if operations string is valid

      Parameters:
      :   `operations` - ByteString representation of operations

      Returns:
      :   true if valid, false otherwise
    - #### getContractTypeByName

      ```
      public static Chain.Transaction.Contract.ContractType getContractTypeByName(java.lang.String contractName)
      ```

      Get contractType by name

      Parameters:
      :   `contractName` - Name of the contract

      Returns:
      :   ContractType or null if not found
    - #### getContractTypeById

      ```
      public static Chain.Transaction.Contract.ContractType getContractTypeById(int contractId)
      ```

      Get contractType by ID

      Parameters:
      :   `contractId` - ID of the contract

      Returns:
      :   ContractType
    - #### buildOperations

      ```
      public static com.google.protobuf.ByteString buildOperations(com.google.protobuf.ByteString currentOperations,
                                                                   boolean enable,
                                                                   Chain.Transaction.Contract.ContractType... contractTypes)
      ```

      Build a new operations ByteString by enabling or disabling specified contract types.

      **Note:** This method does not modify the input `currentOperations`, it returns a new ByteString.
      If currentOperations not contain any of the specified contract types to disable, or already contains those to enable,
      no changes will be made, but a new ByteString which is equal to currentOperations will be returned.

      Example usage:

      ```
       // enable TransferContract and disable VoteContract from account current operations
       ByteString currentOps = account.getActivePermission(0).getOperations();
       ByteString updatedOps = buildOperations(currentOps, true, ContractType.TransferContract);
       updatedOps = buildOperations(updatedOps, false, ContractType.VoteContract);

       // buildOperations from scratch by enabling TransferAssetContract and TransferContract
       ByteString options = ActivePermissionOperationsUtils.buildOperations(
           ByteString.EMPTY,
           true,
           ContractType.TransferAssetContract,
           ContractType.TransferContract);
      ```

      Parameters:
      :   `currentOperations` - current operations ByteString, use ByteString.EMPTY to start from scratch
      :   `enable` - `true` to enable the specified contract types, `false` to disable
      :   `contractTypes` - contract types to update, if null or empty, no changes will be made

      Returns:
      :   New operations ByteString with updated permissions, never null