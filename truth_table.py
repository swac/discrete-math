#!/usr/bin/python

from itertools import product

from operations import *

class Assignment:
  """Assignment of n boolean variables"""
  def __init__(self, args):
    self.args = tuple(args)

  def __str__(self):
    string = ''
    for i in self.args:
      string += i and 'T' or 'F'
      string += ' & '
    return string

  def __getitem__(self, index):
    return self.args[index]

def convert_to_rpn(expr, variables):
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
      variables.append(token)
      output.append(token)
  while op_stack:
    output.append(op_stack.pop(0))
  variables.sort()
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
  return stack[0]

def evaluate_possibilities(expr, variables):
  possibilities = (Assignment(i) for i in product([True, False], repeat=len(variables)))
  indices = {}
  for i,j in enumerate(variables):
    indices[j] = i
  for p in possibilities:
    new_expr = []
    for token in expr:
      if token not in OP_PRIS.keys():
        new_expr.append(p[variables.index(token)])
      else:
        new_expr.append(token)
    row = str(p) + (evaluate_rpn(new_expr) and 'T' or 'F')
    print row + '\\\\'

if __name__ == '__main__':
  expr = raw_input('Enter expression with each token separated by a space: ')
  variables = []
  expr_tokens = expr.split()
  rpn_expr = convert_to_rpn(expr_tokens, variables)
  print '\\begin{tabular}{' + 'c'.join(('|' for i in range(len(variables) + 2))) + '}'
  print ' & '.join(variables) + ' & ' + expr + '\\\\\hline'
  evaluate_possibilities(rpn_expr, variables)
  print '\hline'
  print '\end{tabular}'
