import timeit
global_base = 2
global_exponent = 100


# Exponential function with big-O(n)
def exponential_n(base, exponent):
    answer = 1
    for i in range(0, exponent):
        answer *= base

    return answer


# Exponential function recursive
def exponential_recursive(base, exponent):
    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        return exponential_recursive(base, exponent / 2) * exponential_recursive(base, exponent / 2)
    else:
        return exponential_recursive(base, exponent // 2) * exponential_recursive(base, exponent // 2) * base


# Exponential function with simple memoization (DP)
def exponential_recursive_memo(base, exponent):
    if exponent == 0:
        return 1

    half_way = exponential_recursive_memo(base, exponent//2)
    if exponent % 2 == 0:
        return half_way * half_way
    else:
        return half_way * half_way * base


def call_e_n():
    exponential_n(global_base, global_exponent)


def call_r():
    exponential_recursive(global_base, global_exponent)


def call_r_m():
    exponential_recursive_memo(global_base, global_exponent)


if __name__ == '__main__':

    result = pow(global_base, global_exponent)
    print("Result :" + str(result))

    print("Linear approach")
    print("time : " + str(timeit.timeit("call_e_n()", globals=locals())))
    print()
    print("Recursive approach")
    print("time : " + str(timeit.timeit("call_r()", globals=locals())))
    print()
    print("Recursive approach with memoization")
    print("time : " + str(timeit.timeit("call_r_m()", globals=locals())))
    print()
