# Poker Hand Evaluator

In pure python

27 January 2011, Alvin Liang

## Introduction

This is a pure python library to calculate the rank of the best poker hand
out of 5, 6, or 7 cards. It does not run the board for your, or calculate
winning percentage, EV, or anything like that. But if you give it two hands
and the same board, you will be able to tell which hand wins.

It is nowhere near as fast as pypoker-eval, but it works if you can't use C
for some reason (the early stages of the first MIT pokerbot competition come
to mind). The core algorithm is slower, and you obviously don't have
the speed of C.

## Quick Start

````python
from card import Card
from hand_evaluator import HandEvaluator

hole = [Card(2, 1), Card(2, 2)]
board = []
score = HandEvaluator.evaluate_hand(hole, board)
````

## Algorithm

The algorithm for 5 cards is just a port of this algorithm:
http://www.suffecool.net/poker/evaluator.html

I came up with the 6 and 7 card evaluators myself, using a very similar card
representation and applying some of the same ideas with prime numbers. The
idea was to strike a balance between lookup table size and speed.

Also, I haven't included the code I used to generate the lookup tables, but
you should be able to do that with a simpler, slower algorithm. Maybe I'll
add that later as well.

There is also a two-card ranking/percentile algorithm that is unrelated to
the rest and may get cleaned up later. We used it at one point for some
pre-flop evaluation. Credit to Zach Wissner-Gross for developing this.

Documentation is sparse at the moment, sorry about that, and obviously I did
not really bother to package it or clean it up. I may or may not work on this
in the future. Basically, I made it, so why not release it?

## Contributors

* Me! Go me!
* Zach Wissner-Gross
* arslr