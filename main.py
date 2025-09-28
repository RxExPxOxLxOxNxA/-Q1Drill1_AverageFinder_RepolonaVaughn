from pyscript import display, document

def compute(event):
    s1 = float(document.getElementById("score1").value or 0)
    s2 = float(document.getElementById("score2").value or 0)
    avg = (s1 + s2) / 2

    if avg >= 75:
        display(f"Average: {avg} ✅ Passed", target="result")
    else:
        display(f"Average: {avg} ❌ Failed", target="result")