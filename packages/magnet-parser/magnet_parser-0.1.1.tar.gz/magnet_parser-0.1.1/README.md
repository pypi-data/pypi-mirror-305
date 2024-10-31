# Magnet Parser

A Python library for parsing magnet links and extracting their components, designed to simplify interactions with torrent files.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The Magnet Parser library allows users to decode magnet links, extracting essential metadata such as the info hash, name, and tracker URLs. This functionality is particularly useful for applications that manage or interact with torrent files, enabling seamless integration with torrent clients.

## Installation

To install the `magnet_parser` library, you can use pip:

```bash
pip install magnet-parser
```

```python
from magnet_parser import *

# Example magnet link
magnet_link = "magnet:?xt=urn:btih:93014BF4D458EC39A16C7D3615E3CFBAE42144CC&dn=Winged+Migration+%282001%29+720p+BluRay&tr=http%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2F47.ip-51-68-199.eu%3A6969%2Fannounce"

# Decode the magnet link
decoded = magnet_decode(magnet_link)

# Access the decoded information
print(decoded.__dict__)
```
> Output expected
```json
{
    'xt': 'urn:btih:93014BF4D458EC39A16C7D3615E3CFBAE42144CC',
    'info_hash': '93014bf4d458ec39a16c7d3615e3cfbae42144cc',
    'name': 'Winged Migration (2001) 720p BluRay',
    'tr': [
        'http://p4p.arenabg.com:1337/announce',
        'udp://47.ip-51-68-199.eu:6969/announce',
        'udp://9.rarbg.me:2780/announce',
        ...
    ],
    ...
}
```

### Examples
#### Example 1: Basic Magnet Link
```python
magnet_link = "magnet:?xt=urn:btih:ABC1234567890&dn=Example+File"
decoded = magnet_decode(magnet_link)
print(decoded.name)  # Output: Example File
```
#### Example 2: Magnet Link with Multiple Trackers
```python
magnet_link = "magnet:?xt=urn:btih:DEF9876543210&dn=Another+Example&tr=udp://tracker.example.com:80/announce&tr=http://tracker.example.org:80/announce"
decoded = magnet_decode(magnet_link)
print(decoded.tr)  # Output: ['udp://tracker.example.com:80/announce', 'http://tracker.example.org:80/announce']
```

## just for you to know,

this readme.md file generated with AI chatbot helps, with a few Adjustments from me, for you to getting started.