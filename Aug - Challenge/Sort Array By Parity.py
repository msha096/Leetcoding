class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # 98% faster
        beg, end = 0, len(A)-1
        while beg < end:
            if A[beg]%2 == 0:
                beg += 1
            else:
                A[beg], A[end] = A[end], A [beg]
                end -= 1
        return A
        '''
        # slow, but intuitive
        i = 0
        l = len(A)
        while i < l:
            if A[i] % 2 == 1:
                odd = A.pop(i)
                A.append(odd)
                l -= 1
            else:
                i += 1
        return A
        '''