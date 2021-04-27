"""
(5 Marks)
We are attempting to initialize an instance of class H in the code below.
Class H inherits from classes F,G,A,B,C,D,E,. However the order in which class H
inherits its parents is incorrect and causes an inconsistent method resolution order error.

Re-order how class H inherits from its parents to successfully print out "Consistent MRO found!"
"""


# DO NOT TOUCH CODE BELOW FOR Class A,B,C,D,E,F,G
class A:
    pass


class B:
    pass


class C(A):
    pass


class D(A):
    pass


class E(A, B):
    pass


class F(C, D):
    pass


class G(D, E, B):
    pass


# DO NOT TOUCH CODE ABOVE FOR Class A,B,C,D,E,F,G

#TODO - Modify class H's inheritance order to achieve a consistent MRO with no 'TypeError: Cannot create a consistent method resolution':
# - class H MUST inherit from class F,G,A,B,C,D,E, but in a different order
# - First two parents of H MUST be F, G ie: H(F, G, the other classes)

class H(F, G, C, D, E, A, B):
    pass


h = H()
print("Consistent MRO found!")

# L(A) = ['A']

# L(B) = ['B']

# L(C) = ['C'] + merge(L(A))
# L(C) = ['C'] + ['A']
# L(C) = ['C', 'A']

# L(D) = ['D'] + merge(L(A))
# L(D) = ['D'] + ['A']
# L(D) = ['D', 'A']

# L(E) = ['E'] + merge(L(A),L(B))
# L(E) = ['E'] + [['A'], ['B'], ['A', 'B']]
# L(E) = ['E', 'A', 'B']

# L(F) = ['F'] + merge(L(C),L(D))
# L(F) = ['F'] + [['C', 'A'], ['D', 'A'], ['C', 'D']
# L(F) = ['F', 'C', 'D', 'A']

# L(G) = ['G'] + merge(L(D), L(E), L(B))
# L(G) = ['G'] + [['D', 'A'], ['E', 'A', 'B'], ['B'], ['D', 'E', 'B']]
# L(G) = ['G', 'D', 'E', 'A', 'B']

# L(H) = [H] + merge(L(F), L(G), L(A), L(B), L(C), L(D), L(E))
# L(H) = [H] + merge([F, C, D, A], [G, D, E, A, B], [A], [B], [C, A], [D, A], [E, A, B], [F, G, A, B, C, D, E])
# L(H) = [H, F, G]  + merge([C, D, A], [D, E, A, B], [A], [B], [C, A], [D, A], [E, A, B], [A, B, C, D, E])
# ERROR


