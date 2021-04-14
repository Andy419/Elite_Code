def partitionLabels(self, S: str) -> List[int]:
        ends = {}
        for i in range(len(S)):
            ends[S[i]] = i
        
        ans = []
        total = 0
        while S:
            print(ans, S)
            cur = S[0]
            fin = ends[cur] - total
            while True:
                lets = []
                for i in range(fin):
                    if S[i] not in lets and S[i] != cur:
                        lets.append(S[i])
                change = False
                while lets:
                    on = lets.pop()
                    if ends[on] - total > fin:
                        change = True
                        fin = ends[on] -total

                if not change:
                    ans.append(fin+1)
                    S = S[fin+1:]
                    total += fin+1
                    break
        return ans