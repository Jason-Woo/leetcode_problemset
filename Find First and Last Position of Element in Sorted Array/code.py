class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        lmost = self.leftsearch(A, target)
        rmost = self.rightsearch(A, target)
        return [lmost, rmost]

    def leftsearch(self, A, tar):
        l = 0
        r = len(A) - 1
        tarI = -1  # target index
        while l <= r:
            mid = (l + r) / 2
            if A[mid] > tar:
                r = mid - 1
            elif A[mid] < tar:
                l = mid + 1
            else:
                tarI = mid
                r = mid - 1
        return tarI


    def rightsearch(self, A, tar):
        l = 0
        r = len(A) - 1
        tarI = -1
        while l <= r:
            mid = (l + r) / 2
            if A[mid] > tar:
                r = mid - 1
            elif A[mid] < tar:
                l = mid + 1
            else:
                tarI = mid
                l = mid + 1
        return tarI
