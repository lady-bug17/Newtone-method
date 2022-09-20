def calculate_first(x0):
    f1 = [-4 * x0[0] * x0[1] + 4 * pow(x0[0], 3) + 4 * x0[0] - 4, 2*x0[1]-2*pow(x0[0], 2)]
    print("f'(x) : " + str(f1))
    return f1


def calculate_second(x0):
    f2 = [[-4*x0[1]+12*pow(x0[0], 2)+4, -4*x0[0]],
          [-4*x0[0], 2]]
    print("f''(x) : " + str(f2))
    return f2


def calculate_slar(f2, f1):
    result = []
    if f2[1][0] == 0:
        pass
    elif f2[0][0] != 0:
        coef = f2[1][0]/f2[0][0]
        f2[0][0] *= coef
        f2[0][1] *= coef
        f1[0] *= coef
        f2[1][0] = 0
        f2[1][1] -= f2[0][1]
        f1[1] -= f1[0]
    result.append(f1[1]/f2[1][1])
    result.append((f1[0]-f2[0][1]*result[0])/f2[0][0])
    result.reverse()
    print("deltas: " + str(result))
    return result


def calculate_next_approximation(x0, delta_x0):
    x0[0], x0[1] = x0[0]-delta_x0[0], x0[1]-delta_x0[1]
    print("new approximation: " + str(x0))


def find_min(x):
    return pow(x[1]-pow(x[0], 2), 2)+2*pow(1-x[0], 2)


x = [0, 0]
f1 = calculate_first(x)
f2 = calculate_second(x)
iter = 0
while f1[0] != 0 or f1[1] != 0:
    delta_x = calculate_slar(f2, f1)
    calculate_next_approximation(x, delta_x)
    f1 = calculate_first(x)
    f2 = calculate_second(x)
    iter += 1
print("minimum point: " + str(x))
print("min: " + str(find_min(x)))
print("iterations: " + str(iter))

