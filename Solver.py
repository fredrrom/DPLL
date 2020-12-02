import sys
import ast
import copy

def is_unit(clause):
    return len(clause) == 1

def unit_propagation(s):
    already_propagated = []
    i = 0
    while i < len(s):
        new_s = []
        clause = s[i]
        if is_unit(clause) and clause not in already_propagated:
            literal = clause[0]
            new_s.append(clause)
            already_propagated.append(clause)
            for other_clause in s:
                if -literal in other_clause:
                    other_clause.remove(-literal)
                if literal not in other_clause:
                    new_s.append(other_clause)
            s = copy.deepcopy(new_s)
            i = 0
        else:
            i += 1
    for clause in s:
        if not is_unit(clause):
            return None, copy.deepcopy(s)
    I = "Satisfying assignment: "
    for clause in s:
        I += str(clause[0]) + " "
    I += "(remaining variables can be whatever)"
    return I, []

def atomic_cut(s):
    for clause in s:
        if not is_unit(clause):
            atom = clause[0]
            left_branch = copy.deepcopy(s)
            right_branch = copy.deepcopy(s)
            left_branch.append([atom])
            right_branch.append([-atom])
            return [left_branch, right_branch]
    return [copy.deepcopy(s)]

def pure_literal_elimination(s):
    literals = set()
    for clause in s:
        for literal in clause:
            literals.add(literal)
    pure_literals = []
    for literal in literals:
        if -literal not in literals:
            pure_literals.append(literal)
    new_s = []
    for literal in pure_literals:
        for clause in s:
            if literal not in clause:
                new_s.append(clause)
        new_s.append([literal])
        s = new_s
    return s 

def prove(s):
    I, clauses = unit_propagation(s) 
    if [] in clauses:
        return "unsatisfiable"
    if clauses == []:
        return I
    else:
        #clauses = pure_literal_elimination(clauses)
        prems = atomic_cut(clauses)
        for p in prems:
            answer = prove(copy.deepcopy(p))
            if answer != "unsatisfiable":
                return answer
        # the proofs for all premisses were closed, so...
        return "unsatisfiable"

def generate_formula(n, formula, clause, i):
    if i == n: 
        formula.append(clause.copy())
        return
    clause[i] = i+1
    generate_formula(n, formula, clause, i + 1)    
    clause[i] = -(i+1)
    generate_formula(n, formula, clause, i + 1) 
    return formula

def main():
    if len(sys.argv) < 2:
        print("Invalid formula\nFormat: [[1,-2,3,...],[-1,2,3,...],...,[1,2,-3,...]]\nEmpty clause: []\nUse positive integers for variables and arithmetic negation for propositional negation")
        return
    print(prove(ast.literal_eval(sys.argv[1])))

if __name__ == '__main__':
    main()