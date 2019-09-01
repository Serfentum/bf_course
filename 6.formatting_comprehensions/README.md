# String prefixes, formatting, unpacking, comprehensions, debugging and sorting
Модуль о префиксах строк, их форматировании, распаковке и comprehension'ах


# Источники информации
* [официальная документация по префиксам](https://docs.python.org/3/reference/lexical_analysis.html#strings)
* [байты](https://docs.python.org/3/library/stdtypes.html#bytes)
* [разница между строками и байтовыми строками](https://stackoverflow.com/questions/6224052/what-is-the-difference-between-a-string-and-a-byte-string/31322359)
* [raw strings](https://www.journaldev.com/23598/python-raw-string)
* [пояснение по сырым стокам](https://stackoverflow.com/questions/2081640/what-exactly-do-u-and-r-string-flags-do-and-what-are-raw-string-literals)
* [один гайд по f-строкам](http://zetcode.com/python/fstring/)
* [второй гайд по f-строкам](https://realpython.com/python-f-strings)
* [официальная документация по форматированию](https://docs.python.org/3/library/string.html#formatspec)
* [распаковка таплов](https://www.geeksforgeeks.org/unpacking-a-tuple-in-python/)
* [распаковка в функциях](https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/)
* [разбор * в питоне](https://medium.com/understand-the-python/understanding-the-asterisk-of-python-8b9daaa4a558)
* [разбор comprehension'ов](https://towardsdatascience.com/python-basics-list-comprehensions-631278f22c40)
* [простые примеры comprehension'ов](https://www.geeksforgeeks.org/comprehensions-in-python/)


# Задания
* Создайте 3 тэмлэйта (возьмите .format() или f-строки), используя
побольше возможностей (padding, округление)  и заполните их пару раз
* Сделайте несколько распаковок произвольных списков/кортежей в переменные
* Напишите следующие comprehension'ы:
    * квадраты чисел от 0 до 10
    * суммы 2-ух чисел взятых из последовательностей от 0 до 3 и от 5 до 8
    * переходы из одного нуклеотида в другой (нуклеотиды должны быть разными) - 'A->T'
    * вложенные списки, представляющие матрицу 3 на 3, заполненную от 0 до 9
* Имплементируйте линейный поиск (принимает на вход элемент и список,
возвращает индекс с этим элементом)
* *Имплементируйте бинарный поиск (принимает на вход элемент и
отсортированный список, возвращает индекс с этим элементом)
