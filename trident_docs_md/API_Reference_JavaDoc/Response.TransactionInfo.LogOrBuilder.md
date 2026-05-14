

org.tron.trident.proto

## Interface Response.TransactionInfo.LogOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.TransactionInfo.Log](../../../../org/tron/trident/proto/Response.TransactionInfo.Log.html "class in org.tron.trident.proto"), [Response.TransactionInfo.Log.Builder](../../../../org/tron/trident/proto/Response.TransactionInfo.Log.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response.TransactionInfo](../../../../org/tron/trident/proto/Response.TransactionInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.TransactionInfo.LogOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getAddress()` `bytes address = 1;` |
    | `com.google.protobuf.ByteString` | `getData()` `bytes data = 3;` |
    | `com.google.protobuf.ByteString` | `getTopics(int index)` `repeated bytes topics = 2;` |
    | `int` | `getTopicsCount()` `repeated bytes topics = 2;` |
    | `java.util.List<com.google.protobuf.ByteString>` | `getTopicsList()` `repeated bytes topics = 2;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getAddress

      ```
      com.google.protobuf.ByteString getAddress()
      ```

      `bytes address = 1;`

      Returns:
      :   The address.
    - #### getTopicsList

      ```
      java.util.List<com.google.protobuf.ByteString> getTopicsList()
      ```

      `repeated bytes topics = 2;`

      Returns:
      :   A list containing the topics.
    - #### getTopicsCount

      ```
      int getTopicsCount()
      ```

      `repeated bytes topics = 2;`

      Returns:
      :   The count of topics.
    - #### getTopics

      ```
      com.google.protobuf.ByteString getTopics(int index)
      ```

      `repeated bytes topics = 2;`

      Parameters:
      :   `index` - The index of the element to return.

      Returns:
      :   The topics at the given index.
    - #### getData

      ```
      com.google.protobuf.ByteString getData()
      ```

      `bytes data = 3;`

      Returns:
      :   The data.