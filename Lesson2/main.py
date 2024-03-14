from matplotlib import pyplot
from openpyxl import load_workbook


wb = load_workbook('data_analysis_lab.xlsx') # Загрузить таблицу Excel из файла в переменную wb
sheet = wb['Data'] # Загрузить лист с именем "Data" в переменную sheet
#sheet['A'][1:] # Получить содержимое колонки A в виде списка

# print("sheet['A'][1:]")
# print(sheet['A'][1].value)
# print()

def getvalue(x):
    return x.value


list_x = list(map(getvalue, sheet['A'][1:])) # Преобразовать содержимое колонки A в список, содержащий только значения (без форматирования и т. п.)
list_y = list(map(getvalue, sheet['B'][1:])) # Преобразовать содержlist_x = list(map(getvalue, sheet['A'][1:])) # Преобразовать содержимое колонки A в список, содержащий только значения (без форматирования и т. п.)
list_y1 = list(map(getvalue, sheet['C'][1:])) # Преобразовать содержимое колонки B в список, содержащий только значения (без форматирования и т. п.)
list_y2 = list(map(getvalue, sheet['D'][1:])) # Преобразовать содержимое колонки B в список, содержащий только значения (без форматирования и т. п.)


# print(list(map(getvalue, sheet['A'][1:])))
pyplot.title('График для лабораторной работы')
pyplot.xlabel('Год')
pyplot.ylabel('Температура/Относительная температура/Активность')
pyplot.legend(loc='upper left')
# pyplot.axis([0,5,0,20])
pyplot.plot(list_x, list_y,"r-", list_x, list_y1, "b-",list_x, list_y2, "g-", label="Метка1") # Построить график по точкам, в первом списке значения по оси X, во втором — значения по оси Y
# pyplot.plot(list_x, list_y,"r-",  label="Метка2") # Построить график по точкам, в первом списке значения по оси X, во втором — значения по оси Y


pyplot.show() # показать график
