# task1
Пример в задании плохой, так как легко видно, что условие (j * j < 0) никогда не выполнится, а значит и условие ((j > 0) && ( j * j < 0)) всегда будет ложным. А так как перед условием стоит оператор логического отрицания, всегда будет выполняться первая ветвь тернарного оператора, определить значение которой не составляет труда.
Реализованная библиотека вносит избыточность и запутанность в выражения с помощью побитовых операций, тригонометрических функций и возведения в степень.
_______________________________________________

## How to use the library:
* make sure that your Python version is **3.6 or higher** and "asteval" library is installed;
* place "myobfuscator" folder to the directory "...\Lib\site-packages" where "..." is your directory with Python. Also, you can place the jibrary in your project directory;
* to use obfuscator, do the following: 
    ```python
    from myobfuscator import ob
    ```
  `ob(value: int, known: dict, unknown: list)` takes 3 arguments, where:
  * _value_ is the value which should take the expression;
  * _known_ is a dict containing pairs of known vars, like {'a': 100, 'b': 200};
  * _unknown_ is a list with names of unknown vars, like ['x', 'y', 'z'].
______________________________________________

## Description of the files:
* \myobfuscator\sources.py : contains functions for obfuscator realization;
* tests.py : contains some tests for the library, including accuracy test on 1000 random sets of input data;
* main.py : running this file, you'll be suggested to enter input data for generation of the obfuscated expression. Also, the value of expression will be counted and printed.
