

org.tron.trident.proto

## Interface Response.AssetIssueListOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.AssetIssueList](../../../../org/tron/trident/proto/Response.AssetIssueList.html "class in org.tron.trident.proto"), [Response.AssetIssueList.Builder](../../../../org/tron/trident/proto/Response.AssetIssueList.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.AssetIssueListOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Contract.AssetIssueContract` | `getAssets(int index)` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `int` | `getAssetsCount()` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `java.util.List<Contract.AssetIssueContract>` | `getAssetsList()` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `Contract.AssetIssueContractOrBuilder` | `getAssetsOrBuilder(int index)` `repeated .protocol.AssetIssueContract assets = 1;` |
    | `java.util.List<? extends Contract.AssetIssueContractOrBuilder>` | `getAssetsOrBuilderList()` `repeated .protocol.AssetIssueContract assets = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getAssetsList

      ```
      java.util.List<Contract.AssetIssueContract> getAssetsList()
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`
    - #### getAssets

      ```
      Contract.AssetIssueContract getAssets(int index)
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`
    - #### getAssetsCount

      ```
      int getAssetsCount()
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`
    - #### getAssetsOrBuilderList

      ```
      java.util.List<? extends Contract.AssetIssueContractOrBuilder> getAssetsOrBuilderList()
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`
    - #### getAssetsOrBuilder

      ```
      Contract.AssetIssueContractOrBuilder getAssetsOrBuilder(int index)
      ```

      `repeated .protocol.AssetIssueContract assets = 1;`