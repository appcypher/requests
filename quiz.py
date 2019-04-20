# ---------------------------------( 1 )-------------------------------------#

ls = [
    104, 116, 116, 112, 115, 58, 47, 47, 101, 110, 103, 105, 110, 101, 101,
    114, 105, 110, 103, 45, 97, 112, 112, 108, 105, 99, 97, 116, 105, 111, 110,
    46, 98, 114, 105, 116, 101, 99, 111, 114, 101, 46, 99, 111, 109, 47, 113,
    117, 105, 122, 47, 115, 100, 102, 103, 119, 114, 52, 52, 104, 114, 102,
    104, 102, 104, 45, 119, 115
]

print('>>>>', ''.join([chr(i) for i in ls]))

# ---------------------------------( 2 )-------------------------------------#

from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = (
    b'gAAAAABct2WKIp0nThWh7QQOmMUeVQhzbsv6FOiDTXNICNlFDEtDUoMzt9cKDdDpV5gu'
    b'YxP0H6JpHfMUdhVXGykxoL60C9L1ahSybjvC6BTaBAM7e7nQT00ZjQVKXf8hk34iGgcK'
    b'5O2XjZT9GvU7FvdwElrp4MgiuySj7AkwlDk95AF0_NfydTogR4LydHnMPIxsde9A3Qff'
)


def main():
    f = Fernet(key)
    print('>>>>', f.decrypt(message))


if __name__ == "__main__":
    main()
