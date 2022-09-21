
from logging import root
from tree_of_symptoms_base import SymptomBase, TreeOfSymptomsBase


class Symptom(SymptomBase):
    def __init__(self, symptom, severity):
        super().__init__(symptom, severity)
    """
        Add functions here if necessary
    """

class TreeOfSymptoms(TreeOfSymptomsBase):
    def __init__(self, root: Symptom):
        super().__init__(root)

    """
        Implement the described functions here !
    """
    def in_order_traversal(self):
        stack = []
        result = []
        og_root = self.root
        if self.root is None:
            return result
        else:
            while self.root is not None or len(stack) != 0:
                while self.root is not None:
                    stack.append(self.root)
                    self.root = self.root.left
                self.root = stack.pop()
                result.append(self.root)
                self.root = self.root.right
        self.root = og_root
        return result

    def post_order_traversal(self):
        stack = []
        result = []
        og_root = self.root
        if self.root is None:
            return result
        else:
            while self.root is not None or len(stack) != 0:
                while self.root is not None:
                    stack.append(self.root)
                    self.root = self.root.left
                temp_node = stack[-1].right
                if temp_node is not None:
                    self.root = temp_node
                else:
                    temp_node = stack.pop()
                    result.append(temp_node)
                    while len(stack) != 0 and temp_node == stack[-1].right:
                        temp_node = stack.pop()
                        result.append(temp_node)
        self.root = og_root
        return result

    def tree_restructure(self, severity):
        all_nodes = self.post_order_traversal()
        threshold = severity
        left_tree = []
        right_tree = []
        cur_sev = 0
        root_found = False
        for node in range(len(all_nodes)):
            temp_node = all_nodes[node]
            if temp_node.severity > cur_sev:
                cur_sev = temp_node.severity
                cur_sev_node = temp_node
            if temp_node.severity == threshold:
                self.root = temp_node
                root_found = True
            elif temp_node.severity > threshold:
                if root_found == True:
                    right_tree.append(temp_node)
                elif temp_node.severity <= cur_sev:
                    lowest_sev = temp_node
                    print("lowest", lowest_sev)
                    
                    if temp_node == all_nodes[-1]:
                        self.root = lowest_sev
                        print("here3")
                    continue
                else:
                    right_tree.append(temp_node)
            elif temp_node.severity < threshold:
                left_tree.append(temp_node)

        if len(left_tree) == len(all_nodes):
            self.root = cur_sev_node
        
        for node in range(len(left_tree)):
            self.root.left = left_tree[node]
            if left_tree[node] == left_tree[0]:
                self.root = self.root.left
            if left_tree[node].severity < self.root.severity:
                self.root.left = left_tree[node]
            elif left_tree[node].severity > self.root.severity:
                self.root.right = left_tree[node]
                
        for node in range(len(right_tree)):
            self.root.right = right_tree[node]
            if len(right_tree) == 0:
                break
            if right_tree[node] == right_tree[0]:
                self.root = self.root.right
            if right_tree[node].severity < self.root.severity:
                self.root.left = right_tree[node]
            elif right_tree[node].severity > self.root.severity:
                self.root.right = right_tree[node]
        
        print("root = ", self.root.left)
        print("right_tree = ", right_tree)
        print("left_tree = ", left_tree)


if __name__ == "__main__":
    """
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        REMOVE THE MAIN FUNCTION BEFORE SUBMITTING TO THE AUTOGRADER 
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        The following main function is provided for simple debugging only
    """

    cough = Symptom("Cough", severity=3)
    fever = Symptom("Fever", severity=6)
    red_eyes = Symptom("Red Eyes", severity=1)

    red_eyes.left = cough
    red_eyes.right = fever

    tree = TreeOfSymptoms(red_eyes)
    in_order_traversal = tree.post_order_traversal()
    correct_traversal = [cough, fever, red_eyes]
    for i, el in enumerate(in_order_traversal):
        assert el == correct_traversal[i]
    assert tree.root == red_eyes
    

    tree.tree_restructure(severity=2)
    in_order_traversal = tree.in_order_traversal()
    correct_traversal = [red_eyes, cough, fever]
    for i, el in enumerate(in_order_traversal):
        assert el == correct_traversal[i]
    assert tree.root == cough

