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


# Задание на следующий урок
Посмотреть уроки по [работе с файлами](https://stepik.org/lesson/3363/step/1?unit=1135)
и [модулями](https://stepik.org/lesson/3377/step/1?unit=960)


# Задания
* Создайте 3 тэмплэйта (возьмите .format() или f-строки), используя
побольше возможностей (padding, округление)  и заполните их пару раз
(6 баллов)
* Сделайте несколько распаковок произвольных списков/кортежей в переменные
(3 балла)
* Напишите следующие comprehension'ы:
    * квадраты чисел от 0 до 10
    * суммы 2-ух чисел взятых из последовательностей от 0 до 3 и от 5 до 8
    * строки, представляющие переходы из одних нуклеотидов в другие 'A->T', 'A->C',  'A->G', 'T->A', ...
    * вложенные списки, представляющие матрицу 3 на 3, заполненную от 0 до 9
(13 баллов)
* Имплементируйте линейный поиск (принимает на вход элемент и список,
возвращает индекс с этим элементом)
(10 баллов)
* *Имплементируйте бинарный поиск (принимает на вход элемент и
отсортированный список, возвращает индекс с этим элементом)
(15 баллов)
