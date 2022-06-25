import numpy as np
import random


def read_from_file(filename):
    with open("Alphabeta.txt") as file:
        for line_number, line_content in enumerate(file):
            if line_number == 0:
                turn = int(line_content)
                depth = 2 * turn
            elif line_number == 1:
                branch = int(line_content)
                nodes = int((branch ** ((depth + 1)) - 1) / (branch - 1))
            elif line_number == 2:
                values = line_content.split(" ")
                minimum = int(values[0])
                maximum = int(values[1])

    return turn, depth, branch, nodes, minimum, maximum


def generating_tree(nodes, leaf):
    tree = np.zeros(nodes)

    for x in range(nodes - 1, nodes - leaf - 1, -1):
        tree[x] = int(minimum + random.random() * ((maximum - minimum) + 1))
    return tree


def alpha_beta_pruning(node, depth, alpha, beta, maximizingPlayer):
    global trimmed
    global max_value

    if depth == 0:
        return tree[node]

    if maximizingPlayer:
        p = -max_value
        child_nodes = (branch * node) + 1

        for x in range(0, branch):
            p = int(max(p, alpha_beta_pruning(child_nodes, depth - 1, alpha, beta, False)))
            alpha = (int(max(alpha, p)))

            if beta <= alpha:
                trimmed += branch - (x + 1)
                break

            child_nodes += 1
            x += 1
        return p
    else:
        p = max_value
        child_nodes = (branch * node) + 1

        for x in range(0, branch):
            p = int(min(p, alpha_beta_pruning(child_nodes, depth - 1, alpha, beta, True)))
            beta = (int(min(beta, p)))

            if beta <= alpha:
                trimmed += branch - (x + 1)
                break

            child_nodes += 1
            x += 1
        return p


if __name__ == '__main__':
    turn, depth, branch, nodes, minimum, maximum = read_from_file("Alphabeta.txt")
    leaf = int(branch ** depth)
    tree = generating_tree(nodes, leaf)

    print("Depth: ", depth)
    print("Branch: ", branch)
    print("Terminal States (Leaf Nodes): ", leaf)

    trimmed = 0
    max_value = 10000

    maximum_amount = alpha_beta_pruning(0, depth, -max_value, max_value, True)

    if maximum_amount != -max_value:
        print("Maximum amount: ", maximum_amount)
    else:
        print("No Solution")

    print("Comparisons: ", leaf)
    print("Comparisons: ", (leaf - trimmed))
    max(2, 3)

