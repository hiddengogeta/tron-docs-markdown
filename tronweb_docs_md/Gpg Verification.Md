

* GPG verification
Version: 6.3.0

On this page

# GPG verification

GNU Privacy Guard (GPG) is a free, open-source cryptographic tool that uses encryption and signing to secure data and communication. We use it to protect the integrity and confidentiality of TronWeb source files.

## Verification process[​](#verification-process "Direct link to Verification process")

1. Import TronWeb pubKey

* TronWeb pubKey: 4371 AB85 E5A5 8FAA 88AD 7FDF 9945 DBCA 8C4B B810
* TronWeb uid: [[email protected]](/cdn-cgi/l/email-protection#680c0d1e281c1a07061f0d0a46060d1c1f071a03)
* Run Command `gpg --keyserver hkp://keys.openpgp.org --recv-keys 4371AB85E5A58FAA88AD7FDF9945DBCA8C4BB810` to import pubKey.

2. Download files

* Download URL: <https://github.com/tronprotocol/tronweb/releases>
* Download the same version of the TronWeb source file and the sig file. For example tronweb-6.0.0-beta.4.zip and tronweb-6.0.0-beta.4.sig.

3. Verify signature

* Run command `gpg --verify tronweb-6.0.0-beta.4.zip.sig tronweb-6.0.0-beta.4.zip`.
* Remember to replace the sig file and the source file with your downloaded version of them.
* If the result shows `Good signature` then the source file is untampered or it will show `BAD signature`.