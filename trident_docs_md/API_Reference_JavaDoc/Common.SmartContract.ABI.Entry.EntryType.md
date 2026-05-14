

org.tron.trident.proto

## Enum Common.SmartContract.ABI.Entry.EntryType

* java.lang.Object
* + java.lang.Enum<[Common.SmartContract.ABI.Entry.EntryType](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.EntryType.html "enum in org.tron.trident.proto")>
  + - org.tron.trident.proto.Common.SmartContract.ABI.Entry.EntryType

* All Implemented Interfaces:
  :   com.google.protobuf.Internal.EnumLite, com.google.protobuf.ProtocolMessageEnum, java.io.Serializable, java.lang.Comparable<[Common.SmartContract.ABI.Entry.EntryType](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.EntryType.html "enum in org.tron.trident.proto")>

  Enclosing class:
  :   [Common.SmartContract.ABI.Entry](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static enum Common.SmartContract.ABI.Entry.EntryType
  extends java.lang.Enum<Common.SmartContract.ABI.Entry.EntryType>
  implements com.google.protobuf.ProtocolMessageEnum
  ```

  Protobuf enum `protocol.SmartContract.ABI.Entry.EntryType`

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant and Description |
    | `Constructor` `Constructor = 1;` |
    | `Error` `Error = 6;` |
    | `Event` `Event = 3;` |
    | `Fallback` `Fallback = 4;` |
    | `Function` `Function = 2;` |
    | `Receive` `Receive = 5;` |
    | `UnknownEntryType` `UnknownEntryType = 0;` |
    | `UNRECOGNIZED` |
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `Constructor_VALUE` `Constructor = 1;` |
    | `static int` | `Error_VALUE` `Error = 6;` |
    | `static int` | `Event_VALUE` `Event = 3;` |
    | `static int` | `Fallback_VALUE` `Fallback = 4;` |
    | `static int` | `Function_VALUE` `Function = 2;` |
    | `static int` | `Receive_VALUE` `Receive = 5;` |
    | `static int` | `UnknownEntryType_VALUE` `UnknownEntryType = 0;` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `static Common.SmartContract.ABI.Entry.EntryType` | `forNumber(int value)` |
    | `static com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptorForType()` |
    | `int` | `getNumber()` |
    | `com.google.protobuf.Descriptors.EnumValueDescriptor` | `getValueDescriptor()` |
    | `static com.google.protobuf.Internal.EnumLiteMap<Common.SmartContract.ABI.Entry.EntryType>` | `internalGetValueMap()` |
    | `static Common.SmartContract.ABI.Entry.EntryType` | `valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)` |
    | `static Common.SmartContract.ABI.Entry.EntryType` | `valueOf(int value)` Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.EntryType.html#forNumber-int-) instead. |
    | `static Common.SmartContract.ABI.Entry.EntryType` | `valueOf(java.lang.String name)` Returns the enum constant of this type with the specified name. |
    | `static Common.SmartContract.ABI.Entry.EntryType[]` | `values()` Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.Enum

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.Object

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### UnknownEntryType

      ```
      public static final Common.SmartContract.ABI.Entry.EntryType UnknownEntryType
      ```

      `UnknownEntryType = 0;`
    - #### Constructor

      ```
      public static final Common.SmartContract.ABI.Entry.EntryType Constructor
      ```

      `Constructor = 1;`
    - #### Function

      ```
      public static final Common.SmartContract.ABI.Entry.EntryType Function
      ```

      `Function = 2;`
    - #### Event

      ```
      public static final Common.SmartContract.ABI.Entry.EntryType Event
      ```

      `Event = 3;`
    - #### Fallback

      ```
      public static final Common.SmartContract.ABI.Entry.EntryType Fallback
      ```

      `Fallback = 4;`
    - #### Receive

      ```
      public static final Common.SmartContract.ABI.Entry.EntryType Receive
      ```

      `Receive = 5;`
    - #### Error

      ```
      public static final Common.SmartContract.ABI.Entry.EntryType Error
      ```

      `Error = 6;`
    - #### UNRECOGNIZED

      ```
      public static final Common.SmartContract.ABI.Entry.EntryType UNRECOGNIZED
      ```
  + ### Field Detail

    - #### UnknownEntryType\_VALUE

      ```
      public static final int UnknownEntryType_VALUE
      ```

      `UnknownEntryType = 0;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.EntryType.UnknownEntryType_VALUE)
    - #### Constructor\_VALUE

      ```
      public static final int Constructor_VALUE
      ```

      `Constructor = 1;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.EntryType.Constructor_VALUE)
    - #### Function\_VALUE

      ```
      public static final int Function_VALUE
      ```

      `Function = 2;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.EntryType.Function_VALUE)
    - #### Event\_VALUE

      ```
      public static final int Event_VALUE
      ```

      `Event = 3;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.EntryType.Event_VALUE)
    - #### Fallback\_VALUE

      ```
      public static final int Fallback_VALUE
      ```

      `Fallback = 4;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.EntryType.Fallback_VALUE)
    - #### Receive\_VALUE

      ```
      public static final int Receive_VALUE
      ```

      `Receive = 5;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.EntryType.Receive_VALUE)
    - #### Error\_VALUE

      ```
      public static final int Error_VALUE
      ```

      `Error = 6;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Common.SmartContract.ABI.Entry.EntryType.Error_VALUE)
  + ### Method Detail

    - #### values

      ```
      public static Common.SmartContract.ABI.Entry.EntryType[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (Common.SmartContract.ABI.Entry.EntryType c : Common.SmartContract.ABI.Entry.EntryType.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static Common.SmartContract.ABI.Entry.EntryType valueOf(java.lang.String name)
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
      public static Common.SmartContract.ABI.Entry.EntryType valueOf(int value)
      ```

      Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Common.SmartContract.ABI.Entry.EntryType.html#forNumber-int-) instead.

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### forNumber

      ```
      public static Common.SmartContract.ABI.Entry.EntryType forNumber(int value)
      ```

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### internalGetValueMap

      ```
      public static com.google.protobuf.Internal.EnumLiteMap<Common.SmartContract.ABI.Entry.EntryType> internalGetValueMap()
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
      public static Common.SmartContract.ABI.Entry.EntryType valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)
      ```