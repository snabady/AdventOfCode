from __future__ import annotations
import sys 
from typing import Optional
# https://adventofcode.com/2022/day/7
#                            |                         _...._
#                         \  _  /                    .::o:::::.
#                          (\o/)                    .:::'''':o:.
#                      ---  / \  ---                :o:_    _:::
#                           >*<                     `:}_>()<_{:'
#                          >0<@<                 @    `'//\\'`    @
#                         >>>@<<*              @ #     //  \\     # @
#                        >@>*<0<<<           __#_#____/'____'\____#_#__
#                       >*>>@<<<@<<         [__________________________]
#                      >@>>0<<<*<<@<         |=_- .-/\ /\ /\ /\--. =_-|
#                     >*>>0<<@<<<@<<<        |-_= | \ \\ \\ \\ \ |-_=-|
#                    >@>>*<<@<>*<<0<*<       |_=-=| / // // // / |_=-_|
#      \*/          >0>>*<<@<>0><<*<@<<      |=_- |`-'`-'`-'`-'  |=_=-|
#  ___\\U//___     >*>>@><0<<*>>@><*<0<<     | =_-| o          o |_==_|
#  |\\ | | \\|    >@>>0<*<<0>>@<<0<<<*<@<    |=_- | !     (    ! |=-_=|
#  | \\| | _(UU)_ >((*))_>0><*<0><@<<<0<*<  _|-,-=| !    ).    ! |-_-=|_
#  |\ \| || / //||.*.*.*.|>>@<<*<<@>><0<<@</=-((=_| ! __(:')__ ! |=_==_-\
#  |\\_|_|&&_// ||*.*.*.*|_\\db//__     (\_/)-=))-|/^\=^=^^=^=/^\| _=-_-_\
#  """"|'.'.'.|~~|.*.*.*|     ____|_   =('.')=//   ,------------.
#  jgs |'.'.'.|   ^^^^^^|____|>>>>>>|  ( ~~~ )/   (((((((())))))))
#      ~~~~~~~~         '""""`------'  `w---w`     `------------'

class TreeDay:

    def __init__(self, name, parent:Optional[TreeDay]=None) -> None:
        self.name: str                  = name
        self.parent: Optional[TreeDay]  = parent
        self.files: dict[str, int]      = {}
        self.dirs: dict[str, TreeDay]   = {}
        self.size: int                  = 0

    def add_file(self,filename, size):
        self.files[filename] = size

    def add_dir(self, dirname):
        if dirname not in self.dirs:
            self.dirs[dirname] = TreeDay(dirname, self)
   
def print_tree(tree, indent=0):
    print("  " * indent + f"- {tree.name} (dir)")
    for name, size in tree.files.items():
        print("  " * (indent + 1) + f"- {name} (file, {size})")
    for sub in tree.dirs.values():
        print_tree(sub, indent + 1)

def get_dir_size(tree)->int:
    current_size =0
    for size in tree.files.values():
        current_size += size
    for dir_ in tree.dirs.values():
        current_size += get_dir_size(dir_)
    tree.size=current_size
    return current_size

def sum_dir_size(tree) -> int :
    size = tree.size 
    for dir_ in tree.dirs.values():
        size += sum_dir_size(dir_)
    return size 

def part_one(tree) -> int:
    res=0
    if tree.size <= 100000:
        res+=tree.size 
    for dirs in tree.dirs.values():
        res+=part_one(dirs)
    return res
   

def parsedata() -> TreeDay:
    data =  [ x.strip() for x in sys.stdin.read().split("$") ][1:]
    
    root = TreeDay("/")
    current=root
    for group in data:
        if group.startswith("cd"):
            parts = group.split(" ")
            if parts[1]=="/":
                current = root
            elif parts[1]=="..":
                if current.parent != None:
                    current =  current.parent
            else:
                current.add_dir(parts[1]) 
                current = current.dirs[parts[1]]
        elif group.startswith("ls"):
            parts = group.splitlines()[1:]
            for part in parts:
                if part.startswith("dir"):
                    current.add_dir(part.split(" ")[1])
                else:
                    current.add_file(part.split(" ")[1], int(part.split(" ")[0]))
    return root

root = parsedata()
#print_tree(root)
total_size = get_dir_size(root)
print("part_one: ", part_one(root))
def part_two(tree):
    used = root.size 
    unused = 70000000 - used
    spaceneeded = 30000000 - unused
    res=[]
    if tree.size >= spaceneeded :
        res.append(tree.size)
    for node in tree.dirs.values():
        res.extend(part_two(node))

    return res
part_two_=part_two(root) 
print("part two: ", min(part_two_))
