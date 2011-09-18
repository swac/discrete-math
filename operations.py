lnot = lambda args : not args[0]

land = lambda args: args[0] and args[1]

lor = lambda args: args[0] or args[1]

rightarrow = lambda args: not args[0] or args[1]

leftrightarrow = lambda args: args[0] == args[1]

OPS = {
  '\lnot' : {
    'pri'     : 5,
    'func'    : lnot,
    'argc'    : 1
  },
  '\land' : {
    'pri'     : 4,
    'func'    : land,
    'argc'    : 2
  },
  '\lor' : {
    'pri'     : 3,
    'func'    : lor,
    'argc'    : 2
  },
  '\\rightarrow' : {
    'pri'     : 2,
    'func'    : rightarrow,
    'argc'    : 2
  },
  '\leftrightarrow' : {
    'pri'     : 1,
    'func'    : leftrightarrow,
    'argc'    : 2
  }
}
