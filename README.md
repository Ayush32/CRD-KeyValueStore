# CRD-operations-of-a-file-based-key-value-data-store
## Screenshot

<img alt="GIF" height= 400 src="https://github.com/Ayush32/CRD-KeyValueStore/blob/master/githubImages/Capture2.png" /> <img alt="GIF" height= 400 src="https://github.com/Ayush32/CRD-KeyValueStore/blob/master/githubImages/Capture1.PNG" />

---
### This is a file which can be exposed as a library that supports the basic CRD(create, read, write) operations. Data store is meant to local storage for one single process on single laptop

1. It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a reasonable location on the laptop.

2. A new key-value pair can be added to the data store using the Create operation. The key is always a string - capped at 32chars. The value is always a JSON object - capped at 16KB.

3. If Create is invoked for an existing key, an appropriate error must be returned.

4. A Read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object.

5. A Delete operation can be performed by providing the key.

6. Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds the key must be retained in the data store. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.

7. Appropriate error responses must always be returned to a client if it uses the data store in unexpected ways or breaches any limits

### The Data Store will also support the following non-functional requirments.

1. The file size never exceeds 1GB
2. More than one client process cannot be allowed to use the same file as a data store at any given time.
3. A client process si allowed to access the data store using multiple threads, If it desires to. the data store must therefore be thread-safe.


