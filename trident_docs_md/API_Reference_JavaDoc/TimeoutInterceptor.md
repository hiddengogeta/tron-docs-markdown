

org.tron.trident.core.interceptor

## Class TimeoutInterceptor

* java.lang.Object
* + org.tron.trident.core.interceptor.TimeoutInterceptor

* All Implemented Interfaces:
  :   io.grpc.ClientInterceptor

  ---

    

  ```
  public class TimeoutInterceptor
  extends java.lang.Object
  implements io.grpc.ClientInterceptor
  ```

* + ### Constructor Summary

    Constructors

    | Constructor and Description |
    | `TimeoutInterceptor(long timeout)` |
  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method and Description |
    | `<ReqT,RespT> io.grpc.ClientCall<ReqT,RespT>` | `interceptCall(io.grpc.MethodDescriptor<ReqT,RespT> method, io.grpc.CallOptions callOptions, io.grpc.Channel next)` |

    - ### Methods inherited from class java.lang.Object

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### TimeoutInterceptor

      ```
      public TimeoutInterceptor(long timeout)
      ```
  + ### Method Detail

    - #### interceptCall

      ```
      public <ReqT,RespT> io.grpc.ClientCall<ReqT,RespT> interceptCall(io.grpc.MethodDescriptor<ReqT,RespT> method,
                                                                       io.grpc.CallOptions callOptions,
                                                                       io.grpc.Channel next)
      ```

      Specified by:
      :   `interceptCall` in interface `io.grpc.ClientInterceptor`