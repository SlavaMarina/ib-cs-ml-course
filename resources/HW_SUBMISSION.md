# 📤 Homework Submission Guide — for students

> **Read this FIRST** before your first homework. It will save you hours.

---

## 📋 TL;DR — the key rules

1. ✅ **Make your own copy** of the notebook (Drive or Fork)
2. ✅ **Run all cells** before submitting (`Runtime → Run all`)
3. ✅ **Declare any AI use** (see section below)
4. ✅ **Submit before the deadline** (late = -10%/day; after 7 days = Missing)
5. ✅ **Use the checklist** at the end of this document before every submission

---

## 🎯 What your teacher is looking for

Every homework is graded along **three axes**:

| Axis | Criterion | Weight |
|---|---|---|
| **Correctness** | correct answers / working code | ~60% |
| **IB style** | correct command terms, structure, terminology | ~25% |
| **Effort** | filled-in cells, attempts at hard tasks, reflections | ~15% |

> 💎 **Low-hanging fruit:** fill in EVERY block. An empty block = 0 marks; any attempt = partial credit.

---

## 🟢 Submitting via Google Classroom

### One-time setup
1. Get the repository link from your teacher
2. Open the assignment in Google Classroom

### For each homework:
1. **Open the notebook in Colab** via the homework attachment in Classroom
2. **Save a copy immediately:**
   ```
   File → Save a copy in Drive
   ```
   > ⚠️ **WITHOUT THIS, YOUR PROGRESS IS NOT SAVED!** This is the most common mistake.
3. **Rename your copy:** `[YourSurname]_[NotebookName].ipynb`
4. **Work in your copy.** Fill in:
   - 🟠 Cells marked `# === YOUR CODE ===`
   - 🔵 Markdown blocks with questions (write answers right under the question)
5. **When done:** `Runtime → Run all` — make sure every cell runs without errors
6. **Download:** `File → Download → .ipynb`
7. **Upload** to Google Classroom as your assignment response
8. **Click "Hand in"**

---

## 🤖 AI Usage Policy

### ✅ ALLOWED

| What | Example |
|---|---|
| Asking AI about concepts | "Explain gradient descent with a simple example" |
| Debugging your own code | "Why does this code raise an IndexError?" + code |
| Explanation **after** your own attempt | "I tried X, got Y. Where's the mistake?" |
| Translation / grammar fixes in your answers | for non-native English speakers |

### ❌ NOT ALLOWED (plagiarism)

| What | Why |
|---|---|
| Asking AI to **write the whole homework** | this is academic dishonesty |
| Copying AI answers without understanding | IB plagiarism policy |
| Using AI during **exams or mocks** | strictly forbidden |
| Not declaring AI use | -20% penalty |

### Required AI Usage Declaration

Add this markdown cell at the **END of EVERY** submitted homework:

```markdown
## 🤖 AI Usage Declaration

- [ ] I did not use any AI assistants
- [x] I used AI for code debugging (cells X, Y)
- [ ] I used AI to explain a concept **after** my own attempt

**AI tools used:** ChatGPT 4 / Claude / Copilot / other: ____

**What exactly I asked:**
- "Why does my code return NaN?" — for cell 12
- "Explain KNN more simply" — to understand the theory
```

> ⚠️ **No declaration = automatic -20% penalty**, even if you didn't use AI.
> A declaration with "did not use" ticked is mandatory.

---

## ⏰ Deadlines and late penalties

| Lateness | Penalty |
|---|---|
| < 24 hours | **-10%** of the final grade |
| 1-2 days | **-25%** |
| 3-7 days | **-50%** |
| > 7 days | **0%** (Missing) |

### Valid reasons (no penalty)
- Illness with a medical note
- School infrastructure failures
- Family circumstances (notify the teacher IN ADVANCE)

### Invalid reasons
- "Forgot" / "ran out of time"
- "Home Wi-Fi was down" (use a mobile hotspot)
- "Didn't understand the task" (ask IN ADVANCE, not after the deadline)

---

## 🎨 Format & Style — what your teacher values

### Well-formatted answer

```markdown
**Q3 (a):** Calculate Precision.

**Answer:**

Precision = TP / (TP + FP)
         = 80 / (80 + 10)
         = 80 / 90
         = 0.889 (or 88.9%)

This means that out of all predictions classified as positive,
88.9% were actually correct.
```

✅ Formula, values, calculation, **interpretation**.

### Poorly-formatted answer

```
0.889
```

❌ Just a number. No formula, no interpretation — 0-1 marks out of 3.

---

## ✅ Pre-Submission Checklist

> Save or print this. Check it **before every submission**.

### Technical
- [ ] File renamed: `[Surname]_[name].ipynb`
- [ ] `Runtime → Run all` completed **without errors**
- [ ] All charts / visualizations **display**
- [ ] No `# TODO` or unfilled `[Your answer]` left
- [ ] File saved locally (`.ipynb` downloaded)

### Content
- [ ] **ALL** question cells filled in (even if unsure)
- [ ] **IB command terms** used correctly (Discuss = argument + counter + conclusion)
- [ ] Calculations shown with **formula + values + result**
- [ ] In ethics — **specific case studies** mentioned (COMPAS, Amazon AI, etc.)
- [ ] In extended responses — a **conclusion** added

### Ethics
- [ ] **AI Usage Declaration** added at the end
- [ ] All sources cited (if used)
- [ ] The work is **yours**, not a copy of a classmate's

---

## 🔄 What to do if...

### "I accidentally deleted my copy"
- Check Google Drive → Trash (kept for 30 days)
- In Colab: `File → Revision history` — auto-saves exist

### "My code crashed and I can't figure it out"
1. Read the error message **to the end** (the answer is often in the last line)
2. Google the exact error message
3. Ask AI with **full context** (code + error)
4. Ask your teacher in Classroom comments

### "I don't understand the task"
- Read it **again** slowly
- Check the hints (💎 **TIP** blocks in the notebook)
- Ask your teacher **IN ADVANCE**, not an hour before the deadline

### "I submitted but then found a mistake"
- Upload the corrected version (Classroom accepts the latest)
- Do it before the deadline!

---

## 🎯 Final advice

> 💎 **The most important rule of the ML course:**
>
> **Imperfect code that exists > a perfect plan that's never written.**
>
> Submit a **working (even imperfect)** solution on time — it beats a perfect but late one.

---

[⬅ Back to Resources](./README.md) · [⬅ Repository root](../README.md)
