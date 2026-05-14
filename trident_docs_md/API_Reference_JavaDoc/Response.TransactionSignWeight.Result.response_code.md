

org.tron.trident.proto

## Enum Response.TransactionSignWeight.Result.response\_code

* java.lang.Object
* + java.lang.Enum<[Response.TransactionSignWeight.Result.response\_code](../../../../org/tron/trident/proto/Response.TransactionSignWeight.Result.response_code.html "enum in org.tron.trident.proto")>
  + - org.tron.trident.proto.Response.TransactionSignWeight.Result.response\_code

* All Implemented Interfaces:
  :   com.google.protobuf.Internal.EnumLite, com.google.protobuf.ProtocolMessageEnum, java.io.Serializable, java.lang.Comparable<[Response.TransactionSignWeight.Result.response\_code](../../../../org/tron/trident/proto/Response.TransactionSignWeight.Result.response_code.html "enum in org.tron.trident.proto")>

  Enclosing class:
  :   [Response.TransactionSignWeight.Result](../../../../org/tron/trident/proto/Response.TransactionSignWeight.Result.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static enum Response.TransactionSignWeight.Result.response_code
  extends java.lang.Enum<Response.TransactionSignWeight.Result.response_code>
  implements com.google.protobuf.ProtocolMessageEnum
  ```

  Protobuf enum `protocol.TransactionSignWeight.Result.response_code`

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant and Description |
    | `COMPUTE_ADDRESS_ERROR` `COMPUTE_ADDRESS_ERROR = 3;` |
    | `ENOUGH_PERMISSION` `ENOUGH_PERMISSION = 0;` |
    | `NOT_ENOUGH_PERMISSION` error in |
    | `OTHER_ERROR` `OTHER_ERROR = 20;` |
    | `PERMISSION_ERROR` The key is not in permission |
    | `SIGNATURE_FORMAT_ERROR` `SIGNATURE_FORMAT_ERROR = 2;` |
    | `UNRECOGNIZED` |
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `COMPUTE_ADDRESS_ERROR_VALUE` `COMPUTE_ADDRESS_ERROR = 3;` |
    | `static int` | `ENOUGH_PERMISSION_VALUE` `ENOUGH_PERMISSION = 0;` |
    | `static int` | `NOT_ENOUGH_PERMISSION_VALUE` error in |
    | `static int` | `OTHER_ERROR_VALUE` `OTHER_ERROR = 20;` |
    | `static int` | `PERMISSION_ERROR_VALUE` The key is not in permission |
    | `static int` | `SIGNATURE_FORMAT_ERROR_VALUE` `SIGNATURE_FORMAT_ERROR = 2;` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `static Response.TransactionSignWeight.Result.response_code` | `forNumber(int value)` |
    | `static com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptorForType()` |
    | `int` | `getNumber()` |
    | `com.google.protobuf.Descriptors.EnumValueDescriptor` | `getValueDescriptor()` |
    | `static com.google.protobuf.Internal.EnumLiteMap<Response.TransactionSignWeight.Result.response_code>` | `internalGetValueMap()` |
    | `static Response.TransactionSignWeight.Result.response_code` | `valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)` |
    | `static Response.TransactionSignWeight.Result.response_code` | `valueOf(int value)` Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Response.TransactionSignWeight.Result.response_code.html#forNumber-int-) instead. |
    | `static Response.TransactionSignWeight.Result.response_code` | `valueOf(java.lang.String name)` Returns the enum constant of this type with the specified name. |
    | `static Response.TransactionSignWeight.Result.response_code[]` | `values()` Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.Enum

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.Object

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### ENOUGH\_PERMISSION

      ```
      public static final Response.TransactionSignWeight.Result.response_code ENOUGH_PERMISSION
      ```

      `ENOUGH_PERMISSION = 0;`
    - #### NOT\_ENOUGH\_PERMISSION

      ```
      public static final Response.TransactionSignWeight.Result.response_code NOT_ENOUGH_PERMISSION
      ```

      ```
       error in
      ```

      `NOT_ENOUGH_PERMISSION = 1;`
    - #### SIGNATURE\_FORMAT\_ERROR

      ```
      public static final Response.TransactionSignWeight.Result.response_code SIGNATURE_FORMAT_ERROR
      ```

      `SIGNATURE_FORMAT_ERROR = 2;`
    - #### COMPUTE\_ADDRESS\_ERROR

      ```
      public static final Response.TransactionSignWeight.Result.response_code COMPUTE_ADDRESS_ERROR
      ```

      `COMPUTE_ADDRESS_ERROR = 3;`
    - #### PERMISSION\_ERROR

      ```
      public static final Response.TransactionSignWeight.Result.response_code PERMISSION_ERROR
      ```

      ```
       The key is not in permission
      ```

      `PERMISSION_ERROR = 4;`
    - #### OTHER\_ERROR

      ```
      public static final Response.TransactionSignWeight.Result.response_code OTHER_ERROR
      ```

      `OTHER_ERROR = 20;`
    - #### UNRECOGNIZED

      ```
      public static final Response.TransactionSignWeight.Result.response_code UNRECOGNIZED
      ```
  + ### Field Detail

    - #### ENOUGH\_PERMISSION\_VALUE

      ```
      public static final int ENOUGH_PERMISSION_VALUE
      ```

      `ENOUGH_PERMISSION = 0;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionSignWeight.Result.response_code.ENOUGH_PERMISSION_VALUE)
    - #### NOT\_ENOUGH\_PERMISSION\_VALUE

      ```
      public static final int NOT_ENOUGH_PERMISSION_VALUE
      ```

      ```
       error in
      ```

      `NOT_ENOUGH_PERMISSION = 1;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionSignWeight.Result.response_code.NOT_ENOUGH_PERMISSION_VALUE)
    - #### SIGNATURE\_FORMAT\_ERROR\_VALUE

      ```
      public static final int SIGNATURE_FORMAT_ERROR_VALUE
      ```

      `SIGNATURE_FORMAT_ERROR = 2;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionSignWeight.Result.response_code.SIGNATURE_FORMAT_ERROR_VALUE)
    - #### COMPUTE\_ADDRESS\_ERROR\_VALUE

      ```
      public static final int COMPUTE_ADDRESS_ERROR_VALUE
      ```

      `COMPUTE_ADDRESS_ERROR = 3;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionSignWeight.Result.response_code.COMPUTE_ADDRESS_ERROR_VALUE)
    - #### PERMISSION\_ERROR\_VALUE

      ```
      public static final int PERMISSION_ERROR_VALUE
      ```

      ```
       The key is not in permission
      ```

      `PERMISSION_ERROR = 4;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionSignWeight.Result.response_code.PERMISSION_ERROR_VALUE)
    - #### OTHER\_ERROR\_VALUE

      ```
      public static final int OTHER_ERROR_VALUE
      ```

      `OTHER_ERROR = 20;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionSignWeight.Result.response_code.OTHER_ERROR_VALUE)
  + ### Method Detail

    - #### values

      ```
      public static Response.TransactionSignWeight.Result.response_code[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (Response.TransactionSignWeight.Result.response_code c : Response.TransactionSignWeight.Result.response_code.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static Response.TransactionSignWeight.Result.response_code valueOf(java.lang.String name)
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
      public static Response.TransactionSignWeight.Result.response_code valueOf(int value)
      ```

      Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Response.TransactionSignWeight.Result.response_code.html#forNumber-int-) instead.

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### forNumber

      ```
      public static Response.TransactionSignWeight.Result.response_code forNumber(int value)
      ```

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### internalGetValueMap

      ```
      public static com.google.protobuf.Internal.EnumLiteMap<Response.TransactionSignWeight.Result.response_code> internalGetValueMap()
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
      public static Response.TransactionSignWeight.Result.response_code valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)
      ```