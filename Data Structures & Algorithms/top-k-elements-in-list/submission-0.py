class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # number : frequency
        kFreq = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for i in range(k):
            mostFreqNum = -1
            mostFreqCount = -1

            for c in count:
                if count[c] > mostFreqCount:
                    mostFreqNum = c
                    mostFreqCount = count[c]
                
            kFreq.append(mostFreqNum)
            count.pop(mostFreqNum)
        
        return kFreq