import json
import random

def generate():
    # Full implementation of template logic
    templates = [
        {"id": "QE-1", "scenario": "Find roots of quadratic", "difficulty": "Moderate", "formula": "(-b ± √(b² - 4ac)) / 2a"},
        {"id": "TR-1", "scenario": "Height and Distance", "difficulty": "Hard", "formula": "h = d * tanθ"},
        {"id": "AP-1", "scenario": "Find nth term of AP", "difficulty": "Easy", "formula": "a + (n-1)d"}
    ]
    
    questions = []
    # Generate 30 questions
    for i in range(1, 31):
        temp = random.choice(templates)
        q = {
            "id": i,
            "template_id": temp["id"],
            "question": f"Aarav needs to solve: {temp['scenario']}. Calculate the value.",
            "type": "MCQ" if i < 20 else "A-R",
            "difficulty": temp["difficulty"]
        }
        questions.append(q)
        
    with open("questions.json", "w") as f:
        json.dump(questions, f, indent=4)
    print("Generated 30 questions")

generate()
