

org.tron.trident.proto

## Interface Response.WitnessListOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.WitnessList](../../../../org/tron/trident/proto/Response.WitnessList.html "class in org.tron.trident.proto"), [Response.WitnessList.Builder](../../../../org/tron/trident/proto/Response.WitnessList.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.WitnessListOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Response.Witness` | `getWitnesses(int index)` `repeated .protocol.Witness witnesses = 1;` |
    | `int` | `getWitnessesCount()` `repeated .protocol.Witness witnesses = 1;` |
    | `java.util.List<Response.Witness>` | `getWitnessesList()` `repeated .protocol.Witness witnesses = 1;` |
    | `Response.WitnessOrBuilder` | `getWitnessesOrBuilder(int index)` `repeated .protocol.Witness witnesses = 1;` |
    | `java.util.List<? extends Response.WitnessOrBuilder>` | `getWitnessesOrBuilderList()` `repeated .protocol.Witness witnesses = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getWitnessesList

      ```
      java.util.List<Response.Witness> getWitnessesList()
      ```

      `repeated .protocol.Witness witnesses = 1;`
    - #### getWitnesses

      ```
      Response.Witness getWitnesses(int index)
      ```

      `repeated .protocol.Witness witnesses = 1;`
    - #### getWitnessesCount

      ```
      int getWitnessesCount()
      ```

      `repeated .protocol.Witness witnesses = 1;`
    - #### getWitnessesOrBuilderList

      ```
      java.util.List<? extends Response.WitnessOrBuilder> getWitnessesOrBuilderList()
      ```

      `repeated .protocol.Witness witnesses = 1;`
    - #### getWitnessesOrBuilder

      ```
      Response.WitnessOrBuilder getWitnessesOrBuilder(int index)
      ```

      `repeated .protocol.Witness witnesses = 1;`