

org.tron.trident.proto

## Enum Common.Permission.PermissionType

* java.lang.Object
* + java.lang.Enum<[Common.Permission.PermissionType](../../../../org/tron/trident/proto/Common.Permission.PermissionType.html "enum in org.tron.trident.proto")>
  + - org.tron.trident.proto.Common.Permission.PermissionType

* All Implemented Interfaces:
  :   com.google.protobuf.Internal.EnumLite, com.google.protobuf.ProtocolMessageEnum, java.io.Serializable, java.lang.Comparable<[Common.Permission.PermissionType](../../../../org/tron/trident/proto/Common.Permission.PermissionType.html "enum in org.tron.trident.proto")>

  Enclosing class:
  :   [Common.Permission](../../../../org/tron/trident/proto/Common.Permission.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static enum Common.Permission.PermissionType
  extends java.lang.Enum<Common.Permission.PermissionType>
  implements com.google.protobuf.ProtocolMessageEnum
  ```

  Protobuf enum `protocol.Permission.PermissionType`

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant and Description |
    | `Active` `Active = 2;` |
    | `Owner` `Owner = 0;` |
    | `UNRECOGNIZED` |
    | `Witness` `Witness = 1;` |
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `Active_VALUE` `Active = 2;` |
    | `static int` | `Owner_VALUE` `Owner = 0;` |
    | `static int` | `Witness_VALUE` `Witness = 1;` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `static Common.Permission.PermissionType` | `forNumber(int value)` |
    | `static com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptorForType()` |
    | `int` | `getNumber()` |
    | `com.google.protobuf.Descriptors.EnumValueDescriptor` | `getValueDescriptor()` |
    | `static com.google.protobuf.Internal.EnumLiteMap<Common.Permission.PermissionType>` | `internalGetValueMap()` |
    | `static Common.Permission.PermissionType` | `valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)` |
    | `static Common.Permission.PermissionType` | `valueOf(int value)` Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Common.Permission.PermissionType.html#forNumber-int-) instead. |
    | `static Common.Permission.PermissionType` | `valueOf(java.lang.String name)` Returns the enum constant of this type with the specified name. |
    | `static Common.Permission.PermissionType[]` | `values()` Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.Enum

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.Object

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### Owner

      ```
      public static final Common.Permission.PermissionType Owner
      ```

      `Owner = 0;`
    - #### Witness

      ```
      public static final Common.Permission.PermissionType Witness
      ```

      `Witness = 1;`
    - #### Active

      ```
      public static final Common.Permission.PermissionType Active
      ```

      `Active = 2;`
    - #### UNRECOGNIZED

      ```
      public static final Common.Permission.PermissionType UNRECOGNIZED
      ```
  + ### Field Detail

    - #### Owner\_VALUE

      ```
      public static final int Owner_VALUE
      ```

      `Owner = 0;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.Permission.PermissionType.Owner_VALUE)
    - #### Witness\_VALUE

      ```
      public static final int Witness_VALUE
      ```

      `Witness = 1;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.Permission.PermissionType.Witness_VALUE)
    - #### Active\_VALUE

      ```
      public static final int Active_VALUE
      ```

      `Active = 2;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.Permission.PermissionType.Active_VALUE)
  + ### Method Detail

    - #### values

      ```
      public static Common.Permission.PermissionType[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (Common.Permission.PermissionType c : Common.Permission.PermissionType.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static Common.Permission.PermissionType valueOf(java.lang.String name)
      ```

      Returns the enum constant of this type with the specified name.
      The string must match *exactly* an identifier used to declare an
      enum constant in this type. (Extraneous whitespace characters are
      not permitted.)

      Parameters:
      :   `name` - the name of the enum constant to be returned.

      Returns:
      :   the enum constant with the specified name

      Throws:
      :   `java.lang.IllegalArgumentException` - if this enum type has no constant with the specified name
      :   `java.lang.NullPointerException` - if the argument is null
    - #### getNumber

      ```
      public final int getNumber()
      ```

      Specified by:
      :   `getNumber` in interface `com.google.protobuf.Internal.EnumLite`

      Specified by:
      :   `getNumber` in interface `com.google.protobuf.ProtocolMessageEnum`
    - #### valueOf

      ```
      @Deprecated
      public static Common.Permission.PermissionType valueOf(int value)
      ```

      Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Common.Permission.PermissionType.html#forNumber-int-) instead.

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### forNumber

      ```
      public static Common.Permission.PermissionType forNumber(int value)
      ```

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### internalGetValueMap

      ```
      public static com.google.protobuf.Internal.EnumLiteMap<Common.Permission.PermissionType> internalGetValueMap()
      ```
    - #### getValueDescriptor

      ```
      public final com.google.protobuf.Descriptors.EnumValueDescriptor getValueDescriptor()
      ```

      Specified by:
      :   `getValueDescriptor` in interface `com.google.protobuf.ProtocolMessageEnum`
    - #### getDescriptorForType

      ```
      public final com.google.protobuf.Descriptors.EnumDescriptor getDescriptorForType()
      ```

      Specified by:
      :   `getDescriptorForType` in interface `com.google.protobuf.ProtocolMessageEnum`
    - #### getDescriptor

      ```
      public static final com.google.protobuf.Descriptors.EnumDescriptor getDescriptor()
      ```
    - #### valueOf

      ```
      public static Common.Permission.PermissionType valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)
      ```