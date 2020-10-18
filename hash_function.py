import hashlib
def _hash(key):
        hash_obj = hashlib.md5(bkey)
        return hash_obj.hexdigest()
        # hash_code = 0
        # for i in range(len(key)):
        #     charcode = ord(key[i]) %10
        #     hash_code += charcode *i
        # return hash_code%10
        

#123 = 1*10^2 + 2*10^1 + 3 * 10^0

print(_hash('bad'))
print(_hash('abd'))
print(_hash('i2outp3jegnkdjlnlj34hnpiu'))
print(_hash('jierhjlian78943y9gheih'))
print(_hash('dwejlirnmcufi3btoc7ctn32hghjvuehvbwebhfkqwhebkgjbuiyebhbchudbfou'))
print(_hash('ueiqgdxmy43ugn34yfb34'))
print(_hash('baj3lgjlwbrhjgbliuj4bgljd'))
print(_hash('abuifhoiehbfd'))
print(_hash('nvm,knjadlijpoajfipj'))
print(_hash('jierhjliaeyugbhrueon78943y9gheih'))
print(_hash('ejwklfnhjalenjfl'))
