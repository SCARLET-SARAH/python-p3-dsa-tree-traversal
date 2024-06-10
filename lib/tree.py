class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self, data):
        self.root = self.create_tree(data)

    def create_tree(self, data):
        if 'tag_name' not in data:
            return None

        node = TreeNode(data)
        if 'children' in data:
            for child_data in data['children']:
                child = self.create_tree(child_data)
                node.children.append(child)

        return node

    def get_element_by_id(self, id):
        return self._get_element_by_id(self.root, id)

    def _get_element_by_id(self, node, id):
        if node is None:
            return None

        if 'id' in node.data and node.data['id'] == id:
            return node.data

        for child in node.children:
            result = self._get_element_by_id(child, id)
            if result is not None:
                return result

        return None