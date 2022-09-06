class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]         # convert to binary, and remove the usual 0b prefix
        n = '%32s' % n         # print number into a pre-formatted string with space-padding
        n = n.replace(' ','0') # Convert the useful space-padding into zeros
        # Now we have a  proper binary representation, so we can make the final transformation
        return int(n[::-1],2)