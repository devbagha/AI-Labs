class Node:
    def __init__(self, coeff, exponent, nexts=None):
        self.coeff = coeff
        self.exponent = exponent
        self.next = nexts

class Polynomial:
    def __init__(self, terms=None):
        self.terms = terms
        self.head = None
        self.degree = None

    def insert(self, coeff, exp):
        if self.head is None:
            self.head = Node(coeff, exp)
            self.degree = exp
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(coeff, exp)

    def add(self, pol2):
        new = Polynomial()
        itr = self.head
        itr2 = pol2.head

        while itr or itr2:
            if itr and itr2 and itr.exponent == itr2.exponent:
                new.insert(itr.coeff + itr2.coeff, itr.exponent)
                itr = itr.next
                itr2 = itr2.next
            elif itr and (not itr2 or itr.exponent > itr2.exponent):
                new.insert(itr.coeff, itr.exponent)
                itr = itr.next
            elif itr2 and (not itr or itr2.exponent > itr.exponent):
                new.insert(itr2.coeff, itr2.exponent)
                itr2 = itr2.next

        new.traverse()
    def sub(self,pol2):
        new = Polynomial()
        itr = self.head
        itr2 = pol2.head

        while itr or itr2:
            if itr and itr2 and itr.exponent == itr2.exponent:
                new.insert(itr.coeff - itr2.coeff, itr.exponent)
                itr = itr.next
                itr2 = itr2.next
            elif itr and (not itr2 or itr.exponent > itr2.exponent):
                new.insert(itr.coeff, itr.exponent)
                itr = itr.next
            elif itr2 and (not itr or itr2.exponent > itr.exponent):
                new.insert(itr2.coeff, itr2.exponent)
                itr2 = itr2.next

        new.traverse()
    
    def traverse(self):
        itr = self.head
        while itr:
            print(str(itr.coeff) + "x^" + str(itr.exponent), end=" ")
            itr = itr.next


poly1 = Polynomial()
poly1.insert(3, 2)
poly1.insert(5, 1)
poly1.insert(2, 0)
poly1.traverse()
poly2 = Polynomial()
poly2.insert(4, 3)
poly2.insert(6, 1)
poly2.insert(1, 0)
poly2.traverse()
poly1.add(poly2)
poly1.sub(poly2)
