

org.tron.trident.proto

## Enum Common.SmartContract.ABI.Entry.StateMutabilityType

* java.lang.Object
* + java.lang.Enum<[Common.SmartContract.ABI.Entry.StateMutabilityType](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.StateMutabilityType.html "enum in org.tron.trident.proto")>
  + - org.tron.trident.proto.Common.SmartContract.ABI.Entry.StateMutabilityType

* All Implemented Interfaces:
  :   com.google.protobuf.Internal.EnumLite, com.google.protobuf.ProtocolMessageEnum, java.io.Serializable, java.lang.Comparable<[Common.SmartContract.ABI.Entry.StateMutabilityType](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.StateMutabilityType.html "enum in org.tron.trident.proto")>

  Enclosing class:
  :   [Common.SmartContract.ABI.Entry](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static enum Common.SmartContract.ABI.Entry.StateMutabilityType
  extends java.lang.Enum<Common.SmartContract.ABI.Entry.StateMutabilityType>
  implements com.google.protobuf.ProtocolMessageEnum
  ```

  Protobuf enum `protocol.SmartContract.ABI.Entry.StateMutabilityType`

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant and Description |
    | `Nonpayable` `Nonpayable = 3;` |
    | `Payable` `Payable = 4;` |
    | `Pure` `Pure = 1;` |
    | `UnknownMutabilityType` `UnknownMutabilityType = 0;` |
    | `UNRECOGNIZED` |
    | `View` `View = 2;` |
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `Nonpayable_VALUE` `Nonpayable = 3;` |
    | `static int` | `Payable_VALUE` `Payable = 4;` |
    | `static int` | `Pure_VALUE` `Pure = 1;` |
    | `static int` | `UnknownMutabilityType_VALUE` `UnknownMutabilityType = 0;` |
    | `static int` | `View_VALUE` `View = 2;` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `static Common.SmartContract.ABI.Entry.StateMutabilityType` | `forNumber(int value)` |
    | `static com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptorForType()` |
    | `int` | `getNumber()` |
    | `com.google.protobuf.Descriptors.EnumValueDescriptor` | `getValueDescriptor()` |
    | `static com.google.protobuf.Internal.EnumLiteMap<Common.SmartContract.ABI.Entry.StateMutabilityType>` | `internalGetValueMap()` |
    | `static Common.SmartContract.ABI.Entry.StateMutabilityType` | `valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)` |
    | `static Common.SmartContract.ABI.Entry.StateMutabilityType` | `valueOf(int value)` Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.StateMutabilityType.html#forNumber-int-) instead. |
    | `static Common.SmartContract.ABI.Entry.StateMutabilityType` | `valueOf(java.lang.String name)` Returns the enum constant of this type with the specified name. |
    | `static Common.SmartContract.ABI.Entry.StateMutabilityType[]` | `values()` Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.Enum

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.Object

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### UnknownMutabilityType

      ```
      public static final Common.SmartContract.ABI.Entry.StateMutabilityType UnknownMutabilityType
      ```

      `UnknownMutabilityType = 0;`
    - #### Pure

      ```
      public static final Common.SmartContract.ABI.Entry.StateMutabilityType Pure
      ```

      `Pure = 1;`
    - #### View

      ```
      public static final Common.SmartContract.ABI.Entry.StateMutabilityType View
      ```

      `View = 2;`
    - #### Nonpayable

      ```
      public static final Common.SmartContract.ABI.Entry.StateMutabilityType Nonpayable
      ```

      `Nonpayable = 3;`
    - #### Payable

      ```
      public static final Common.SmartContract.ABI.Entry.StateMutabilityType Payable
      ```

      `Payable = 4;`
    - #### UNRECOGNIZED

      ```
      public static final Common.SmartContract.ABI.Entry.StateMutabilityType UNRECOGNIZED
      ```
  + ### Field Detail

    - #### UnknownMutabilityType\_VALUE

      ```
      public static final int UnknownMutabilityType_VALUE
      ```

      `UnknownMutabilityType = 0;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.StateMutabilityType.UnknownMutabilityType_VALUE)
    - #### Pure\_VALUE

      ```
      public static final int Pure_VALUE
      ```

      `Pure = 1;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.StateMutabilityType.Pure_VALUE)
    - #### View\_VALUE

      ```
      public static final int View_VALUE
      ```

      `View = 2;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.StateMutabilityType.View_VALUE)
    - #### Nonpayable\_VALUE

      ```
      public static final int Nonpayable_VALUE
      ```

      `Nonpayable = 3;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.StateMutabilityType.Nonpayable_VALUE)
    - #### Payable\_VALUE

      ```
      public static final int Payable_VALUE
      ```

      `Payable = 4;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.StateMutabilityType.Payable_VALUE)
  + ### Method Detail

    - #### values

      ```
      public static Common.SmartContract.ABI.Entry.StateMutabilityType[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (Common.SmartContract.ABI.Entry.StateMutabilityType c : Common.SmartContract.ABI.Entry.StateMutabilityType.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static Common.SmartContract.ABI.Entry.StateMutabilityType valueOf(java.lang.String name)
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
      public static Common.SmartContract.ABI.Entry.StateMutabilityType valueOf(int value)
      ```

      Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.StateMutabilityType.html#forNumber-int-) instead.

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### forNumber

      ```
      public static Common.SmartContract.ABI.Entry.StateMutabilityType forNumber(int value)
      ```

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### internalGetValueMap

      ```
      public static com.google.protobuf.Internal.EnumLiteMap<Common.SmartContract.ABI.Entry.StateMutabilityType> internalGetValueMap()
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
      public static Common.SmartContract.ABI.Entry.StateMutabilityType valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)
      ```