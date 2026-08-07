from functools import lru_cache

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:

     
        need = [0, 0, 0, 0]   # factors of 2, 3, 5, 7
        primes = [2, 3, 5, 7]

        for i, p in enumerate(primes):
            while t % p == 0:
                need[i] += 1
                t //= p

        # If t has any other prime factor
        if t != 1:
            return "-1"

        
        digit_factor = [(0, 0, 0, 0)] * 10

        for digit in range(1, 10):
            x = digit
            cnt = [0, 0, 0, 0]

            for i, p in enumerate(primes):
                while x % p == 0:
                    cnt[i] += 1
                    x //= p

            digit_factor[digit] = tuple(cnt)

        
        @lru_cache(None)
        def min_digits(a, b, c, d):

            if a == 0 and b == 0 and c == 0 and d == 0:
                return 0

            INF = 10**9
            ans = INF

            for digit in range(2, 10):

                x, y, z, w = digit_factor[digit]

                na = max(0, a - x)
                nb = max(0, b - y)
                nc = max(0, c - z)
                nd = max(0, d - w)

                # digit actually removes something
                if (na, nb, nc, nd) != (a, b, c, d):
                    ans = min(
                        ans,
                        1 + min_digits(na, nb, nc, nd)
                    )

            return ans

        if "0" not in num:

            have = [0, 0, 0, 0]

            for ch in num:
                f = digit_factor[int(ch)]

                for j in range(4):
                    have[j] += f[j]

            if all(have[i] >= need[i] for i in range(4)):
                return num

        n = len(num)

        def build_smallest(length, req):

            ans = []

            for pos in range(length):

                remaining_slots = length - pos - 1

                for digit in range(1, 10):

                    f = digit_factor[digit]

                    nr = (
                        max(0, req[0] - f[0]),
                        max(0, req[1] - f[1]),
                        max(0, req[2] - f[2]),
                        max(0, req[3] - f[3])
                    )

                    if min_digits(*nr) <= remaining_slots:
                        ans.append(str(digit))
                        req = nr
                        break

            return "".join(ans)

        total = [0, 0, 0, 0]

        for ch in num:
            f = digit_factor[int(ch)]

            for j in range(4):
                total[j] += f[j]

        
        zero_count = num.count("0")

        for i in range(n - 1, -1, -1):

            current_digit = int(num[i])

            
            f = digit_factor[current_digit]

            for j in range(4):
                total[j] -= f[j]

            if current_digit == 0:
                zero_count -= 1

            # Prefix must be zero-free
            if zero_count > 0:
                continue

            prefix = num[:i]

            # Try a larger digit
            for digit in range(current_digit + 1, 10):

                f = digit_factor[digit]

                req = (
                    max(0, need[0] - total[0] - f[0]),
                    max(0, need[1] - total[1] - f[1]),
                    max(0, need[2] - total[2] - f[2]),
                    max(0, need[3] - total[3] - f[3])
                )

                remaining = n - i - 1

               
                if min_digits(*req) <= remaining:

                    suffix = build_smallest(
                        remaining,
                        req
                    )

                    return prefix + str(digit) + suffix


        minimum_length = min_digits(*need)

        length = max(n + 1, minimum_length)

        return build_smallest(length, tuple(need))