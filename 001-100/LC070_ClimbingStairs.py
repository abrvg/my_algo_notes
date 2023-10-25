
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
def climbStairs(n: int) -> int:

    if n == 1 or n ==0:
        return 1
    else:
        return climbStairs(n-1) + climbStairs(n-2)


def climbStairsFast(n: int) -> int:
    a, b = 1, 1
    for i in range(n):
        a, b = b, a+b

    return a


