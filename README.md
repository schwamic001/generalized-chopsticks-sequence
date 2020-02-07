# generalized-chopsticks-sequence

See this link for details on the Generalized Chopsticks Sequence: http://oeis.org/A302403.

## Definitions
Chopsticks: https://en.wikipedia.org/wiki/Chopsticks_(hand_game)
Single-Handed Chopsticks: A variant of the game where each player has a single hand.  This makes the game deterministic.
Number of fingers on hand = n (in a conventional one-handed game, n = 5)
Number of fingers up at start of game = i (in a conventional game, i = 1)
Michael/AJ: The two players of a game of Single-Handed Chopsticks.  Michael always plays first.
GC Number: A number n is part of the GC sequence if all i from 1 to n-1 result in the same winner in a game of Single-Handed Chopsticks
Consistency: A number n is consistent if it meets these two criteria:
    (1) Is a GC number
    (2) The game always ends on the same turn for any i from 1 to n-1

## Documents
There are 2 documents in this repository relating to the sequence:
1) GC Numbers.xlsx: Excel workbook that generates all GC numbers through 100 and shares a few insights.  Reference this document for background on the game of Single-Handed Chopsticks and the development of the sequence.  Produced by Michael Schwalen & AJ Robinson.
2) generalized_chopsticks_sequence.R: R code that generates all GC numbers through 1,000.  Produced by Michael Schwalen, AJ Robinson, & Angela Lin

## Other Notes
Feel free to use the code and Excel document however you see fit.
Enjoy!
