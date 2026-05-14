

org.tron.trident.proto

## Enum Response.Proposal.State

* java.lang.Object
* + java.lang.Enum<[Response.Proposal.State](../../../../org/tron/trident/proto/Response.Proposal.State.html "enum in org.tron.trident.proto")>
  + - org.tron.trident.proto.Response.Proposal.State

* All Implemented Interfaces:
  :   com.google.protobuf.Internal.EnumLite, com.google.protobuf.ProtocolMessageEnum, java.io.Serializable, java.lang.Comparable<[Response.Proposal.State](../../../../org/tron/trident/proto/Response.Proposal.State.html "enum in org.tron.trident.proto")>

  Enclosing class:
  :   [Response.Proposal](../../../../org/tron/trident/proto/Response.Proposal.html "class in org.tron.trident.proto")

  ---

    

  ```
  public static enum Response.Proposal.State
  extends java.lang.Enum<Response.Proposal.State>
  implements com.google.protobuf.ProtocolMessageEnum
  ```

  Protobuf enum `protocol.Proposal.State`

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant and Description |
    | `APPROVED` `APPROVED = 2;` |
    | `CANCELED` `CANCELED = 3;` |
    | `DISAPPROVED` `DISAPPROVED = 1;` |
    | `PENDING` `PENDING = 0;` |
    | `UNRECOGNIZED` |
  + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static int` | `APPROVED_VALUE` `APPROVED = 2;` |
    | `static int` | `CANCELED_VALUE` `CANCELED = 3;` |
    | `static int` | `DISAPPROVED_VALUE` `DISAPPROVED = 1;` |
    | `static int` | `PENDING_VALUE` `PENDING = 0;` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);) [Deprecated Methods](javascript:show(32);)

    | Modifier and Type | Method and Description |
    | `static Response.Proposal.State` | `forNumber(int value)` |
    | `static com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptor()` |
    | `com.google.protobuf.Descriptors.EnumDescriptor` | `getDescriptorForType()` |
    | `int` | `getNumber()` |
    | `com.google.protobuf.Descriptors.EnumValueDescriptor` | `getValueDescriptor()` |
    | `static com.google.protobuf.Internal.EnumLiteMap<Response.Proposal.State>` | `internalGetValueMap()` |
    | `static Response.Proposal.State` | `valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)` |
    | `static Response.Proposal.State` | `valueOf(int value)` Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Response.Proposal.State.html#forNumber-int-) instead. |
    | `static Response.Proposal.State` | `valueOf(java.lang.String name)` Returns the enum constant of this type with the specified name. |
    | `static Response.Proposal.State[]` | `values()` Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.Enum

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.Object

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### PENDING

      ```
      public static final Response.Proposal.State PENDING
      ```

      `PENDING = 0;`
    - #### DISAPPROVED

      ```
      public static final Response.Proposal.State DISAPPROVED
      ```

      `DISAPPROVED = 1;`
    - #### APPROVED

      ```
      public static final Response.Proposal.State APPROVED
      ```

      `APPROVED = 2;`
    - #### CANCELED

      ```
      public static final Response.Proposal.State CANCELED
      ```

      `CANCELED = 3;`
    - #### UNRECOGNIZED

      ```
      public static final Response.Proposal.State UNRECOGNIZED
      ```
  + ### Field Detail

    - #### PENDING\_VALUE

      ```
      public static final int PENDING_VALUE
      ```

      `PENDING = 0;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Proposal.State.PENDING_VALUE)
    - #### DISAPPROVED\_VALUE

      ```
      public static final int DISAPPROVED_VALUE
      ```

      `DISAPPROVED = 1;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Proposal.State.DISAPPROVED_VALUE)
    - #### APPROVED\_VALUE

      ```
      public static final int APPROVED_VALUE
      ```

      `APPROVED = 2;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Proposal.State.APPROVED_VALUE)
    - #### CANCELED\_VALUE

      ```
      public static final int CANCELED_VALUE
      ```

      `CANCELED = 3;`

      See Also:
      :   [Constant Field Values](../../../../constant-values.html#org.tron.trident.proto.Response.Proposal.State.CANCELED_VALUE)
  + ### Method Detail

    - #### values

      ```
      public static Response.Proposal.State[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (Response.Proposal.State c : Response.Proposal.State.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static Response.Proposal.State valueOf(java.lang.String name)
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
      public static Response.Proposal.State valueOf(int value)
      ```

      Deprecated. Use [`forNumber(int)`](../../../../org/tron/trident/proto/Response.Proposal.State.html#forNumber-int-) instead.

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### forNumber

      ```
      public static Response.Proposal.State forNumber(int value)
      ```

      Parameters:
      :   `value` - The numeric wire value of the corresponding enum entry.

      Returns:
      :   The enum associated with the given numeric wire value.
    - #### internalGetValueMap

      ```
      public static com.google.protobuf.Internal.EnumLiteMap<Response.Proposal.State> internalGetValueMap()
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
      public static Response.Proposal.State valueOf(com.google.protobuf.Descriptors.EnumValueDescriptor desc)
      ```