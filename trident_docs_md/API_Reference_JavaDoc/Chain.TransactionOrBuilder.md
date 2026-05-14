

org.tron.trident.proto

## Interface Chain.TransactionOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Chain.Transaction](../../../../org/tron/trident/proto/Chain.Transaction.html "class in org.tron.trident.proto"), [Chain.Transaction.Builder](../../../../org/tron/trident/proto/Chain.Transaction.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Chain](../../../../org/tron/trident/proto/Chain.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Chain.TransactionOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Chain.Transaction.raw` | `getRawData()` `.protocol.Transaction.raw raw_data = 1;` |
    | `Chain.Transaction.rawOrBuilder` | `getRawDataOrBuilder()` `.protocol.Transaction.raw raw_data = 1;` |
    | `Chain.Transaction.Result` | `getRet(int index)` `repeated .protocol.Transaction.Result ret = 5;` |
    | `int` | `getRetCount()` `repeated .protocol.Transaction.Result ret = 5;` |
    | `java.util.List<Chain.Transaction.Result>` | `getRetList()` `repeated .protocol.Transaction.Result ret = 5;` |
    | `Chain.Transaction.ResultOrBuilder` | `getRetOrBuilder(int index)` `repeated .protocol.Transaction.Result ret = 5;` |
    | `java.util.List<? extends Chain.Transaction.ResultOrBuilder>` | `getRetOrBuilderList()` `repeated .protocol.Transaction.Result ret = 5;` |
    | `com.google.protobuf.ByteString` | `getSignature(int index)` only support size = 1, repeated list here for muti-sig extension |
    | `int` | `getSignatureCount()` only support size = 1, repeated list here for muti-sig extension |
    | `java.util.List<com.google.protobuf.ByteString>` | `getSignatureList()` only support size = 1, repeated list here for muti-sig extension |
    | `boolean` | `hasRawData()` `.protocol.Transaction.raw raw_data = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### hasRawData

      ```
      boolean hasRawData()
      ```

      `.protocol.Transaction.raw raw_data = 1;`

      Returns:
      :   Whether the rawData field is set.
    - #### getRawData

      ```
      Chain.Transaction.raw getRawData()
      ```

      `.protocol.Transaction.raw raw_data = 1;`

      Returns:
      :   The rawData.
    - #### getRawDataOrBuilder

      ```
      Chain.Transaction.rawOrBuilder getRawDataOrBuilder()
      ```

      `.protocol.Transaction.raw raw_data = 1;`
    - #### getSignatureList

      ```
      java.util.List<com.google.protobuf.ByteString> getSignatureList()
      ```

      ```
       only support size = 1, repeated list here for muti-sig extension
      ```

      `repeated bytes signature = 2;`

      Returns:
      :   A list containing the signature.
    - #### getSignatureCount

      ```
      int getSignatureCount()
      ```

      ```
       only support size = 1, repeated list here for muti-sig extension
      ```

      `repeated bytes signature = 2;`

      Returns:
      :   The count of signature.
    - #### getSignature

      ```
      com.google.protobuf.ByteString getSignature(int index)
      ```

      ```
       only support size = 1, repeated list here for muti-sig extension
      ```

      `repeated bytes signature = 2;`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The signature at the given index.
    - #### getRetList

      ```
      java.util.List<Chain.Transaction.Result> getRetList()
      ```

      `repeated .protocol.Transaction.Result ret = 5;`
    - #### getRet

      ```
      Chain.Transaction.Result getRet(int index)
      ```

      `repeated .protocol.Transaction.Result ret = 5;`
    - #### getRetCount

      ```
      int getRetCount()
      ```

      `repeated .protocol.Transaction.Result ret = 5;`
    - #### getRetOrBuilderList

      ```
      java.util.List<? extends Chain.Transaction.ResultOrBuilder> getRetOrBuilderList()
      ```

      `repeated .protocol.Transaction.Result ret = 5;`
    - #### getRetOrBuilder

      ```
      Chain.Transaction.ResultOrBuilder getRetOrBuilder(int index)
      ```

      `repeated .protocol.Transaction.Result ret = 5;`