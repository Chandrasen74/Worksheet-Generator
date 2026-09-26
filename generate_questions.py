import json
import random

def generate():
    # Load knowledge base
    with open("knowledge_base.json", "r") as f:
        kb = json.load(f)
    
    questions = []
    # Simplified generation for demonstration
    for i in range(5):
        q = {
            "id": i+1,
            "topic": "Quadratic Equations",
            "question": f"Find roots of x² - {random.randint(1,5)}x + {random.randint(1,5)} = 0",
            "difficulty": "Moderate"
        }
        questions.append(q)
    
    with open("questions.json", "w") as f:
        json.dump(questions, f, indent=4)
    print("5 questions generated in questions.json")

generate()
