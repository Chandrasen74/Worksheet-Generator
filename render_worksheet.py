import json

with open("questions.json", "r") as f:
    questions = json.load(f)

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <style>
        @page { size: A4; margin: 2.9pt; }
        body { font-family: 'Times New Roman', serif; font-size: 12pt; line-height: 1.5; margin: 36pt; }
        .header { border-bottom: 0.5pt solid black; height: 50pt; }
        .logo { float: right; width: 155pt; }
        .question { margin-bottom: 18pt; page-break-inside: avoid; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo">
            <img src="logo_green_on_white.png" style="width:155pt">
        </div>
        <div>
            Name: _____________________________________<br>
            Class: X                  Section: A<br>
            Subject: MATHEMATICS                            Date: ____________
        </div>
    </div>
    <h2>PRACTICE WORKSHEET</h2>
"""
for q in questions:
    html_content += f'<div class="question">Q{q["id"]}. {q["question"]}</div>'

html_content += "</body></html>"

with open("worksheet.html", "w", encoding="utf-8") as f:
    f.write(html_content)
print("Worksheet rendered in worksheet.html")
