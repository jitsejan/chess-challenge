# Usage
```
jitsejan@jitsejan:~/code/chess$ python __main__.py -h
usage: __main__.py [-h] [-x WIDTH] [-y HEIGHT] [-k KING] [-q QUEEN]
                   [-b BISHOP] [-r ROOK] [-n KNIGHT] [-p]

optional arguments:
  -h, --help            show this help message and exit
  -x WIDTH, --horizontal WIDTH
                        Horizontal dimension (default=3)
  -y HEIGHT, --vertical HEIGHT
                        Vertical dimension (default=3)
  -k KING, --kings KING
                        Number of kings
  -q QUEEN, --queens QUEEN
                        Number of queens
  -b BISHOP, --bishops BISHOP
                        Number of bishops
  -r ROOK, --rooks ROOK
                        Number of rooks
  -n KNIGHT, --knights KNIGHT
                        Number of knights
  -p, --print           Print the solutions
```
# Notes
Tried to run the assignment on a 7 by 7 grid, but the current code fails at 32218 solutions. Besides that it took more than
15 hours to calculate the 32218 solutions before it crashed. I think the program runs out of memory, because the dictionary 
becomes to big. 
## Update 19 Mar 2016
Finished run of assignment on a 6 by 6 grid. After 15 hours it gave 18750 solutions
```
jitsejan@jitsejan:~/code/chess$ python __main__.py
Start 2016-03-17 21:24:10.370950
End 2016-03-18 12:20:11.744166
Duration 14:56:01.373216
Found 18750 solutions
```

## Possible improvements
* Calculate from two sides in parallel. One piece starts on top-left, one piece starts at bottom-right.
* Do not calculate the positions for the full grid. Take the first piece and only calculate for the top-left quarter of the
grid. Mirror the solutions first horizontally then vertically and remove the duplicate solutions.
* Calculate all positions first ignoring the margin for threatening the other pieces. Then walk through all possible 
positions of the pieces and cancel out all duplicates and invalid solutions.

# Coverage results
## Coverage result for the assignment on a 5 by 5 grid
[Coverage report](http://scripts.jitsejan.nl/htmlcov/htmlcov_assignment_5x5/ "Link")
```
jitsejan@jitsejan:~/code/chess$ coverage run __main__.py && coverage report
No chess pieces given. Nothing to do. Running the assignment!
Start 2016-03-18 10:38:29.322920
End 2016-03-18 10:38:38.690195
Duration 0:00:09.367275
Found 8 solutions
Name                                                                      Stmts   Miss  Cover
---------------------------------------------------------------------------------------------
__init__.py                                                                   0      0   100%
__main__.py                                                                  56     20    64%
board.py                                                                    132     23    83%
pieces.py                                                                    95      5    95%
/usr/local/lib/python2.7/dist-packages/pkg_resources/_vendor/six.py         444    442     1%
/usr/local/lib/python2.7/dist-packages/pkg_resources/extern/__init__.py      35     32     9%
---------------------------------------------------------------------------------------------
TOTAL                                                                      762    522    31%
```

## Coverage result for the unittest for this module
[Coverage report](http://scripts.jitsejan.nl/htmlcov/htmlcov_chesstest/ "Link")
```
jitsejan@jitsejan:~/code/chess$ coverage run chesstest.py && coverage report
...........
----------------------------------------------------------------------
Ran 11 tests in 1.591s

OK
Name                                                                      Stmts   Miss  Cover
---------------------------------------------------------------------------------------------
__init__.py                                                                   0      0   100%
board.py                                                                    132     21    84%
chesstest.py                                                                 63      0   100%
pieces.py                                                                    95      4    96%
/usr/local/lib/python2.7/dist-packages/pkg_resources/_vendor/six.py         444    442     1%
/usr/local/lib/python2.7/dist-packages/pkg_resources/extern/__init__.py      35     32     9%
---------------------------------------------------------------------------------------------
TOTAL                                                                       769    499    35%
```
## Coverage result for placing every piece once on a 4 by 4 grid, including printing the output
[Coverage report](http://scripts.jitsejan.nl/htmlcov/htmlcov_all_pieces_once_4x4/ "Link")
```
jitsejan@jitsejan:~/code/chess$ coverage run __main__.py -x 4 -y 4 -q 1 -k 1 -r 1 -b 1 -n 1 -p && coverage report
Chess pieces:
- Kings 1
- Queens 1
- Bishops 1
- Rooks 1
- Knights 1
Start 2016-03-18 10:39:46.622880
End 2016-03-18 10:39:47.010428
Found 16 solutions
- - - - - - - - - 
|   | Q |   |   | 
- - - - - - - - - 
|   |   |   | R | 
- - - - - - - - - 
| B |   |   |   | 
- - - - - - - - - 
| N |   | K |   | 
- - - - - - - - - 
- - - - - - - - - 
|   | Q |   |   | 
- - - - - - - - - 
|   |   |   | K | 
- - - - - - - - - 
| R |   |   |   | 
- - - - - - - - - 
|   |   | B | N | 
- - - - - - - - - 
- - - - - - - - - 
|   |   | Q |   | 
- - - - - - - - - 
| R |   |   |   | 
- - - - - - - - - 
|   |   |   | B | 
- - - - - - - - - 
|   | K |   | N | 
- - - - - - - - - 
- - - - - - - - - 
|   |   | Q |   | 
- - - - - - - - - 
| K |   |   |   | 
- - - - - - - - - 
|   |   |   | R | 
- - - - - - - - - 
| N | B |   |   | 
- - - - - - - - - 
- - - - - - - - - 
|   |   | R |   | 
- - - - - - - - - 
| Q |   |   |   | 
- - - - - - - - - 
|   |   |   | B | 
- - - - - - - - - 
|   | K |   | N | 
- - - - - - - - - 
- - - - - - - - - 
|   |   | B | N | 
- - - - - - - - - 
| Q |   |   |   | 
- - - - - - - - - 
|   |   |   | K | 
- - - - - - - - - 
|   | R |   |   | 
- - - - - - - - - 
- - - - - - - - - 
|   | R |   |   | 
- - - - - - - - - 
|   |   |   | Q | 
- - - - - - - - - 
| B |   |   |   | 
- - - - - - - - - 
| N |   | K |   | 
- - - - - - - - - 
- - - - - - - - - 
| N | B |   |   | 
- - - - - - - - - 
|   |   |   | Q | 
- - - - - - - - - 
| K |   |   |   | 
- - - - - - - - - 
|   |   | R |   | 
- - - - - - - - - 
- - - - - - - - - 
|   | R |   |   | 
- - - - - - - - - 
|   |   |   | K | 
- - - - - - - - - 
| Q |   |   |   | 
- - - - - - - - - 
|   |   | B | N | 
- - - - - - - - - 
- - - - - - - - - 
|   | K |   | N | 
- - - - - - - - - 
|   |   |   | B | 
- - - - - - - - - 
| Q |   |   |   | 
- - - - - - - - - 
|   |   | R |   | 
- - - - - - - - - 
- - - - - - - - - 
|   |   | R |   | 
- - - - - - - - - 
| K |   |   |   | 
- - - - - - - - - 
|   |   |   | Q | 
- - - - - - - - - 
| N | B |   |   | 
- - - - - - - - - 
- - - - - - - - - 
| N |   | K |   | 
- - - - - - - - - 
| B |   |   |   | 
- - - - - - - - - 
|   |   |   | Q | 
- - - - - - - - - 
|   | R |   |   | 
- - - - - - - - - 
- - - - - - - - - 
|   |   | B | N | 
- - - - - - - - - 
| R |   |   |   | 
- - - - - - - - - 
|   |   |   | K | 
- - - - - - - - - 
|   | Q |   |   | 
- - - - - - - - - 
- - - - - - - - - 
| N |   | K |   | 
- - - - - - - - - 
| B |   |   |   | 
- - - - - - - - - 
|   |   |   | R | 
- - - - - - - - - 
|   | Q |   |   | 
- - - - - - - - - 
- - - - - - - - - 
| N | B |   |   | 
- - - - - - - - - 
|   |   |   | R | 
- - - - - - - - - 
| K |   |   |   | 
- - - - - - - - - 
|   |   | Q |   | 
- - - - - - - - - 
- - - - - - - - - 
|   | K |   | N | 
- - - - - - - - - 
|   |   |   | B | 
- - - - - - - - - 
| R |   |   |   | 
- - - - - - - - - 
|   |   | Q |   | 
- - - - - - - - - 
Name                                                                      Stmts   Miss  Cover
---------------------------------------------------------------------------------------------
__init__.py                                                                   0      0   100%
__main__.py                                                                  56     18    68%
board.py                                                                    132      5    96%
pieces.py                                                                    95      4    96%
/usr/local/lib/python2.7/dist-packages/pkg_resources/_vendor/six.py         444    442     1%
/usr/local/lib/python2.7/dist-packages/pkg_resources/extern/__init__.py      35     32     9%
---------------------------------------------------------------------------------------------
TOTAL                                                                       762    501    34%
```
# Pylint
## Notes
The current result warns about too many public method because of the use of the unittest module. This message can be suppressed
in Pylint, but for completeness I left this in.
## Results
```
jitsejan@jitsejan:~/code/chess$ pylint chess
No config file found, using default configuration
************* Module chess.chesstest
R: 28, 0: Too many public methods (56/20) (too-many-public-methods)


Report
======
347 statements analysed.

Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |=          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |0      |0        |=          |
+-----------+-------+---------+-----------+
|refactor   |1      |1        |=          |
+-----------+-------+---------+-----------+
|warning    |0      |0        |=          |
+-----------+-------+---------+-----------+
|error      |0      |0        |=          |
+-----------+-------+---------+-----------+



Messages
--------

+------------------------+------------+
|message id              |occurrences |
+========================+============+
|too-many-public-methods |1           |
+------------------------+------------+



Global evaluation
-----------------
Your code has been rated at 9.97/10 (previous run: 9.97/10, -0.00)

Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |383    |65.81 |386      |-3.00      |
+----------+-------+------+---------+-----------+
|docstring |71     |12.20 |71       |=          |
+----------+-------+------+---------+-----------+
|comment   |90     |15.46 |90       |=          |
+----------+-------+------+---------+-----------+
|empty     |38     |6.53  |37       |+1.00      |
+----------+-------+------+---------+-----------+



Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |5      |5          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |8      |8          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|method   |53     |53         |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|function |3      |3          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
```
