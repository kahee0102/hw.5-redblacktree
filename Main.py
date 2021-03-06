import os
from Node import Node
from Tree import RBT

def search():
    filenames = os.listdir('./input/')
    filename_lst = []

    for filename in filenames:
        filename_lst.append(filename)

    return filename_lst

def getFileData(names):
    data = []
    _dir = './input/'

    for name in names:
        f = open(_dir + name, 'r')
        lines = f.readlines()
        tmp_data = []

        for line in lines:
            tmp_data.append(int(line.strip("\n")))

        data.append(tmp_data)
        f.close()

    return data

def main():

    names = search()
    datas = getFileData(names)
    sequence = 0

    for data in datas:
        rbt = RBT()

        for i in data:
            if i > 0:
                rbt.insert(rbt.root, Node(i))
            elif i < 0:
                rbt.delete(rbt.root, -i)
            else:
                break

        print("filename = " + names[sequence])

        rbt.printNodeCount(rbt.root)

        rbt.printInsertNode(rbt.root)

        rbt.printDeleteNode(rbt.root)

        rbt.printMissNode(rbt.root)

        rbt.printBlackNodeCount(rbt.root)

        rbt.printBlackHeight(rbt.root)

        rbt.inOrderTraversal(rbt.root)

        sequence += 1

main()