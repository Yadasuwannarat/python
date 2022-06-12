def gcd_01(a,b):

    while a != b:
        while a > b:
            a = a - b
        while b > a:
            b = b -a
        return a
    def lcm_sum(a,b):
        return abs(a*b)//gcd_01(a,b)    