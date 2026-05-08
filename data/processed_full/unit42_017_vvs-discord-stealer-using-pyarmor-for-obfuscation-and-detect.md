---
title: "VVS Discord Stealer Using Pyarmor for Obfuscation and Detection Evasion"
date: "2026-01-02"
url: https://unit42.paloaltonetworks.com/vvs-stealer/
source: unit42
---

# VVS Discord Stealer Using Pyarmor for Obfuscation and Detection Evasion

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
* [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
* [Malware](https://unit42.paloaltonetworks.com/category/malware/ "Malware")

[Malware](https://unit42.paloaltonetworks.com/category/malware/)

# VVS Discord Stealer Using Pyarmor for Obfuscation and Detection Evasion

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg)  11  min read

Related Products

[![Advanced DNS Security icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced DNS Security](https://unit42.paloaltonetworks.com/product-category/advanced-dns-security/ "Advanced DNS Security")[![Advanced URL Filtering icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced URL Filtering](https://unit42.paloaltonetworks.com/product-category/advanced-url-filtering/ "Advanced URL Filtering")[![Advanced WildFire icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced WildFire](https://unit42.paloaltonetworks.com/product-category/advanced-wildfire/ "Advanced WildFire")[![Cortex XDR icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XDR](https://unit42.paloaltonetworks.com/product-category/cortex-xdr/ "Cortex XDR")[![Cortex XSIAM icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XSIAM](https://unit42.paloaltonetworks.com/product-category/cortex-xsiam/ "Cortex XSIAM")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

* ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

  By:
  + [Pranay Kumar Chhaparwal](https://unit42.paloaltonetworks.com/author/pranay-kumar-chhaparwal/)
  + [Lee Wei Yeong](https://unit42.paloaltonetworks.com/author/lee-wei-yeong/)
* ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

  Published:January 2, 2026
* ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

  Categories:
  + [Malware](https://unit42.paloaltonetworks.com/category/malware/)
  + [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)
* ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

  Tags:
  + [Discord](https://unit42.paloaltonetworks.com/tag/discord/)
  + [Infostealer](https://unit42.paloaltonetworks.com/tag/infostealer/)
  + [Python](https://unit42.paloaltonetworks.com/tag/python/)
  + [Telegram](https://unit42.paloaltonetworks.com/tag/telegram/)

* [![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/vvs-stealer/?pdf=download&lg=en&_wpnonce=9711c8889b "Click here to download")
* [![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/vvs-stealer/?pdf=print&lg=en&_wpnonce=9711c8889b "Click here to print")

[Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)](# "Click here to share")

* [![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)](# "Copy link")
* [![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=VVS%20Discord%20Stealer%20Using%20Pyarmor%20for%20Obfuscation%20and%20Detection%20Evasion&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fvvs-stealer%2F "Share in email")
* [![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fvvs-stealer%2F "Share in Facebook")
* [![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fvvs-stealer%2F&title=VVS%20Discord%20Stealer%20Using%20Pyarmor%20for%20Obfuscation%20and%20Detection%20Evasion "Share in LinkedIn")
* [![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fvvs-stealer%2F&text=VVS%20Discord%20Stealer%20Using%20Pyarmor%20for%20Obfuscation%20and%20Detection%20Evasion "Share in Twitter")
* [![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fvvs-stealer%2F "Share in Reddit")
* [![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=VVS%20Discord%20Stealer%20Using%20Pyarmor%20for%20Obfuscation%20and%20Detection%20Evasion%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fvvs-stealer%2F "Share in Mastodon")

## Executive Summary

This article details our technical analysis of VVS stealer, also styled VVS $tealer, including its distributors’ use of obfuscation and detection evasion.

The stealer is written in Python and targets Discord users, exfiltrating sensitive information like credentials and tokens stored in Discord accounts. This stealer was once in active development and marketed for sale on Telegram as early as April 2025.

VVS stealer's code is obfuscated by [Pyarmor](https://github.com/dashingsoft/pyarmor). This tool is used to obfuscate Python scripts to hinder static analysis and signature-based detection. Pyarmor can be used for legitimate purposes and also leveraged to build stealthy malware.

Malware authors are increasingly leveraging advanced obfuscation techniques to evade detection by cybersecurity tools, making their malicious software harder to analyze and reverse-engineer. This article shows how we deobfuscated VVS stealer samples to better understand its operations.

Because Python is easy for malware authors to use and the complex obfuscation used by this threat, the result is a highly effective and stealthy malware family.

Palo Alto Networks customer are better protected through the following products and services:

* [Advanced WildFire](https://docs.paloaltonetworks.com/wildfire)
* [Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering/administration) and [Advanced DNS Security](https://docs.paloaltonetworks.com/dns-security)
* [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM) prevents the threats described in this article by employing the [Malware Prevention Engine](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-4.x-Documentation/Malware-protection)

If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

|  |  |
| --- | --- |
| **Related Unit 42 Topics** | [**Infostealer**](https://unit42.paloaltonetworks.com/tag/Infostealer)**,** [**Anti-analysis**](https://unit42.paloaltonetworks.com/tag/anti-analysis/) |

## Introduction

Discord is a social messaging and communications platform that has become a popular target for malware, like VVS stealer. VVS stealer is designed to steal a victim's Discord information and browser data.

Figure 1 shows VVS stealer's advertised capabilities, including:

* Stealing Discord data (tokens and account information)
* Intercepting active Discord sessions via injection
* Extracting web browser data (cookies, passwords, browsing history and autofill details)

![Screenshot collage of a computer screen displaying information about "VS Stealer on Telegram," talking about its use as a hacking tool, with features listed and pricing details. Also visible is a Telegram contact link for further communication.]()

Figure 1. VVS stealer advertisement, focused on Telegram.

The stealer also achieves persistence by automatically installing itself on startup. It operates stealthily by displaying fake error messages and capturing screenshots. For a deeper investigation into the operation, please refer to the article by DeepCode, [Investigating VVS $tealer: A Python-Based Discord Malware](https://decodecybercrime.com/investigating-vvs-tealer-a-python-based-discord-malware).

## Technical Analysis

This section analyzes a Pyarmor-protected VVS stealer malware sample with the following SHA-256 hash:

* c7e6591e5e021daa30f949a6f6e0699ef2935d2d7c06ea006e3b201c52666e07

Figure 2 shows a summary diagram illustrating the entire sample analysis workflow.

![Flowchart showing the process of extracting Python bytecode from a PyInstaller executable, decompiling it to Python source code, and decrypting Pyarmor bytecode to ELF.]()

Figure 2. Overview of the workflow for analyzing the VVS stealer malware sample.

### Step One: Extracting From the PyInstaller Binary

The sample we analyzed is distributed as a [PyInstaller](https://pyinstaller.org) package. PyInstaller is a tool that bundles a Python application and its dependencies into a package to allow execution of a packaged app without installing additional modules.

Any standard PyInstaller installation ships with the built-in utility [pyi-archive\_viewer](https://pyinstaller.org/en/stable/advanced-topics.html#using-pyi-archive-viewer). We used this utility to extract and inspect the following files from our sample:

* The Python bytecode file named vvs
* The Pyarmor runtime dynamic-link library (DLL) file named pyarmor\_runtime.pyd, located under subfolder pyarmor\_runtime\_007444
  + The accompanying \_\_init\_\_.py file within this same subfolder, which includes the following information:
    - Pyarmor version: 9.1.4 ([Pro](https://pyarmor.readthedocs.io/en/latest/licenses.html#license-types))
    - Unique license number: 007444
    - Timestamp: 2025-04-27T11:04:52.523525
    - Product name: vvs
* Python 3.11 DLL file named python311.dll
  + The file version information indicates the Python version is 3.11.5

PyInstaller stores Python bytecode (listed as 1.) in its raw form. This raw form refers to the bytecode sequence beginning with the value e3. The value e3 is a combination of both flag and type, combined via the constant FLAG\_REF.

The type represented by the value e3 is computed as: type = e3 & ~FLAG\_REF. This means the value e3 is actually the type 0x63 (the letter c), also known as the enumeration constant TYPE\_CODE. The full implementation of this derivation can be found in the [CPython 3.11 codebase](https://github.com/python/cpython/blob/3.11/Python/marshal.c).

Figure 3 below shows this code object serialized by the [marshal](https://docs.python.org/3/library/marshal.html) module is bare, missing an accompanying 16-byte header (marked in blue). To provide enough Python for the decompiler not to reject the file, we need to restore at least one of the header values (Python 3.11.5 magic number in 4-byte, little-endian format) prior to decompilation, because the Python decompiler expects a valid Python bytecode (.pyc) file as its input.

![Hexadecimal data visualization showing rows of hex codes with some values highlighted.]()

Figure 3. Python bytecode (.pyc) file named vvs, with its header restored.

We begin our analysis by decompiling the Python bytecode .pyc) file named vvs to recover its equivalent Python source code (.py).

### Step Two: Decompiling to Python Source Code

[Pycdc](https://github.com/zrax/pycdc) is a Python bytecode decompiler written in C++. It is part of the Decompyle++ project. It supports decompiling Python 3.11 bytecode “back into valid and human-readable Python source code.” (Source: [GitHub](https://github.com/zrax/pycdc/blob/master/README.markdown).) [PyLingual](https://pylingual.io) is another Python bytecode decompiler.

After cloning the code repository and compiling the codebase, the generated executable can be invoked as follows to decompile Python bytecode to Python source code via Pycdc:

* pycdc.exe -c -v "3.11.5" "vvs.pyc" > "vvs.py"

This will produce the decompiled Python source code shown in Figure 4.

![Screenshot of a line of Python code involving an import statement from a library named "pyarmor," with obscured additional text.]()

Figure 4. Decompiled vvs Python source code.

We then analyze the last function argument, which can be extracted via Python 3's [ast.NodeVisitor](https://docs.python.org/3/library/ast.html#ast.NodeVisitor).

### Step Three: Unraveling Pyarmor Obfuscation

The payload begins with the Pyarmor header shown in Figure 5.

![A screenshot displaying a section of a hexadecimal code with ASCII characters on the right side, including a visible string "PY00744...]()

Figure 5. Pyarmor header, with particular fields of interest highlighted.

Cryptography is performed throughout using the Advanced Encryption Standard (AES) algorithm with a 128-bit key, operating in Counter (CTR) mode with an initial value of two (i.e., AES-128-CTR). Table 1 shows the breakdown of the fields.

|  |  |  |
| --- | --- | --- |
| **Offsets** | **Values** | **Description** |
| 0x00 … 0x07 | PY007444 | File signature containing the unique license number |
| 0x09 | 03 | Python major version |
| 0x0a | 0b | Python minor version |
| 0x14 | 09 | Protection type:  * 09 if Pyarmor [BCC mode](https://pyarmor.readthedocs.io/en/stable/topic/bccmode.html) (briefly explained in the next section) is enabled * 08 otherwise |
| 0x1c … 0x1f | 40 00 00 00 | Start of the ELF payload, in little-endian format |
| 0x24 … 0x27 | 12 c9 06 00 | First four bytes of the AES-128-CTR nonce |
| 0x2c … 0x33 | dc d2 98 a1 ea 11 fd f4 | Remaining eight bytes of the AES-128-CTR nonce |
| 0x38 … 0x3b | a0 7f 02 00 | End of the ELF payload, in little-endian format |

Table 1. Breakdown of fields present in the Pyarmor header.

This same pattern (highlighted in yellow) repeats itself once again after the end of the ELF payload, for extracting and decrypting the Pyarmor bytecode payload.

#### BCC Mode

BCC (likely an abbreviation of ByteCode-to-Compilation) mode converts most “functions and methods in the scripts to equivalent C functions. Those C functions will be compiled to machine instructions directly, then called by obfuscated scripts.” (Source: [Pyarmor documentation](https://pyarmor.readthedocs.io/en/stable/topic/bccmode.html).)

BCC mode is invoked as follows: pyarmor gen --enable-bcc script.py.

These converted C functions are stored in a separate ELF file, produced alongside the Pyarmor-marshaled bytecode.

The mapping of Python constants to BCC functions can be obtained using this [implementation](https://github.com/GDATAAdvancedAnalytics/Pyarmor-Tooling/blob/main/bcc_info.py). For instance, in the Python method get\_encryption\_key(browser\_path), the constant \_\_pyarmor\_bcc\_58580\_\_ maps to the BCC function bcc\_180, whose function body is located at offset 0x4e70 of the ELF file.

Referencing [this analysis](https://cyber.wtf/2025/05/30/pyarmor-bcc-notes) of the ELF file contents, especially the bcc\_ftable structure, Figure 6 shows part of the BCC function bcc\_180 decompiled:

![Screenshot depicting two side-by-side images of complex Python code examples on a computer screen.]()

Figure 6. Decompilation of the BCC function bcc\_180.

We can roughly recover an equivalent of the original code of the Python method get\_encryption\_key, as shown in Figure 7.

![Screenshot of Python code in a text editor, showing a function to retrieve the decryption key for Chromium browsers with highlighted syntax.]()

Figure 7. Equivalent Python code of the get\_encryption\_key method.

#### Marshaled Bytecode Format

Pyarmor 9 marshaled bytecode differs from standard Python 3.11 bytecode in several ways. Firstly, the 0x20000000 bit is set in the co\_flags field to indicate that it is Pyarmor obfuscated. Secondly, there is an extra data field, whose length is denoted by the value of its first byte.

Moreover, [deopt\_code()](https://github.com/python/cpython/blob/3.11/Objects/codeobject.c#L1473) needs to be disabled for the bytecode sequence to be successfully decrypted. We will discuss the cryptographic parameters in a later section of this article.

#### Code Object Structure

Pyarmor code objects are specially crafted, in that they should contain certain artifacts. It is common to expect to find the LOAD\_CONST \_\_pyarmor\_enter\_\*\_\_ instruction in the preamble and the LOAD\_CONST \_\_pyarmor\_exit\_\*\_\_ instruction in the trailer of the disassembly. These two instructions would wrap the encrypted bytecode, as shown in Table 2.

|  |  |
| --- | --- |
| **Operation** | **Argument** |
| … | |
| LOAD\_CONST | \_\_pyarmor\_enter\_58592\_\_ |
| LOAD\_CONST | \x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x20\x16\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 |
| … encrypted bytecode sequence (to be examined in the next section) … | |
| LOAD\_CONST | \_\_pyarmor\_exit\_58593\_\_ |
| LOAD\_CONST | \x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x20\x16\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 |
| … | |

Table 2. Pyarmor-related instructions in the disassembly listing of <module>.

Once the encrypted bytecode sequence is decrypted, it could reveal encrypted strings or BCC function invocations. Encrypted strings (reviewed in a later section of this article) are preceded by a LOAD\_CONST \_\_pyarmor\_assert\_\*\_\_ instruction. There is also the LOAD\_CONST \_\_pyarmor\_bcc\_\*\_\_ instruction to invoke a BCC function (reviewed earlier in this article).

#### Code Object Encryption

Bytecode sequences between the start marker (\_\_pyarmor\_enter\_\*\_\_) and the end marker (\_\_pyarmor\_exit\_\*\_\_) are AES-128-CTR encrypted. The associated AES key (273b1b1373cf25e054a61e2cb8a947b8) [is extracted from](https://github.com/Lil-House/Pyarmor-Static-Unpack-1shot/blob/main/helpers/runtime.py) the Pyarmor runtime DLL linked to the unique license number.

On the other hand, the corresponding AES nonce exclusive OR (XOR) key (2db99d18a0763ed70bbd6b3c) is only specific to the Pyarmor bytecode payload, for which there [is an implementation](https://github.com/Lil-House/Pyarmor-Static-Unpack-1shot/blob/main/pyc_module.cpp#L360) of the logic for extracting this value. This key is XORed with the 12 bytes at the end marker (\_\_pyarmor\_exit\_\*\_\_) to produce the correct AES nonce used in the decryption.

#### String Encryption

Similarly, string constants longer than eight characters are AES-128-CTR encrypted (known as ["mixed" in Pyarmor terminology](https://pyarmor.readthedocs.io/en/latest/tutorial/obfuscation.html#more-options-to-protect-script)”). The associated AES key is also 273b1b1373cf25e054a61e2cb8a947b8, but this time, the corresponding AES nonce (692e767673e95c45a1e6876d) [is computed from](https://github.com/Lil-House/Pyarmor-Static-Unpack-1shot/blob/main/helpers/runtime.py) the Pyarmor runtime DLL linked to the unique license number.

Additionally, a 0x81 prefix value denotes that the string constant is encrypted. Otherwise, a 0x01 prefix value is used instead.

Now that the Pyarmor protection is disarmed, we shall proceed to cover some of the key capabilities of the VVS stealer in the next section.

## Malware Capabilities

With the layers of Pyarmor obfuscation — including the BCC mode and AES-128-CTR string encryption — successfully stripped away, we were able to expose the underlying Python logic. This deobfuscated code revealed a stealer designed not just for data exfiltration, but for active session hijacking and persistence. The following section details the specific operational capabilities of the VVS stealer that were uncovered during this analysis.

The malware sample expires after 2026-10-31 23:59:59. It will stop working by terminating itself prematurely.

The malware sample performs all HTTP requests by sending the fixed User-Agent string Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36.

We shall now provide an overview of the main malware capabilities, as advertised on Telegram.

### Discord Data

The malware sample first searches for potential encrypted Discord tokens. Encrypted Discord tokens are strings beginning with the prefix [dQw4w9WgXcQ:](https://reddit.com/r/discordapp/comments/tyb1u0/discord_easter_egg_all_encrypted_discord_tokens). The malware sample uses regular expressions to form a pattern from this string prefix. It then uses this pattern to search inside the contents of files with the .ldb or .log file extensions, stored within the [LevelDB](https://en.wikipedia.org/wiki/LevelDB) directory.

Next, the malware sample decrypts the encrypted\_key value in the Local State file, via the [Data Protection Application Programming Interface (DPAPI)](https://en.wikipedia.org/wiki/Data_Protection_API). With this decrypted encrypted\_key value as the AES key parameter, the malware sample applies the AES algorithm, operating in Galois/Counter Mode (GCM) mode, on the encrypted Discord tokens, to decrypt them.

The malware sample then uses the decrypted Discord tokens to query various Discord application programming interface (API) endpoints for user information, including:

* [Nitro](https://discord.com/nitro) subscription (Discord Premium features)
* Payment methods
* User ID
* Username
* Email
* Phone number
* Friends
* Guilds
* Multifactor authentication (MFA) status
* Locale
* Verification status
* Avatar image
* IP address (via the [ipify](https://ipify.org) service)
* Computer name

After gathering all this information, the malware sample proceeds to exfiltrate it in JavaScript Object Notation (JSON) format. The exfiltration takes place via HTTP POST requests to the predefined webhook endpoints (%WEBHOOK% environment variable and hard-coded fall back URLs).

Webhooks are “a low-effort way to post messages to channels in Discord. They do not require a bot user or authentication to use.” (Source: [Discord Developer Portal](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).)

### Discord Injection

The code responsible for this functionality is in class Inj, likely an abbreviation of Injection.

In this class, the malware sample first kills running Discord application processes, if any are running. It then downloads the JavaScript (JS) payload from a remote file named injection-obf.js (the -obf suffix likely stands for an obfuscated version of the script), replacing the webhook endpoint URL and discord\_desktop\_core, into the Discord application directory. This JS file is obfuscated by the [JavaScript Obfuscator Tool](https://obfuscator.io) and can be deobfuscated via the [Obfuscator.io Deobfuscator](https://obf-io.deobfuscate.io).

Some of the main functionality of the injected JS code is highlighted in the following screenshots, starting with its configuration and exfiltration code snippets, shown in Figure 8.

![Screenshot of a JavaScript configuration file involving URLs and paths related to a Discord API and a remote authorization gateway. The code is displayed in a text editor with syntax highlighting.]()

Figure 8. Injected JS configuration and exfiltration.

Figure 8 shows the injected JS code responsible for establishing persistence in the Discord application, based on the [Electron](https://electronjs.org) framework. This framework uses Atom Shell Archive Format ([ASAR](https://electronjs.org/docs/latest/tutorial/asar-archives)) archives to bundle the entire application's codebase into a single file, shown in Figure 9.

![Screenshot of a code snippet related to a software initialization function, mentioning paths and configuration for "app.js", "index.js", and "discord.js". The code is written in JavaScript.]()

Figure 9. Injected JS code to perform persistence.

Figure 10 shows the injected JS code responsible for monitoring network traffic via the [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/tot/Network) (CDP).

![Screenshot of software code in an editor, displaying a network-related JavaScript function.]()

Figure 10. Injected JS code to monitor network traffic.

Figure 11 shows supporting utility functions and event hooks in the injected JS code. Event hooks are callback functions that execute upon the Discord application user performing a specific action. The actions of interest are when the user views their backup codes, changes their password or adds a payment method. The callback functions linked to these actions are capable of collecting Discord user account and billing information.

![Screenshot of a computer code editor displaying multiple lines of JavaScript code, involving functions related to user data handling and API requests.]()

Figure 11. Injected JS code of utility functions and event hooks.

Thereafter, the malware sample restarts a compromised Discord application process via Update.exe, which it does with the command-line switch --processStart.

### Web Browser Data

The malware sample targets a list of web browser applications, including:

* Chrome
* Edge
* 7Star
* Amigo
* Brave
* CentBrowser
* Discord
* Epic Privacy Browser
* Iridium
* Kometa
* Lightcord
* Mozilla Firefox
* Opera
* Orbitum
* Sputnik
* Torch
* Uran
* Vivaldi
* Yandex

To these targets, the malware sample extracts the following data, where present:

* Autofill
* Cookies
* History
* Passwords

Once these data are extracted, the malware sample prepares it for exfiltration by compressing it into a single ZIP archive file named <USERNAME>\_vault.zip. It then exfiltrates this file via HTTP POST requests to the predefined webhook endpoints, similar to the Discord data exfiltration process.

### Startup Persistence

The malware sample copies itself to the %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup folder to achieve startup persistence. The malware remains on the user’s device, enabling it to continue exfiltrating data if, for example, the user attempts to install a fresh copy of the Discord application.

### Fake Error

The malware sample uses the Win32 API, specifically the MessageBoxW function in the User32.dll library, to display a modal message box about a fake fatal error that requires restarting the computer. A modal message box is a small dialog window requiring user interaction before the application can continue, as shown in Figure 12.

![Error message dialog box displaying "Fatal Error" with error code 0x80070002 and a suggestion to restart the computer. An "OK" button is present for acknowledgement.]()

Figure 12. A fake message box instructing the victim to restart the computer.

## Conclusion

VVS stealer demonstrates how tools like Pyarmor, which can be used for legitimate purposes, can also be leveraged to build stealthy malware aimed at hijacking credentials for popular platforms such as Discord. Its emergence signals a need for defenders to strengthen monitoring around credential theft and account abuse.

### Palo Alto Networks Protection and Mitigation

Palo Alto Networks customers are better protected from the threats discussed above through the following products:

The [Advanced WildFire](https://docs.paloaltonetworks.com/wildfire) machine-learning models and analysis techniques have been reviewed and updated in light of the indicators shared in this research.

[Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering/administration) and [Advanced DNS Security](https://docs.paloaltonetworks.com/dns-security) identify known domains and URLs associated with this activity as malicious.

[Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM) prevents the threats described in this article by employing the [Malware Prevention Engine](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-4.x-Documentation/Malware-protection). This approach combines several layers of protection, including [Advanced WildFire](https://docs.paloaltonetworks.com/wildfire), Behavioral Threat Protection and the Local Analysis module, to prevent both known and unknown malware from causing harm to endpoints.

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

## Indicators of Compromise

SHA-256 hashes of malware samples:

* 307d9cefa7a3147eb78c69eded273e47c08df44c2004f839548963268d19dd87
* 7a1554383345f31f3482ba3729c1126af7c1d9376abb07ad3ee189660c166a2b
* c7e6591e5e021daa30f949a6f6e0699ef2935d2d7c06ea006e3b201c52666e07

Discord webhook URLs

* hxxps[://]ptb.discord[.]com/api/webhooks/1360401843963826236/TkFvXfHFXrBIKT3EaqekJefvdvt39XTAxeOIWECeSrBbNLKDR5yPcn75uIqKEzdfs9o2
* hxxps[://]ptb.discord[.]com/api/webhooks/1360259628440621087/YCo9eVnIBOYSMn8Xr6zX5C7AJF22z26WljaJk4zr6IiThnUrVyfWCZYs6JjSC12IC8c0

## Additional Resources

* [Unpacking Pyarmor v8+ scripts](https://cyber.wtf/2025/02/12/unpacking-pyarmor-v8-scripts) – Leonard Rapp and Hendrik Eckardt, G DATA Advanced Analytics GmbH
* [Obfuscated Malicious Python Scripts with PyArmor](https://isc.sans.edu/diary/31840) – Xavier Mertens, SANS Internet Storm Center

Back to top

### Tags

* [Discord](https://unit42.paloaltonetworks.com/tag/discord/ "Discord")
* [Infostealer](https://unit42.paloaltonetworks.com/tag/infostealer/ "Infostealer")
* [Python](https://unit42.paloaltonetworks.com/tag/python/ "Python")
* [Telegram](https://unit42.paloaltonetworks.com/tag/telegram/ "Telegram")

[Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
[Next: Who Does Cybersecurity Need? You!](https://unit42.paloaltonetworks.com/cybersecurity-is-for-everyone/ "Who Does Cybersecurity Need? You!")

### Table of Contents

### Related Articles

* [That AI Extension Helping You Write Emails? It’s Reading Them First](https://unit42.paloaltonetworks.com/high-risk-gen-ai-browser-extensions/ "article - table of contents")
* [Weaponizing the Protectors: TeamPCP’s Multi-Stage Supply Chain Attack on Security Infrastructure](https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/ "article - table of contents")
* [Analyzing the Current State of AI Use in Malware](https://unit42.paloaltonetworks.com/ai-use-in-malware/ "article - table of contents")

## Related Malware Resources

![Pictorial representation of the npm packages supply chain attack. Screen displaying code with a prominent alert symbol and the words 'VIRUS DETECTED' highlighted in red.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/05_Malware_Category_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) May 1, 2026
[#### The npm Threat Landscape: Attack Surface and Mitigations (Updated May 1)](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/)

* [Credential Harvesting](https://unit42.paloaltonetworks.com/tag/credential-harvesting/ "Credential Harvesting")
* [GitHub](https://unit42.paloaltonetworks.com/tag/github/ "GitHub")
* [Npm packages](https://unit42.paloaltonetworks.com/tag/npm-packages/ "npm packages")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/ "The npm Threat Landscape: Attack Surface and Mitigations (Updated May 1)")

![Pictorial representation of high-risk GenAI and agentic browser extensions. A person interacts with a digital screen displaying an AI symbol, circuit patterns, and various technology icons.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/AdobeStock_739390615-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 30, 2026
[#### That AI Extension Helping You Write Emails? It’s Reading Them First](https://unit42.paloaltonetworks.com/high-risk-gen-ai-browser-extensions/)

* [AI browser](https://unit42.paloaltonetworks.com/tag/ai-browser/ "AI browser")
* [Browser extension](https://unit42.paloaltonetworks.com/tag/browser-extension/ "browser extension")
* [GenAI](https://unit42.paloaltonetworks.com/tag/genai/ "GenAI")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/high-risk-gen-ai-browser-extensions/ "That AI Extension Helping You Write Emails? It’s Reading Them First")

![Pictorial representation of AirSnitch attacks on enterprise wireless infrastructure. A globe with the continents illuminated in blue lighting and scattered red lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/11_Security-Technology_Category_1505x922-718x440.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 22, 2026
[#### When Wi-Fi Encryption Fails: Protecting Your Enterprise from AirSnitch Attacks](https://unit42.paloaltonetworks.com/air-snitch-enterprise-wireless-attacks/)

* [AirSnitch](https://unit42.paloaltonetworks.com/tag/airsnitch/ "AirSnitch")
* [MitM](https://unit42.paloaltonetworks.com/tag/mitm/ "MitM")
* [Network security](https://unit42.paloaltonetworks.com/tag/network-security/ "network security")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/air-snitch-enterprise-wireless-attacks/ "When Wi-Fi Encryption Fails: Protecting Your Enterprise from AirSnitch Attacks")

![Pictorial representation of Iran cyber attacks. Close-up of a person wearing glasses, with computer code reflected in the lenses.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/12_Security-Technology_Category_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) April 17, 2026
[#### Threat Brief: Escalation of Cyber Risk Related to Iran (Updated April 17)](https://unit42.paloaltonetworks.com/iranian-cyberattacks-2026/)

* [APK](https://unit42.paloaltonetworks.com/tag/apk/ "APK")
* [DDoS attacks](https://unit42.paloaltonetworks.com/tag/ddos-attacks/ "DDoS attacks")
* [GenAI](https://unit42.paloaltonetworks.com/tag/genai/ "GenAI")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/iranian-cyberattacks-2026/ "Threat Brief: Escalation of Cyber Risk Related to Iran (Updated April 17)")

![Pictorial representation of "Agent God Mode" in Amazon Bedrock AgentCore. A futuristic digital landscape depicting cloud technology with glowing orange and blue circuits. Several cloud icons are connected by circuits, symbolizing a network.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/03_Cloud_cybersecurity_research_Category_1505x922-718x440.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 8, 2026
[#### Cracks in the Bedrock: Agent God Mode](https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode/)

* [Agentcore](https://unit42.paloaltonetworks.com/tag/agentcore/ "agentcore")
* [AI agents](https://unit42.paloaltonetworks.com/tag/ai-agents/ "AI agents")
* [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode/ "Cracks in the Bedrock: Agent God Mode")

![Pictorial representation of the AWS AgentCore Sandbox. Digital illustration of a 3D cloud made up of glowing lights and dots with a padlock on its front. It floats above a glowing network of dots and lines.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/05_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 7, 2026
[#### Cracks in the Bedrock: Escaping the AWS AgentCore Sandbox](https://unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/)

* [Agentcore](https://unit42.paloaltonetworks.com/tag/agentcore/ "agentcore")
* [Agentcore runtime](https://unit42.paloaltonetworks.com/tag/agentcore-runtime/ "agentcore runtime")
* [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/ "Cracks in the Bedrock: Escaping the AWS AgentCore Sandbox")

![](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/03_Malware_Category_1920x900-3-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 6, 2026
[#### Understanding Current Threats to Kubernetes Environments](https://unit42.paloaltonetworks.com/modern-kubernetes-threats/)

* [Audit logs](https://unit42.paloaltonetworks.com/tag/audit-logs/ "audit logs")
* [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/ "Cloud")
* [Containers](https://unit42.paloaltonetworks.com/tag/containers/ "Containers")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/modern-kubernetes-threats/ "Understanding Current Threats to Kubernetes Environments")

![Pictorial representation of Amazon Bedrock's multi-agent applications. A digital illustration depicting complex data flow and connectivity. Numerous lines and nodes extend outward from a central point, resembling a neural network or digital web, against a dark background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/AdobeStock_260323351-2-660x440.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 3, 2026
[#### When an Attacker Meets a Group of Agents: Navigating Amazon Bedrock's Multi-Agent Applications](https://unit42.paloaltonetworks.com/amazon-bedrock-multiagent-applications/)

* [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
* [Amazon](https://unit42.paloaltonetworks.com/tag/amazon/ "Amazon")
* [Bedrock](https://unit42.paloaltonetworks.com/tag/bedrock/ "bedrock")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/amazon-bedrock-multiagent-applications/ "When an Attacker Meets a Group of Agents: Navigating Amazon Bedrock's Multi-Agent Applications")

![Pictorial representation of the supply chain attack compromising Axios. A giant eye made of glowing binary code.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/02_Security-Technology_Category_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) April 1, 2026
[#### Threat Brief: Widespread Impact of the Axios Supply Chain Attack](https://unit42.paloaltonetworks.com/axios-supply-chain-attack/)

* [API attacks](https://unit42.paloaltonetworks.com/tag/api-attacks/ "API attacks")
* [JavaScript](https://unit42.paloaltonetworks.com/tag/javascript/ "JavaScript")
* [PowerShell](https://unit42.paloaltonetworks.com/tag/powershell/ "PowerShell")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/axios-supply-chain-attack/ "Threat Brief: Widespread Impact of the Axios Supply Chain Attack")

![Pictorial representation of TeamPCP. Glowing code on a screen where several word such as Crime, Hackers, and Security are highlighted in a contrasting color.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/03_Cybercrime_Category_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) March 31, 2026
[#### Weaponizing the Protectors: TeamPCP’s Multi-Stage Supply Chain Attack on Security Infrastructure](https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/)

* [CVE-2025-55182](https://unit42.paloaltonetworks.com/tag/cve-2025-55182/ "CVE-2025-55182")
* [GitHub](https://unit42.paloaltonetworks.com/tag/github/ "GitHub")
* [Infostealer](https://unit42.paloaltonetworks.com/tag/infostealer/ "Infostealer")

[Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg)](https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/ "Weaponizing the Protectors: TeamPCP’s Multi-Stage Supply Chain Attack on Security Infrastructure")

* ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
* ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)

![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg)
![Enlarged Image]()
