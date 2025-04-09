from BubbleSort import BubbleSort
from QuickSort import QuickSort
from SortApp import SortApp
import time
'''
23. Выбрать любой алгоритм сортировки и улучшить его при помощи многопоточности так, 
чтобы был выигрыш в скорости сортировки при добавлении новых потоков.
Засечь время сортировки большого массива чисел. 
Результат сортировки сохранить в файл. 
Запрограммировать этот алгоритм сортировки на нескольких языках из списка:
C++, Java, C#, NodeJS, Python.
'''

sortApp = SortApp(4, BubbleSort())