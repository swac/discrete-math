#!/usr/bin/python

OP_PRIS = {
  '\lnot'            : 5,
  '\land'            : 4,
  '\lor'             : 3,
  '\\rightarrow'      : 2,
  '\leftrightarrow'  : 1
}

def convert_to_rpn(expr):
  global OP_PRIS
  output = []
  op_stack = []

  for token in expr:
    if token in OP_PRIS.keys():
      while op_stack and OP_PRIS[op_stack[0]] >= OP_PRIS[token]:
        output.append(op_stack.pop(0))
      op_stack.insert(0, token)
    elif token == '(':
      op_stack.insert(0, token)
    elif token == ')':
      while op_stack[0] != '(':
        output.append(op_stack.pop(0))
      op_stack.remove(0)
    else:
      output.append(token)
  while op_stack:
    output.append(op_stack.pop(0))
  return output

if __name__ == '__main__':
  print convert_to_rpn('p \\rightarrow q \land \lnot r'.split())
