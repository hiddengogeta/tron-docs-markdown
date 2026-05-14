

org.tron.trident.proto

## Enum Chain.Transaction.Result.contractResult

* java.lang.Object
* + java.lang.Enum<[Chain.Transaction.Result.contractResult](../../../../org/tron/trident/proto/Chain.Transaction.Result.contractResult.html "enum in org.tron.trident.proto")>
  + - org.tron.trident.proto.Chain.Transaction.Result.contractResult

* All Implemented Interfaces:
  :   com.google.protobuf.Internal.EnumLite, com.google.protobuf.ProtocolMessageEnum, java.io.Serializable, java.lang.Comparable<[Chain.Transaction.Result.contractResult](../../../../org/tron/trident/proto/Chain.Transaction.Result.contractResult.html "enum in org.tron.trident.proto")>

  Enclosing class:
  :   [Chain.Transaction.Result](../../../../org/tron/trident/proto/Chain.Transaction.Result.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static enum Chain.Transaction.Result.contractResult
  extends java.lang.Enum<Chain.Transaction.Result.contractResult>
  implements com.google.protobuf.ProtocolMessageEnum
  ```

  Protobuf enum `protocol.Transaction.Result.contractResult`

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant and Description |
    | `BAD_JUMP_DESTINATION` `BAD_JUMP_DESTINATION = 3;` |
    | `DEFAULT` `DEFAULT = 0;` |
    | `ILLEGAL_OPERATION` `ILLEGAL_OPERATION = 8;` |
    | `INVALID_CODE` `INVALID_CODE = 15;` |
    | `JVM_STACK_OVER_FLOW` `JVM_STACK_OVER_FLOW = 12;` |
    | `OUT_OF_ENERGY` `OUT_OF_ENERGY = 10;` |
    | `OUT_OF_MEMORY` `OUT_OF_MEMORY = 4;` |
    | `OUT_OF_TIME` `OUT_OF_TIME = 11;` |
    | `PRECOMPILED_CONTRACT` `PRECOMPILED_CONTRACT = 5;` |
    | `REVERT` `REVERT = 2;` |
    | `STACK_OVERFLOW` `STACK_OVERFLOW = 9;` |
    | `STACK_TOO_LARGE` `STACK_TOO_LARGE = 7;` |
    | `STACK_TOO_SMALL` `STACK_TOO_SMALL = 6;` |
    | `SUCCESS` `SUCCESS = 1;` |
    | `TRANSFER_FAILED` `TRANSFER_FAILED = 14;` |
    | `UNKNOWN` `UNKNOWN = 13;` |
    | `UNRECOGNIZED` |
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `BAD_JUMP_DESTINATION_VALUE` `BAD_JUMP_DESTINATION = 3;` |
    | `static int` | `DEFAULT_VALUE` `DEFAULT = 0;` |
    | `static int` | `ILLEGAL_OPERATION_VALUE` `ILLEGAL_OPERATION = 8;` |
    | `static int` | `INVALID_CODE_VALUE` `INVALID_CODE = 15;` |
    | `static int` | `JVM_STACK_OVER_FLOW_VALUE` `JVM_STACK_OVER_FLOW = 12;` |
    | `static int` | `OUT_OF_ENERGY_VALUE` `OUT_OF_ENERGY = 10;` |
    | `static int` | `OUT_OF_MEMORY_VALUE` `OUT_OF_MEMORY = 4;` |
    | `static int` | `OUT_OF_TIME_VALUE` `OUT_OF_TIME = 11;` |
    | `static int` | `PRECOMPILED_CONTRACT_VALUE` `PRECOMPILED_CONTRACT = 5;` |
    | `static int` | `REVERT_VALUE` `REVERT = 2;` |
    | `static int` | `STACK_OVERFLOW_VALUE` `STACK_OVERFLOW = 9;` |
    | `static int` | `STACK_TOO_LARGE_VALUE` `STACK_TOO_LARGE = 7;` |
    | `static int` | `STACK_TOO_SMALL_VALUE` `STACK_TOO_SMALL = 6;` |
    | `static int` | `SUCCESS_VALUE` `SUCCESS = 1;` |
    | `static int` | `TRANSFER_FAILED_VALUE` `TRANSFER_FAILED = 14;` |
    | `static int` | `UNKNOWN_VALUE` `UNKNOWN = 13;` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `static Chain.Transaction.Result.contractResult` | `forNumber(int value)` |
    | `static com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptorForType()` |
    | `int` | `getNumber()` |
    | `com.google.protobuf.Descriptors.EnumValueDescriptor` | `getValueDescriptor()` |
    | `static com.google.protobuf.Internal.EnumLiteMap<Chain.Transaction.Result.contractResult>` | `internalGetValueMap()` |
    | `static Chain.Transaction.Result.contractResult` | `valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)` |
    | `static Chain.Transaction.Result.contractResult` | `valueOf(int value)` Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Chain.Transaction.Result.contractResult.html#forNumber-int-) instead. |
    | `static Chain.Transaction.Result.contractResult` | `valueOf(java.lang.String name)` Returns the enum constant of this type with the specified name. |
    | `static Chain.Transaction.Result.contractResult[]` | `values()` Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.Enum

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.Object

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### DEFAULT

      ```
      public static final Chain.Transaction.Result.contractResult DEFAULT
      ```

      `DEFAULT = 0;`
    - #### SUCCESS

      ```
      public static final Chain.Transaction.Result.contractResult SUCCESS
      ```

      `SUCCESS = 1;`
    - #### REVERT

      ```
      public static final Chain.Transaction.Result.contractResult REVERT
      ```

      `REVERT = 2;`
    - #### BAD\_JUMP\_DESTINATION

      ```
      public static final Chain.Transaction.Result.contractResult BAD_JUMP_DESTINATION
      ```

      `BAD_JUMP_DESTINATION = 3;`
    - #### OUT\_OF\_MEMORY

      ```
      public static final Chain.Transaction.Result.contractResult OUT_OF_MEMORY
      ```

      `OUT_OF_MEMORY = 4;`
    - #### PRECOMPILED\_CONTRACT

      ```
      public static final Chain.Transaction.Result.contractResult PRECOMPILED_CONTRACT
      ```

      `PRECOMPILED_CONTRACT = 5;`
    - #### STACK\_TOO\_SMALL

      ```
      public static final Chain.Transaction.Result.contractResult STACK_TOO_SMALL
      ```

      `STACK_TOO_SMALL = 6;`
    - #### STACK\_TOO\_LARGE

      ```
      public static final Chain.Transaction.Result.contractResult STACK_TOO_LARGE
      ```

      `STACK_TOO_LARGE = 7;`
    - #### ILLEGAL\_OPERATION

      ```
      public static final Chain.Transaction.Result.contractResult ILLEGAL_OPERATION
      ```

      `ILLEGAL_OPERATION = 8;`
    - #### STACK\_OVERFLOW

      ```
      public static final Chain.Transaction.Result.contractResult STACK_OVERFLOW
      ```

      `STACK_OVERFLOW = 9;`
    - #### OUT\_OF\_ENERGY

      ```
      public static final Chain.Transaction.Result.contractResult OUT_OF_ENERGY
      ```

      `OUT_OF_ENERGY = 10;`
    - #### OUT\_OF\_TIME

      ```
      public static final Chain.Transaction.Result.contractResult OUT_OF_TIME
      ```

      `OUT_OF_TIME = 11;`
    - #### JVM\_STACK\_OVER\_FLOW

      ```
      public static final Chain.Transaction.Result.contractResult JVM_STACK_OVER_FLOW
      ```

      `JVM_STACK_OVER_FLOW = 12;`
    - #### UNKNOWN

      ```
      public static final Chain.Transaction.Result.contractResult UNKNOWN
      ```

      `UNKNOWN = 13;`
    - #### TRANSFER\_FAILED

      ```
      public static final Chain.Transaction.Result.contractResult TRANSFER_FAILED
      ```

      `TRANSFER_FAILED = 14;`
    - #### INVALID\_CODE

      ```
      public static final Chain.Transaction.Result.contractResult INVALID_CODE
      ```

      `INVALID_CODE = 15;`
    - #### UNRECOGNIZED

      ```
      public static final Chain.Transaction.Result.contractResult UNRECOGNIZED
      ```
  + ### Field Detail

    - #### DEFAULT\_VALUE

      ```
      public static final int DEFAULT_VALUE
      ```

      `DEFAULT = 0;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.contractResult.DEFAULT_VALUE)
    - #### SUCCESS\_VALUE

      ```
      public static final int SUCCESS_VALUE
      ```

      `SUCCESS = 1;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.contractResult.SUCCESS_VALUE)
    - #### REVERT\_VALUE

      ```
      public static final int REVERT_VALUE
      ```

      `REVERT = 2;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.contractResult.REVERT_VALUE)
    - #### BAD\_JUMP\_DESTINATION\_VALUE

      ```
      public static final int BAD_JUMP_DESTINATION_VALUE
      ```

      `BAD_JUMP_DESTINATION = 3;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.contractResult.BAD_JUMP_DESTINATION_VALUE)
    - #### OUT\_OF\_MEMORY\_VALUE

      ```
      public static final int OUT_OF_MEMORY_VALUE
      ```

      `OUT_OF_MEMORY = 4;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.contractResult.OUT_OF_MEMORY_VALUE)
    - #### PRECOMPILED\_CONTRACT\_VALUE

      ```
      public static final int PRECOMPILED_CONTRACT_VALUE
      ```

      `PRECOMPILED_CONTRACT = 5;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.contractResult.PRECOMPILED_CONTRACT_VALUE)
    - #### STACK\_TOO\_SMALL\_VALUE

      ```
      public static final int STACK_TOO_SMALL_VALUE
      ```

      `STACK_TOO_SMALL = 6;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.contractResult.STACK_TOO_SMALL_VALUE)
    - #### STACK\_TOO\_LARGE\_VALUE

      ```
      public static final int STACK_TOO_LARGE_VALUE
      ```

      `STACK_TOO_LARGE = 7;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.contractResult.STACK_TOO_LARGE_VALUE)
    - #### ILLEGAL\_OPERATION\_VALUE

      ```
      public static final int ILLEGAL_OPERATION_VALUE
      ```

      `ILLEGAL_OPERATION = 8;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.contractResult.ILLEGAL_OPERATION_VALUE)
    - #### STACK\_OVERFLOW\_VALUE

      ```
      public static final int STACK_OVERFLOW_VALUE
      ```

      `STACK_OVERFLOW = 9;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.contractResult.STACK_OVERFLOW_VALUE)
    - #### OUT\_OF\_ENERGY\_VALUE

      ```
      public static final int OUT_OF_ENERGY_VALUE
      ```

      `OUT_OF_ENERGY = 10;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.contractResult.OUT_OF_ENERGY_VALUE)
    - #### OUT\_OF\_TIME\_VALUE

      ```
      public static final int OUT_OF_TIME_VALUE
      ```

      `OUT_OF_TIME = 11;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.contractResult.OUT_OF_TIME_VALUE)
    - #### JVM\_STACK\_OVER\_FLOW\_VALUE

      ```
      public static final int JVM_STACK_OVER_FLOW_VALUE
      ```

      `JVM_STACK_OVER_FLOW = 12;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.contractResult.JVM_STACK_OVER_FLOW_VALUE)
    - #### UNKNOWN\_VALUE

      ```
      public static final int UNKNOWN_VALUE
      ```

      `UNKNOWN = 13;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.contractResult.UNKNOWN_VALUE)
    - #### TRANSFER\_FAILED\_VALUE

      ```
      public static final int TRANSFER_FAILED_VALUE
      ```

      `TRANSFER_FAILED = 14;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.contractResult.TRANSFER_FAILED_VALUE)
    - #### INVALID\_CODE\_VALUE

      ```
      public static final int INVALID_CODE_VALUE
      ```

      `INVALID_CODE = 15;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Chain.Transaction.Result.contractResult.INVALID_CODE_VALUE)
  + ### Method Detail

    - #### values

      ```
      public static Chain.Transaction.Result.contractResult[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (Chain.Transaction.Result.contractResult c : Chain.Transaction.Result.contractResult.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static Chain.Transaction.Result.contractResult valueOf(java.lang.String name)
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
      public static Chain.Transaction.Result.contractResult valueOf(int value)
      ```

      Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Chain.Transaction.Result.contractResult.html#forNumber-int-) instead.

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### forNumber

      ```
      public static Chain.Transaction.Result.contractResult forNumber(int value)
      ```

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### internalGetValueMap

      ```
      public static com.google.protobuf.Internal.EnumLiteMap<Chain.Transaction.Result.contractResult> internalGetValueMap()
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
      public static Chain.Transaction.Result.contractResult valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)
      ```