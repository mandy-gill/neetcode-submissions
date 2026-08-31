class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-w for w in stones]
        heapq.heapify(maxHeap)

        while maxHeap:
            x = -heapq.heappop(maxHeap)
            if not maxHeap: return x
            y = -heapq.heappop(maxHeap)

            if x != y:
                heapq.heappush(maxHeap, -(x - y))

        return 0