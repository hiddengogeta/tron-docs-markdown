

org.tron.trident.core.utils

## Class Utils

* java.lang.Object
* + org.tron.trident.core.utils.Utils

* ---

    

  ```
  public class Utils
  extends java.lang.Object
  ```

* + ### Field Summary

    Fields

    | Modifier and Type | Field and Description |
    | `static byte` | `ADD_PRE_FIX_BYTE_MAINNET` |
    | `static byte` | `ADD_PRE_FIX_BYTE_TESTNET` |
    | `static int` | `ADDRESS_SIZE` |
  + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `Utils()` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static boolean` | `addressValid(byte[] address)` |
    | `static byte[]` | `decodeFromBase58Check(java.lang.String addressBase58)` |
    | `static java.lang.String` | `encode58Check(byte[] input)` |
    | `static com.google.protobuf.ByteString` | `encodeParameter(java.util.List<Type<?>> params)` |
    | `static byte` | `getAddressPreFixByte()` |
    | `static BlockId` | `getBlockId(Response.BlockExtention blockExtention)` |
    | `static Contract.CreateSmartContract` | `getSmartContractFromTransaction(Chain.Transaction trx)` |
    | `static byte[]` | `replaceLibraryAddress(java.lang.String code, java.lang.String libraryAddressPair, java.lang.String compilerVersion)` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Field Detail

    - #### ADD\_PRE\_FIX\_BYTE\_MAINNET

      ```
      public static byte ADD_PRE_FIX_BYTE_MAINNET
      ```
    - #### ADD\_PRE\_FIX\_BYTE\_TESTNET

      ```
      public static byte ADD_PRE_FIX_BYTE_TESTNET
      ```
    - #### ADDRESS\_SIZE

      ```
      public static int ADDRESS_SIZE
      ```
  + ### Constructor Detail

    - #### Utils

      ```
      public Utils()
      ```
  + ### Method Detail

    - #### getBlockId

      ```
      public static BlockId getBlockId(Response.BlockExtention blockExtention)
      ```
    - #### getSmartContractFromTransaction

      ```
      public static Contract.CreateSmartContract getSmartContractFromTransaction(Chain.Transaction trx)
      ```
    - #### getAddressPreFixByte

      ```
      public static byte getAddressPreFixByte()
      ```
    - #### addressValid

      ```
      public static boolean addressValid(byte[] address)
      ```
    - #### encode58Check

      ```
      public static java.lang.String encode58Check(byte[] input)
      ```
    - #### decodeFromBase58Check

      ```
      public static byte[] decodeFromBase58Check(java.lang.String addressBase58)
      ```
    - #### encodeParameter

      ```
      public static com.google.protobuf.ByteString encodeParameter(java.util.List<Type<?>> params)
                                                            throws ContractCreateException
      ```

      Throws:
      :   `ContractCreateException`
    - #### replaceLibraryAddress

      ```
      public static byte[] replaceLibraryAddress(java.lang.String code,
                                                 java.lang.String libraryAddressPair,
                                                 java.lang.String compilerVersion)
      ```