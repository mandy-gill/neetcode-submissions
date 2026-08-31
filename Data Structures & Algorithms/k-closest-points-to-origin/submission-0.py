class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            d = x**2 + y**2
            maxHeap.append([-d, x, y])

        heapq.heapify(maxHeap)

        while len(maxHeap) > k:
            heapq.heappop(maxHeap)

        return [[x, y] for d, x, y in maxHeap]