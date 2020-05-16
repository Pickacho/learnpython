secret_message = 'TzH?!xC7zAhSH[n[m$_;e>?6: YiT< 8)4=5Kv\r>p4/{b2vw>fa}^~HNH}sms<_y{`KuK!s9Nt\'Ckl]{wlEMsmP&,uoDx\rW zVvvr%M+RXNzE d/cH#hq;}) BR`eBp|;BirGX\x0cK%Su,s("BX6sMa. 1MZ|*\x0b\x0bsvA9~:%=p;y^v#l.\n\r)63\noLz]{,|q|!cxd\'Eik;VVa.vj\x0c;>c\t-dw8Fr0TRUro|<t-SV|Z['
string = "password"
i = 1
password_try = 0
while string not in secret_message[::i]:
    password_try = secret_message[::i]
    print(f"When I try and jump {i} steps this is what I am getting: {secret_message[::i]} ")
    i = i + 1

print(f"And the answer is when I jump {i} steps : {secret_message[::i]} ")
