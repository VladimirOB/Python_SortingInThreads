import threading
from SortStrategy import SortStrategy

class QuickSortThread(threading.Thread):
    def __init__(self, nums):
        self.__numbers = nums
        threading.Thread.__init__(self)

    def run(self):
        size = len(self.__numbers)
        self.QSort(self.__numbers, 0, size -1)

    def QSort(self, nums, start, end):
        if(start >= end): return
        i = start
        j = end

        #середина
        baseElementIndex = int(start + (end - start ) / 2)
        # пока индекс левой части меньше правой
        while i < j:
            # значение погран. эл.
            value = nums[baseElementIndex]

            #перемещаем инд. левой части вперёд, пока не встретится большой элемент
            while i < baseElementIndex and nums[i] <= value: i+=1

            #перемещать индекс правой части массива назад, пока не встретится слишком маленький элемент
            while j > baseElementIndex and nums[j] >= value: j-=1

            #i, j - индексы элементов, которые нужно поменять местами
            #если индесы правильные (есть смысл обмена элементов)
            if i < j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

                #корректировка
                if i == baseElementIndex: baseElementIndex = j
                elif j == baseElementIndex: baseElementIndex = i
        self.QSort(nums, start, baseElementIndex)
        self.QSort(nums, baseElementIndex + 1, end)

class QuickSort(SortStrategy):
    def __init__(self):
        pass

    def sort(self, nums):
        threadSort = QuickSortThread(nums)
        threadSort.start()
        threadSort.join()