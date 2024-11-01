# Nilan Proxy
Library to locally interface with HVAC systems running Nilan or Genvex Connect gateways.
Usually, those are only cloud accessible; however, after lots of work, we finally have a local solution ready.

The library is primarily built to be used by the Home Assistant custom component [Nilan Connect](https://github.com/HairingX/nilan_connect).

### Supported Controller Models
| Controller         | Gateway Required      | Supported | Tested |
|-------------------:|:---------------------:|:---------:|:------:|
| Optima 250         | Yes, internet gateway | ✅        |        |
| Optima 251         | Yes, internet gateway | ✅        |        |
| Optima 260         | Yes, internet gateway | ✅        |        |
| Optima 270         | Built-in              | ✅        |        |
| Optima 301         | Yes, internet gateway | ✅        |        |
| Optima 312         | Yes, internet gateway | ✅        |        |
| Optima 314         | Built-in              | ✅        |        |
| Nilan CTS400       | Yes, Nilan gateway    | ✅        | ✅     |
| Nilan CTS602       | Yes, Nilan gateway    | ✅        |        |
| Nilan CTS602 Light | Yes, Nilan gateway    | ✅        |        |
| Nilan CTS602 Geo   | Yes, Nilan gateway    | ✅        |        |

For any controllers that require a gateway, it is mandatory that the device supports Modbus. Optima controllers delivered before 2014 might not have Modbus.

## Obligatory Statement
I am not personally or in any way responsible for any damages should you choose to use the library. No warranty provided.

## Special Thanks
This library owes special thanks to superrob; without him, this would not exist.
For more info see his library here: https://github.com/superrob/genvexnabto

### How Superrob Got the Base Library Developed
See more in his repository.

> Genvex Connect and Nilan gateways both use the proprietary "Micro Nabto" protocol. Any mentions of it are very scarce online, with most official documentation being wiped from the internet after the companies released "Nabto Edge," which is highly incompatible with the older "Micro Nabto."

> The usual connection flow is for the user to use the respective dedicated app. The app loads a comically large 6MB+ binary client for Nabto communication. The binary is closed source and seems obfuscated to prevent easy "decompilation." 
This is also a huge issue as binaries are only available for Win32, Linux, Mac, Android, and iOS. No generic Linux ARM binaries are available, and thus using those to implement a Home Assistant custom component would exclude the most popular hosting devices, such as the Raspberry Pi.

> The binary scans for any gateways by sending out a broadcast UDP packet. This packet either has a specific device identifier in it or a star (*) to request any gateway to respond.
Any available gateways will respond to the receiver with their unique identifier on the same UDP IP and port the broadcast was sent.

> The normal flow is then handled online, with the library using a client certificate encrypted using the password supplied when first using the device. The flow, unfortunately, is where I got stuck for a long time. 
The client requests a server peer ID from the Nabto server, which, if properly authenticated, is sent back together with a NONCE and a server certificate. The client, using the NONCE, calculates an AES encryption key, which is later used to set up a direct local connection to the device.
Next, the client sends a connection request to the Nabto server. This request is encrypted using the server certificate public key and signed using the client certificate private key. The contents of this request are currently not known, as that would require extensive reverse engineering of the Nabto client binary, and thus where I got stuck.

> The server replies back, again encrypted. I am guessing the contents to be encrypted using the public RSA key from the client certificate. I have not looked into the contents of the reply, as I currently do not know the contents of the original request.
What is clear is that these packets set up the communication on the local device where the encryption context for the connection is set up.

> The client then connects locally to the device and is expected to provide all communication forwards in CRYPT payloads, encrypted using the AES keys which the server has set for the connection during the last two phases.
Luckily, the Nabto binary has a lot of logging built in and actually displays the AES and HMAC keys during the connection request! 
Using that key, I was able to decrypt and study the payloads, which matched the "Micro Nabto" device source code I had found a while ago on their GitHub.
Their device source code contains details on the protocol used and allowed me to decode and even build my own packets.

> However, without understanding the client connection request sent to the server, this is not useful.

> That was until I tried using an extremely old version of the Nabto client binary. To my surprise, it talked with the device using cleartext CRYPT payloads! I had seen in the device source code that if an "isLocal" flag is set for the connection, that any encryption can be specified to be used. However, I couldn't figure out how to set the flag.
However, this old client binary connected to a different port on the device. To my surprise, using that UDP port instead of the one used by the newer client library, it actually set the isLocal flag and allowed for unencrypted CRYPT payloads!

> From here, I only had to implement the "Micro Nabto" protocol in my own portable library.
I have only been able to test the Optima 270 implementation as I only have a Genvex ventilation unit with the Optima 270 controller (Has the gateway built-in). 
However, I have tried implementing the older controllers which should, in theory, be compatible. I have also added the Nilan CTS400 controller as the gateway for Nilan is built by the same company and uses the same command structure.
