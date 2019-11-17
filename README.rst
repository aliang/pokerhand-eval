Poker Hand Evaluator
====================

In pure python

27 January 2011, Alvin Liang

Introduction
------------

This is a pure python library to calculate the rank of the best poker
hand out of 5, 6, or 7 cards. It does not run the board for you, or
calculate winning percentage, EV, or anything like that. But if you give
it two hands and the same board, you will be able to tell which hand
wins.

It is nowhere near as fast as pypoker-eval, but it works if you can't
use C for some reason (the early stages of the first MIT pokerbot
competition come to mind). The core algorithm is slower, and you
obviously don't have the speed of C.

Quick Start
-----------

.. code:: python

    from pokereval.card import Card
    from pokereval.hand_evaluator import HandEvaluator

    hole = [Card(2, 1), Card(2, 2)]
    board = []
    score = HandEvaluator.evaluate_hand(hole, board)

Rank is 2-14 representing 2-A, while suit is 1-4 representing
spades, hearts, diamonds, clubs.

The Card constructor accepts two arguments, rank, and suit.

.. code:: python

    aceOfSpades = Card(14, 1)
    twoOfDiamonds = Card(2, 3)

Algorithm
---------

The algorithm for 5 cards is just a port of the algorithm that used to
be at the following URL. (I purposely broke the link because it now hosts
a malware site.)
httx://wwx.suffecool.net/poker/evaluator.html

I came up with the 6 and 7 card evaluators myself, using a very similar
card representation and applying some of the same ideas with prime
numbers. The idea was to strike a balance between lookup table size and
speed.

Also, I haven't included the code I used to generate the lookup tables,
but you should be able to do that with a simpler, slower algorithm.
Maybe I'll add that later as well.

There is also a two-card ranking/percentile algorithm that is unrelated
to the rest and may get cleaned up later. We used it at one point for
some pre-flop evaluation. Credit to Zach Wissner-Gross for developing
this.

Documentation is sparse at the moment, sorry about that, and obviously I
did not really bother to package it or clean it up. I may or may not
work on this in the future. Basically, I made it, so why not release it?

Contributors
------------

-  Me! Go me!
-  Zach Wissner-Gross (2-card algorithm)
-  arslr (Fixes for other Python versions)
-  Jim Kelly (Help with packaging, additional documentation)
-  hwmrocker (Improvements to Card constructor, Python 3 compatibility)
-  radekj (Tests, Python 3 compatibility)