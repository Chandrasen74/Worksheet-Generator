"""
PHASE 2: KNOWLEDGE BASE FOR CBSE CLASS 10 MATHEMATICS
Chapters: Real Numbers, Polynomials, Intro to Trigonometry, Probability,
          Pair of Linear Equations, Arithmetic Progression, Quadratic Equations,
          Coordinate Geometry, Applications of Trigonometry, Triangles
"""

import random
import math

# ============================================================================
# A. SOLVER CORE - Formula Table
# ============================================================================

SOLVER_CORE = {
    # Real Numbers
    "hcf_lcm": lambda a, b, hcf: (a * b) // hcf,
    "lcm_from_factors": lambda a, b: (a * b) // math.gcd(a, b),
    
    # Polynomials
    "sum_of_zeroes": lambda a, b, c: -b / a,  # α + β = -b/a
    "product_of_zeroes": lambda a, b, c: c / a,  # αβ = c/a
    "quadratic_from_roots": lambda alpha, beta: (1, -(alpha + beta), alpha * beta),
    
    # Quadratic Equations
    "discriminant": lambda a, b, c: b**2 - 4*a*c,
    "quadratic_roots": lambda a, b, c: (
        (-b + math.sqrt(b**2 - 4*a*c)) / (2*a),
        (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    ) if b**2 - 4*a*c >= 0 else None,
    
    # Arithmetic Progression
    "ap_nth_term": lambda a, n, d: a + (n - 1) * d,
    "ap_sum_n": lambda a, n, d: (n / 2) * (2*a + (n - 1) * d),
    "ap_sum_first_last": lambda n, first, last: (n / 2) * (first + last),
    
    # Coordinate Geometry
    "distance": lambda x1, y1, x2, y2: math.sqrt((x2 - x1)**2 + (y2 - y1)**2),
    "section_formula": lambda x1, y1, x2, y2, m, n: ((m*x2 + n*x1)/(m+n), (m*y2 + n*y1)/(m+n)),
    "midpoint": lambda x1, y1, x2, y2: ((x1 + x2)/2, (y1 + y2)/2),
    "area_triangle": lambda x1, y1, x2, y2, x3, y3: abs(0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))),
    
    # Trigonometry
    "sin": lambda theta_deg: math.sin(math.radians(theta_deg)),
    "cos": lambda theta_deg: math.cos(math.radians(theta_deg)),
    "tan": lambda theta_deg: math.tan(math.radians(theta_deg)),
    "cot": lambda theta_deg: 1 / math.tan(math.radians(theta_deg)),
    "sec": lambda theta_deg: 1 / math.cos(math.radians(theta_deg)),
    "cosec": lambda theta_deg: 1 / math.sin(math.radians(theta_deg)),
    
    # Heights and Distances
    "height_from_angle": lambda distance, angle_deg: distance * math.tan(math.radians(angle_deg)),
    "distance_from_height": lambda height, angle_deg: height / math.tan(math.radians(angle_deg)),
    
    # Triangles (Similarity)
    "similar_triangle_side": lambda a, b, c: (a / b) * c,  # If a:b then x:c
    "pythagoras": lambda a, b: math.sqrt(a**2 + b**2),
    
    # Probability
    "probability": lambda favorable, total: favorable / total,
}

# Standard Values (for exact computation)
TRIG_VALUES = {
    0: {"sin": 0, "cos": 1, "tan": 0},
    30: {"sin": 0.5, "cos": math.sqrt(3)/2, "tan": 1/math.sqrt(3)},
    45: {"sin": 1/math.sqrt(2), "cos": 1/math.sqrt(2), "tan": 1},
    60: {"sin": math.sqrt(3)/2, "cos": 0.5, "tan": math.sqrt(3)},
    90: {"sin": 1, "cos": 0, "tan": float('inf')},
}

# ============================================================================
# B. QUESTION TEMPLATES (50 templates across all chapters)
# ============================================================================

TEMPLATES = [
    # Real Numbers (5 templates)
    {
        "id": "RN01",
        "scenario": "HCF-LCM product relationship",
        "params": {"a": range(12, 48, 6), "b": range(18, 60, 6)},
        "difficulty": "Easy",
        "context_pool": ["numbers", "dimensions", "quantities"],
        "ask_rotation": ["Find LCM", "Find HCF", "Verify product"],
    },
    {
        "id": "RN02",
        "scenario": "Decimal expansion terminating/non-terminating",
        "params": {"p": range(1, 20), "q": [2, 4, 5, 8, 10, 16, 20, 25]},
        "difficulty": "Easy",
        "context_pool": ["fraction", "ratio"],
        "ask_rotation": ["Terminating?", "Decimal form"],
    },
    {
        "id": "RN03",
        "scenario": "Prime factorization application",
        "params": {"n": [60, 72, 84, 90, 108, 120, 144, 180]},
        "difficulty": "Easy",
        "context_pool": ["number", "code"],
        "ask_rotation": ["Prime factors", "Smallest divisor"],
    },
    {
        "id": "RN04",
        "scenario": "LCM of three numbers",
        "params": {"a": range(6, 20, 2), "b": range(8, 24, 2), "c": range(10, 30, 2)},
        "difficulty": "Moderate",
        "context_pool": ["bells", "traffic lights", "events"],
        "ask_rotation": ["Find LCM", "Next simultaneous occurrence"],
    },
    {
        "id": "RN05",
        "scenario": "Irrational proof by contradiction",
        "params": {"number": ["√2", "√3", "√5"]},
        "difficulty": "Hard",
        "context_pool": ["proof"],
        "ask_rotation": ["Prove irrational"],
    },
    
    # Polynomials (5 templates)
    {
        "id": "PO01",
        "scenario": "Sum and product of zeroes",
        "params": {"a": range(1, 5), "b": range(-10, 10), "c": range(-10, 10)},
        "difficulty": "Easy",
        "context_pool": ["polynomial", "equation"],
        "ask_rotation": ["Find sum of zeroes", "Find product of zeroes"],
    },
    {
        "id": "PO02",
        "scenario": "Form quadratic from given zeroes",
        "params": {"alpha": range(-5, 6), "beta": range(-5, 6)},
        "difficulty": "Easy",
        "context_pool": ["roots", "zeroes"],
        "ask_rotation": ["Form polynomial", "Write equation"],
    },
    {
        "id": "PO03",
        "scenario": "Find k if one zero is given",
        "params": {"a": range(1, 5), "b": range(-8, 8), "zero": range(-3, 4)},
        "difficulty": "Moderate",
        "context_pool": ["polynomial"],
        "ask_rotation": ["Find k", "Find constant term"],
    },
    {
        "id": "PO04",
        "scenario": "Relationship between zeroes",
        "params": {"relation": ["twice", "reciprocal", "negative"]},
        "difficulty": "Moderate",
        "context_pool": ["equation"],
        "ask_rotation": ["Find zeroes", "Form equation"],
    },
    {
        "id": "PO05",
        "scenario": "Cubic polynomial properties",
        "params": {"a": range(1, 4), "zeroes": [(-1, 2, 3), (1, -2, 4), (2, 3, -1)]},
        "difficulty": "Hard",
        "context_pool": ["cubic"],
        "ask_rotation": ["Sum of zeroes", "Product of zeroes taken two at a time"],
    },
    
    # Linear Equations (5 templates)
    {
        "id": "LE01",
        "scenario": "Elimination method",
        "params": {"a1": range(1, 6), "b1": range(1, 6), "a2": range(1, 6), "b2": range(1, 6)},
        "difficulty": "Easy",
        "context_pool": ["cost problems", "age problems", "number problems"],
        "ask_rotation": ["Find x and y", "Solve the system"],
    },
    {
        "id": "LE02",
        "scenario": "Substitution method word problem",
        "params": {"total": range(20, 100, 10), "diff": range(5, 25, 5)},
        "difficulty": "Easy",
        "context_pool": ["tickets", "coins", "students"],
        "ask_rotation": ["Find quantities", "Determine numbers"],
    },
    {
        "id": "LE03",
        "scenario": "Fraction-digit problem",
        "params": {"units": range(1, 9), "tens": range(1, 9)},
        "difficulty": "Moderate",
        "context_pool": ["two-digit number"],
        "ask_rotation": ["Find original number", "Find reversed number"],
    },
    {
        "id": "LE04",
        "scenario": "Speed-distance-time problem",
        "params": {"speed1": range(20, 60, 5), "speed2": range(20, 60, 5), "time": range(2, 6)},
        "difficulty": "Moderate",
        "context_pool": ["boat", "train", "car"],
        "ask_rotation": ["Find speeds", "Find distance"],
    },
    {
        "id": "LE05",
        "scenario": "Mixture and alligation",
        "params": {"qty1": range(10, 50, 5), "qty2": range(10, 50, 5), "price1": range(20, 100, 10)},
        "difficulty": "Hard",
        "context_pool": ["milk-water", "tea varieties", "rice"],
        "ask_rotation": ["Find mixture price", "Find quantities"],
    },
    
    # Quadratic Equations (5 templates)
    {
        "id": "QE01",
        "scenario": "Nature of roots from discriminant",
        "params": {"a": range(1, 5), "b": range(-10, 10), "c": range(-10, 10)},
        "difficulty": "Easy",
        "context_pool": ["equation"],
        "ask_rotation": ["Nature of roots", "Real or imaginary"],
    },
    {
        "id": "QE02",
        "scenario": "Solve by factorization",
        "params": {"product": [6, 12, 15, 18, 20, 24], "sum": range(-10, 10)},
        "difficulty": "Easy",
        "context_pool": ["equation"],
        "ask_rotation": ["Find roots", "Solve"],
    },
    {
        "id": "QE03",
        "scenario": "Solve by quadratic formula",
        "params": {"a": range(1, 5), "b": range(-12, 12), "c": range(-10, 10)},
        "difficulty": "Moderate",
        "context_pool": ["equation"],
        "ask_rotation": ["Find roots using formula"],
    },
    {
        "id": "QE04",
        "scenario": "Word problem - area",
        "params": {"length": range(10, 30, 2), "breadth": range(5, 20, 2), "border": range(1, 5)},
        "difficulty": "Moderate",
        "context_pool": ["garden", "field", "plot"],
        "ask_rotation": ["Find dimensions", "Find border width"],
    },
    {
        "id": "QE05",
        "scenario": "Relation between roots",
        "params": {"sum": range(-10, 10), "product": range(-20, 20)},
        "difficulty": "Hard",
        "context_pool": ["roots"],
        "ask_rotation": ["Form equation", "Find k"],
    },
    
    # Arithmetic Progression (5 templates)
    {
        "id": "AP01",
        "scenario": "Find nth term",
        "params": {"a": range(2, 20, 2), "d": range(2, 10), "n": range(5, 25)},
        "difficulty": "Easy",
        "context_pool": ["sequence", "series"],
        "ask_rotation": ["Find 10th term", "Find nth term"],
    },
    {
        "id": "AP02",
        "scenario": "Find sum of n terms",
        "params": {"a": range(1, 15), "d": range(1, 8), "n": range(10, 30)},
        "difficulty": "Easy",
        "context_pool": ["series"],
        "ask_rotation": ["Find sum", "Calculate S_n"],
    },
    {
        "id": "AP03",
        "scenario": "Find number of terms",
        "params": {"a": range(5, 20), "d": range(2, 8), "last": range(50, 150)},
        "difficulty": "Moderate",
        "context_pool": ["sequence"],
        "ask_rotation": ["How many terms", "Find n"],
    },
    {
        "id": "AP04",
        "scenario": "Three terms in AP",
        "params": {"a": range(5, 30), "b": range(10, 50), "c": range(15, 70)},
        "difficulty": "Moderate",
        "context_pool": ["terms"],
        "ask_rotation": ["Verify AP", "Find common difference"],
    },
    {
        "id": "AP05",
        "scenario": "Sum of first and last n terms equal",
        "params": {"total_terms": range(20, 40), "k": range(3, 10)},
        "difficulty": "Hard",
        "context_pool": ["series"],
        "ask_rotation": ["Find middle term", "Find sum property"],
    },
    
    # Coordinate Geometry (5 templates)
    {
        "id": "CG01",
        "scenario": "Distance between two points",
        "params": {"x1": range(-10, 10), "y1": range(-10, 10), "x2": range(-10, 10), "y2": range(-10, 10)},
        "difficulty": "Easy",
        "context_pool": ["points", "coordinates"],
        "ask_rotation": ["Find distance", "Calculate length"],
    },
    {
        "id": "CG02",
        "scenario": "Midpoint of line segment",
        "params": {"x1": range(-8, 8), "y1": range(-8, 8), "x2": range(-8, 8), "y2": range(-8, 8)},
        "difficulty": "Easy",
        "context_pool": ["line segment"],
        "ask_rotation": ["Find midpoint", "Find coordinates"],
    },
    {
        "id": "CG03",
        "scenario": "Section formula internal division",
        "params": {"x1": range(-6, 6), "y1": range(-6, 6), "x2": range(-6, 6), "y2": range(-6, 6), "m": range(1, 5), "n": range(1, 5)},
        "difficulty": "Moderate",
        "context_pool": ["division", "ratio"],
        "ask_rotation": ["Find point dividing in ratio", "Internal division"],
    },
    {
        "id": "CG04",
        "scenario": "Collinearity of three points",
        "params": {"points": [((1, 2), (3, 4), (5, 6)), ((0, 0), (2, 3), (4, 6)), ((-1, -1), (0, 0), (1, 1))]},
        "difficulty": "Moderate",
        "context_pool": ["triangle", "points"],
        "ask_rotation": ["Check collinear", "Find area"],
    },
    {
        "id": "CG05",
        "scenario": "Find third vertex of triangle",
        "params": {"x1": range(-5, 5), "y1": range(-5, 5), "x2": range(-5, 5), "y2": range(-5, 5), "area": range(5, 30)},
        "difficulty": "Hard",
        "context_pool": ["triangle"],
        "ask_rotation": ["Find third vertex", "Determine coordinates"],
    },
    
    # Trigonometry (5 templates)
    {
        "id": "TR01",
        "scenario": "Evaluate standard angles",
        "params": {"angle": [0, 30, 45, 60, 90], "ratio": ["sin", "cos", "tan"]},
        "difficulty": "Easy",
        "context_pool": ["angle", "ratio"],
        "ask_rotation": ["Find value", "Evaluate"],
    },
    {
        "id": "TR02",
        "scenario": "Trigonometric identity verification",
        "params": {"identity": ["sin²θ + cos²θ = 1", "1 + tan²θ = sec²θ", "1 + cot²θ = cosec²θ"]},
        "difficulty": "Easy",
        "context_pool": ["identity"],
        "ask_rotation": ["Verify", "Prove"],
    },
    {
        "id": "TR03",
        "scenario": "Find other ratios given one",
        "params": {"given_ratio": ["sin", "cos", "tan"], "value_num": range(3, 13), "value_den": range(4, 14)},
        "difficulty": "Moderate",
        "context_pool": ["right triangle"],
        "ask_rotation": ["Find cos θ", "Find tan θ", "Find sec θ"],
    },
    {
        "id": "TR04",
        "scenario": "Simplify trigonometric expression",
        "params": {"expr": ["sin θ cos θ + sin θ", "tan θ + cot θ", "sec²θ - tan²θ"]},
        "difficulty": "Moderate",
        "context_pool": ["expression"],
        "ask_rotation": ["Simplify", "Evaluate"],
    },
    {
        "id": "TR05",
        "scenario": "Prove trigonometric equation",
        "params": {"equation": ["(sin θ + cos θ)² = 1 + 2 sin θ cos θ", "tan θ / (1 - cot θ) + cot θ / (1 - tan θ) = 1 + sec θ cosec θ"]},
        "difficulty": "HOTS",
        "context_pool": ["proof"],
        "ask_rotation": ["Prove", "Establish"],
    },
    
    # Applications of Trigonometry (5 templates)
    {
        "id": "AT01",
        "scenario": "Height of tower from angle of elevation",
        "params": {"distance": range(10, 100, 10), "angle": [30, 45, 60]},
        "difficulty": "Easy",
        "context_pool": ["tower", "building", "tree", "pole"],
        "ask_rotation": ["Find height", "Calculate height"],
    },
    {
        "id": "AT02",
        "scenario": "Distance from angle of depression",
        "params": {"height": range(20, 100, 10), "angle": [30, 45, 60]},
        "difficulty": "Easy",
        "context_pool": ["cliff", "lighthouse", "airplane"],
        "ask_rotation": ["Find distance", "Calculate distance"],
    },
    {
        "id": "AT03",
        "scenario": "Two angles of elevation from same point",
        "params": {"distance": range(20, 80, 10), "angle1": [30, 45], "angle2": [45, 60]},
        "difficulty": "Moderate",
        "context_pool": ["buildings", "towers"],
        "ask_rotation": ["Find heights", "Find difference in heights"],
    },
    {
        "id": "AT04",
        "scenario": "Change in angle on moving towards object",
        "params": {"height": range(20, 80, 10), "angle1": [30], "angle2": [60]},
        "difficulty": "Moderate",
        "context_pool": ["tower", "tree", "monument"],
        "ask_rotation": ["Find distance moved", "Find initial distance"],
    },
    {
        "id": "AT05",
        "scenario": "Angle of elevation from two points in same line",
        "params": {"height": range(30, 90, 10), "dist1": range(20, 60, 10), "dist2": range(40, 100, 10)},
        "difficulty": "Hard",
        "context_pool": ["tower", "statue"],
        "ask_rotation": ["Find angles", "Verify height"],
    },
    
    # Triangles (5 templates)
    {
        "id": "TG01",
        "scenario": "Basic proportionality theorem",
        "params": {"AB": range(6, 20, 2), "AC": range(8, 24, 2), "ratio_m": range(1, 4), "ratio_n": range(1, 4)},
        "difficulty": "Easy",
        "context_pool": ["triangle"],
        "ask_rotation": ["Find DE", "Verify parallel"],
    },
    {
        "id": "TG02",
        "scenario": "Similar triangles - corresponding sides",
        "params": {"side1": range(6, 18, 2), "side2": range(9, 27, 3), "side3": range(4, 12)},
        "difficulty": "Easy",
        "context_pool": ["triangles"],
        "ask_rotation": ["Find unknown side", "Find ratio"],
    },
    {
        "id": "TG03",
        "scenario": "Pythagoras theorem application",
        "params": {"base": range(6, 16, 2), "height": range(8, 20, 2)},
        "difficulty": "Easy",
        "context_pool": ["right triangle"],
        "ask_rotation": ["Find hypotenuse", "Find third side"],
    },
    {
        "id": "TG04",
        "scenario": "AAA similarity criterion",
        "params": {"angle1": range(30, 70, 10), "angle2": range(40, 80, 10)},
        "difficulty": "Moderate",
        "context_pool": ["triangles"],
        "ask_rotation": ["Prove similar", "Find third angle"],
    },
    {
        "id": "TG05",
        "scenario": "Converse of Pythagoras theorem",
        "params": {"a": range(3, 12), "b": range(4, 16), "c": range(5, 20)},
        "difficulty": "Moderate",
        "context_pool": ["triangle"],
        "ask_rotation": ["Check right triangle", "Verify Pythagoras"],
    },
    
    # Probability (5 templates)
    {
        "id": "PR01",
        "scenario": "Single die probability",
        "params": {"outcome": ["even", "odd", "prime", "composite", "greater than 4"]},
        "difficulty": "Easy",
        "context_pool": ["die", "dice"],
        "ask_rotation": ["Find probability"],
    },
    {
        "id": "PR02",
        "scenario": "Card probability - single draw",
        "params": {"card_type": ["red", "black", "king", "queen", "ace", "spade", "heart"]},
        "difficulty": "Easy",
        "context_pool": ["deck of cards"],
        "ask_rotation": ["Find probability", "Calculate P(E)"],
    },
    {
        "id": "PR03",
        "scenario": "Bag with colored balls",
        "params": {"red": range(2, 8), "blue": range(3, 9), "green": range(1, 6)},
        "difficulty": "Moderate",
        "context_pool": ["bag", "box"],
        "ask_rotation": ["Find P(red)", "Find P(not blue)"],
    },
    {
        "id": "PR04",
        "scenario": "Two coins tossed",
        "params": {"outcome": ["both heads", "at least one head", "exactly one tail"]},
        "difficulty": "Moderate",
        "context_pool": ["coins"],
        "ask_rotation": ["Find probability"],
    },
    {
        "id": "PR05",
        "scenario": "Conditional probability - without replacement",
        "params": {"total": range(10, 20), "defective": range(2, 6)},
        "difficulty": "Hard",
        "context_pool": ["bulbs", "pens", "items"],
        "ask_rotation": ["Find P(both defective)", "Find P(at least one good)"],
    },
]

# ============================================================================
# C. MISCONCEPTION BANK (20 entries)
# ============================================================================

MISCONCEPTIONS = [
    {"error": "sin²θ + cos²θ = 2", "why": "Confuses Pythagorean identity", "distractor_rule": "Use 2 instead of 1"},
    {"error": "tan θ = sin θ / cos θ → always 1", "why": "Cancels incorrectly", "distractor_rule": "Answer 1"},
    {"error": "√(a² + b²) = a + b", "why": "Distributes square root", "distractor_rule": "Sum instead of Pythagoras"},
    {"error": "Distance is always positive, so drop absolute value in coordinate formula", "why": "Forgets squared differences are already positive", "distractor_rule": "Negative distance"},
    {"error": "(a + b)² = a² + b²", "why": "Forgets middle term", "distractor_rule": "Missing 2ab"},
    {"error": "In AP, a_n = a + nd", "why": "Forgets (n-1)", "distractor_rule": "Add d*n instead of d*(n-1)"},
    {"error": "Discriminant < 0 means no roots", "why": "Thinks complex roots don't exist", "distractor_rule": "State 'no solution'"},
    {"error": "HCF × LCM = a + b", "why": "Confuses product with sum", "distractor_rule": "Sum instead of product"},
    {"error": "Probability > 1 is possible", "why": "Misunderstands favorable/total", "distractor_rule": "P > 1"},
    {"error": "Sum of zeroes = b/a (forgets negative)", "why": "Drops sign", "distractor_rule": "Positive when should be negative"},
    {"error": "Midpoint formula uses subtraction", "why": "Confuses with distance", "distractor_rule": "Subtract coordinates"},
    {"error": "Angle of elevation = 90° - angle of depression", "why": "Confuses complementary angles", "distractor_rule": "Wrong angle relationship"},
    {"error": "In similar triangles, sides add instead of multiply", "why": "Confuses ratio", "distractor_rule": "Use sum"},
    {"error": "Area of triangle can be negative", "why": "Forgets absolute value", "distractor_rule": "Negative area"},
    {"error": "sec θ = 1/sin θ", "why": "Confuses reciprocal identities", "distractor_rule": "Wrong reciprocal"},
    {"error": "Common difference d must be positive", "why": "Forgets decreasing sequences", "distractor_rule": "Reject negative d"},
    {"error": "Roots of quadratic must be rational", "why": "Forgets surds", "distractor_rule": "Force rational answer"},
    {"error": "LCM < both numbers", "why": "Confuses HCF and LCM", "distractor_rule": "Smaller value"},
    {"error": "Two digit number: 10a + b becomes 10b + a when reversed (but forgets value changes)", "why": "Mechanical reversal without understanding", "distractor_rule": "Same value"},
    {"error": "Probability of sure event = 0", "why": "Confuses impossible and sure", "distractor_rule": "P(sure) = 0"},
]

# ============================================================================
# D. VALIDITY GUARDS (15 guards)
# ============================================================================

VALIDITY_GUARDS = [
    "Distance ≥ 0",
    "Discriminant check for real roots",
    "Denominators ≠ 0",
    "Trigonometric ratios: |sin θ|, |cos θ| ≤ 1",
    "Angle measures: 0° ≤ θ ≤ 90° for standard problems",
    "Probability: 0 ≤ P(E) ≤ 1",
    "Triangle inequality: sum of two sides > third side",
    "In AP, n ≥ 1 and integer",
    "Heights must be positive in application problems",
    "Observer height < object height for angle of elevation",
    "Area ≥ 0 (take absolute value)",
    "LCM ≥ max(a, b)",
    "HCF ≤ min(a, b)",
    "Quadratic coefficients: a ≠ 0",
    "Square roots: argument ≥ 0 for real numbers",
]

# ============================================================================
# E. DIFFICULTY CALIBRATION
# ============================================================================

DIFFICULTY_TIERS = {
    "Easy": "1-2 steps, direct formula application, recall",
    "Moderate": "3-4 steps, multi-concept, requires reasoning",
    "Hard": "5+ steps, multiple concepts, non-obvious path",
    "HOTS": "Proof, generalization, or non-routine problem",
}

print("Knowledge base constructed successfully.")
print(f"Solver functions: {len(SOLVER_CORE)}")
print(f"Question templates: {len(TEMPLATES)}")
print(f"Misconceptions: {len(MISCONCEPTIONS)}")
print(f"Validity guards: {len(VALIDITY_GUARDS)}")
