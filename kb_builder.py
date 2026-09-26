import json

kb = {
    "solver": {
        "Real Numbers": {"formula": "HCF(a,b) × LCM(a,b) = a × b", "note": "Valid for a,b > 0"},
        "Polynomials": {"formula": "sum of zeroes = −b/a, product = c/a", "note": "For ax²+bx+c"},
        "Trigonometry": {"formula": "sin²θ + cos²θ = 1", "note": "Valid for 0 ≤ θ ≤ 90°"},
        "AP": {"formula": "aₙ = a + (n−1)d", "note": "n must be positive integer"}
    },
    "misconceptions": [
        "Dividing by zero (undefined)", "sin²θ as sin(θ²)", "Ignoring negative roots in quadratics",
        "Confusing AP and GP", "Assuming ∠A = ∠P in △ABC ∼ △PQR", "Adding units incorrectly"
    ],
    "validity_guards": [
        "denominator ≠ 0", "discriminant ≥ 0", "triangle sides > 0", "distance ≥ 0",
        "sin θ ≤ 1", "cos θ ≤ 1", "n > 0 for terms", "sum of probabilities = 1"
    ]
}

with open("kb.json", "w") as f:
    json.dump(kb, f, indent=4)
