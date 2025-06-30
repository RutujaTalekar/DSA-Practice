class MedianFinder:
    '''
    To solve this problem you will have to maintain a list as you call ADD function
    And then get the median of the list

    Brute force way will take O(n) to add as you will have to reorder the list everytime
    to store it in sorted way
    And then findMedian will be O(1) cause list is already sorted

    To optimize, lets use heaps
    we can store the list as 2 sublists/heaps - lets call one small and the other large
    Small will be a max heap so it can give us the max of that list in O(1)
    Large will be min heap so it can give us the min in O(1)'
    this will be used while getting median, that's why we are using max and min heap
    All elements in Small will be smaller than the ones in Large
    Both lists should be nearly of equal lengths

    For Add function - 
    By default we add element to the Small
    1. Check - all elements in Small should be lesser than all elements in Large
    2. Check - the sizes of both lists should be nearly equal
        If not pop max from small, and store it in Large or
            pop min from large and store it in small

    ** Remember that python by default only provides min heap, to maintain max heap just multiply the nums by -1
    '''
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # check condition 1
        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # check sizes condition 2
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
            
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()