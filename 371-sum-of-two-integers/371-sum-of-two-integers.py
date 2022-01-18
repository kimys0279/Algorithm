class Solution(object):
    def getSum(self, a, b):
        xor = a ^ b
        carry = a & b
        if carry == 0:
            return xor
        else:
            return add(xor, carry << 1)