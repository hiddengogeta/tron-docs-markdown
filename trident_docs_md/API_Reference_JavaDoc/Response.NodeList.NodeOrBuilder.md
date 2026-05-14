

org.tron.trident.proto

## Interface Response.NodeList.NodeOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Response.NodeList.Node](../../../../org/tron/trident/proto/Response.NodeList.Node.html "class in org.tron.trident.proto"), [Response.NodeList.Node.Builder](../../../../org/tron/trident/proto/Response.NodeList.Node.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Response.NodeList](../../../../org/tron/trident/proto/Response.NodeList.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Response.NodeList.NodeOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Response.NodeList.Node.Address` | `getAddress()` `.protocol.NodeList.Node.Address address = 1;` |
    | `Response.NodeList.Node.AddressOrBuilder` | `getAddressOrBuilder()` `.protocol.NodeList.Node.Address address = 1;` |
    | `boolean` | `hasAddress()` `.protocol.NodeList.Node.Address address = 1;` |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### hasAddress

      ```
      boolean hasAddress()
      ```

      `.protocol.NodeList.Node.Address address = 1;`

      Returns:
      :   Whether the address field is set.
    - #### getAddress

      ```
      Response.NodeList.Node.Address getAddress()
      ```

      `.protocol.NodeList.Node.Address address = 1;`

      Returns:
      :   The address.
    - #### getAddressOrBuilder

      ```
      Response.NodeList.Node.AddressOrBuilder getAddressOrBuilder()
      ```

      `.protocol.NodeList.Node.Address address = 1;`