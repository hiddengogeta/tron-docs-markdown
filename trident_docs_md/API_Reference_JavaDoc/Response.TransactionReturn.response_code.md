

org.tron.trident.proto

## Enum Response.TransactionReturn.response\_code

* java.lang.Object
* + java.lang.Enum<[Response.TransactionReturn.response\_code](../../../../org/tron/trident/proto/Response.TransactionReturn.response_code.html "enum in org.tron.trident.proto")>
  + - org.tron.trident.proto.Response.TransactionReturn.response\_code

* All Implemented Interfaces:
  :   com.google.protobuf.Internal.EnumLite, com.google.protobuf.ProtocolMessageEnum, java.io.Serializable, java.lang.Comparable<[Response.TransactionReturn.response\_code](../../../../org/tron/trident/proto/Response.TransactionReturn.response_code.html "enum in org.tron.trident.proto")>

  Enclosing class:
  :   [Response.TransactionReturn](../../../../org/tron/trident/proto/Response.TransactionReturn.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static enum Response.TransactionReturn.response_code
  extends java.lang.Enum<Response.TransactionReturn.response_code>
  implements com.google.protobuf.ProtocolMessageEnum
  ```

  Protobuf enum `protocol.TransactionReturn.response_code`

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant and Description |
    | `BANDWITH_ERROR` `BANDWITH_ERROR = 4;` |
    | `BLOCK_UNSOLIDIFIED` `BLOCK_UNSOLIDIFIED = 12;` |
    | `CONTRACT_EXE_ERROR` `CONTRACT_EXE_ERROR = 3;` |
    | `CONTRACT_VALIDATE_ERROR` `CONTRACT_VALIDATE_ERROR = 2;` |
    | `DUP_TRANSACTION_ERROR` `DUP_TRANSACTION_ERROR = 5;` |
    | `NO_CONNECTION` `NO_CONNECTION = 10;` |
    | `NOT_ENOUGH_EFFECTIVE_CONNECTION` `NOT_ENOUGH_EFFECTIVE_CONNECTION = 11;` |
    | `OTHER_ERROR` `OTHER_ERROR = 20;` |
    | `SERVER_BUSY` `SERVER_BUSY = 9;` |
    | `SIGERROR` error in signature |
    | `SUCCESS` `SUCCESS = 0;` |
    | `TAPOS_ERROR` `TAPOS_ERROR = 6;` |
    | `TOO_BIG_TRANSACTION_ERROR` `TOO_BIG_TRANSACTION_ERROR = 7;` |
    | `TRANSACTION_EXPIRATION_ERROR` `TRANSACTION_EXPIRATION_ERROR = 8;` |
    | `UNRECOGNIZED` |
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `BANDWITH_ERROR_VALUE` `BANDWITH_ERROR = 4;` |
    | `static int` | `BLOCK_UNSOLIDIFIED_VALUE` `BLOCK_UNSOLIDIFIED = 12;` |
    | `static int` | `CONTRACT_EXE_ERROR_VALUE` `CONTRACT_EXE_ERROR = 3;` |
    | `static int` | `CONTRACT_VALIDATE_ERROR_VALUE` `CONTRACT_VALIDATE_ERROR = 2;` |
    | `static int` | `DUP_TRANSACTION_ERROR_VALUE` `DUP_TRANSACTION_ERROR = 5;` |
    | `static int` | `NO_CONNECTION_VALUE` `NO_CONNECTION = 10;` |
    | `static int` | `NOT_ENOUGH_EFFECTIVE_CONNECTION_VALUE` `NOT_ENOUGH_EFFECTIVE_CONNECTION = 11;` |
    | `static int` | `OTHER_ERROR_VALUE` `OTHER_ERROR = 20;` |
    | `static int` | `SERVER_BUSY_VALUE` `SERVER_BUSY = 9;` |
    | `static int` | `SIGERROR_VALUE` error in signature |
    | `static int` | `SUCCESS_VALUE` `SUCCESS = 0;` |
    | `static int` | `TAPOS_ERROR_VALUE` `TAPOS_ERROR = 6;` |
    | `static int` | `TOO_BIG_TRANSACTION_ERROR_VALUE` `TOO_BIG_TRANSACTION_ERROR = 7;` |
    | `static int` | `TRANSACTION_EXPIRATION_ERROR_VALUE` `TRANSACTION_EXPIRATION_ERROR = 8;` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `static Response.TransactionReturn.response_code` | `forNumber(int value)` |
    | `static com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptorForType()` |
    | `int` | `getNumber()` |
    | `com.google.protobuf.Descriptors.EnumValueDescriptor` | `getValueDescriptor()` |
    | `static com.google.protobuf.Internal.EnumLiteMap<Response.TransactionReturn.response_code>` | `internalGetValueMap()` |
    | `static Response.TransactionReturn.response_code` | `valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)` |
    | `static Response.TransactionReturn.response_code` | `valueOf(int value)` Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Response.TransactionReturn.response_code.html#forNumber-int-) instead. |
    | `static Response.TransactionReturn.response_code` | `valueOf(java.lang.String name)` Returns the enum constant of this type with the specified name. |
    | `static Response.TransactionReturn.response_code[]` | `values()` Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.Enum

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.Object

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### SUCCESS

      ```
      public static final Response.TransactionReturn.response_code SUCCESS
      ```

      `SUCCESS = 0;`
    - #### SIGERROR

      ```
      public static final Response.TransactionReturn.response_code SIGERROR
      ```

      ```
       error in signature
      ```

      `SIGERROR = 1;`
    - #### CONTRACT\_VALIDATE\_ERROR

      ```
      public static final Response.TransactionReturn.response_code CONTRACT_VALIDATE_ERROR
      ```

      `CONTRACT_VALIDATE_ERROR = 2;`
    - #### CONTRACT\_EXE\_ERROR

      ```
      public static final Response.TransactionReturn.response_code CONTRACT_EXE_ERROR
      ```

      `CONTRACT_EXE_ERROR = 3;`
    - #### BANDWITH\_ERROR

      ```
      public static final Response.TransactionReturn.response_code BANDWITH_ERROR
      ```

      `BANDWITH_ERROR = 4;`
    - #### DUP\_TRANSACTION\_ERROR

      ```
      public static final Response.TransactionReturn.response_code DUP_TRANSACTION_ERROR
      ```

      `DUP_TRANSACTION_ERROR = 5;`
    - #### TAPOS\_ERROR

      ```
      public static final Response.TransactionReturn.response_code TAPOS_ERROR
      ```

      `TAPOS_ERROR = 6;`
    - #### TOO\_BIG\_TRANSACTION\_ERROR

      ```
      public static final Response.TransactionReturn.response_code TOO_BIG_TRANSACTION_ERROR
      ```

      `TOO_BIG_TRANSACTION_ERROR = 7;`
    - #### TRANSACTION\_EXPIRATION\_ERROR

      ```
      public static final Response.TransactionReturn.response_code TRANSACTION_EXPIRATION_ERROR
      ```

      `TRANSACTION_EXPIRATION_ERROR = 8;`
    - #### SERVER\_BUSY

      ```
      public static final Response.TransactionReturn.response_code SERVER_BUSY
      ```

      `SERVER_BUSY = 9;`
    - #### NO\_CONNECTION

      ```
      public static final Response.TransactionReturn.response_code NO_CONNECTION
      ```

      `NO_CONNECTION = 10;`
    - #### NOT\_ENOUGH\_EFFECTIVE\_CONNECTION

      ```
      public static final Response.TransactionReturn.response_code NOT_ENOUGH_EFFECTIVE_CONNECTION
      ```

      `NOT_ENOUGH_EFFECTIVE_CONNECTION = 11;`
    - #### BLOCK\_UNSOLIDIFIED

      ```
      public static final Response.TransactionReturn.response_code BLOCK_UNSOLIDIFIED
      ```

      `BLOCK_UNSOLIDIFIED = 12;`
    - #### OTHER\_ERROR

      ```
      public static final Response.TransactionReturn.response_code OTHER_ERROR
      ```

      `OTHER_ERROR = 20;`
    - #### UNRECOGNIZED

      ```
      public static final Response.TransactionReturn.response_code UNRECOGNIZED
      ```
  + ### Field Detail

    - #### SUCCESS\_VALUE

      ```
      public static final int SUCCESS_VALUE
      ```

      `SUCCESS = 0;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionReturn.response_code.SUCCESS_VALUE)
    - #### SIGERROR\_VALUE

      ```
      public static final int SIGERROR_VALUE
      ```

      ```
       error in signature
      ```

      `SIGERROR = 1;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionReturn.response_code.SIGERROR_VALUE)
    - #### CONTRACT\_VALIDATE\_ERROR\_VALUE

      ```
      public static final int CONTRACT_VALIDATE_ERROR_VALUE
      ```

      `CONTRACT_VALIDATE_ERROR = 2;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionReturn.response_code.CONTRACT_VALIDATE_ERROR_VALUE)
    - #### CONTRACT\_EXE\_ERROR\_VALUE

      ```
      public static final int CONTRACT_EXE_ERROR_VALUE
      ```

      `CONTRACT_EXE_ERROR = 3;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionReturn.response_code.CONTRACT_EXE_ERROR_VALUE)
    - #### BANDWITH\_ERROR\_VALUE

      ```
      public static final int BANDWITH_ERROR_VALUE
      ```

      `BANDWITH_ERROR = 4;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionReturn.response_code.BANDWITH_ERROR_VALUE)
    - #### DUP\_TRANSACTION\_ERROR\_VALUE

      ```
      public static final int DUP_TRANSACTION_ERROR_VALUE
      ```

      `DUP_TRANSACTION_ERROR = 5;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionReturn.response_code.DUP_TRANSACTION_ERROR_VALUE)
    - #### TAPOS\_ERROR\_VALUE

      ```
      public static final int TAPOS_ERROR_VALUE
      ```

      `TAPOS_ERROR = 6;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionReturn.response_code.TAPOS_ERROR_VALUE)
    - #### TOO\_BIG\_TRANSACTION\_ERROR\_VALUE

      ```
      public static final int TOO_BIG_TRANSACTION_ERROR_VALUE
      ```

      `TOO_BIG_TRANSACTION_ERROR = 7;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionReturn.response_code.TOO_BIG_TRANSACTION_ERROR_VALUE)
    - #### TRANSACTION\_EXPIRATION\_ERROR\_VALUE

      ```
      public static final int TRANSACTION_EXPIRATION_ERROR_VALUE
      ```

      `TRANSACTION_EXPIRATION_ERROR = 8;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionReturn.response_code.TRANSACTION_EXPIRATION_ERROR_VALUE)
    - #### SERVER\_BUSY\_VALUE

      ```
      public static final int SERVER_BUSY_VALUE
      ```

      `SERVER_BUSY = 9;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionReturn.response_code.SERVER_BUSY_VALUE)
    - #### NO\_CONNECTION\_VALUE

      ```
      public static final int NO_CONNECTION_VALUE
      ```

      `NO_CONNECTION = 10;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionReturn.response_code.NO_CONNECTION_VALUE)
    - #### NOT\_ENOUGH\_EFFECTIVE\_CONNECTION\_VALUE

      ```
      public static final int NOT_ENOUGH_EFFECTIVE_CONNECTION_VALUE
      ```

      `NOT_ENOUGH_EFFECTIVE_CONNECTION = 11;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionReturn.response_code.NOT_ENOUGH_EFFECTIVE_CONNECTION_VALUE)
    - #### BLOCK\_UNSOLIDIFIED\_VALUE

      ```
      public static final int BLOCK_UNSOLIDIFIED_VALUE
      ```

      `BLOCK_UNSOLIDIFIED = 12;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionReturn.response_code.BLOCK_UNSOLIDIFIED_VALUE)
    - #### OTHER\_ERROR\_VALUE

      ```
      public static final int OTHER_ERROR_VALUE
      ```

      `OTHER_ERROR = 20;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.TransactionReturn.response_code.OTHER_ERROR_VALUE)
  + ### Method Detail

    - #### values

      ```
      public static Response.TransactionReturn.response_code[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (Response.TransactionReturn.response_code c : Response.TransactionReturn.response_code.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static Response.TransactionReturn.response_code valueOf(java.lang.String name)
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
      public static Response.TransactionReturn.response_code valueOf(int value)
      ```

      Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Response.TransactionReturn.response_code.html#forNumber-int-) instead.

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### forNumber

      ```
      public static Response.TransactionReturn.response_code forNumber(int value)
      ```

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### internalGetValueMap

      ```
      public static com.google.protobuf.Internal.EnumLiteMap<Response.TransactionReturn.response_code> internalGetValueMap()
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
      public static Response.TransactionReturn.response_code valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)
      ```