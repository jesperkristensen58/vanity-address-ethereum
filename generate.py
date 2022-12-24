# Generate an Ethereum Vanity address. Based on Nick Johnson's script, but updated to
# Python 3 and we use a different objective function: maximize leading zeros.
# @author: Jesper Kristensen
import os
import re
from ethereum.tools.keys import privtoaddr
from ethereum.utils import mk_contract_address, encode_hex

# find address with the most leading zeros
NUMITER = 1000 # <-- increase the mining duration here

# =========== find the vanity address
best = None
bestprivkey = None
for _ in range(NUMITER):
    # generate a random private key
    privkey = os.urandom(32)
    addr = privtoaddr(privkey)
    contractaddr = encode_hex(mk_contract_address(addr, 0))
    
    # count leading zeros
    leadingzs = re.search('(?!0)', contractaddr).start()

    if best is None or leadingzs > best:
        best = leadingzs
        bestaddr = contractaddr
        bestprivkey = privkey

        print(f"0x{bestaddr}")

print(f"Found 0x{bestaddr} with {best} leading zeros.")
print("Private key:")
print(f"0x{encode_hex(bestprivkey)}")
