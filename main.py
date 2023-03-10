import pytholog as pl

def kings():
    kb = pl.KnowledgeBase("Kings")

    # Rules
    kb(
        [
        "king(john)",
        "person(richard)",
        "person(X) :- king(X)",
        "brother(john,richard)",
        "brother(richard,john)"
        ]
    )

    # Ask expression
    print(kb.query(pl.Expr("king(john)")))
    print(kb.query(pl.Expr("king(richard)")))
    print(kb.query(pl.Expr("brother(richard,X)")))

    

def animals():
    kb=pl.KnowledgeBase("Animals")

    kb([
        "dog(fido)",
        "wolf(razor)",
        "cat(clara)",
        "lion(simba)",
        "turtle(franklin)",
        "animal(X) :- mammal(X)",
        "mammal(X) :- feline(X)",
        "feline(X) :- cat(X)",
        "feline(X) :- lion(X)",
        "mammal(X) :- canine(X)",
        "canine(X) :- dog(X)",
        "caniine(X) :- wolf(X)",
        "animal(X) :- reptile(X)",
        "reptile(X) :- turtle(X)"
        ]
    )

    print(kb.query(pl.Expr("animal(franklin)")))
    print(kb.query(pl.Expr("canine(sparky)")))
    print(kb.query(pl.Expr("animal(X)")))
    print(kb.query(pl.Expr("mammal(X)")))

def kinship():
    # and = ",", or = ";"
    # if M is a female and M is a parenmt to C, then mother(Mother, Child)
    # if C is a child of P, then P is a parent of child
    # if G is parent to P and P is parent to C then G is grandparent to C

    kb = pl.KnowledgeBase("Kinship")

    kb([
        "parent(M)",
        "child(C)",
        "mother(M,C) :- female(M) , parent(M,C)",
        "parent(P,C) :- child(C,P)",
        "grandparent(G,C) :- parent(G,P) , parent (P,C)",
        "female(melanie)",
        "child(eden, melanie)",
        "child(eden,kenny)",
        "child(kenny,joan)",
    ])

    print(kb.query(pl.Expr("grandparent(joan,eden)")))

def main():
    print("hello.")
    #kinship()
    # kings()
    animals()

if __name__ == "__main__":
    main()