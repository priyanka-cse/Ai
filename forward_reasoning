global facts
global is_changed

is_changed = True
facts = [["vertebrate","duck"],["flying","duck"],["mammal","cat"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "mammal":
            assert_fact(["vertebrate",A1[1]])
        if A1[0] == "vertebrate":
            assert_fact(["animal",A1[1]])
        if A1[0] == "vertebrate" and ["flying",A1[1]] in facts:
            assert_fact(["bird",A1[1]])

print(facts)

"""
mammal(A) ==> vertebrate(A).
vertebrate(A) ==> animal(A).
vertebrate(A),flying(A) ==> bird(A).
vertebrate("duck").
flying("duck").
mammal("cat")."""


""" output
[['vertebrate', 'duck'], ['flying', 'duck'], ['mammal', 'cat'], ['animal', 'duck'], ['bird', 'duck'], ['vertebrate', 'cat'], ['animal', 'cat']]"""
