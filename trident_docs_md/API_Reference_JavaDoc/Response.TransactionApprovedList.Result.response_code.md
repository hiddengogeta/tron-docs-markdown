

org.tron.trident.proto

## Enum Response.TransactionApprovedList.Result.response\_code

* java.lang.Object
* + java.lang.Enum<[Response.TransactionApprovedList.Result.response\_code](../../../../org/tron/trident/proto/Response.TransactionApprovedList.Result.response_code.html "enum in org.tron.trident.proto")>
  + - org.tron.trident.proto.Response.TransactionApprovedList.Result.response\_code

* All Implemented Interfaces:
  :   com.google.protobuf.Internal.EnumLite, com.google.protobuf.ProtocolMessageEnum, java.io.Serializable, java.lang.Comparable<[Response.TransactionApprovedList.Result.response\_code](../../../../org/tron/trident/proto/Response.TransactionApprovedList.Result.response_code.html "enum in org.tron.trident.proto")>

  Enclosing class:
  :   [Response.TransactionApprovedList.Result](../../../../org/tron/trident/proto/Response.TransactionApprovedList.Result.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static enum Response.TransactionApprovedList.Result.response_code
  extends java.lang.Enum<Response.TransactionApprovedList.Result.response_code>
  implements com.google.protobuf.ProtocolMessageEnum
  ```

  Protobuf enum `protocol.TransactionApprovedList.Result.response_code`

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant and Description |
    | `COMPUTE_ADDRESS_ERROR` `COMPUTE_ADDRESS_ERROR = 2;` |
    | `OTHER_ERROR` `OTHER_ERROR = 20;` |
    | `SIGNATURE_FORMAT_ERROR` `SIGNATURE_FORMAT_ERROR = 1;` |
    | `SUCCESS` `SUCCESS = 0;` |
    | `UNRECOGNIZED` |
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `COMPUTE_ADDRESS_ERROR_VALUE` `COMPUTE_ADDRESS_ERROR = 2;` |
    | `static int` | `OTHER_ERROR_VALUE` `OTHER_ERROR = 20;` |
    | `static int` | `SIGNATURE_FORMAT_ERROR_VALUE` `SIGNATURE_FORMAT_ERROR = 1;` |
    | `static int` | `SUCCESS_VALUE` `SUCCESS = 0;` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `static Response.TransactionApprovedList.Result.response_code` | `forNumber(int value)` |
    | `static com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptorForType()` |
    | `int` | `getNumber()` |
    | `com.google.protobuf.Descriptors.EnumValueDescriptor` | `getValueDescriptor()` |
    | `static com.google.protobuf.Internal.EnumLiteMap<Response.TransactionApprovedList.Result.response_code>` | `internalGetValueMap()` |
    | `static Response.TransactionApprovedList.Result.response_code` | `valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)` |
    | `static Response.TransactionApprovedList.Result.response_code` | `valueOf(int value)` Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Response.TransactionApprovedList.Result.response_code.html#forNumber-int-) instead. |
    | `static Response.TransactionApprovedList.Result.response_code` | `valueOf(java.lang.String name)` Returns the enum constant of this type with the specified name. |
    | `static Response.TransactionApprovedList.Result.response_code[]` | `values()` Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.Enum

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.Object

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### SUCCESS

      ```
      public static final Response.TransactionApprovedList.Result.response_code SUCCESS
      ```

      `SUCCESS = 0;`
    - #### SIGNATURE\_FORMAT\_ERROR

      ```
      public static final Response.TransactionApprovedList.Result.response_code SIGNATURE_FORMAT_ERROR
      ```

      `SIGNATURE_FORMAT_ERROR = 1;`
    - #### COMPUTE\_ADDRESS\_ERROR

      ```
      public static final Response.TransactionApprovedList.Result.response_code COMPUTE_ADDRESS_ERROR
      ```

      `COMPUTE_ADDRESS_ERROR = 2;`
    - #### OTHER\_ERROR

      ```
      public static final Response.TransactionApprovedList.Result.response_code OTHER_ERROR
      ```

      `OTHER_ERROR = 20;`
    - #### UNRECOGNIZED

      ```
      public static final Response.TransactionApprovedList.Result.response_code UNRECOGNIZED
      ```
  + ### Field Detail

    - #### SUCCESS\_VALUE

      ```
      public static final int SUCCESS_VALUE
      ```

      `SUCCESS = 0;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionApprovedList.Result.response_code.SUCCESS_VALUE)
    - #### SIGNATURE\_FORMAT\_ERROR\_VALUE

      ```
      public static final int SIGNATURE_FORMAT_ERROR_VALUE
      ```

      `SIGNATURE_FORMAT_ERROR = 1;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionApprovedList.Result.response_code.SIGNATURE_FORMAT_ERROR_VALUE)
    - #### COMPUTE\_ADDRESS\_ERROR\_VALUE

      ```
      public static final int COMPUTE_ADDRESS_ERROR_VALUE
      ```

      `COMPUTE_ADDRESS_ERROR = 2;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionApprovedList.Result.response_code.COMPUTE_ADDRESS_ERROR_VALUE)
    - #### OTHER\_ERROR\_VALUE

      ```
      public static final int OTHER_ERROR_VALUE
      ```

      `OTHER_ERROR = 20;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionApprovedList.Result.response_code.OTHER_ERROR_VALUE)
  + ### Method Detail

    - #### values

      ```
      public static Response.TransactionApprovedList.Result.response_code[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (Response.TransactionApprovedList.Result.response_code c : Response.TransactionApprovedList.Result.response_code.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static Response.TransactionApprovedList.Result.response_code valueOf(java.lang.String name)
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
      public static Response.TransactionApprovedList.Result.response_code valueOf(int value)
      ```

      Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Response.TransactionApprovedList.Result.response_code.html#forNumber-int-) instead.

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### forNumber

      ```
      public static Response.TransactionApprovedList.Result.response_code forNumber(int value)
      ```

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### internalGetValueMap

      ```
      public static com.google.protobuf.Internal.EnumLiteMap<Response.TransactionApprovedList.Result.response_code> internalGetValueMap()
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
      public static Response.TransactionApprovedList.Result.response_code valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)
      ```