

org.tron.trident.abi

## Class TypeDecoder

* java.lang.Object
* + org.tron.trident.abi.TypeDecoder

* ---

    

  ```
  public class TypeDecoder
  extends java.lang.Object
  ```

  Ethereum Contract Application Binary Interface (ABI) decoding for types. Decoding is not
  documented, but is the reverse of the encoding details located [here](https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI).

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `TypeDecoder()` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static <T extends Array> T` | `decode(java.lang.String input, int offset, TypeReference<T> typeReference)` |
    | `static Address` | `decodeAddress(java.lang.String input)` |
    | `static Bool` | `decodeBool(java.lang.String rawInput, int offset)` |
    | `static <T extends Bytes> T` | `decodeBytes(java.lang.String input, java.lang.Class<T> type)` |
    | `static <T extends Bytes> T` | `decodeBytes(java.lang.String input, int offset, java.lang.Class<T> type)` |
    | `static <T extends Type> T` | `decodeDynamicArray(java.lang.String input, int offset, TypeReference<T> typeReference)` |
    | `static DynamicBytes` | `decodeDynamicBytes(java.lang.String input, int offset)` |
    | `static <T extends Type> T` | `decodeDynamicStruct(java.lang.String input, int offset, TypeReference<T> typeReference)` |
    | `static <T extends NumericType> T` | `decodeNumeric(java.lang.String input, java.lang.Class<T> type)` |
    | `static <T extends Type> T` | `decodeStaticStruct(java.lang.String input, int offset, TypeReference<T> typeReference)` |
    | `static Utf8String` | `decodeUtf8String(java.lang.String input, int offset)` |
    | `static Type` | `instantiateType(java.lang.String solidityType, java.lang.Object value)` |
    | `static Type` | `instantiateType(TypeReference ref, java.lang.Object value)` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### TypeDecoder

      ```
      public TypeDecoder()
      ```
  + ### Method Detail

    - #### instantiateType

      ```
      public static Type instantiateType(java.lang.String solidityType,
                                         java.lang.Object value)
                                  throws java.lang.reflect.InvocationTargetException,
                                         java.lang.NoSuchMethodException,
                                         java.lang.InstantiationException,
                                         java.lang.IllegalAccessException,
                                         java.lang.ClassNotFoundException
      ```

      Throws:
      :   `java.lang.reflect.InvocationTargetException`
      :   `java.lang.NoSuchMethodException`
      :   `java.lang.InstantiationException`
      :   `java.lang.IllegalAccessException`
      :   `java.lang.ClassNotFoundException`
    - #### instantiateType

      ```
      public static Type instantiateType(TypeReference ref,
                                         java.lang.Object value)
                                  throws java.lang.NoSuchMethodException,
                                         java.lang.IllegalAccessException,
                                         java.lang.reflect.InvocationTargetException,
                                         java.lang.InstantiationException,
                                         java.lang.ClassNotFoundException
      ```

      Throws:
      :   `java.lang.NoSuchMethodException`
      :   `java.lang.IllegalAccessException`
      :   `java.lang.reflect.InvocationTargetException`
      :   `java.lang.InstantiationException`
      :   `java.lang.ClassNotFoundException`
    - #### decode

      ```
      public static <T extends Array> T decode(java.lang.String input,
                                               int offset,
                                               TypeReference<T> typeReference)
      ```
    - #### decodeAddress

      ```
      public static Address decodeAddress(java.lang.String input)
      ```
    - #### decodeNumeric

      ```
      public static <T extends NumericType> T decodeNumeric(java.lang.String input,
                                                            java.lang.Class<T> type)
      ```
    - #### decodeBool

      ```
      public static Bool decodeBool(java.lang.String rawInput,
                                    int offset)
      ```
    - #### decodeBytes

      ```
      public static <T extends Bytes> T decodeBytes(java.lang.String input,
                                                    java.lang.Class<T> type)
      ```
    - #### decodeBytes

      ```
      public static <T extends Bytes> T decodeBytes(java.lang.String input,
                                                    int offset,
                                                    java.lang.Class<T> type)
      ```
    - #### decodeDynamicBytes

      ```
      public static DynamicBytes decodeDynamicBytes(java.lang.String input,
                                                    int offset)
      ```
    - #### decodeUtf8String

      ```
      public static Utf8String decodeUtf8String(java.lang.String input,
                                                int offset)
      ```
    - #### decodeStaticStruct

      ```
      public static <T extends Type> T decodeStaticStruct(java.lang.String input,
                                                          int offset,
                                                          TypeReference<T> typeReference)
      ```
    - #### decodeDynamicArray

      ```
      public static <T extends Type> T decodeDynamicArray(java.lang.String input,
                                                          int offset,
                                                          TypeReference<T> typeReference)
      ```
    - #### decodeDynamicStruct

      ```
      public static <T extends Type> T decodeDynamicStruct(java.lang.String input,
                                                           int offset,
                                                           TypeReference<T> typeReference)
      ```