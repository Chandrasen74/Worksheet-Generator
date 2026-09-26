import json
import base64

with open("questions.json", "r") as f:
    questions = json.load(f)

# Embed logo as base64
with open("logo_green_on_white.png", "rb") as logo_file:
    logo_b64 = base64.b64encode(logo_file.read()).decode()

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <style>
        @page {{ size: A4; margin: 8.5mm; }}
        @media print {{ body {{ print-color-adjust: exact; -webkit-print-color-adjust: exact; }} }}
        body {{ 
            font-family: 'Times New Roman', serif; 
            font-size: 12pt; 
            line-height: 1.5; 
            margin: 0; 
            padding: 0;
        }}
        .page-border {{
            border: 2.9pt solid #003300;
            outline: 0.7pt solid #003300;
            outline-offset: 0.7pt;
            margin: 8.5mm;
            padding: 20pt;
            min-height: calc(297mm - 17mm - 40pt);
        }}
        .header {{ 
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 20pt;
            border-bottom: 0.5pt solid #000;
            padding-bottom: 10pt;
            margin-bottom: 20pt;
        }}
        .header-left {{ font-size: 12pt; line-height: 24pt; }}
        .logo {{ width: 155pt; height: 50pt; object-fit: contain; }}
        .section-header {{ 
            text-transform: uppercase; 
            font-weight: normal; 
            margin: 26pt 0 18pt 0; 
            font-size: 12pt;
        }}
        .question {{ 
            margin-bottom: 18pt; 
            page-break-inside: avoid; 
        }}
        .mcq-options {{ 
            display: grid; 
            grid-template-columns: 262.9pt 1fr; 
            margin-top: 8pt;
            row-gap: 8pt;
        }}
        .ar-direction {{
            margin-bottom: 18pt;
            line-height: 1.5;
        }}
        .footer {{
            position: fixed;
            bottom: 15mm;
            right: 15mm;
            font-size: 11pt;
        }}
    </style>
</head>
<body>
<div class="page-border">
    <div class="header">
        <div class="header-left">
            Name:  _____________________________________<br>
            Class: X                   Section: A<br>
            Subject: MATHEMATICS                          Date: ____________<br>
            Chapter/Topic: MULTIPLE CHAPTERS
        </div>
        <img src="data:image/png;base64,{logo_b64}" class="logo" alt="DPS Logo">
    </div>
    
    <div class="section-header">SECTION A — MULTIPLE CHOICE QUESTIONS</div>
"""

mcq_questions = [q for q in questions if q["type"] == "MCQ"]
ar_questions = [q for q in questions if q["type"] == "A-R"]

for q in mcq_questions:
    html_content += f'''    <div class="question">
        <strong>Q{q["id"]}.</strong> {q["question"]}
        <div class="mcq-options">
            <div>(a) Option A</div><div>(b) Option B</div>
            <div>(c) Option C</div><div>(d) Option D</div>
        </div>
    </div>
'''

if ar_questions:
    html_content += '''
    <div class="section-header">SECTION B — ASSERTION-REASON QUESTIONS</div>
    <div class="ar-direction">
        <strong>Direction:</strong> In the following questions, a statement of assertion (A) is followed by a statement of reason (R). Mark the correct choice as:<br>
        (a) Both assertion (A) and reason (R) are true and reason (R) is the correct explanation of assertion (A).<br>
        (b) Both assertion (A) and reason (R) are true but reason (R) is not the correct explanation of assertion (A).<br>
        (c) Assertion (A) is true but reason (R) is false.<br>
        (d) Assertion (A) is false but reason (R) is true.
    </div>
'''
    for q in ar_questions:
        html_content += f'''    <div class="question">
        <strong>Q{q["id"]}.</strong><br>
        <strong>Assertion (A):</strong> Sample assertion statement.<br>
        <strong>Reason (R):</strong> Sample reason statement.
    </div>
'''

html_content += '''    <div class="footer">Page <strong>1</strong> of 1</div>
</div>
</body>
</html>'''

with open("worksheet.html", "w", encoding="utf-8") as f:
    f.write(html_content)
print("Worksheet rendered in worksheet.html")
