EXP_STEP = None

class LOG_TREE:
    def __init__(self, before=None, after=None, desc=None):
        self.child = []
        self.before = before
        self.after = after
        self.desc = desc

def is_trivial(expr):
    if expr.is_Integer: return expr.args[0]
    elif expr.is_UMinus: return -expr.args[1]
    elif expr.is_Symbol: return expr
    else:
        print("need more step")
        return False

def core_add(expr): # len expr == 2
    return is_trivial(expr.args[0]) + is_trivial(expr.args[1])

def core_eq(expr): # len expr == 2 & expr[0] == x
    return Eq(expr[0], exp_intp(expr[1]))

def exp_intp(expr, node):
    # Solution(description="수를 곱하세요", before=expr,
    # after=Add(step_1_sub_2.after, *expr.args[1:]), steps=[step_1_sub_1, step_1_sub_2])
    ret = is_trivial(expr)
    if not ret: # False
        if expr.is_Eq:
            desc = "값을 계산하세요"
            after = core_eq(expr)
        elif expr.is_Add:
            desc = "두 수를 더하세요"
            after = core_add(expr)

        cur_node = LOG_TREE(expr, after, desc)

        if node:
            node.child.append(cur_node)
        else:
            node = cur_node

        return after
    else: return ret
