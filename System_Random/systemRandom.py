import secrets

# ------------------------------------------------------------
# SECURE RANDOM MODULE
# ------------------------------------------------------------
class systemRandom:
    def choose_random_element(self, sequence):
        return secrets.choice(sequence)

    def random_below(self, upper_limit):
        return secrets.randbelow(upper_limit)

    def random_bits(self, bit_count):
        return secrets.randbits(bit_count)

    def generate_token_hex(self, nbytes):
        return secrets.token_hex(nbytes)

# ------------------------------------------------------------
# TOKEN GENERATION (RAW BYTES → HEX)
# ------------------------------------------------------------
class tokenRandom:
    def generate(self, nbytes):
        RAW_BYTES = secrets.token_bytes(nbytes)
        HEX_STRING = RAW_BYTES.hex()
        return HEX_STRING