class Node:
    """
    이진 트리의 노드를 나타내는 클래스
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    이진 트리 클래스로, 노드를 추가하고 순회하는 기능을 제공
    """

    def __init__(self, root):
        self.root = root

    def __iter__(self):
        return InOrderIterator(self.root)


class InOrderIterator:
    """
    중위 순회를 위한 이터레이터
    """

    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def __next__(self):
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        result = node.value
        if node.right:
            self._push_left(node.right)
        return result


# 사용 예시
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)

tree = BinaryTree(root)

print("이진 트리 중위 순회:")
for value in tree:
    print(value)
