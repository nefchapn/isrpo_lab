def perimeter(a, b, c):
    return a + b + c
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# a, b, c = map(int, input().split())
# if is_triangle(a, b, c):
#     print('Perimeter:', perimeter(a, b, c))
# else:
#     print('Not a valid triangle')