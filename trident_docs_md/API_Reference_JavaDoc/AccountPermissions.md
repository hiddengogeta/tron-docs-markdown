

org.tron.trident.core.account

## Class AccountPermissions

* java.lang.Object
* + org.tron.trident.core.account.AccountPermissions

* ---

    

  ```
  public class AccountPermissions
  extends java.lang.Object
  ```

  Aggregates owner, witness and active permissions for a TRON account.

  **Note:** This class is NOT thread-safe. If you need to share an instance
  across multiple threads, external synchronization is required.

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `AccountPermissions(Response.Account account)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `AccountPermissions` | `addActivePermission(Common.Permission active)` Add an active permission |
    | `Common.Permission` | `createActivePermission(int permissionId, long threshold, com.google.protobuf.ByteString operations, java.util.Map<java.lang.String,java.lang.Long> keys)` Create a Permission object for Active type, default name "active" |
    | `Common.Permission` | `createActivePermission(java.lang.String permissionName, int permissionId, long threshold, com.google.protobuf.ByteString operations, java.util.Map<java.lang.String,java.lang.Long> keys)` Create a Permission object for Active type |
    | `Common.Key` | `createKey(java.lang.String address, long weight)` Create a Key object with address and weight |
    | `Common.Permission` | `createOwnerPermission(long threshold, java.util.Map<java.lang.String,java.lang.Long> keys)` Create a Permission object for Owner type, default name "owner" |
    | `Common.Permission` | `createOwnerPermission(java.lang.String permissionName, long threshold, java.util.Map<java.lang.String,java.lang.Long> keys)` Create a Permission object for Owner type |
    | `Common.Permission` | `createWitnessPermission(long threshold, java.util.Map<java.lang.String,java.lang.Long> keys)` Create a Permission object for Witness type, default name "witness" |
    | `Common.Permission` | `createWitnessPermission(java.lang.String permissionName, long threshold, java.util.Map<java.lang.String,java.lang.Long> keys)` Create a Permission object for Witness type |
    | `AccountPermissions` | `disableActivePermissionOperation(int permissionId, Chain.Transaction.Contract.ContractType... contractTypes)` Disable active permission operation for specific contract types. |
    | `AccountPermissions` | `enableActivePermissionOperation(int permissionId, Chain.Transaction.Contract.ContractType... contractTypes)` Enable active permission operation for a specific contract type. |
    | `Common.Permission` | `getActivePermissionByPermissionId(int permissionId)` get an active permission by its Permission ID |
    | `java.util.List<Common.Permission>` | `getActivePermissions()` get a copy of active permission list |
    | `AccountPermissions` | `removeActivePermission(int permissionId)` Remove an active permission by its ID |
    | `AccountPermissions` | `setActivePermission(java.util.List<Common.Permission> actives)` Set the list of active permissions |
    | `AccountPermissions` | `setOwnerPermission(Common.Permission owner)` Set the owner permission |
    | `AccountPermissions` | `setWitnessPermission(Common.Permission witness)` Set the witness permission |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### AccountPermissions

      ```
      public AccountPermissions(Response.Account account)
      ```
  + ### Method Detail

    - #### getActivePermissions

      ```
      public java.util.List<Common.Permission> getActivePermissions()
      ```

      get a copy of active permission list

      This method returns a copy of the internal list, to update the active permissions, use
      [`setActivePermission(List)`](../../../../../org/tron/trident/core/account/AccountPermissions.html#setActivePermission-java.util.List-) instead.
    - #### setOwnerPermission

      ```
      public AccountPermissions setOwnerPermission(Common.Permission owner)
      ```

      Set the owner permission

      Parameters:
      :   `owner` - Owner permission

      Returns:
      :   Updated AccountPermissions object
    - #### setWitnessPermission

      ```
      public AccountPermissions setWitnessPermission(Common.Permission witness)
      ```

      Set the witness permission

      Parameters:
      :   `witness` - Witness permission

      Returns:
      :   Updated AccountPermissions object
    - #### setActivePermission

      ```
      public AccountPermissions setActivePermission(java.util.List<Common.Permission> actives)
      ```

      Set the list of active permissions

      Parameters:
      :   `actives` - List of active permissions

      Returns:
      :   Updated AccountPermissions object
    - #### addActivePermission

      ```
      public AccountPermissions addActivePermission(Common.Permission active)
      ```

      Add an active permission

      Parameters:
      :   `active` - Permission to add

      Returns:
      :   Updated AccountPermissions object
    - #### removeActivePermission

      ```
      public AccountPermissions removeActivePermission(int permissionId)
      ```

      Remove an active permission by its ID

      Parameters:
      :   `permissionId` - Permission ID to remove

      Returns:
      :   Updated AccountPermissions object
    - #### getActivePermissionByPermissionId

      ```
      public Common.Permission getActivePermissionByPermissionId(int permissionId)
      ```

      get an active permission by its Permission ID

      Parameters:
      :   `permissionId` - Permission ID

      Returns:
      :   Permission object if found, null otherwise
    - #### enableActivePermissionOperation

      ```
      public AccountPermissions enableActivePermissionOperation(int permissionId,
                                                                Chain.Transaction.Contract.ContractType... contractTypes)
      ```

      Enable active permission operation for a specific contract type.

      Example: to enable TransferContract and TransferAssetContract for permission ID 2:

      ```
         accountPermissions.enableActivePermissionOperation(2,
             ContractType.TransferContract, ContractType.TransferAssetContract);
      ```

      Parameters:
      :   `permissionId` - Permission ID
      :   `contractTypes` - Contract type to add, cannot be null

      Returns:
      :   Updated AccountPermissions object
    - #### disableActivePermissionOperation

      ```
      public AccountPermissions disableActivePermissionOperation(int permissionId,
                                                                 Chain.Transaction.Contract.ContractType... contractTypes)
      ```

      Disable active permission operation for specific contract types.

      Example: to disable TransferContract and TransferAssetContract for permission ID 2

      ```
         accountPermissions.disableActivePermissionOperation(2,
         ContractType.TransferContract, ContractType.TransferAssetContract);
      ```

      Parameters:
      :   `permissionId` - Permission ID
      :   `contractTypes` - Contract type to remove, cannot be null

      Returns:
      :   Updated AccountPermissions object
    - #### createKey

      ```
      public Common.Key createKey(java.lang.String address,
                                  long weight)
      ```

      Create a Key object with address and weight

      Parameters:
      :   `address` - Base58Check address
      :   `weight` - Key weight

      Returns:
      :   Key object
    - #### createOwnerPermission

      ```
      public Common.Permission createOwnerPermission(long threshold,
                                                     java.util.Map<java.lang.String,java.lang.Long> keys)
      ```

      Create a Permission object for Owner type, default name "owner"

      See Also:
      :   [`createOwnerPermission(String, long, Map)`](../../../../../org/tron/trident/core/account/AccountPermissions.html#createOwnerPermission-java.lang.String-long-java.util.Map-)
    - #### createOwnerPermission

      ```
      public Common.Permission createOwnerPermission(java.lang.String permissionName,
                                                     long threshold,
                                                     java.util.Map<java.lang.String,java.lang.Long> keys)
      ```

      Create a Permission object for Owner type

      Parameters:
      :   `permissionName` - Permission name
      :   `threshold` - Threshold value
      :   `keys` - Map of address -> weight

      Returns:
      :   Permission object
    - #### createWitnessPermission

      ```
      public Common.Permission createWitnessPermission(long threshold,
                                                       java.util.Map<java.lang.String,java.lang.Long> keys)
      ```

      Create a Permission object for Witness type, default name "witness"

      See Also:
      :   [`createWitnessPermission(String, long, Map)`](../../../../../org/tron/trident/core/account/AccountPermissions.html#createWitnessPermission-java.lang.String-long-java.util.Map-)
    - #### createWitnessPermission

      ```
      public Common.Permission createWitnessPermission(java.lang.String permissionName,
                                                       long threshold,
                                                       java.util.Map<java.lang.String,java.lang.Long> keys)
      ```

      Create a Permission object for Witness type

      Parameters:
      :   `permissionName` - Permission name
      :   `threshold` - Threshold value
      :   `keys` - Map of address -> weight

      Returns:
      :   Permission object
    - #### createActivePermission

      ```
      public Common.Permission createActivePermission(java.lang.String permissionName,
                                                      int permissionId,
                                                      long threshold,
                                                      com.google.protobuf.ByteString operations,
                                                      java.util.Map<java.lang.String,java.lang.Long> keys)
      ```

      Create a Permission object for Active type

      Parameters:
      :   `permissionName` - Permission name
      :   `permissionId` - Permission ID (must be >= 2)
      :   `threshold` - Threshold value
      :   `operations` - Operation ByteString, which can be built using
          [`ActivePermissionOperationsUtils.buildOperations(
          com.google.protobuf.ByteString, boolean, org.tron.trident.proto.Chain.Transaction.Contract.ContractType...)`](../../../../../org/tron/trident/core/account/ActivePermissionOperationsUtils.html#buildOperations-com.google.protobuf.ByteString-boolean-org.tron.trident.proto.Chain.Transaction.Contract.ContractType...-)
      :   `keys` - Map of address -> weight

      Returns:
      :   Permission object
    - #### createActivePermission

      ```
      public Common.Permission createActivePermission(int permissionId,
                                                      long threshold,
                                                      com.google.protobuf.ByteString operations,
                                                      java.util.Map<java.lang.String,java.lang.Long> keys)
      ```

      Create a Permission object for Active type, default name "active"

      See Also:
      :   [`createActivePermission(String, int, long, ByteString, Map)`](../../../../../org/tron/trident/core/account/AccountPermissions.html#createActivePermission-java.lang.String-int-long-com.google.protobuf.ByteString-java.util.Map-)