
from solver.base import Solution
from solver.tree import *
import math

class Recorder:
    def __init__(self):
        self.record = list() # staok
        self.before = list() # stack

    def add_before(self, bf):
        self.before.append(bf)

    def add_record(self, des, af, step):
        self.record.append([des, self.before.pop(), af, step])

def record_intp():

def trivial_ops(expr):
    if expr.is_Integer: return expr.args[0]
    elif expr.is_Uminus: return -expr.args[0]
    elif expr.is_Symbol: return expr
    else:
        # print("Not trivial?")
        return False

def core_sum(expr): # expr.args length == 1
    if len(expr.args) == 1:
        return exp_intp(expr.args[0])
    return  + core_sum()

def dynamic_ops(expr): # expr.args length >= 2
    if expr.is_Add:
        if len(expr.args) == 2:
            return exp_intp(expr.args[0]) + exp_intp(expr.args[1])
        else: # >= 3
            return

    elif expr.is_Eq:

    elif expr.is_Div:

def exp_intp(expr):
    is_trivial = trivial_ops(expr)

    if not is_trivial: # It's Dynamic!


def exp_recursion(expr, recorder:Recorder):
    # trivial ops
    if expr.is_Integer: #len(expr) == 1 and expr.args[0] != type(int):
        return expr.args[0]
    elif expr.is_Uminus:
        return -expr.args[0]
    elif expr.is_Symbol:
        return expr  # TODO
    # dynamic ops
    else:
        stack = [] # max len(2)
        for exp in expr.args:
            stack.append(exp_recursion(exp))
        if expr.is_Mul:
            recorder.add_record("두 수를 곱하세요", )

            return ret
        elif expr.is_Add:
            return sum(stack)
        elif expr.is_Eq:
            return Eq(stack[0],Integer(stack[1]))
            #return Solution(description="값을 계산하세요", before=expr, after= Eq(stack[0],Integer(stack[1])), steps=[v]) #TODO
        elif expr.is_Div: return stack[0] / stack[1]

'''
from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')
print(solve(x**2-1,x))
'''

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
    STEP_RECORD = Recorder()

    exp_recursion(expr, STEP_RECORD)
    #Solution(description="mola", before=expr, after=result)
    #return result
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

    return record_intp(STEP_RECORD)
