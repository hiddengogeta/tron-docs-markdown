

org.tron.trident.proto

## Interface Contract.AccountPermissionUpdateContractOrBuilder

* All Superinterfaces:
  :   com.google.protobuf.MessageLiteOrBuilder, com.google.protobuf.MessageOrBuilder

  All Known Implementing Classes:
  :   [Contract.AccountPermissionUpdateContract](../../../../org/tron/trident/proto/Contract.AccountPermissionUpdateContract.html "class in org.tron.trident.proto"), [Contract.AccountPermissionUpdateContract.Builder](../../../../org/tron/trident/proto/Contract.AccountPermissionUpdateContract.Builder.html "class in org.tron.trident.proto")

  Enclosing class:
  :   [Contract](../../../../org/tron/trident/proto/Contract.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static interface Contract.AccountPermissionUpdateContractOrBuilder
  extends com.google.protobuf.MessageOrBuilder
  ```

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method and Description |
    | `Common.Permission` | `getActives(int index)` Empty is invalidate |
    | `int` | `getActivesCount()` Empty is invalidate |
    | `java.util.List<Common.Permission>` | `getActivesList()` Empty is invalidate |
    | `Common.PermissionOrBuilder` | `getActivesOrBuilder(int index)` Empty is invalidate |
    | `java.util.List<? extends Common.PermissionOrBuilder>` | `getActivesOrBuilderList()` Empty is invalidate |
    | `Common.Permission` | `getOwner()` Empty is invalidate |
    | `com.google.protobuf.ByteString` | `getOwnerAddress()` `bytes owner_address = 1;` |
    | `Common.PermissionOrBuilder` | `getOwnerOrBuilder()` Empty is invalidate |
    | `Common.Permission` | `getWitness()` Can be empty |
    | `Common.PermissionOrBuilder` | `getWitnessOrBuilder()` Can be empty |
    | `boolean` | `hasOwner()` Empty is invalidate |
    | `boolean` | `hasWitness()` Can be empty |

    - ### Methods inherited from interface com.google.protobuf.MessageOrBuilder

      `findInitializationErrors, getAllFields, getDefaultInstanceForType, getDescriptorForType, getField, getInitializationErrorString, getOneofFieldDescriptor, getRepeatedField, getRepeatedFieldCount, getUnknownFields, hasField, hasOneof`
    - ### Methods inherited from interface com.google.protobuf.MessageLiteOrBuilder

      `isInitialized`

* + ### Method Detail

    - #### getOwnerAddress

      ```
      com.google.protobuf.ByteString getOwnerAddress()
      ```

      `bytes owner_address = 1;`

      Returns:
      :   The ownerAddress.
    - #### hasOwner

      ```
      boolean hasOwner()
      ```

      ```
       Empty is invalidate
      ```

      `.protocol.Permission owner = 2;`

      Returns:
      :   Whether the owner field is set.
    - #### getOwner

      ```
      Common.Permission getOwner()
      ```

      ```
       Empty is invalidate
      ```

      `.protocol.Permission owner = 2;`

      Returns:
      :   The owner.
    - #### getOwnerOrBuilder

      ```
      Common.PermissionOrBuilder getOwnerOrBuilder()
      ```

      ```
       Empty is invalidate
      ```

      `.protocol.Permission owner = 2;`
    - #### hasWitness

      ```
      boolean hasWitness()
      ```

      ```
       Can be empty
      ```

      `.protocol.Permission witness = 3;`

      Returns:
      :   Whether the witness field is set.
    - #### getWitness

      ```
      Common.Permission getWitness()
      ```

      ```
       Can be empty
      ```

      `.protocol.Permission witness = 3;`

      Returns:
      :   The witness.
    - #### getWitnessOrBuilder

      ```
      Common.PermissionOrBuilder getWitnessOrBuilder()
      ```

      ```
       Can be empty
      ```

      `.protocol.Permission witness = 3;`
    - #### getActivesList

      ```
      java.util.List<Common.Permission> getActivesList()
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`
    - #### getActives

      ```
      Common.Permission getActives(int index)
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`
    - #### getActivesCount

      ```
      int getActivesCount()
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`
    - #### getActivesOrBuilderList

      ```
      java.util.List<? extends Common.PermissionOrBuilder> getActivesOrBuilderList()
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`
    - #### getActivesOrBuilder

      ```
      Common.PermissionOrBuilder getActivesOrBuilder(int index)
      ```

      ```
       Empty is invalidate
      ```

      `repeated .protocol.Permission actives = 4;`