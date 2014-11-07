# The Parade Problem
## Overview
[Parade](http://boardgamegeek.com/boardgame/56692/parade) is a card game published 2007. The cards are of six different colours/sorts and have a rank of 0-10, so in total 66 cards.

This algorithm tries to find the longest possible row of cards that do not break the games' two rules (if you break those rules, you'll need to take someone out of the parade):
 1. If there exists a card of rank i and at position j there cannot be a card at positions >= j+i with rank >= i.
 2. If there exists a card of rank i, at positions j and some type there cannot be a card of the same type at positions >= j+i of any rank.
 
So far the longest possible row I've found using this algorithm is 24.