from BinaryTree import BinaryTree
import time





if __name__ == "__main__":
    root = BinaryTree(5)

    root.insertLeft(30)

    root.getLeftChild().insertLeft(40)

    root.getLeftChild().insertRight(25)

    root.insertRight(2)
    root.getRightChild().insertLeft(4)

    
    print("----- postorder traversal ----")
    t1 = time.time()
    res = root.postorder()
    t2 = time.time()
    print(res)
    print("postorder traversal took", t2 - t1, "seconds")
    
    print()
    print("----- preorder traversal -----")
    t1 = time.time()
    res = root.preorder()
    print(res)
    t2 = time.time()
    print("preorder traversal took", t2 - t1, "seconds")
    