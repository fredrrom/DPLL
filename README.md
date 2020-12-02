# Davis–Putnam–Logemann–Loveland (DPLL) algorithm

#### A simple implementation of the resolution-based DPLL SAT solving algorithm in Python. 

### Syntax
Propositional formulae are provided in conjunctive normal form. Conversion from logical to program syntax is done as follows:

|  Logical | Program                  |
|----------|--------------------------|
| Literal  | Non-zero integer         |
| Negation | Arithmetic negation      |
| Clause   | List of integers         |
| Formula  | List of list of integers |

For example: 

<img src="https://i.upmath.me/svg/(A%20%5Clor%20B)%20%5Cland%20(%5Cneg%20B%20%5Clor%20A)" alt="(A \lor B) \land (\neg B \lor A)" /> 

can be written as:

```
[[1,2],[-2,1]]
```

### Usage

To find a satisfying assignment run:
```
python3 solver.py '[[1,2],[-2,1]]'
```
