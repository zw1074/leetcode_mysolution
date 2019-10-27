import functools
class Solution:
    @functools.lru_cache(None)
    def tilingRectangle(self, n: int, m: int) -> int:
        if n == 0 or m == 0:
            return 0
        
        @functools.lru_cache(None)
        def ell(l1, l2, l3, l4):
            if l3 == l1 and l4 == l2:
                return self.tilingRectangle(l1, l2)
            if l3 > l1:
                l1, l3 = l3, l1
            if l4 > l2:
                l2, l4 = l4, l2
            
            if l1 < l4:
                if l2 % l3 == 0:
                    cand1 =  l2//l3 + self.tilingRectangle(l1-l3, l4)
                else:
                    cand1 = l2//l3 + ell(l2-l2//l3*l3,l1 - l3, l4, l1)
                if l4 % l1 == 0:
                    cand2 = l4//l1 + self.tilingRectangle(l2-l4, l3)
                else:
                    cand2 = l4//l1 + ell(l1, l2 - l4//l1*l1, l3, l4 - l4//l1*l1)
                return min(cand1, cand2)
            elif l2 < l3:
                if l1 % l4 == 0:
                    cand1 =  l1//l4 + self.tilingRectangle(l2-l4, l3)
                else:
                    cand1 = l1//l4 + ell(l1-l1//l4*l4, l2-l4, l3, l2)
                if l3 % l2 == 0:
                    cand2 = l3//l2 + self.tilingRectangle(l1-l3, l4)
                else:
                    cand2 = l3//l2 + ell(l2, l1 - l3//l2*l2, l4, l3 - l3//l2*l2)
                return min(cand1, cand2)
            else:
                if l1 % l4 == 0:
                    cand1 = l1//l4 + self.tilingRectangle(l2-l4, l3)
                else:
                    if l1 - l1//l4*l4 < l3:
                        cand1 = l1//l4 + ell(l1-l1//l4*l4, l2-l4, l3, l2)
                    elif l1 - l1//l4*l4 == l3:
                        cand1 = l1//l4 + self.tilingRectangle(l3, l2)
                    else:
                        cand1 = l1//l4 + ell(l1-l1//l4*l4, l2, l3, l4)
                if l2 % l3 == 0:
                    cand2 = l2//l3 + self.tilingRectangle(l1-l3, l4)
                else:
                    if l2 - l2//l3*l3 < l4:
                        cand2 = l2//l4 + ell(l2-l2//l3*l3, l1-l3, l4, l1)
                    elif l2 - l2//l3*l3 == l4:
                        cand2 = l2//l3 + self.tilingRectangle(l4, l1)
                    else:
                        cand2 = l2//l3 + ell(l2-l2//l3*l3, l1, l4, l3)
                return min(cand1, cand2)
        if n == m:
            return 1
        # just give a try
        if n > m: # always let n be the minimum
            n, m = m, n
        # give a try:
        ans = float('inf')
        k = 0
        for l in range(1, n+1):
            if n % l == 0 and m % l == 0:
                ans = min(ans, n//l * m//l)
            elif n % l == 0:
                ans = min(ans, n//l * m//l + self.tilingRectangle(n, m - m//l*l))
            elif m % l == 0:
                ans = min(ans, n//l*m//l + self.tilingRectangle(m, n- n//l*l))
            else:
                k = ell(n, m, n - n//l*l, m - m//l*l)
                ans = min(ans, n//l*m//l + k)
        return ans
