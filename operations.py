#!/usr/bin/python

OP_PRIS = {
  '\lnot'            : 5,
  '\land'            : 4,
  '\lor'             : 3,
  '\\rightarrow'     : 2,
  '\leftrightarrow'  : 1
}

lnot = lambda args : not args[0]

land = lambda args: args[0] and args[1]

lor = lambda args: args[0] or args[1]

rightarrow = lambda args: not args[0] or args[1]

leftrightarrow = lambda args: args[0] == args[1]

OP_MAPS = {
  '\lnot'            : lnot,
  '\land'            : land,
  '\lor'             : lor,
  '\\rightarrow'     : rightarrow,
  '\leftrightarrow'  : leftrightarrow
}

OP_ARG_COUNT = {
  '\lnot'            : 1,
  '\land'            : 2,
  '\lor'             : 2,
  '\\rightarrow'     : 2,
  '\leftrightarrow'  : 2
}
