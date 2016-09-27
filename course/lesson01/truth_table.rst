======================================
EPAM Python Software Engineer Training
======================================

********
Lesson 1
********

.. contents::

Truth Table
===========
1. A and B or C
2. (A and B) or C
3. A and (B or C)
4. A or not (B or A) or (not C and B)
5. (A or not B) and (C or not A)

+----+-------+-------+-------+----------+----------+----------+----------+----------+
| No | A     | B     | C     |        1 |        2 |        3 |        4 |        5 |
+====+=======+=======+=======+==========+==========+==========+==========+==========+
| 1  | False | False | False |    False |    False |    False |     True |     True |
+----+-------+-------+-------+----------+----------+----------+----------+----------+
| 2  | False | False | True  |     True |     True |    False |     True |     True |
+----+-------+-------+-------+----------+----------+----------+----------+----------+
| 3  | False | True  | False |    False |    False |    False |     True |    False |
+----+-------+-------+-------+----------+----------+----------+----------+----------+
| 4  | False | True  | True  |     True |     True |    False |    False |    False |
+----+-------+-------+-------+----------+----------+----------+----------+----------+
| 5  | True  | False | False |    False |    False |    False |     True |    False |
+----+-------+-------+-------+----------+----------+----------+----------+----------+
| 6  | True  | False | True  |     True |     True |     True |     True |     True |
+----+-------+-------+-------+----------+----------+----------+----------+----------+
| 7  | True  | True  | False |     True |     True |     True |     True |    False |
+----+-------+-------+-------+----------+----------+----------+----------+----------+
| 8  | True  | True  | True  |     True |     True |     True |     True |     True |
+----+-------+-------+-------+----------+----------+----------+----------+----------+

Convert to HTML
===============

Commands
--------
1. rst2html truth_table.rst truth_table.html

Convert to PDF
==============

Commands
--------
1. rst2pdf truth_table.rst truth_table.pdf

Installed packages
------------------
In case of using python3, download python3 versions of this libraries. In most cases pip contain python 2 libraries.

1. aafigure==0.5
2. docutils==0.12
3. reportlab==3.3.0
4. rst2pdf===0.93.dev-r0
5. Sphinx==1.4.6
6. sphinxcontrib-aafig==1.0
7. svg2rlg==0.3
8. tenjin==1.1.1
9. tex==1.8

Install libraries for python 3
------------------------------
1. Download python 3 distribution
2. Unpack it
3. run: python setup.py install
