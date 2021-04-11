def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ''' basically change the min of the right hand side of the
            intervals
        '''
        
        # edge case
        if firstList == [] or secondList == []:
            return []
        
        matching = []
        
        # initialize length and pointers
        l1 = len(firstList)
        l2 = len(secondList)
        i = 0
        j = 0
        
        while i < l1 and j < l2:
            fir = firstList[i]
            sec = secondList[j]
            
            # first two cases are in case there is no overlapping
            if fir[1] < sec[0]:
                i += 1
            elif sec[1] < fir[0]:
                j += 1
                
            # third case handels overlapping
            else:
                if sec[1] > fir[1]:
                    matching.append([max(sec[0], fir[0]), fir[1]])
                    i += 1
                elif fir[1] > sec[1]:
                    matching.append([max(fir[0], sec[0]), sec[1]])
                    j += 1
                else:
                    matching.append([max(fir[0], sec[0]), max(fir[1], sec[1])])
                    i += 1
                    j += 1
        
        return matching
            