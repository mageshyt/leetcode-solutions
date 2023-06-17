"""Problem Statement

You are playing a fun game. Your favorite character,
Seele, is very strong. She can kill monsters in either '1*
or '2' attacks.
There are 'N' monsteks ready to fight. You are given on
array 'A' of length 'N' such that 'A[i ]' represents the
number of attacks Seele takes to kill the 'i-th' enemy.
Seele and the monsters take turns attacking. They
attack once per turn. The damage dealt by the
monsters to Seele is negligible. Each attack from Seele
only targets one monster.
Seele also has a unique ability. If she kills a monster,
she gets to attack again in the same turn. However. if
the second attack kills another monster, Seele does not
get another extra attack.
Return the minimum number of turns Seele takes to kill
all the monsters.
For Example:

Let 'N' = 4, 'A' = [ 1, 1, 1, 2 ].
Turn 1: Seele attacks the first monster and
kills it. With her extra attack, she
targets the second monster and kills it.

Turn 2: Seele attacks the third monster and
kills it. With her extra attack, she
targets the fourth monster and reduces the
number of attacks to kill it to '1'
Turn 3: Seele attacks the fourth monster
and kills it.
It can be shown that this is the minimum
number of turns Seele can take.
Thus, the answer is '3'
"""
from collections import *


def butterflies(nums):

    # count the fequency of each number

    freq = Counter(nums)  # O(n)
    res = 0

    # start from the smallest number

    for i in range(1, max(nums) + 1):  # O(n)

        # if the number is not in the array, skip

        if i not in freq:
            continue

        # if the number is in the array, we need to kill all the monsters

        # with the same number of attacks

        # if the number of monsters is less than the number of attacks,

        # we need to kill them one by one

        if freq[i] <= i:
            res += 1

        # if the number of monsters is more than the number of attacks,
        # we can kill them in one turn

        else:
            # if the number of monsters is even, we can kill them in one turn

            if freq[i] % 2 == 0:  # even number of monsters can finish in one turn
                res += freq[i] // 2
            # if the number of monsters is odd, we can kill them in two turns
            else:
                # odd number of monsters can finish in two turns
                res += freq[i] // 2 + 1

    return res


print(butterflies([1, 2,  1, 2, 1, 2, 1, 1, 1, 2]))
