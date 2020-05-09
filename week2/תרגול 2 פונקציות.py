def is_triangle_v1(a, b, c):
    if ((a +b) > c) and ((a + c) > b) and ((b + c) > a):
        print("these edges can make a triangle ")
        return True
    else:
        print("these edges can Not make a triangle ")
        return False

# x = is_triangle_v1(3, 4, 5)
# print(x)


def is_triangle_option_v2(a, b, c):
    if ((a +b) <= c) or ((a + c) <= b) or ((b + c) <= a):
        print("these edges can Not make a triangle ")
    else:
        print("these edges can make a triangle ")

#is_triangle(1, 2, 3)


def is_right_angle_triangle_v4(a, b, c):
    if ((a +b) > c) and ((a + c) > b) and ((b + c) > a):
        print("these edges can make a triangle ")
    else:
        print("these edges can Not make a triangle ")
    #

    if ((a ** 2) + (b ** 2)) == (c ** 2) or ((b ** 2) + (c ** 2)) == (a ** 2) or ((a ** 2) + (c ** 2)) == (b ** 2):
        print("This will create a Pyhagorean Triangle")
    # we need to check all options of a, b, c
    else:
        print("this won\'t work for you")

#is_right_angle_triangle(5, 3, 5)


def is_it_right_angle_triangle_v5(a, b, c):
    if not is_triangle_v1(a, b, c):
        print("these edges cannot be right for triangle because they cannot be a triangle at all")
        return
    if ((a ** 2) + (b ** 2)) == (c ** 2) or ((b ** 2) + (c ** 2)) == (a ** 2) or ((a ** 2) + (c ** 2)) == (b ** 2):
        print("these edges# can be a right angle triangle ")
    else:
        print("these edges cannot be a right triangle")


def is_pythagorean(a, b, c):
    return ((a ** 2) + (b ** 2)) == (c ** 2)


def is_pythagorean_combition(a, b, c):
    return is_pythagorean(3, 4, 5) or is_pythagorean(5, 4, 3) or is_pythagorean(3, 5, 4)


def is_right_angle_triangle_v5_1(a, b, c):
    if not is_triangle_v1(a, b, c):
        print("these edges cannot be a right angle because they cannot be a triangle at all")
        return
    if is_pythagorean_combition(a, b, c):
        print("these edges can be a right angle triangle")
    else:
        print("these edges cannot be a right triangle")


is_right_angle_triangle_v5_1(1, 2, 1)
