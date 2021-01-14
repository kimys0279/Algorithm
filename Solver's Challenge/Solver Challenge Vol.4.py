from solver.base import Solution
from solver.tree import *
import copy
import math

# OPS_dict = {
#     "Eq": "값을 계산하세요",
#     "Add_Two": "두 수를 더하세요",
#     "Add": "수를 더하세요"
# }
#
# HEAD = None
#
# def get_ops_type(expr):
#     if expr.is_Add:
#         if len(expr.args) == 2: return "Add_Two"
#         else: return "Add"
#     elif expr.is_Eq:
#         return "Eq"
#     elif expr.is_Integer:
#         return expr.args[0]
#     elif expr.is_Symbol:
#         return expr
#
# class Tree:
#     def __init__(self, desc=None):
#         self.desc = desc
#         self.child = []
#
# def tree_create(expr, node):
#     for arg in expr.args:
#         new_node = Tree(get_ops_type(arg))
#         if isinstance(new_node.desc, str): # not end node
#             tree_create(arg, new_node)
#         node.child.append(new_node)
#
# def tree_calculator(node, before):
#     desc = get_ops_type(before)
#     vals = []
#     steps = []
#     ret_val = None
#     if desc == "Eq": # child is always 2
#         for i, child in enumerate(node.child):
#             val, step = tree_calculator(child, before.args[i])
#             vals.append(val)
#             if step: steps.append(step)
#         after = Eq(vals[0], Integer(vals[1])) # right is always Integer
#         ret_val = after # should not used....?
#     elif desc == "Add_Two": # child is always 2
#         if isinstance(before.args[0], Integer) and isinstance(before.args[1], Integer):
#             for i, child in enumerate(node.child):
#                 val, step = tree_calculator(child, before.args[i])
#                 vals.append(val)
#                 if step: steps.append(step)
#             after = Integer(vals[0] + vals[1])
#             ret_val = vals[0] + vals[1]
#         else: # left Symbol is included
#             # node.child[0] -- Symbol , node.child[1] - int
#             # (EQ LEFT)
#             temp_add = Tree("Add_Two")
#             temp_left = node.child[1]
#             temp_right = Tree(-node.child[1].desc)
#             use_val = -node.child[1].desc
#             temp_add.child.append(temp_left)
#             temp_add.child.append(temp_right)
#             node.child[1] = temp_add
#             # (EQ RIGHT) - eq_right_add
#             temp_add = Tree("Add_Two")
#             temp_left = HEAD.child[1]
#             temp_right = Tree(use_val)
#             temp_add.child.append(temp_left)
#             temp_add.child.append(temp_right)
#             HEAD.child[1] = temp_add
#
#             return
#
#     elif isinstance(desc, Symbol):
#         return desc, None
#     elif isinstance(desc, int):
#         return desc, None
#
#     return ret_val, Solution(OPS_dict[desc], before, after, steps)

def expr_calculator(node, full_before, parent=None):
    steps = []
    vals = []
    if node.is_Eq: # args length is 2
        left, left_step = expr_calculator(node.args[0], full_before, parent=node)

        if not left.is_Symbol:
            next, next_step = expr_calculator(left, full_before, parent=node)
            left_step.steps=[next_step]

            left.args = [left.args[0]]
            left_step.steps.append(Solution(
                description="계산 하세요", before=next_step.after,
                after=copy.deepcopy(full_before),
                steps=[]
            ))

        vals.append(left)
        if left_step: steps.append(left_step)

        right, right_step = expr_calculator(node.args[1], full_before, parent=node)

        vals.append(right)
        if right_step: steps.append(right_step)

        # check terminal
        if isinstance(left, Mul) and isinstance(right, Integer):
            return node, steps[0].before, steps[-1].after, steps, True
        else:
            return node, steps[0].before, steps[-1].after, steps, False
        # Solution(
        #     description="깂을 계산하세요", before=steps[0].before,
        #     after=steps[-1].after,
        #     steps=steps
        # )
    elif node.is_Mul:
        if isinstance(node.args[0], Integer) and isinstance(node.args[1], Integer):
            left, left_step = expr_calculator(node.args[0], full_before, parent=node)
            right, right_step = expr_calculator(node.args[1], full_before, parent=node)

            vals.append(left)
            vals.append(right)
            if left_step: steps.append(left_step)
            if right_step: steps.append(right_step)

            full_before_temp = copy.deepcopy(full_before)
            ret_val = vals[0].args[0] * vals[1].args[0]

            parent.args = list(parent.args)
            parent.args[1] = Integer(ret_val)

            return ret_val, Solution(
                description="두 수를 곱하세요", before=full_before_temp,
                after=copy.deepcopy(full_before),
                steps=steps
            )
        elif isinstance(node.args[0], Symbol) and isinstance(node.args[1], Integer):
            full_before_temp = copy.deepcopy(full_before)

            node.args = list(node.args)
            use_val = -node.args[1].args[0]
            node.args[1] = Add(node.args[1], Integer(use_val))

            right = full_before.args[1]
            full_before.args = list(full_before.args)
            full_before.args[1] = Add(right, Integer(use_val))

    elif node.is_Add: # args length is 2 == (Add_Two)
        if isinstance(node.args[0], Integer) and isinstance(node.args[1], Integer):
            left, left_step = expr_calculator(node.args[0], full_before, parent=node)
            right, right_step = expr_calculator(node.args[1], full_before, parent=node)

            vals.append(left)
            vals.append(right)
            if left_step: steps.append(left_step)
            if right_step: steps.append(right_step)

            full_before_temp = copy.deepcopy(full_before)
            ret_val = vals[0].args[0] + vals[1].args[0]

            parent.args = list(parent.args)
            parent.args[1] = Integer(ret_val)

            return ret_val, Solution(
                description="두 수를 더하세요", before=full_before_temp,
                after=copy.deepcopy(full_before),
                steps=steps
            )
        elif isinstance(node.args[0], Symbol) and isinstance(node.args[1], Integer):
            full_before_temp = copy.deepcopy(full_before)

            node.args = list(node.args)
            use_val = -node.args[1].args[0]
            node.args[1] = Add(node.args[1], Integer(use_val))

            right = full_before.args[1]
            full_before.args = list(full_before.args)
            full_before.args[1] = Add(right, Integer(use_val))

            return node, Solution(
                description="계산 하세요", before=full_before_temp,
                after=copy.deepcopy(full_before),
                steps=steps
            )
        elif isinstance(node.args[0], Symbol) and isinstance(node.args[1], Add):
            return expr_calculator(node.args[1], full_before, node)
        elif isinstance(node.args[0], Mul) and isinstance(node.args[1], Add):
            return expr_calculator(node.args[1], full_before, node)
        elif isinstance(node.args[0], Mul) and isinstance(node.args[1], Integer):
            full_before_temp = copy.deepcopy(full_before)

            node.args = list(node.args)
            use_val = -node.args[1].args[0]
            node.args[1] = Add(node.args[1], Integer(use_val))

            right = full_before.args[1]
            full_before.args = list(full_before.args)
            full_before.args[1] = Add(right, Integer(use_val))

            return node, Solution(
                description="계산 하세요", before=full_before_temp,
                after=copy.deepcopy(full_before),
                steps=steps
            )

    elif node.is_Symbol:
        return node, None
    elif node.is_Integer:
        return node, None

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
    # node = Tree(get_ops_type(expr))
    # tree_create(expr, node)
    # val, sol = tree_calculator(node, expr)

    not_complete = True

    while not_complete:
        val, before, after, steps, not_complete = expr_calculator(expr, expr, None)

    sol = Solution(
        description="값을 계산하시오",
        before=before,
        after=after,
        steps=steps
    )

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
