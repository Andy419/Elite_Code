def numTilePossibilities(self, tiles: str) -> int:
        
        # default permutations set-up and execution
        already = set()
        already.add("")
        
        def combos(lets, cur):
            if cur not in already:
                already.add(cur)
                total[0] += 1
            
            for i in range(len(lets)):
                combos(lets[0:i]+lets[i+1:], cur + lets[i])
            
        total = [0]
        combos(tiles, "")
        return total[0]