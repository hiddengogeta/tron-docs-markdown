

org.tron.trident.core.contract.abi

## Class AbiUtils

* java.lang.Object
* + org.tron.trident.core.contract.abi.AbiUtils

* ---

    

  ```
  public class AbiUtils
  extends java.lang.Object
  ```

  Utility class for handling Tron smart contract ABI (Application Binary Interface).
  Provides functionality to parse and convert between JSON ABI representations and protobuf ABI objects.

  Example usage:

  ```
   String jsonAbi = "{\"entrys\": [{\"name\": \"transfer\",\"type\": \"function\",...}]}";
   
   // Convert JSON string to ABI object
   ABI abi = AbiUtils.jsonStr2ABI(jsonAbi);
   
   // Or use builder pattern
   ABI.Builder builder = ABI.newBuilder();
   AbiUtils.loadAbiFromJson(jsonAbi, builder);
  ```

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `AbiUtils()` |
  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `static Common.SmartContract.ABI` | `jsonStr2ABI(java.lang.String jsonStr)` Converts a JSON string representation of an ABI to ABI protobuf object. |
    | `static void` | `loadAbiFromJson(java.lang.String abiString, Common.SmartContract.ABI.Builder builder)` Loads ABI information from a JSON string into an existing ABI builder. |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### AbiUtils

      ```
      public AbiUtils()
      ```
  + ### Method Detail

    - #### loadAbiFromJson

      ```
      public static void loadAbiFromJson(java.lang.String abiString,
                                         Common.SmartContract.ABI.Builder builder)
      ```

      Loads ABI information from a JSON string into an existing ABI builder.

      Parameters:
      :   `abiString` - The JSON string containing the ABI definition
      :   `builder` - The ABI builder to populate

      Throws:
      :   `java.lang.IllegalArgumentException` - if the JSON format is invalid or required fields are missing
    - #### jsonStr2ABI

      ```
      public static Common.SmartContract.ABI jsonStr2ABI(java.lang.String jsonStr)
      ```

      Converts a JSON string representation of an ABI to ABI protobuf object.
      Supports both direct array format and object format with "entrys" field.

      Parameters:
      :   `jsonStr` - The JSON string containing the ABI definition

      Returns:
      :   ABI protobuf object

      Throws:
      :   `java.lang.IllegalArgumentException` - if the input JSON string is invalid or cannot be parsed