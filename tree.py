from typing import Generic, TypeVar, Union

ElemType = TypeVar('ElemType')


class BinaryTree(Generic[ElemType]):
    class Node:
        def __init__(self, _value: ElemType):
            self.value = _value
            self.l_child = None
            self.r_child = None
            self.parent = None

    def __init__(self):
        self.root_ptr: Union[BinaryTree.Node, None] = None

    def is_empty(self) -> bool:
        return self.root_ptr is None

    def preorder(self) -> list[ElemType]:
        _traversal_list = []

        if self.is_empty():
            return _traversal_list
        else:
            def recursion(tmp_ptr: BinaryTree.Node) -> None:
                if tmp_ptr is not None:
                    _traversal_list.append(tmp_ptr.value)
                    recursion(tmp_ptr.l_child)
                    recursion(tmp_ptr.r_child)

        recursion(self.root_ptr)
        return _traversal_list

    def inorder(self) -> list[ElemType]:
        _traversal_list = []

        if self.is_empty():
            return _traversal_list
        else:
            def recursion(tmp_ptr: BinaryTree.Node) -> None:
                if tmp_ptr is not None:
                    recursion(tmp_ptr.l_child)
                    _traversal_list.append(tmp_ptr.value)
                    recursion(tmp_ptr.r_child)

        recursion(self.root_ptr)
        return _traversal_list

    def postorder(self) -> list[ElemType]:
        _traversal_list = []

        if self.is_empty():
            return _traversal_list
        else:
            def recursion(tmp_ptr: BinaryTree.Node) -> None:
                if tmp_ptr is not None:
                    recursion(tmp_ptr.l_child)
                    recursion(tmp_ptr.r_child)
                    _traversal_list.append(tmp_ptr.value)

        recursion(self.root_ptr)
        return _traversal_list


if __name__ == '__main__':
    bi_tree = BinaryTree[int]()
    print(bi_tree.is_empty())
    bi_tree.root_ptr = BinaryTree.Node(1)
    bi_tree.root_ptr.l_child = BinaryTree.Node(2)
    bi_tree.root_ptr.r_child = BinaryTree.Node(3)
    bi_tree.root_ptr.l_child.l_child = BinaryTree.Node(4)
    bi_tree.root_ptr.l_child.r_child = BinaryTree.Node(5)

    print(bi_tree.preorder())
    print(bi_tree.inorder())
    print(bi_tree.postorder())
