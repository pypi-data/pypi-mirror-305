import re

def clean_address(address):
    if address is None:
        return ''
    return re.sub(r'[^A-Za-z0-9 ,.-]+', ' ', address)

