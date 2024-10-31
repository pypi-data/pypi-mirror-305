import urllib.parse
import argparse
import binascii
import re
from typing import List, Union, Optional

class MagnetData:
    def __init__(self):
        self.xt: Optional[Union[str, List[str]]] = None
        self.info_hash: Optional[str] = None
        self.info_hash_int_array: Optional[bytes] = None
        self.info_hash_v2: Optional[str] = None
        self.info_hash_v2_int_array: Optional[bytes] = None
        self.name: Optional[Union[str, List[str]]] = None
        self.dn: Optional[Union[str, List[str]]] = None
        self.tr: Optional[Union[str, List[str]]] = None
        self.announce: List[str] = []
        self.xs: Optional[Union[str, List[str]]] = None
        self.as_: Optional[Union[str, List[str]]] = None
        self.ws: Optional[Union[str, List[str]]] = None
        self.kt: Optional[List[str]] = None
        self.so: Optional[Union[List[str], List[int]]] = None
        self.x_pe: Optional[Union[str, List[str]]] = None
        self.keywords: Optional[Union[str, List[str]]] = None
        self.ix: Optional[Union[int, List[int]]] = None
        self.xl: Optional[str] = None
        self.url_list: List[str] = []
        self.peer_addresses: List[str] = []
        self.public_key: Optional[str] = None
        self.public_key_int_array: Optional[bytes] = None

start = 'magnet:?'

def magnet_decode(uri: str) -> MagnetData:
    data = uri[uri.index(start) + len(start):]
    params = data.split('&') if data else []

    result = MagnetData()
    
    for param in params:
        keyval = param.split('=')
        if len(keyval) != 2:
            continue

        key = keyval[0]
        val = parse_query_param_value(key, keyval[1])

        if val is None:
            continue

        existing_value = getattr(result, key, None)
        if existing_value is None:
            setattr(result, key, val)
        elif isinstance(existing_value, list):
            existing_value.append(val)
        else:
            setattr(result, key, [existing_value, val])

    process_info_hashes(result)
    process_public_keys(result)
    
    result.name = result.dn if result.dn else result.name
    result.keywords = result.kt if result.kt else result.keywords
    result.announce = list(set(result.tr)) if isinstance(result.tr, list) else ([result.tr] if isinstance(result.tr, str) else [])
    
    result.url_list = []
    if isinstance(result.as_, list) or isinstance(result.as_, str):
        result.url_list.extend(result.as_ if isinstance(result.as_, list) else [result.as_])
    if isinstance(result.ws, list) or isinstance(result.ws, str):
        result.url_list.extend(result.ws if isinstance(result.ws, list) else [result.ws])
    
    result.peer_addresses = []
    if isinstance(result.x_pe, list) or isinstance(result.x_pe, str):
        result.peer_addresses.extend(result.x_pe if isinstance(result.x_pe, list) else [result.x_pe])

    return result

def process_info_hashes(result: MagnetData):
    if result.xt:
        xts = result.xt if isinstance(result.xt, list) else [result.xt]
        for xt in xts:
            if match := re.match(r'^urn:btih:(.{40})', xt):
                result.info_hash = match[1].lower()
            elif match := re.match(r'^urn:btih:(.{32})', xt):
                decoded_bytes = base32_decode(match[1])
                result.info_hash = bytes_to_hex(decoded_bytes)
            elif match := re.match(r'^urn:btmh:1220(.{64})', xt):
                result.info_hash_v2 = match[1].lower()
    
    if result.info_hash:
        result.info_hash_int_array = hex_to_bytes(result.info_hash)

    if result.info_hash_v2:
        result.info_hash_v2_int_array = hex_to_bytes(result.info_hash_v2)

def process_public_keys(result: MagnetData):
    if result.xs:
        xss = result.xs if isinstance(result.xs, list) else [result.xs]
        for xs in xss:
            if match := re.match(r'^urn:btpk:(.{64})', xs):
                result.public_key = match[1].lower()
    
    if result.public_key:
        result.public_key_int_array = hex_to_bytes(result.public_key)

def parse_query_param_value(key: str, val: str) -> Optional[Union[str, int, List[str], List[int]]]:
    decoded_val = urllib.parse.unquote(val)
    
    if key == 'dn':
        return decoded_val.replace('+', ' ')
    elif key in ('tr', 'xs', 'as', 'ws'):
        return decoded_val
    elif key == 'kt':
        return decoded_val.split('+')
    elif key == 'ix':
        return int(decoded_val)
    return decoded_val

def hex_to_bytes(hex_str: str) -> bytes:
    return binascii.unhexlify(hex_str)

def bytes_to_hex(byte_array: bytes) -> str:
    return binascii.hexlify(byte_array).decode()

def base32_decode(encoded: str) -> bytes:
    # Base32 decoding (you may need to install a library for this)
    # For simplicity, using built-in base64 with padding
    import base64
    padded_encoded = encoded + '=' * (-len(encoded) % 8)  # Add padding
    return base64.b32decode(padded_encoded)

def magnet_encode(data: MagnetData) -> str:
    obj = data.__dict__.copy()
    xts = set()

    if isinstance(obj.get('xt'), str):
        xts.add(obj['xt'])
    elif isinstance(obj.get('xt'), list):
        xts.update(obj['xt'])

    if obj.get('info_hash_int_array'):
        xts.add(f"urn:btih:{bytes_to_hex(obj['info_hash_int_array'])}")
    if obj.get('info_hash'):
        xts.add(f"urn:btih:{obj['info_hash']}")
    if obj.get('info_hash_v2_int_array'):
        xts.add(f"urn:btmh:1220{bytes_to_hex(obj['info_hash_v2_int_array'])}")
    if obj.get('info_hash_v2'):
        xts.add(f"urn:btmh:1220{obj['info_hash_v2']}")

    obj['xt'] = list(xts)
    
    obj['dn'] = obj.get('name', obj.get('dn'))
    obj['xs'] = obj.get('public_key', obj.get('public_key_int_array'))
    
    params = []
    for key, value in obj.items():
        if value is None:
            continue
        if isinstance(value, list):
            for v in value:
                params.append(f"{key}={urllib.parse.quote(v)}")
        else:
            params.append(f"{key}={urllib.parse.quote(value)}")
    
    return f"{start}{'&'.join(params)}"

def main():
    parser = argparse.ArgumentParser(description="Decode and encode a magnet URI.")
    parser.add_argument("magnet_uri", type=str, help="The magnet URI to process.")
    parser.add_argument("-d", "--decode", action="store_true", help="Return decoded data.")
    parser.add_argument("-e", "--encode", action="store_true", help="Return encoded data.")

    args = parser.parse_args()
    input_uri = args.magnet_uri

    if args.decode:
        decoded_data = magnet_decode(input_uri)
        print("\nDecoded Magnet Data:")
        for attr, value in decoded_data.__dict__.items():
            print(f"{attr}: {value}")

    if args.encode:
        decoded_data = magnet_decode(input_uri)
        encoded_uri = magnet_encode(decoded_data)
        print("\nRe-encoded Magnet URI:")
        print(encoded_uri)

    if not args.decode and not args.encode:
        print("Please specify -d to decode or -e to encode.")

if __name__ == "__main__":
    main()