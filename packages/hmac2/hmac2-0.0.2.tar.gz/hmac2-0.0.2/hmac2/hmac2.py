import hashlib


class HMAC:
    """
    Implements an HMAC (Hash-based Message Authentication Code) using a specified hash function.
    
    Usage:
        # Create a new HMAC instance with a given key, message, and hash algorithm
        key = b'secret_key'
        message = b'my message'
        h = HMAC(key, message, digestmod='sha256')
        
        # Update the HMAC with more data if needed
        h.update(b' additional message')
        
        # Get the final HMAC value in hexadecimal format
        print(h.hexdigest())
        
    Methods:
        - __init__(key, msg=None, digestmod='sha256'): Initialize an HMAC instance.
        - update(msg): Update the HMAC with more message bytes.
        - digest(): Return the binary HMAC value.
        - hexdigest(): Return the HMAC value in hexadecimal format.
        
    Alternative Usage:
        # Using the 'new' function for a simpler syntax
        import hmac2
        hmac_value = hmac2.new(key, message, 'sha256').hexdigest()
        print("HMAC: ", hmac_value)
    """

    def __init__(self, key, msg=None, digestmod='sha256'):
        if isinstance(digestmod, str):
            digestmod = getattr(hashlib, digestmod)
        self.digestmod = digestmod
        self.outer = self.digestmod()
        self.inner = self.digestmod()
        
        block_size = self.inner.block_size
        if len(key) > block_size:
            key = digestmod(key).digest()
        key = key.ljust(block_size, b'\x00')
        
        o_key_pad = bytes((x ^ 0x5c) for x in key)
        i_key_pad = bytes((x ^ 0x36) for x in key)
        
        self.outer.update(o_key_pad)
        self.inner.update(i_key_pad)
        
        if msg is not None:
            self.update(msg)
    
    def update(self, msg):
        self.inner.update(msg)
    
    def digest(self):
        h_inner = self.inner.digest()
        self.outer.update(h_inner)
        return self.outer.digest()
    
    def hexdigest(self):
        return self.digest().hex()


def new(key, msg=None, digestmod='sha256'):
    return HMAC(key, msg, digestmod)
