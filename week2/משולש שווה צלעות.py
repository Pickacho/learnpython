def is_triangle_v1(a, b, c):
    if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
        print("these edges can make a triangle ")
        return True
    else:
        print("these edges can Not make a triangle ")
        return False


# def is_all_equal_edges(a, b, c):
# check if triangle
# verify all edges are the same


def is_all_equal_edges(a, b, c):
    if not is_triangle_v1(a, b, c):
        print("These edges cannot be All equal-edges triangle because they cannot be a triangle at all ")
        return
    if a == b == c:
        print("These edges can make All-equal-edges triangle")
    else:
        print("these edges cannot make an All-equal-edges triangle")


def is_all_equal_edges_v2(a, b, c):
    return is_triangle_v1(a, b, c) and a == b == c


is_all_equal_edges(1, 1, 1)
