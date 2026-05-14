

org.tron.trident.proto

## Interface Response.ChainParametersOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.ChainParameters](../../../../org/tron/trident/proto/Response.ChainParameters.html "class in org.tron.trident.proto"), [Response.ChainParameters.Builder](../../../../org/tron/trident/proto/Response.ChainParameters.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response](../../../../org/tron/trident/proto/Response.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.ChainParametersOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Response.ChainParameters.ChainParameter` | `getChainParameter(int index)` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `int` | `getChainParameterCount()` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `java.util.List<Response.ChainParameters.ChainParameter>` | `getChainParameterList()` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `Response.ChainParameters.ChainParameterOrBuilder` | `getChainParameterOrBuilder(int index)` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |
    | `java.util.List<? extends Response.ChainParameters.ChainParameterOrBuilder>` | `getChainParameterOrBuilderList()` `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getChainParameterList

      ```
      java.util.List<Response.ChainParameters.ChainParameter> getChainParameterList()
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`
    - #### getChainParameter

      ```
      Response.ChainParameters.ChainParameter getChainParameter(int index)
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`
    - #### getChainParameterCount

      ```
      int getChainParameterCount()
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`
    - #### getChainParameterOrBuilderList

      ```
      java.util.List<? extends Response.ChainParameters.ChainParameterOrBuilder> getChainParameterOrBuilderList()
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`
    - #### getChainParameterOrBuilder

      ```
      Response.ChainParameters.ChainParameterOrBuilder getChainParameterOrBuilder(int index)
      ```

      `repeated .protocol.ChainParameters.ChainParameter chainParameter = 1;`