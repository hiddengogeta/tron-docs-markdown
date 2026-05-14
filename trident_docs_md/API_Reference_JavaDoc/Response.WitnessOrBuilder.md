

org.tron.trident.proto

## Interface Response.WitnessOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.Witness](../../../../org/tron/trident/proto/Response.Witness.html "class in org.tron.trident.proto"), [Response.Witness.Builder](../../../../org/tron/trident/proto/Response.Witness.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.WitnessOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `com.google.protobuf.ByteString` | `getAddress()` `bytes address = 1;` |
    | `boolean` | `getIsJobs()` `bool isJobs = 9;` |
    | `long` | `getLatestBlockNum()` `int64 latestBlockNum = 7;` |
    | `long` | `getLatestSlotNum()` `int64 latestSlotNum = 8;` |
    | `com.google.protobuf.ByteString` | `getPubKey()` `bytes pubKey = 3;` |
    | `long` | `getTotalMissed()` `int64 totalMissed = 6;` |
    | `long` | `getTotalProduced()` `int64 totalProduced = 5;` |
    | `java.lang.String` | `getUrl()` `string url = 4;` |
    | `com.google.protobuf.ByteString` | `getUrlBytes()` `string url = 4;` |
    | `long` | `getVoteCount()` `int64 voteCount = 2;` |

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
    - #### getVoteCount

      ```
      long getVoteCount()
      ```

      `int64 voteCount = 2;`

      Returns:
      :   The voteCount.
    - #### getPubKey

      ```
      com.google.protobuf.ByteString getPubKey()
      ```

      `bytes pubKey = 3;`

      Returns:
      :   The pubKey.
    - #### getUrl

      ```
      java.lang.String getUrl()
      ```

      `string url = 4;`

      Returns:
      :   The url.
    - #### getUrlBytes

      ```
      com.google.protobuf.ByteString getUrlBytes()
      ```

      `string url = 4;`

      Returns:
      :   The bytes for url.
    - #### getTotalProduced

      ```
      long getTotalProduced()
      ```

      `int64 totalProduced = 5;`

      Returns:
      :   The totalProduced.
    - #### getTotalMissed

      ```
      long getTotalMissed()
      ```

      `int64 totalMissed = 6;`

      Returns:
      :   The totalMissed.
    - #### getLatestBlockNum

      ```
      long getLatestBlockNum()
      ```

      `int64 latestBlockNum = 7;`

      Returns:
      :   The latestBlockNum.
    - #### getLatestSlotNum

      ```
      long getLatestSlotNum()
      ```

      `int64 latestSlotNum = 8;`

      Returns:
      :   The latestSlotNum.
    - #### getIsJobs

      ```
      boolean getIsJobs()
      ```

      `bool isJobs = 9;`

      Returns:
      :   The isJobs.