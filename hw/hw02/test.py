from operator import add, mul, sub

square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1


HW_SOURCE_FILE=__file__


# def product(n, term):
#
#     k = 1
#     sum = 1
#     while k <= n:
#         sum = sum * term(k)
#         k = k + 1
#     print(sum)
#     return sum
#
# product(3, identity)
# product(5, identity)
# product(3, square)
# product(3, increment)
# product(3, triple)

#
# def accumulate(combiner, base, n, term):
#
#     # >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
#
#     while n >= 1:
#         base = combiner(base, term(n))
#         n -= 1
#     print(base)
#
# accumulate(add, 0, 5, identity)
# accumulate(add, 11, 0, identity)
# accumulate(lambda x, y: x + y + 1, 2, 3, square)


