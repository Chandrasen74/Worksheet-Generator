import json

knowledge_base = {
    "solver_core": {
        "Real Numbers": {"formula": "HCF(a,b) * LCM(a,b) = a * b", "note": "Only for two numbers"},
        "Polynomials": {"formula": "sum of zeroes = -b/a, product of zeroes = c/a", "note": "For ax^2+bx+c"},
        "Quadratic Equations": {"formula": "x = (-b ± √(b^2 - 4ac)) / 2a", "note": "Valid if b^2 - 4ac ≥ 0"}
    },
    "misconceptions": [
        {"error": "Dividing by zero", "correction": "undefined"},
        {"error": "Confusing AP and GP", "correction": "AP uses common difference"},
        {"error": "Ignoring negative roots in quadratics", "correction": "check discriminant"}
    ],
    "validity_guards": [
        "denominator != 0",
        "discriminant >= 0 for real roots",
        "triangle sides > 0"
    ]
}

with open("knowledge_base.json", "w") as f:
    json.dump(knowledge_base, f, indent=4)
print("Knowledge base built in knowledge_base.json")
