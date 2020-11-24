parenthesis = ""


def printParenthesis(str, n):
    global result
    if (n > 0):
        _printParenthesis(str, 0, n, 0, 0);
    return parenthesis


def _printParenthesis(str, pos, n, open, close):
    global result, parenthesis
    if (close == n):
        for i in str:
            parenthesis += i
        parenthesis += ' '
        return
    else:
        if (open > close):
            str[pos] = '}'
            _printParenthesis(str, pos + 1, n, open, close + 1)
        if (open < n):
            str[pos] = '{'
            _printParenthesis(str, pos + 1, n,
                              open + 1, close)


def BalancedParentheses(n):
    str = [""] * 2 * n
    result = printParenthesis(str, n)
    return result[:-1]
