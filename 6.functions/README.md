# Functions
Модуль о функциях


# Источники информации
* [Туториал по функциям](https://www.digitalocean.com/community/tutorials/how-to-define-functions-in-python-3)
* [Ещё один туториал по функциям](https://www.python-course.eu/python3_functions.php)
* [Документация функций](https://www.datacamp.com/community/tutorials/docstrings-python)
* [Ещё гайд по документации функций](https://realpython.com/documenting-python-code/)
* [Официальное предложение по докстрингам](https://www.python.org/dev/peps/pep-0257/)
* [Статья о монолитной организации приложений](https://en.wikipedia.org/wiki/Monolithic_application)
* [Статья о противоположности предыдущему - декомпозиции](https://en.wikipedia.org/wiki/Decomposition_(computer_science))
* [timeit](https://docs.python.org/3.7/library/timeit.html)
* [О профилировании](https://habr.com/en/company/mailru/blog/201594/)
* [Как работает профайлер](https://hackernoon.com/how-profilers-work-1826163e1bbc)
* [cprofile](https://python-scripts.com/cprofile-code-profiling)


# Заданиe на следующий урок
Посмотреть видео по list comprehension'ам - [один](https://stepik.org/lesson/3368/step/8?unit=951),
[два](https://stepik.org/lesson/3368/step/12?unit=951),
[три](https://stepik.org/lesson/3368/step/13?unit=951)


# Задания
* *Сделайте функцию, принимающую лист и возвращающую выпрямленный лист
(исходный не должен был измениться):
```python
flatten([1, [1, 2], 3, [[4, 5, [6]]]])
[1, 1, 2, 3, 4, 5, 6]
```
(15 баллов)
* Напишите функцию, принимающую число и вычисляющую число Фибоначчи с
номером поданного числа
```python
fibo(8)
21
```
(10 баллов)

В данных заданиях нельзя пользоваться функциями len, max, reversed, но
можно переиспользовать написанные вами функции
* Напишите функцию, возвращающую максимум, который есть в списке чисел
```python
maximum([100, 2, 3, 45, -2, 4])
100
```
(10 баллов)
* Функцию, возвращающую список в обратном порядке
```python
reverse([100, 2, 3, 45, -2, 4])
[4, -2, 45, 3, 2, 100]
```
(5 баллов)
* Функцию, вычисляющую среднее списка
```python
mean([100, 2, 3, 45, -2, 4])
25.333333333333332
```
(10 баллов)
* Функцию, находящую самый частый элемент в списке, если их несколько, то все
```python
moda([100, 3, 100, 2, 45, 45, 45, 3, 45, 3, 3, -2, 4])
(3, 45)
```
(10 баллов)
* Функцию, берущую указанный элемент из коллекции
```python
get([1, 2, 15, 36], 2)
15
get((1, 2, 15, 36), -1)
36
get({1: 2, 'kva': 36}, 'kva')
36
```
(10 баллов)
