from solver.base import Solution
from solver.tree import *
import math

OPS_dict = {
    "Eq": "값을 계산하세요",
    "Add_Two": "두 수를 더하세요",
    "Add": "수를 더하세요"
}

def get_ops_type(expr):
    if expr.is_Add:
        if len(expr.args) == 2: return "Add_Two"
        else: return "Add"
    elif expr.is_Eq:
        return "Eq"
    elif expr.is_Integer:
        return expr.args[0]
    elif expr.is_Symbol:
        return expr

class Tree:
    def __init__(self, desc=None):
        self.desc = desc
        self.child = []

def tree_create(expr, node):
    for arg in expr.args:
        new_node = Tree(get_ops_type(arg))
        if isinstance(new_node.desc, str): # not end node
            tree_create(arg, new_node)
        node.child.append(new_node)

def tree_aggregate(node, before):
    desc = get_ops_type(before)
    vals = []
    steps = []
    ret_val = None
    if desc == "Eq": # child is always 2
        for i, child in enumerate(node.child):
            val, step = tree_aggregate(child, before.args[i])
            vals.append(val)
            if step: steps.append(step)
        after = Eq(vals[0], Integer(vals[1])) # right is always Integer
        ret_val = after # should not used....?
    elif desc == "Add_Two": # child is always 2
        for i, child in enumerate(node.child):
            val, step = tree_aggregate(child, before.args[i])
            vals.append(val)
            if step: steps.append(step)
        after = Integer(vals[0] + vals[1])
        ret_val = vals[0] + vals[1]
    elif isinstance(desc, Symbol):
        return desc, None
    elif isinstance(desc, int):
        return desc, None

    return ret_val, Solution(OPS_dict[desc], before, after, steps)

def solve(expr):
    """
    Example
    =======

    값을 계산하세요
    input: 2*3*4+3
    output: 27
    steps:
        ** 수를 곱하세요
        before: 2*3*4+3
        after: 24+3
        detail_steps:
            ** 두 수를 곱하세요
            before: 2*3*4
            after: 6*4

            ** 두 수를 곱하세요
            before: 6*4
            after: 24

        ** 두 수를 더하세요
        before: 24+3-4
        after: 27-4

        ** 두 수를 빼세요
        before: 27-4
        after: 23


     Challenge 1
     #1
     x = 2+3
     #2
     x+1 = 3
     #3
     2x+3 = 7
    """
    node = Tree(get_ops_type(expr))
    tree_create(expr, node)
    val, sol = tree_aggregate(node, expr)
    # expr = Add(
    #   Mul(Integer(2), Integer(3), Integer(4)),
    #   Integer(3),
    #   UMinus(Integer(2))
    # )
    # [description, before, after, steps]
    # step_1_sub_1 = Solution(description="두 수를 곱하세요", before=expr.args[0],
    #                         after=Mul(expr.args[0].args[0] * expr.args[0].args[1], *expr.args[0].args[2:]), steps=[])
    # step_1_sub_2 = Solution(description="두 수를 곱하세요", before=step_1_sub_1.after,
    #                         after=step_1_sub_1.after.args[0] * step_1_sub_1.after.args[1], steps=[])
    # step_1 = Solution(description="수를 곱하세요", before=expr,
    #                   after=Add(step_1_sub_2.after, *expr.args[1:]), steps=[step_1_sub_1, step_1_sub_2])
    # step_2 = Solution(description="두 수를 더하세요", before=step_1.after,
    #                   after=Add(step_1.after.args[0] + step_1.after.args[1], *step_1.after.args[2:]), steps=[])
    # step_3 = Solution(description="두 수를 빼세요", before=step_2.after,
    #                   after=step_2.after.args[0] - step_2.after.args[1].args[0], steps=[])
    # result = Solution(description="값을 계산하세요", before=expr, after=step_3.after, steps=[step_1, step_2, step_3])

    return sol



'''
from sympy import symbols, solve ,Eq
x = symbols('x')
eq1 = Eq(3+2*x,5*x - 7)

print(solve(eq1, x))
'''
