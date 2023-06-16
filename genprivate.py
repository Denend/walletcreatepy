from eth_account import Account
import secrets

for i in range (10):
    
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    print ("SAVE BUT DO NOT SHARE THIS:", private_key)
    acct = Account.from_key(private_key)
    print("Address:", acct.address)

    with open('out.txt', 'a') as f:
       print('PRIVATE:', private_key, file=f)
       print('Address:', acct.address, file=f)