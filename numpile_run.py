from numpile import *


if __name__ == "__main__":
    source = open(sys.argv[1]).read()
    transformer = PythonVisitor()
    tree = transformer(source)
    #print(dump(tree))
    (ty, mgu) = typeinfer(tree)
    #print("infer:", (ty, mgu))
    fun = specialize(tree, ty, mgu)
    #print(fun)
    print(fun(1, 2))
