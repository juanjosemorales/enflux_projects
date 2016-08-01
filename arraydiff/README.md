#Array Difference Calculator

## Description From the Test Question: This program that will take 2 arrays of integers, "current" and "target", and produce 2 arrays representing an additions list and a
   deletions list such that applying the additions and deletions to the "current" array will yield the "target" array. For example, given the following

inputs:

``current: [1, 3, 5, 6, 8, 9]``

``target: [1, 2, 5, 7, 9]``

The outputs would be:

``additions: [2, 7]``

``deletions: [3, 6, 8]``

So that the following is true:

``current([1, 3, 5, 6, 8, 9]) + additions([2, 7]) - deletions([3, 6, 8]) = target([1, 2, 5, 7, 9])``

##How To Run:
- This project runs on Python 3, so there is no need to install any additional libraries
- ``Download to desired directory and unzip``
- ``go into arraydiff/array_diff``
- ``The program takes two arguments -current and -target. Each is a list of integers and should be entered in the following format:
    -current|target int int int ...``
- ``python3 array_diff.py [-h] for usage ``

##Examples:
- Get Help: ``python3 array_diff.py -h``
- Run Sample: ``python3 array_diff.py -current 1 2 3 -target 2 3 4``
