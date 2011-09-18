#!/usr/bin/python

from operations import *

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

def evaluate_rpn(expr):
  global OP_MAPS

  stack = []
  for token in expr:
    print stack
    if token not in OP_PRIS.keys():
      stack.insert(0, token)
    else:
      args = []
      for i in range(OP_ARG_COUNT[token]):
        args.insert(0, stack.pop(0))
      stack.insert(0, OP_MAPS[token](args))
  print stack
  return stack[0]

if __name__ == '__main__':
  evaluate_rpn([False, False, False, '\lnot', '\land', '\\rightarrow'])
