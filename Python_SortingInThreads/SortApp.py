import datetime
from SortStrategy import SortStrategy
class SortApp:
    LOG_NAME = "log.txt"
    def __init__(self, threadsNumbers, sortStrategy):
        if isinstance (sortStrategy, SortStrategy):
            startTime = datetime.datetime.now()
            self.__threadsNumbers = threadsNumbers
            self.__strategy = sortStrategy
            self.__strategy.run(threadsNumbers)
            self.Log(datetime.datetime.now() - startTime)
            self.Save()
            #for num in self.__strategy.Numbers:
            #    print(num)
            

    def Log(self, time):
        log = f"Sort end.\nAlgorithm: {self.__strategy.__class__.__name__}\nThreads: {self.__threadsNumbers}\nTime: {time}\n"
        with open(SortApp.LOG_NAME, "a") as filew:
            filew.write(f"{log}\n")
        print(log)

    def Save(self):
        try:
            with open("numbers.txt", "w") as filew:
                for num in self.__strategy.Numbers:
                    filew.write(f"{num}\n")
        except Exception as ex: print(f"ERROR!\n{ex}")


      
