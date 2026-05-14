

org.tron.trident.proto

## Enum Response.TransactionInfo.code

* java.lang.Object
* + java.lang.Enum<[Response.TransactionInfo.code](../../../../org/tron/trident/proto/Response.TransactionInfo.code.html "enum in org.tron.trident.proto")>
  + - org.tron.trident.proto.Response.TransactionInfo.code

* All Implemented Interfaces:
  :   com.google.protobuf.Internal.EnumLite, com.google.protobuf.ProtocolMessageEnum, java.io.Serializable, java.lang.Comparable<[Response.TransactionInfo.code](../../../../org/tron/trident/proto/Response.TransactionInfo.code.html "enum in org.tron.trident.proto")>

  Enclosing class:
  :   [Response.TransactionInfo](../../../../org/tron/trident/proto/Response.TransactionInfo.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static enum Response.TransactionInfo.code
  extends java.lang.Enum<Response.TransactionInfo.code>
  implements com.google.protobuf.ProtocolMessageEnum
  ```

  Protobuf enum `protocol.TransactionInfo.code`

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant and Description |
    | `FAILED` `FAILED = 1;` |
    | `SUCESS` `SUCESS = 0;` |
    | `UNRECOGNIZED` |
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `FAILED_VALUE` `FAILED = 1;` |
    | `static int` | `SUCESS_VALUE` `SUCESS = 0;` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `static Response.TransactionInfo.code` | `forNumber(int value)` |
    | `static com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptorForType()` |
    | `int` | `getNumber()` |
    | `com.google.protobuf.Descriptors.EnumValueDescriptor` | `getValueDescriptor()` |
    | `static com.google.protobuf.Internal.EnumLiteMap<Response.TransactionInfo.code>` | `internalGetValueMap()` |
    | `static Response.TransactionInfo.code` | `valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)` |
    | `static Response.TransactionInfo.code` | `valueOf(int value)` Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Response.TransactionInfo.code.html#forNumber-int-) instead. |
    | `static Response.TransactionInfo.code` | `valueOf(java.lang.String name)` Returns the enum constant of this type with the specified name. |
    | `static Response.TransactionInfo.code[]` | `values()` Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.Enum

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.Object

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### SUCESS

      ```
      public static final Response.TransactionInfo.code SUCESS
      ```

      `SUCESS = 0;`
    - #### FAILED

      ```
      public static final Response.TransactionInfo.code FAILED
      ```

      `FAILED = 1;`
    - #### UNRECOGNIZED

      ```
      public static final Response.TransactionInfo.code UNRECOGNIZED
      ```
  + ### Field Detail

    - #### SUCESS\_VALUE

      ```
      public static final int SUCESS_VALUE
      ```

      `SUCESS = 0;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.code.SUCESS_VALUE)
    - #### FAILED\_VALUE

      ```
      public static final int FAILED_VALUE
      ```

      `FAILED = 1;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionInfo.code.FAILED_VALUE)
  + ### Method Detail

    - #### values

      ```
      public static Response.TransactionInfo.code[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (Response.TransactionInfo.code c : Response.TransactionInfo.code.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static Response.TransactionInfo.code valueOf(java.lang.String name)
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
      public static Response.TransactionInfo.code valueOf(int value)
      ```

      Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Response.TransactionInfo.code.html#forNumber-int-) instead.

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### forNumber

      ```
      public static Response.TransactionInfo.code forNumber(int value)
      ```

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### internalGetValueMap

      ```
      public static com.google.protobuf.Internal.EnumLiteMap<Response.TransactionInfo.code> internalGetValueMap()
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
      public static Response.TransactionInfo.code valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)
      ```