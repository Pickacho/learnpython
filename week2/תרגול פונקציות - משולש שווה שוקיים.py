def is_triangle_v1(a, b, c):
    if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
        print("these edges can make a triangle ")
        return True
    else:
        print("these edges can Not make a triangle ")
        return False


def equal_triangle_v1(a, b, c):
    if (a == b) and (a == c) and (c == b):
        print("we can make a even triangle from that")
        return True
    else:
        print("we can't build a even triangle from that")
        return False


def check_if_even_triangle(a, b, c):
    return is_triangle_v1(a, b, c) and equal_triangle_v1(a, b, c)


check_if_even_triangle(5, 5, 5)
