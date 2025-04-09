import threading
from SortStrategy import SortStrategy

class BubbleSortThread(threading.Thread):
    def __init__(self, nums):
        self.__numbers = nums
        threading.Thread.__init__(self)

    def run(self):
        print("BubbleSort - sort")
        size = len(self.__numbers)
        for i in range(1, size):
            for j in range(size-1, i-1, -1):
                if  self.__numbers[j -1] >  self.__numbers[j]:
                    temp =  self.__numbers[j-1]
                    self.__numbers[j-1] =  self.__numbers[j]
                    self.__numbers[j] = temp

class BubbleSort(SortStrategy):
    def __init__(self):
        pass

    def sort(self, nums):
        threadSort = BubbleSortThread(nums)
        threadSort.start()
        #threadSort.join()
   