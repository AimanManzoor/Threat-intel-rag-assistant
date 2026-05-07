---
title: "Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication"
date: "2026-03-23"
url: https://unit42.paloaltonetworks.com/passwordless-authentication/
source: unit42
---

# Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
* [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
* [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/ "Cloud Cybersecurity Research")

[Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)

# Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg)  13  min read

Related Products

[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex Cloud](https://unit42.paloaltonetworks.com/product-category/cortex-cloud/ "Cortex Cloud")[![Unit 42 Cloud Security Assessment icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Cloud Security Assessment](https://unit42.paloaltonetworks.com/product-category/cloud-security-assessment/ "Unit 42 Cloud Security Assessment")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

* ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

  By:
  + [Arie Olshtein](https://unit42.paloaltonetworks.com/author/arie-olshtein/)
* ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

  Published:March 23, 2026
* ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

  Categories:
  + [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
  + [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)
* ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

  Tags:
  + [Google](https://unit42.paloaltonetworks.com/tag/google/)
  + [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/)
  + [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/)
  + [Identity](https://unit42.paloaltonetworks.com/tag/identity/)
  + [Passkey](https://unit42.paloaltonetworks.com/tag/passkey/)
  + [Passwordless](https://unit42.paloaltonetworks.com/tag/passwordless/)

* [![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/passwordless-authentication/?pdf=download&lg=en&_wpnonce=9711c8889b "Click here to download")
* [![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/passwordless-authentication/?pdf=print&lg=en&_wpnonce=9711c8889b "Click here to print")

[Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)](# "Click here to share")

* [![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)](# "Copy link")
* [![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Google%20Cloud%20Authenticator:%20The%20Hidden%20Mechanisms%20of%20Passwordless%20Authentication&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fpasswordless-authentication%2F "Share in email")
* [![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fpasswordless-authentication%2F "Share in Facebook")
* [![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fpasswordless-authentication%2F&title=Google%20Cloud%20Authenticator:%20The%20Hidden%20Mechanisms%20of%20Passwordless%20Authentication "Share in LinkedIn")
* [![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fpasswordless-authentication%2F&text=Google%20Cloud%20Authenticator:%20The%20Hidden%20Mechanisms%20of%20Passwordless%20Authentication "Share in Twitter")
* [![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fpasswordless-authentication%2F "Share in Reddit")
* [![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Google%20Cloud%20Authenticator:%20The%20Hidden%20Mechanisms%20of%20Passwordless%20Authentication%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fpasswordless-authentication%2F "Share in Mastodon")

## Executive Summary

Passwordless authentication is often presented as the end of account takeover. But to understand the real threat landscape, we need to examine how passwordless is actually deployed in the real world. Attackers do not break protocols in theory. They target the most common implementations, the places where usability, scale and architecture intersect.

Focusing on one of those common implementations, we examine Google Cloud Authenticator. This discussion explores the hidden mechanisms behind synced passkeys and their implementation within the Google ecosystem. Our aim is to help defenders better understand the technology, to lay the groundwork to show how new attack vectors could emerge in a passwordless environment.

This post is Part 2 in our series examining passkey adoption from a security perspective. If you haven’t read Part 1 yet, we recommend starting here: [The Art of the Invisible Key – Passkey Global Breakthrough](https://www.cyberark.com/resources/threat-research-blog/the-art-of-the-invisible-key-passkey-global-breakthrough).

Palo Alto Networks customers are better protected from threats that take advantage of issues with cloud authentication through the following products and services:

* Cortex Cloud [Identity Security](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud-Identity-Security)
* [CyberArk Identity Protection](https://docs.cyberark.com/identity/latest/en/content/coreservices/authenticate/configure-passkey.htm)
* [Unit 42 Cloud Security Assessment](https://www.paloaltonetworks.com/unit42/assess/cloud-security-assessment)

If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

|  |  |
| --- | --- |
| **Related Unit 42 Topics** | **[Google](https://unit42.paloaltonetworks.com/tag/google/), [Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/), [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/)** |

## Background on Passkey Authentication

When we set out to evaluate the security of passkeys, we deliberately thought like attackers. Instead of asking whether [Fast IDentity Online (FIDO)](https://fidoalliance.org/) is secure, we asked where passkeys live, how they move, how they sync and which components handle the most sensitive operations. That shift in perspective revealed a surprisingly broad and largely unexplored attack surface. Many of the findings we uncovered have not been publicly discussed, and we will reveal them throughout this series.

However, before diving into new attack vectors, we need to establish a clear architectural foundation. The [FIDO and W3C specifications](https://www.w3.org/TR/webauthn-3/) define the authentication protocols in detail, but the real protection of key material often extends beyond those documents. In practice, critical implementation details are embedded in browsers, operating systems and cloud services, and are rarely described publicly.

We therefore began with one of the most widely adopted passwordless ecosystems: Google’s passkey authentication.

In this article, we examine the architecture behind synced passkeys for desktop users and explore the lesser known [Google Cloud Authenticator](https://www.google.com/url?q=https://chromium.googlesource.com/chromium/src/%2B/main/device/fido/enclave/enclave_websocket_client.cc%2333&sa=D&source=docs&ust=1774279081861756&usg=AOvVaw3uR5FTPYuNHgpPzg5H_5p2), a cloud-based component that performs sensitive cryptographic operations. Once we understand how this system is built, we can analyze the new attack vectors it introduces and discuss how to mitigate them in the next part of this series.

*Disclaimer: This analysis reflects our understanding of a complex, evolving system, based on client code, runtime behavior, network traces and public sources. The research detailed here was conducted for responsible, ethical security analysis. To keep the discussion readable, we simplify certain internal flows and use illustrative pseudocode. Although the Google Cloud Authenticator is used by Chrome across platforms, our focus here is Chrome on Windows with Trusted Platform Module (TPM) support.*

## Meet the Invisible Authenticator

Whenever users authenticate with passkeys backed by Google Password Manager (GPM) across desktop platforms (macOS, Windows, Linux and ChromeOS), we see a connection to the domain enclave.ua5v[.]com.

As of January 2026, searching for enclave.ua5v[.]com yields surprisingly little public information about its role in passkey authentication (as shown in Figure 1). This is despite powering logins worldwide.

![Search engine results for the query "enclave.uA5v.com," featuring the following listings: GitHub for "sensitive.txt," reviews on sites like "scamadviser.com" and "ScamMinder" questioning legitimacy, and "accountingtoday.com" addressing refund concerns.]()

Figure 1. A search for the Google Cloud Authenticator URL returns only a few non-informative results.

The FIDO specifications do not explicitly define a cloud-based authenticator. However, related building-block elements exist in Client-to-Authenticator Protocol ([CTAP) Hybrid transports](https://fidoalliance.org/specs/fido-v2.2-rd-20230321/fido-client-to-authenticator-protocol-v2.2-rd-20230321.html#tunnel-service), where Bluetooth Low Energy (BLE) physical proximity can be used to establish a tunnel service to Google’s caBLE.ua5v[.]com domain.

While Chrome still [leverages](https://source.chromium.org/chromium/chromium/src/+/main:device/fido/cable/v2_handshake.h) portions of the Hybrid (caBLE) transport code, understanding the actual implementation requires examining Chrome’s behavior and the [cloud authenticator](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/third_party/cloud_authenticator/), as observed through its network interface and [Chromium source](https://chromium.googlesource.com/chromium/src.git) code (as shown in Figure 2).

![Code snippet showing a character array and constants for a WebSocket protocol related to Chrome's "Cloud Enclave Passkey Authenticator Client" and passkey synchronization.]()

Figure 2. Google Chromium source code referring to Cloud Enclave Passkey Authenticator.

## Onboarding Device

A Chrome user can perform passkey operations synchronized with their Google account, making passkeys available across all connected devices. Before any passkey can be used, Chrome runs a dedicated onboarding flow behind the scenes (shown in Figure 3). This allows the remote Google Cloud Authenticator to verify both the device’s identity and the user’s possession of it.

![Diagram of an onboarding device process. Red nodes are connected vertically in a sequence. The sequence starts at "Identity Key" and ends at "Passkey Enclave State." Major nodes include "Generating Device Key," "Registration," "GPM’s PIN," and "Member proof." Each node corresponds to a security-related task.]()

Figure 3. High-level overview of the device onboarding.

To establish trust between the device and the cloud authenticator, Chrome assigns two TPM-backed key pairs:

* Identity key: Represents “something you have.” In WebAuthn [terms](https://w3c.github.io/webauthn/#platform-authenticators): “Register a particular client device as a ‘trusted device’, so the client device itself acts as a something-you-have authentication factor for future authentication.”
* User verification key (UV key): Represents “something you know or are.” This key can only be created or used after the user authenticates (verifies) with the same method they use to unlock the device (biometric or PIN).

After generating the device keys, the client sends a registration [request](https://chromium.googlesource.com/chromium/src/+/HEAD/chrome/browser/webauthn/enclave_manager.cc#409) to the cloud authenticator. The message includes:

* Commands: "device/register", "keys/genpair"
* Identity\_public\_key: Public key corresponding to the TPM-protected identity key.
* UV\_public\_key: Public key corresponding to the TPM-protected UV key.
* Device\_id: SHA256 hash of the identity public key (SPKI).

The cloud authenticator creates a new record and stores the device’s hardware-backed public keys associated with the device ID:

devices[device\_id] = {

hw: identity\_public\_key,

uv: uv\_public\_key

}

In addition, the cloud authenticator generates and stores a device-specific wrapping key. This key is used to encrypt secrets, allowing them to be stored on the device as opaque blobs and unwrapped only by the cloud authenticator:

wrapping\_keys[device\_id] = random(32)

Finally, the cloud authenticator generates a member key pair. The private member key is encrypted with the wrapping key. This key is then returned along with the public member key intended for joining the device as a trusted member within the account’s security domain of authorized devices:

(member\_private\_key, a member\_public\_key) = Generate P-256 key pair

wrapped\_member\_private\_key = encrypt(member\_private\_key, key:wrapping\_key)

### First Device

On the first device, the onboarding process also includes generating the account secrets:

* [Security domain secret](https://chromium.googlesource.com/chromium/src/+/HEAD/chrome/browser/webauthn/enclave_manager.cc#1587) (SDS): A symmetric master key used by the cloud authenticator to encrypt and decrypt all synced passkeys for the account
* GPM PIN Code: A user-chosen secret that allows newly added devices to access the account’s synced passkeys

Figure 4 shows the start of the recovery PIN process.

![The image shows a Google Password Manager interface for creating a recovery PIN with six empty input boxes and icons for PIN options, Cancel, and Confirm.]()

Figure 4. Google prompt for creating a PIN.

* Establishing a security domain backed by Google’s [Trusted Vault](https://chromium.googlesource.com/chromium/src.git/+/refs/heads/main/components/trusted_vault) service, linking the user’s authorized devices and managing the encryption keys used by [Chrome Sync](https://chromium.googlesource.com/chromium/src.git/+/refs/heads/main/components/sync/) to securely synchronize passkeys
* Creating a PIN-protected recovery [mechanism](https://chromium.googlesource.com/chromium/src/+/HEAD/chrome/browser/webauthn/enclave_manager.cc#593) to store and recover the SDS securely

### Joined Device

During the first passkey operation on a new device or on a recovered account, Chrome prompts the user to verify with the same GPM PIN. The PIN is verified by the cloud authenticator and protected recovery mechanism. This allows the device to join the account’s security domain, synchronize account passkeys and enable the cloud authenticator to wrap the SDS for that device.

### Passkey Enclave State

To summarize the device onboarding process, we can review the [various key materials](https://chromium.googlesource.com/chromium/src/+/HEAD/chrome/browser/webauthn/proto/enclave_local_state.proto) generated during the onboarding and stored in a [file](https://chromium.googlesource.com/chromium/src/+/HEAD/chrome/browser/webauthn/enclave_manager.cc#2872) under the user’s profile directory:

%LocalAppData%\Google\Chrome\User Data\<Profile>\passkey\_enclave\_state.

The local file enables future device-cloud communication without re-registration or re-entering the PIN and includes the following elements:

* Device keys:
  + Identity key:
    - wrapped\_identity\_private\_key: When Chrome creates the identity key, it asks the TPM to seal the private portion with the TPM’s hard-coded key. This allows the key to be saved as an opaque blob that only that specific TPM can unseal.
    - identity\_public\_key: The corresponding public portion.
    - device\_id: The hash of the identity public key that is used as a unique identifier for the device within the cloud authenticator
  + UV key
    - wrapped\_uv\_private\_key: The label of the hardware-backed key that is gated by local (Windows Hello) user verification
    - uv\_public\_key: The corresponding public portion
* wrapped\_secret: The SDS encrypted with the cloud authenticator’s wrapping key
* wrapped\_pin: PIN data encrypted under the cloud authenticator’s wrapping key, enabling the authenticator to verify the PIN, enforce retry limits and perform secure PIN updates without ever exposing the plaintext PIN

Figure 5 shows the extracted passkey\_enclave\_state file.

![A code snippet displays an internal state object with several attributes. Each entry includes a variable name, data type, and value.]()

Figure 5. Parsed view of the passkey\_enclave\_state file, extracted using a custom script.

## Synced Passkey in Action

After the device onboarding — which involves completing enrollment with the cloud and joining the security domain — the device's user can start creating and using passkeys that are securely synchronized with their Google account. Figure 6 shows the flow for this process.

![Flowchart for creating a synced passkey. It involves these steps: Relying Party: Registration Options, Cloud Authenticator: Create Command, Chrome, Cloud Authenticator: Key Generation and Encryption, Relying Party: Passkey Registration, Security Domain: Passkey Synchronization, Local Storage: Update Account State.]()

Figure 6. High-level Chrome-mediated flow for creating a synced passkey.

## Creating a Synced Passkey

When a user chooses to add a passkey as an authentication method to a service, the relying party (service) invokes a [create](https://w3c.github.io/webappsec-credential-management/#dom-credentialscontainer-create) WebAuthn API:

* navigator.credentials.create(options)

Chrome then displays a prompt offering to save the passkey in GPM as shown in Figure 7.

![This image shows a dialog box asking where to save a passkey for webauthn.io. Options include "Google Password Manager" with an email address partially redacted and "Windows Hello or external security key." There's a "Cancel" button at the bottom.]()

Figure 7. Saving a passkey to GPM makes it a synced passkey.

Once the user selects the GPM option, Chrome prepares the required data and initiates a secure, peer-to-peer (P2P) encrypted session with the cloud authenticator.

#### Create Command (Chrome to Cloud Authenticator)

Chrome sends a request containing the following parameters:

* command: "passkeys/create"
* device\_id
* wrapped\_secret

#### Key Generation and Encryption (Cloud Authenticator to Chrome)

The cloud authenticator performs the following operations:

1. Uses the provided device\_id to locate the corresponding stored wrapping\_key.
2. Unwraps the wrapped\_secret to recover the SDS.
3. Generates a new P-256 ECDSA key pair for the passkey.
4. Encrypts the passkey’s private key using the SDS.
5. Returns the public key and the encrypted private key to the Chrome client.

wrapping\_key = wrapping\_keys[device\_id]

security\_domain\_secret = decrypt(wrapped\_secret, key: wrapping\_key)

(passkey\_private\_key, passkey\_public\_key) = Generate P-256 key pair

encrypted\_private\_key = encrypt(passkey\_private\_key, key:security\_domain\_secret)

Return to the device (passkey\_public\_key, encrypted\_private\_key)

#### Passkey Registration (Chrome to Relying Party)

Chrome forwards the passkey public key to the relying party as part of the WebAuthn registration response. The website stores this public key under the user’s account for future authentication.

#### Passkey Synchronization (Chrome to Security Domain)

Next, Chrome prepares a [protobuf-encoded](https://protobuf.dev/) sync entity [named](https://chromium.googlesource.com/chromium/src/+/lkgr/components/sync/protocol/webauthn_credential_specifics.proto) WebauthnCredentialSpecifics. This record represents the cloud authenticator’s encrypted view of the new credential, enabling any device enrolled in the same security domain to access and use it for authentication. Each WebauthnCredentialSpecifics entry includes:

* RP ID (relying party’s domain)
* Username
* Passkey public key
* Passkey encrypted private key

Chrome uploads this sync entity to the Security Domain service, which distributes the update to the other registered devices.

#### Update Account State (Chrome to Local Storage)

Whenever a new passkey is added to the account, each enrolled device stores the corresponding WebauthnCredentialSpecifics locally in Chrome’s sync database:

%LocalAppData%\Google\Chrome\User Data\<Profile>\Sync Data\LevelDB.

The stored record allows GPM to list the accounts' passkeys and make them available for authentication. Figure 8 shows the authentication flow.

![Diagram outlining the process of using a synced passkey in Chrome, including steps: Relying Party: Authentication Options, Cloud Authenticator: Get Assertion Request, Cloud Authenticator: Assertion Generation, and Relying Party: Authentication Response.]()

Figure 8. Chrome-mediated authentication flow using a synced passkey.

### Log in With Synced Passkey

Once a passkey has been created and synchronized, a user can initiate login to a relying party using the synced passkey from any enrolled device. The relying party then invokes a [get](https://w3c.github.io/webappsec-credential-management/#dom-credentialscontainer-get) WebAuthn API: navigator.credentials.get(options). Chrome locates the WebauthnCredentialSpecifics entity that matches the visited relying party ID and establishes a secure connection to the cloud authenticator.

#### Assertion Request (Chrome to Cloud Authenticator)

Chrome sends a request containing:

* Command: "passkeys/assert"
* client\_data\_json (challenge and rpID from WebAuthn request)
* device\_id
* wrapped\_secret
* WebauthnCredentialSpecifics

#### Assertion Response (Cloud Authenticator to Chrome)

The cloud authenticator performs the following operations:

1. Uses the provided device\_id to locate the corresponding wrapping\_key
2. Unwraps the wrapped\_secret to recover the SDS
3. Decrypts the passkey’s encrypted\_private\_key with the SDS
4. Sets the [authenticator flags](https://w3c.github.io/webauthn/#authdata-flags), including the user-verified flag, based on whether the client’s message is signed with the user verification key (see the secure communication protocol in the [Secure Communication Protocol section](#post-175796-_ooe8u3eqgrr))
5. Constructs authenticator\_data, which [includes](https://www.w3.org/TR/webauthn-2/#sctn-authenticator-data): relying party ID (hash), flags and signature counter (always zero)
6. Using the passkey\_private\_key, signs the concatenation of the client\_data\_json and the authenticator\_data
7. Returns to the client [AuthenticatorAssertionResponse](https://w3c.github.io/webauthn/#authenticatorassertionresponse) containing the client\_data\_json, authenticator\_data and the signature

wrapping\_key = wrapping\_keys[device\_id]

security\_domain\_secret = decrypt(wrapped\_secret, key: wrapping\_key)

passkey\_private\_key = decrypt(WebAuthnCredentialSpecifics.encrypted\_private\_key, key:security\_domain\_secret)

flags = {

flag\_user\_present = 1,

flag\_user\_present = 1 if user-verified else 0,

flag\_backup\_eligible = 1,

flag\_backed\_up\_state = 1,

}

signature\_counter = 0

rpId\_hash = SHA\_256(rpId)

authenticator\_data = {rpId\_hash, flags, signature\_counter}

signed\_data = authenticator\_data + client\_data\_json

assertion\_signature = sign(signed\_data, key:passkey\_private\_key)

return to the client: AuthenticatorAssertionResponse {

clientDataJSON: client\_data\_json,

authenticatorData: authenticator\_data

signature: assertion\_signature,

userHandle: WebauthnCredentialSpecifics.credential\_id

}

#### Authentication Response (Chrome to Relying Party)

Chrome forwards the AuthenticatorAssertionResponse to the relying party, which verifies the signature using the previously registered passkey\_public\_key and authenticates the user.

## Secure Communication Protocol

All requests sent to the cloud authenticator, including device management, key handling, recovery operations and passkey creation or use, are protected by a secure communication protocol. For example, once a WebAuthn API is issued and the user selects GPM as the passkey provider, Chrome initiates secure communication with the cloud authenticator as shown in Figure 9.

![Diagram of a secure communication protocol featuring a linear sequence of red nodes connected by a line. Each node represents a step in the process, beginning with an OAuth2 token and ending with the response being decrypted. ]()

Figure 9. Chrome-cloud authenticator secure communication flow.

### Get OAuth2 Token

Chrome uses a Google OAuth2 access token as the primary authorization signal for cloud authenticator operations. This token is issued for the Google account that is currently signed in. The token includes a dedicated scope: hxxps[:]//www.googleapis[.]com/auth/secureidentity.action.

To obtain the token, Chrome exchanges a locally stored refresh token for a short-lived access token using Google’s OAuth2, as shown in Figure 10.

![A split-screen view of an HTTP request and response interface. On the left side, a request is made to a URL using POST and includes different parameters. The right side displays the response. The interface is organized under tabs labeled "Request" and "Response".]()

Figure 10. Chrome requests the OAuth2 token for cloud authenticator operations.

### WebSocket

Once the token is obtained, Chrome opens a WebSocket connection to the cloud authenticator. See Figure 11, wss[:]//enclave.ua5v[.]com/enclave.

The cloud authenticator returns a WebSocket upgrade response (101 Switching Protocols), and Chrome proceeds to the Noise-NK handshake.

![A split-screen view of a network request and response panel. On the left, a request is displayed with details and various headers. On the right, a response is shown with headers including "Upgrade: websocket." ]()

Figure 11. WebSocket initialization.

### Noise Handshake

Chrome and the cloud authenticator establish an encrypted session using the [Noise Protocol Framework](https://noiseprotocol.org/noise.html). Noise is a framework for flexible cryptographic handshakes that specifies a protocol for two parties to exchange Diffie-Hellman (DH) public keys. It then hashes the DH results into a shared secret and derives symmetric keys to protect all subsequent messages.

Chrome uses the following handshake variant: Noise\_NK\_P256\_AESGCM\_SHA256.

This combination defines:

* [NK](https://noiseexplorer.com/patterns/NK/): the handshake pattern
  + N: the initiator (Chrome client) is unauthenticated
  + K: the responder (cloud authenticator) has a known static public key (the key is [hard-coded](https://source.chromium.org/chromium/chromium/src/+/main:device/fido/enclave/constants.cc;l=37) in Chrome)
* P256: DH uses the NIST P-256 elliptic curve.
* AESGCM: encryption uses AES-GCM.
* SHA256: hashing uses SHA256.

The session begins in an initial handshake state, where both sides prepare to exchange ephemeral keys and progressively mix cryptographic material into the handshake hash state and shared encryption key.

### Message A: Chrome (e, es) to Cloud Authenticator

Chrome sends the first handshake message, which includes its ephemeral public key and the result of an Elliptic Curve Diffie-Hellman (ECDH) operation with the cloud authenticator’s static public key.

### Message B: Cloud Authenticator (e, ee) to Chrome

The cloud authenticator responds with its own ephemeral public key and performs a second ECDH operation using Chrome’s ephemeral key. To this message, the cloud authenticator also attaches an attestation signature for its [Oak execution environment](https://github.com/project-oak/oak/tree/main/oak_functions), intended to allow the client to verify that it is communicating with a trusted authenticator. We did not observe where, or if, Chrome validates this attestation.

After the handshake messages are exchanged, Chrome and the cloud authenticator share a symmetric transport key and a handshake hash. Chrome can then send requests over the secure tunnel, each signed with a device key bound to the handshake.

### Device Key Signature

The device-to-cloud request is signed with one of the device’s hardware-backed keys. (The only exception is the initial onboarding message, which carries the device public keys.)

For each request, Chrome determines which device key to use based on the context. When WebAuthn’s [user verification](https://w3c.github.io/webauthn/#dom-authenticatorselectioncriteria-userverification) is required or preferred, Chrome signs the request with the UV key, prompting the local user to verify before signing. When user verification is discouraged, Chrome uses the identity key instead.

To bind each request to the active Noise session, Chrome creates a signature over both a serialized Concise Binary Object Representation ([CBOR)-encoded](https://cbor.io/) request and the handshake hash. The signature not only proves the device's hardware identity and the integrity of the requested message, but also binds it to the current encrypted session.

Below is an example using a passkeys/assert request. (Other device-to-cloud authenticator requests follow a similar structure, with the request fields changed.)

requests = {

"cmd": "passkeys/assert",

"request": {rpId, challenge, userVerification,..,}

"protobuf": WebauthnCredentialSpecifics,

"wrapped\_secret": wrapped\_secret,

"client\_data\_json": clientDataJSON

}

serialized\_requests = CBOR.encode([requests])

serialized\_requests\_hash = sha256(serialized\_requests)

to\_sign\_message = handshake\_hash || serialized\_requests\_hash

#### Using Windows TPM-Backed Keys for the Signature

For the identity key, Chrome signs the message [using](https://source.chromium.org/chromium/chromium/src/+/main:crypto/unexportable_key_win.cc) the Windows Cryptography Next Generation (CNG) [API](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-portal)s:

* [NCryptOpenStorageProvider](https://learn.microsoft.com/en-us/windows/win32/api/ncrypt/nf-ncrypt-ncryptopenstorageprovider): Opens the MS\_PLATFORM\_CRYPTO\_PROVIDER
* [NCryptImportKey](https://learn.microsoft.com/en-us/windows/win32/api/ncrypt/nf-ncrypt-ncryptimportkey): Imports and unseals the wrapped\_identity\_private\_key within the TPM
* [NCryptSignHash](https://learn.microsoft.com/en-us/windows/win32/api/ncrypt/nf-ncrypt-ncryptsignhash): produces the signature on the message using the imported key

When Chrome needs to sign with the UV key, it calls [RequestSignAsync](https://learn.microsoft.com/en-us/uwp/api/windows.security.credentials.keycredential.requestsignasync) using the UV key label loaded from the passkey\_enclave\_state file. Windows Hello handles the user verification step, and after approval, Windows performs the actual signing inside the TPM and returns the resulting signature.

### Encrypting and Sending the Signed Request

With the signature ready, Chrome appends it to the request, encrypts it with the shared transport key and sends it over the WebSocket tunnel.

request\_body\_map = {

"sig": signature,

"device\_id": device\_id,

"auth\_level": "uv", // or "hw" tag if signed with identity key

"encoded\_requests": serialized\_requests

}

encode\_message = CBOR.encode(request\_body\_map)

// Make the final message length a multiple of 32 bytes

message = encode\_message || zero padding || pad\_length\_byte

encypted\_massage = noise.encrypt(message)

websocket.send(encypted\_message)

The cloud authenticator decrypts the message using the shared transport key and verifies the signature using the stored device public key associated with the device\_id. After processing the request, it prepares a CBOR-encoded response and encrypts it with the same transport key, and then sends it back to the client.

## Conclusion

Google Cloud Authenticator marks a fundamental shift in how passkeys are created, protected and used across devices. Passwordless authentication has traditionally followed two distinct paths:

* Hardware-bound keys, which offer strong protection but are locked to a single device
* Software-based keys, which sync easily but are far more vulnerable to theft

The cloud authenticator introduces a new hybrid model. Sensitive key operations are moved to an isolated cloud environment. Every request remains anchored to hardware-backed keys on the user’s device. This approach allegedly preserves hardware-level assurances while enabling the global usability needed for seamless, synchronized cross-device authentication and recovery.

This analysis lays the groundwork for highlighting the strengths of cloud-based authenticators.

It sets the stage for an upcoming third post, where we’ll explore the new attack vectors in passwordless authentication. This includes cloud-based weaknesses that could allow a remote attacker to impersonate an existing synced device and obtain valid passkey authentication.

### Palo Alto Networks Protection and Mitigation

Palo Alto Networks customers are better protected from threats that take advantage of issues with cloud authentication through the following products and services:

Cortex Cloud [Identity Security](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud-Identity-Security) encompasses Cloud Infrastructure Entitlement Management (CIEM), Identity Security Posture Management (ISPM), Data Access Governance (DAG) and Identity Threat Detection and Response (ITDR). It provides clients with the necessary capabilities to improve their identity-related security requirements. By providing Cortex Cloud visibility into which identities are adding devices or altering their permissions within cloud environments, Cortex Cloud can accurately detect misconfigurations, unwanted access to sensitive data and real-time analysis surrounding usage and access patterns.

[CyberArk Identity Protection](https://docs.cyberark.com/identity/latest/en/content/coreservices/authenticate/configure-passkey.htm) continuously maps authentication configurations and access posture across your human identity environment. It surfaces risks that passwordless deployments can obscure: accounts missing phishing-resistant MFA, misconfigured OAuth token lifetimes, dormant identities with persistent access, and privilege gaps lacking just-in-time controls. Its threat detection capabilities monitor for anomalous authentication patterns and suspicious access behaviors in real time. This enables security teams to identify and respond to identity-based attacks before they escalate, including cases where the initial access vector exploits trusted authentication flows like passkeys or synced credentials.

[Unit 42 Cloud Security Assessment](https://www.paloaltonetworks.com/unit42/assess/cloud-security-assessment) is an evaluation service that reviews cloud infrastructure to identify misconfigurations and security gaps.

If you think you may have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

* North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
* UK: +44.20.3743.3660
* Europe and Middle East: +31.20.299.3130
* Asia: +65.6983.8730
* Japan: +81.50.1790.0200
* Australia: +61.2.4062.7950
* India: 000 800 050 45107
* South Korea: +82.080.467.8774

Palo Alto Networks has shared these findings with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://www.cyberthreatalliance.org).

## Additional Resources

* [The Art of the Invisible Key: Passkey Global Breakthrough](https://www.cyberark.com/resources/threat-research-blog/the-art-of-the-invisible-key-passkey-global-breakthrough) – CyberArk
* [Bypassing Windows Hello Without Masks or Plastic Surgery](https://www.cyberark.com/resources/threat-research-blog/bypassing-windows-hello-without-masks-or-plastic-surgery) – CyberArk

Back to top

### Tags

* [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")
* [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/ "google authenticator")
* [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/ "Google Chrome")
* [Identity](https://unit42.paloaltonetworks.com/tag/identity/ "identity")
* [Passkey](https://unit42.paloaltonetworks.com/tag/passkey/ "passkey")
* [Passwordless](https://unit42.paloaltonetworks.com/tag/passwordless/ "passwordless")

[Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
[Next: Who’s Really Shopping? Retail Fraud in the Age of Agentic AI](https://unit42.paloaltonetworks.com/retail-fraud-agentic-ai/ "Who’s Really Shopping? Retail Fraud in the Age of Agentic AI")

### Table of Contents

### Related Articles

* [Cracks in the Bedrock: Agent God Mode](https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode/ "article - table of contents")
* [Taming Agentic Browsers: Vulnerability in Chrome Allowed Extensions to Hijack New Gemini Panel](https://unit42.paloaltonetworks.com/gemini-live-in-chrome-hijacking/ "article - table of contents")
* [The Next Frontier of Runtime Assembly Attacks: Leveraging LLMs to Generate Phishing JavaScript in Real Time](https://unit42.paloaltonetworks.com/real-time-malicious-javascript-through-llms/ "article - table of contents")

## Related Cloud Cybersecurity Research Resources

![Pictorial representation of autonomous AI attack in cloud environments. Digital illustration of a glowing blue brain connected to a network of lines and lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/12_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 23, 2026
[#### Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/)

* [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
* [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/ "Cloud")
* [Data exfiltration](https://unit42.paloaltonetworks.com/tag/data-exfiltration/ "data exfiltration")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/ "Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System")

![Close-up of a black woman with glasses examining colorful computer code on a screen. The scene is illuminated by various lights, creating a focused and analytical atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/13_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) February 6, 2026
[#### Novel Technique to Detect Cloud Threat Actor Operations](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/)

* [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
* [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")
* [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/ "MITRE")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/ "Novel Technique to Detect Cloud Threat Actor Operations")

![Pictorial representation of Azure OpenAI DNS resolution issue. Futuristic cityscape illustration with luminous structures and floating cloud elements, showcasing advanced technology and a dynamic, digitally enhanced environment.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/02_DNS_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) January 20, 2026
[#### DNS OverDoS: Are Private Endpoints Too Private?](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/)

* [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
* [Networking](https://unit42.paloaltonetworks.com/tag/networking/ "networking")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/ "DNS OverDoS: Are Private Endpoints Too Private?")

![Pictorial representation of cloud discovery with AzureHound. A digital representation of a cloud composed of blue light particles, superimposed over a blurred background of server racks in a data center.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/08_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) October 24, 2025
[#### Cloud Discovery With AzureHound](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/)

* [Control plane](https://unit42.paloaltonetworks.com/tag/control-plane/ "control plane")
* [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
* [Data plane](https://unit42.paloaltonetworks.com/tag/data-plane/ "data plane")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/ "Cloud Discovery With AzureHound")

![Pictorial representation of a gift card fraud campaign. A glowing skull and crossbones on a circuit board.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/07_Cybercrime_Category_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) October 22, 2025
[#### Jingle Thief: Inside a Cloud-Based Gift Card Fraud Campaign](https://unit42.paloaltonetworks.com/cloud-based-gift-card-fraud-campaign/)

* [CL‑CRI‑1032](https://unit42.paloaltonetworks.com/tag/cl-cri-1032/ "CL‑CRI‑1032")
* [Microsoft](https://unit42.paloaltonetworks.com/tag/microsoft/ "Microsoft")
* [Phishing](https://unit42.paloaltonetworks.com/tag/phishing/ "phishing")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/cloud-based-gift-card-fraud-campaign/ "Jingle Thief: Inside a Cloud-Based Gift Card Fraud Campaign")

![Pictorial representation of a vibrant cityscape emerging from a sea of clouds under a sunset sky.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/09/02_Cloud_cybersecurity_research_Category_1505x922-718x440.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/Insights-icon-white.svg)Insights](https://unit42.paloaltonetworks.com/category/insights/) October 7, 2025
[#### Responding to Cloud Incidents: A Step-by-Step Guide From the 2025 Unit 42 Global Incident Response Report](https://unit42.paloaltonetworks.com/responding-to-cloud-incidents/)

* [Cloud Infrastructure Protection](https://unit42.paloaltonetworks.com/tag/cloud-infrastructure-protection/ "Cloud Infrastructure Protection")
* [Cloud Security](https://unit42.paloaltonetworks.com/tag/cloud-security/ "Cloud Security")
* [Unit 42 Incident Response Report](https://unit42.paloaltonetworks.com/tag/unit-42-incident-response-report/ "Unit 42 Incident Response Report")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/responding-to-cloud-incidents/ "Responding to Cloud Incidents: A Step-by-Step Guide From the 2025 Unit 42 Global Incident Response Report")

![Pictorial representation of model namespace reuse. A vibrant digital illustration featuring a glowing cloud icon with a padlock, symbolizing cloud security technology, set against a backdrop of glowing circuit lines in blue and orange.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/05_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 3, 2025
[#### Model Namespace Reuse: An AI Supply-Chain Attack Exploiting Model Name Trust](https://unit42.paloaltonetworks.com/model-namespace-reuse/)

* [Azure](https://unit42.paloaltonetworks.com/tag/azure/ "Azure")
* [GenAI](https://unit42.paloaltonetworks.com/tag/genai/ "GenAI")
* [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/model-namespace-reuse/ "Model Namespace Reuse: An AI Supply-Chain Attack Exploiting Model Name Trust")

![Futuristic illustration with glowing neon lights and advanced technology motifs, depicting cloud computing and data flow through interconnected networks. The scene is highlighted by hovering digital clouds and dynamic, illuminated linear structures, set in a dramatic, blue and orange color scheme.](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/03_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) July 22, 2025
[#### Cloud Logging for Security and Beyond](https://unit42.paloaltonetworks.com/cloud-logging-for-security/)

* [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
* [Azure](https://unit42.paloaltonetworks.com/tag/azure/ "Azure")
* [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/ "Cloud")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/cloud-logging-for-security/ "Cloud Logging for Security and Beyond")

![Pictorial representation of serverless tokens in the cloud. East Asian woman examining data on multiple screens in a high-tech environment, surrounded by digital graphics and code.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/07_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 13, 2025
[#### Serverless Tokens in the Cloud: Exploitation and Detections](https://unit42.paloaltonetworks.com/serverless-authentication-cloud/)

* [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
* [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
* [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/ "Google Cloud")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/serverless-authentication-cloud/ "Serverless Tokens in the Cloud: Exploitation and Detections")

* ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
* ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)

![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg)
![Enlarged Image]()
