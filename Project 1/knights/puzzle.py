from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Information from structure of problem
    Not(And(AKnight, AKnave)),
    Or(AKnight, AKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    # Information from A
    Implication(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Information from structure of problem
    And(Or(BKnave, BKnight), Or(AKnave, AKnight)),
    Implication(AKnight, Not(AKnave)),
    Implication(BKnight, Not(BKnave)),
    # Information from A
    Biconditional(AKnight, And(AKnave, BKnave))  # If A is a Knight, then both A and B are Knaves
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Information from structure of problem
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Implication(AKnight, BKnight),
    Implication(BKnight, AKnave),
    # Information from A
    Biconditional(AKnight, Or(And(AKnight, BKnight),
                              And(AKnave, BKnave))),  # If A is a Knight, then both A and B are Knights OR Knaves
    # Information from B
    Biconditional(BKnight, Or(And(AKnave, BKnight),
                              And(AKnight, BKnave)))   # If B is a Knight, then A is a Knave and B is a Knight OR A is a Knight, B is a Knave
                )

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Information from structure of problem
    Or(AKnight, AKnave),                # A is either a knight or a knave
    Implication(AKnight, Not(AKnave)),  # A cannot be a knave if it is a knight
    Or(BKnight, BKnave),                # Similarly for B
    Implication(BKnight, Not(BKnave)),
    Or(CKnight, CKnave),                # Similarly for C
    Implication(CKnight, Not(CKnave)),

    # Information from A
    Biconditional(AKnight, Or(And(AKnight, AKnave), And(AKnight, AKnight))),  # If A is a Knight, A could be either a Knight or a Knave

    # Information from B
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
    Biconditional(BKnight, CKnave),  # If B is a Knight, then C is a Knave

    # Information from C
    Biconditional(CKnight, AKnight)  # If C is a Knight, then A is a Knight
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
