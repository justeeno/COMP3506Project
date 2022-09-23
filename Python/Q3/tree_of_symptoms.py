
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
        all_nodes = self.in_order_traversal()
        threshold = severity
        ideal_root = None
        below_root = None


        for node in all_nodes:
            if node.severity >= threshold and (ideal_root is None or node.severity < ideal_root.severity):
                ideal_root = node
            elif node.severity < threshold and (below_root is None or node.severity > below_root.severity):
                below_root = node

        if ideal_root is not None:
            self.root = ideal_root
        else:
            self.root = below_root
        
        all_nodes.remove(self.root)
        been_here = False
        been_there = False
        for node in all_nodes:
            current_node = Symptom(self.root.symptom, self.root.severity)
            if been_here:
                current_node.right = past_node
            elif been_there:
                current_node.left = past_node
            been_here = False
            been_there = False
            if current_node.right is not None:
                if current_node.left is not None:
                    while current_node.right is not None or current_node.left is not None:
                        if node.severity < current_node.severity:
                            current_node = current_node.left
                        else:
                            current_node = current_node.right
            if node.severity > current_node.severity:
                current_node.right = node
                been_here = True
            else:
                current_node.left = node
                been_there = True
            
            past_node = node
        return current_node
        

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
    # in_order_traversal = tree.post_order_traversal()
    # correct_traversal = [cough, fever, red_eyes]
    # for i, el in enumerate(in_order_traversal):
    #     assert el == correct_traversal[i]
    # assert tree.root == red_eyes
    

    tree.tree_restructure(severity=2)
    in_order_traversal = tree.in_order_traversal()
    correct_traversal = [red_eyes, cough, fever]
    for i, el in enumerate(in_order_traversal):
        assert el == correct_traversal[i]
    assert tree.root == cough

