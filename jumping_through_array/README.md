In a particular board game, a player has to try to advance through a sequence of positions. Each element in the sequence is a non-negative integer that represents the maximum "jump" the player can take from the index. The goal of the game is to jump until you reach the end if it is possible.

Example:
A = (3, 3, 1, 0, 2, 0, 1) is winnable by going from A[0] to A[1]. A[1] allows us to jump up to 3 places putting us at A[4] = 2. From A[4] we can jump to the end.

A = (3, 2, 0, 0, 2, 0, 1) can not be won because from A[0] we can only go to A[1], and both indices available to us from there (A[2] and A[3]) have zero allowed jumps.

When first looking at this problem I noticed that if I weight each index by how close it is to the end, and take the maximum jump in a given window, that will always be the best path