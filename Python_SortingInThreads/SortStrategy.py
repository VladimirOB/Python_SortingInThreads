from abc import ABC, abstractmethod
import random

class SortStrategy(ABC):
    SIZE = 5000;

    @property
    def Numbers(self):
        return self.__numbers
	
    def SplitArray(self, threadsNumber):
        partSize = int(SortStrategy.SIZE / threadsNumber)
        for i in range(threadsNumber):
            startIndex = i * partSize
            endIndex = 0
            if i == threadsNumber-1:
                endIndex = SortStrategy.SIZE
            else:
                endIndex = (i + 1) * partSize
            self.__splitArrays.append(self.__numbers[startIndex:endIndex])

    def Merge(self):
        currentIndex = 0
        for i in range(len(self.__splitArrays)):
            partLength = len(self.__splitArrays[i])
            self.__numbers[currentIndex:currentIndex+partLength] = self.__splitArrays[i][:partLength]
            currentIndex += partLength
        self.__numbers.sort()

    def run(self, threadsNumber):
        self.__numbers = []
        self.__splitArrays = []
        for i in range(SortStrategy.SIZE):
            self.__numbers.append(random.randint(0,9))

        try:
            if threadsNumber == 1:
                self.sort(self.__numbers)
                return
            self.SplitArray(threadsNumber)
            for i in range(len(self.__splitArrays)):
                self.sort(self.__splitArrays[i])
            self.Merge()
            

        except Exception as ex: print(f"ERROR!\n{ex}")


    @abstractmethod
    def sort(self, data):
        pass