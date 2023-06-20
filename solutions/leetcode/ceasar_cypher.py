def cypher(s, shift):
    '''
    Returns proper values on positive shift
    When negative shift is given results are wrong
        - How Modulo works with negative numbers
        - create a base variable to effect the math
    '''
    new_s = ''
    for letter in s:
        if letter.isalpha():
            base = ord('a') if letter.islower() else ord('A')
            shifted_ordinal = (ord(letter) - base + shift) % 26
            shifted_character = chr(shifted_ordinal + base)
            new_s += shifted_character
        else:
            new_s += letter
    return new_s

s = "VWDQ LV QRW ZKDW KH VHHPV"
shift = -3
print(cypher(s, shift))