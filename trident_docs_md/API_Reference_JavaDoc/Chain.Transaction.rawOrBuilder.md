

org.tron.trident.proto

## Interface Chain.Transaction.rawOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Chain.Transaction.raw](../../../../org/tron/trident/proto/Chain.Transaction.raw.html "class in org.tron.trident.proto"), [Chain.Transaction.raw.Builder](../../../../org/tron/trident/proto/Chain.Transaction.raw.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Chain.Transaction](../../../../org/tron/trident/proto/Chain.Transaction.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Chain.Transaction.rawOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Common.authority` | `getAuths(int index)` `repeated .protocol.authority auths = 9;` |
    | `int` | `getAuthsCount()` `repeated .protocol.authority auths = 9;` |
    | `java.util.List<Common.authority>` | `getAuthsList()` `repeated .protocol.authority auths = 9;` |
    | `Common.authorityOrBuilder` | `getAuthsOrBuilder(int index)` `repeated .protocol.authority auths = 9;` |
    | `java.util.List<? extends Common.authorityOrBuilder>` | `getAuthsOrBuilderList()` `repeated .protocol.authority auths = 9;` |
    | `Chain.Transaction.Contract` | `getContract(int index)` only support size = 1, repeated list here for extension |
    | `int` | `getContractCount()` only support size = 1, repeated list here for extension |
    | `java.util.List<Chain.Transaction.Contract>` | `getContractList()` only support size = 1, repeated list here for extension |
    | `Chain.Transaction.ContractOrBuilder` | `getContractOrBuilder(int index)` only support size = 1, repeated list here for extension |
    | `java.util.List<? extends Chain.Transaction.ContractOrBuilder>` | `getContractOrBuilderList()` only support size = 1, repeated list here for extension |
    | `com.google.protobuf.ByteString` | `getData()` data not used |
    | `long` | `getExpiration()` `int64 expiration = 8;` |
    | `long` | `getFeeLimit()` `int64 fee_limit = 18;` |
    | `com.google.protobuf.ByteString` | `getRefBlockBytes()` `bytes ref_block_bytes = 1;` |
    | `com.google.protobuf.ByteString` | `getRefBlockHash()` `bytes ref_block_hash = 4;` |
    | `long` | `getRefBlockNum()` `int64 ref_block_num = 3;` |
    | `com.google.protobuf.ByteString` | `getScripts()` scripts not used |
    | `long` | `getTimestamp()` `int64 timestamp = 14;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getRefBlockBytes

      ```
      com.google.protobuf.ByteString getRefBlockBytes()
      ```

      `bytes ref_block_bytes = 1;`

      Returns:
      :   The refBlockBytes.
    - #### getRefBlockNum

      ```
      long getRefBlockNum()
      ```

      `int64 ref_block_num = 3;`

      Returns:
      :   The refBlockNum.
    - #### getRefBlockHash

      ```
      com.google.protobuf.ByteString getRefBlockHash()
      ```

      `bytes ref_block_hash = 4;`

      Returns:
      :   The refBlockHash.
    - #### getExpiration

      ```
      long getExpiration()
      ```

      `int64 expiration = 8;`

      Returns:
      :   The expiration.
    - #### getAuthsList

      ```
      java.util.List<Common.authority> getAuthsList()
      ```

      `repeated .protocol.authority auths = 9;`
    - #### getAuths

      ```
      Common.authority getAuths(int index)
      ```

      `repeated .protocol.authority auths = 9;`
    - #### getAuthsCount

      ```
      int getAuthsCount()
      ```

      `repeated .protocol.authority auths = 9;`
    - #### getAuthsOrBuilderList

      ```
      java.util.List<? extends Common.authorityOrBuilder> getAuthsOrBuilderList()
      ```

      `repeated .protocol.authority auths = 9;`
    - #### getAuthsOrBuilder

      ```
      Common.authorityOrBuilder getAuthsOrBuilder(int index)
      ```

      `repeated .protocol.authority auths = 9;`
    - #### getData

      ```
      com.google.protobuf.ByteString getData()
      ```

      ```
       data not used
      ```

      `bytes data = 10;`

      Returns:
      :   The data.
    - #### getContractList

      ```
      java.util.List<Chain.Transaction.Contract> getContractList()
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`
    - #### getContract

      ```
      Chain.Transaction.Contract getContract(int index)
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`
    - #### getContractCount

      ```
      int getContractCount()
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`
    - #### getContractOrBuilderList

      ```
      java.util.List<? extends Chain.Transaction.ContractOrBuilder> getContractOrBuilderList()
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`
    - #### getContractOrBuilder

      ```
      Chain.Transaction.ContractOrBuilder getContractOrBuilder(int index)
      ```

      ```
       only support size = 1, repeated list here for extension
      ```

      `repeated .protocol.Transaction.Contract contract = 11;`
    - #### getScripts

      ```
      com.google.protobuf.ByteString getScripts()
      ```

      ```
       scripts not used
      ```

      `bytes scripts = 12;`

      Returns:
      :   The scripts.
    - #### getTimestamp

      ```
      long getTimestamp()
      ```

      `int64 timestamp = 14;`

      Returns:
      :   The timestamp.
    - #### getFeeLimit

      ```
      long getFeeLimit()
      ```

      `int64 fee_limit = 18;`

      Returns:
      :   The feeLimit.