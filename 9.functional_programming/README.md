# Functional Programming in python
Модуль по функциональному программированию


# Источники информации
* [пост о функциональном программировании в питоне](https://kite.com/blog/python/functional-programming/)
* [howto по функциональному программированию в питоне](https://docs.python.org/3/howto/functional.html)
* [модуль functools](https://docs.python.org/3/library/functools.html)
* [Haskell](https://www.haskell.org/)
* [разбор генераторов](https://www.programiz.com/python-programming/generator)
* [ещё один разбор генераторов](https://realpython.com/introduction-to-python-generators/)
* [хабровский разбор генераторов](https://habr.com/ru/post/132554/)
* [ещё разбор, хотя и с чуть большим упором на 2-ой питон](https://wiki.python.org/moin/Generators)
* [официальная документация по itertools](https://docs.python.org/3/library/itertools.html)
* [ещё о функциях в itertools](https://pythonworld.ru/moduli/modul-itertools.html)
* [гайд по itertools](https://realpython.com/python-itertools/)


# Задания
* Напишите по 3 примера использования map и filter на произвольных коллекциях -
отпроцессируйте их элементы и отфильтруйте как вам угодно, для визуализации
оберните результат в лист (6 баллов)
* Напишите генератор, осуществляющий считывание фасты и возвращающий по 1-ой
оттранслированной последовательности
    * input
        * путь до фасты
        * таблица кодонов - 'Standard' по умолчанию
    * output
        * протеиновый Seq

(12 баллов)
* Сгенерируйте 52-карточную колоду (состоящую из кортежей типа (ранг, масть)
 с помощью приблуд из itertools - в вашем распоряжении iterable с рангами
 (2..10, J..A) и мастями (H, C, S, D) (10 баллов)
* Сделайте функцию-генератор, генерирующую все ДНКовые последовательности до длины n
(аккуратно, не вызывайте её с n > 8)
```python
list(generate(2))
['A', 'T', 'G', 'C', 'AA', 'AT', 'AG', 'AC', 'TA', 'TT', 'TG', 'TC',
'GA', 'GT', 'GG', 'GC', 'CA', 'CT', 'CG', 'CC']
```
(15 баллов)