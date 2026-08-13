class Solution:

    class Node:
        def __init__(self, pre=0, suf=0, maxLen=0,
                     leftChar='', rightChar=''):
            self.pre = pre
            self.suf = suf
            self.maxLen = maxLen
            self.leftChar = leftChar
            self.rightChar = rightChar

    def longestRepeating(self, s: str, queryCharacters: str,
                         queryIndices: List[int]) -> List[int]:

        n = len(s)

        segTree = [self.Node() for _ in range(4 * n)]

        def merge(L, R, leftLen, rightLen):

            res = self.Node()

            res.leftChar = L.leftChar
            res.rightChar = R.rightChar

            # prefix
            res.pre = L.pre

            if L.pre == leftLen and L.rightChar == R.leftChar:
                res.pre = L.pre + R.pre

            # suffix
            res.suf = R.suf

            if R.suf == rightLen and L.rightChar == R.leftChar:
                res.suf = R.suf + L.suf

            # maximum repeating length
            res.maxLen = max(L.maxLen, R.maxLen)

            if L.rightChar == R.leftChar:
                res.maxLen = max(
                    res.maxLen,
                    L.suf + R.pre
                )

            return res

        def build(i, l, r):

            if l == r:
                segTree[i] = self.Node(
                    1, 1, 1,
                    s[l], s[l]
                )
                return

            mid = (l + r) // 2

            build(2 * i + 1, l, mid)
            build(2 * i + 2, mid + 1, r)

            segTree[i] = merge(
                segTree[2 * i + 1],
                segTree[2 * i + 2],
                mid - l + 1,
                r - mid
            )

        def update(i, l, r, pos, ch):

            if l == r:
                segTree[i] = self.Node(
                    1, 1, 1,
                    ch, ch
                )
                return

            mid = (l + r) // 2

            if pos <= mid:
                update(2 * i + 1, l, mid, pos, ch)
            else:
                update(2 * i + 2, mid + 1, r, pos, ch)

            segTree[i] = merge(
                segTree[2 * i + 1],
                segTree[2 * i + 2],
                mid - l + 1,
                r - mid
            )

        build(0, 0, n - 1)

        result = []

        for i in range(len(queryIndices)):

            pos = queryIndices[i]
            ch = queryCharacters[i]

            update(0, 0, n - 1, pos, ch)

            result.append(segTree[0].maxLen)

        return result