class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int):
        s = 0
        c = 0
        maxi = -1
        idx = 0
        maxisum = -1
        for i in range(0, len(customers) - minutes + 1):
            c = 0
            for j in range(i, i + minutes):
                if grumpy[j] == 1:      
                    c += customers[j]
            if c > maxi:
                maxi = c                
                idx = i
                maxisum = sum(customers[i:i+minutes])
            elif c == maxi:
                if sum(customers[i:i+minutes]) > maxisum:
                    maxisum = sum(customers[i:i+minutes])
                    idx = i
        i = 0
        while i < len(customers):
            if i == idx:
                i += minutes            
                continue
            if grumpy[i] == 0:
                s += customers[i]
            i += 1
        s += sum(customers[idx:idx+minutes])
        return s