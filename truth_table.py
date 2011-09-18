#!/usr/bin/python

from itertools import product

from operations import *

VARS = set()

def convert_to_rpn(expr):
  global OP_PRIS
  global VARS
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
      VARS.add(token)
      output.append(token)
  while op_stack:
    output.append(op_stack.pop(0))
  return output

def evaluate_rpn(expr):
  global OP_MAPS

  stack = []
  for token in expr:
    if token not in OP_PRIS.keys():
      stack.insert(0, token)
    else:
      args = []
      for i in range(OP_ARG_COUNT[token]):
        args.insert(0, stack.pop(0))
      stack.insert(0, OP_MAPS[token](args))
  print stack
  return stack[0]

def evaluate_possibilities(expr):
  global VARS
  possibilities = product([True, False], repeat=len(VARS))
  indices = {}
  for i,j in enumerate(VARS):
    indices[j] = i
  print indices
  for p in possibilities:
    new_expr = []
    for token in expr:
      if token not in OP_PRIS.keys():
        new_expr.append(p[indices[token]])
      else:
        new_expr.append(token)
    evaluate_rpn(new_expr)

if __name__ == '__main__':
  evaluate_possibilities(['p', 'q', 'r', '\lnot', '\land', '\\rightarrow'])
