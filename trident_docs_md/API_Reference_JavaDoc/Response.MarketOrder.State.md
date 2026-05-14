

org.tron.trident.proto

## Enum Response.MarketOrder.State

* java.lang.Object
* + java.lang.Enum<[Response.MarketOrder.State](../../../../org/tron/trident/proto/Response.MarketOrder.State.html "enum in org.tron.trident.proto")>
  + - org.tron.trident.proto.Response.MarketOrder.State

* All Implemented Interfaces:
  :   com.google.protobuf.Internal.EnumLite, com.google.protobuf.ProtocolMessageEnum, java.io.Serializable, java.lang.Comparable<[Response.MarketOrder.State](../../../../org/tron/trident/proto/Response.MarketOrder.State.html "enum in org.tron.trident.proto")>

  Enclosing class:
  :   [Response.MarketOrder](../../../../org/tron/trident/proto/Response.MarketOrder.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static enum Response.MarketOrder.State
  extends java.lang.Enum<Response.MarketOrder.State>
  implements com.google.protobuf.ProtocolMessageEnum
  ```

  Protobuf enum `protocol.MarketOrder.State`

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant and Description |
    | `ACTIVE` `ACTIVE = 0;` |
    | `CANCELED` `CANCELED = 2;` |
    | `INACTIVE` `INACTIVE = 1;` |
    | `UNRECOGNIZED` |
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `ACTIVE_VALUE` `ACTIVE = 0;` |
    | `static int` | `CANCELED_VALUE` `CANCELED = 2;` |
    | `static int` | `INACTIVE_VALUE` `INACTIVE = 1;` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `static Response.MarketOrder.State` | `forNumber(int value)` |
    | `static com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptorForType()` |
    | `int` | `getNumber()` |
    | `com.google.protobuf.Descriptors.EnumValueDescriptor` | `getValueDescriptor()` |
    | `static com.google.protobuf.Internal.EnumLiteMap<Response.MarketOrder.State>` | `internalGetValueMap()` |
    | `static Response.MarketOrder.State` | `valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)` |
    | `static Response.MarketOrder.State` | `valueOf(int value)` Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Response.MarketOrder.State.html#forNumber-int-) instead. |
    | `static Response.MarketOrder.State` | `valueOf(java.lang.String name)` Returns the enum constant of this type with the specified name. |
    | `static Response.MarketOrder.State[]` | `values()` Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.Enum

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.Object

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### ACTIVE

      ```
      public static final Response.MarketOrder.State ACTIVE
      ```

      `ACTIVE = 0;`
    - #### INACTIVE

      ```
      public static final Response.MarketOrder.State INACTIVE
      ```

      `INACTIVE = 1;`
    - #### CANCELED

      ```
      public static final Response.MarketOrder.State CANCELED
      ```

      `CANCELED = 2;`
    - #### UNRECOGNIZED

      ```
      public static final Response.MarketOrder.State UNRECOGNIZED
      ```
  + ### Field Detail

    - #### ACTIVE\_VALUE

      ```
      public static final int ACTIVE_VALUE
      ```

      `ACTIVE = 0;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.MarketOrder.State.ACTIVE_VALUE)
    - #### INACTIVE\_VALUE

      ```
      public static final int INACTIVE_VALUE
      ```

      `INACTIVE = 1;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.MarketOrder.State.INACTIVE_VALUE)
    - #### CANCELED\_VALUE

      ```
      public static final int CANCELED_VALUE
      ```

      `CANCELED = 2;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.MarketOrder.State.CANCELED_VALUE)
  + ### Method Detail

    - #### values

      ```
      public static Response.MarketOrder.State[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (Response.MarketOrder.State c : Response.MarketOrder.State.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static Response.MarketOrder.State valueOf(java.lang.String name)
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
      public static Response.MarketOrder.State valueOf(int value)
      ```

      Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Response.MarketOrder.State.html#forNumber-int-) instead.

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### forNumber

      ```
      public static Response.MarketOrder.State forNumber(int value)
      ```

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### internalGetValueMap

      ```
      public static com.google.protobuf.Internal.EnumLiteMap<Response.MarketOrder.State> internalGetValueMap()
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
      public static Response.MarketOrder.State valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)
      ```