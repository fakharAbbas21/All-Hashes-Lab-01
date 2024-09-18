import hashlib
# import bcrypt
input_name = input("Enter your name : ")
# 
name_bytes = input_name.encode()
# md- 5
md5_hash = hashlib.md5(name_bytes).hexdigest()
print( "MD5 hash : ",md5_hash)
# sha1
SHA_hash = hashlib.sha1(name_bytes).hexdigest()
print( "SHA HSAH : ", SHA_hash)
# sha 256
SHA_256 = hashlib.sha256(name_bytes).hexdigest()
print( "SHA_256 : ",SHA_256, )
# sha 512
SHA_512 = hashlib.sha512(name_bytes).hexdigest()
print( "SHA_512 : ",SHA_512,)
#  sha 3
SHA3 = hashlib.sha3_256(name_bytes).hexdigest()
print( "SHA3 : ",SHA3)
# BLAKE
BLAKE = hashlib.blake2b(name_bytes).hexdigest()
print( "BLAKE : ", BLAKE )
# RIPEMD160 ////////////
RIPEMD_160 = hashlib.new("ripemd160", name_bytes).hexdigest()
print( "RIPEMD_160 : ",RIPEMD_160 )
#  Write a program ,
 

