def isNumber(S) -> bool:
    num, exp, sign, dec = False, False, False, False
    for c in S:
        if c >= '0' and c <= '9':
            num = True     
        elif c == 'e' or c == 'E':
            if exp or not num:
                return False
            else:
                exp, num, sign, dec = True, False, False, False
        elif c== '+' or c == '-':
            if sign or num or dec:
                return True
            
