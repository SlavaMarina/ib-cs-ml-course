# 🚀 SETUP — Publishing the course (for teachers)

Step-by-step guide from an unzipped folder to a live course on GitHub.
Time: **~15 minutes** (one-time).

---

## Step 1 · Create a GitHub repository

1. Go to [github.com](https://github.com) → **New repository**
2. Name: `ib-cs-ml-course` (or your own — then update Step 2)
3. Visibility: **Public** (for portfolio) or **Private** (for class only)
4. Do **NOT** add a README / `.gitignore` (they already exist in this folder)
5. Click **Create repository**

---

## Step 2 · Activate the Colab badges

Open `add_colab_badges.py` and edit the **3 lines** at the top:

```python
GITHUB_USER = "your-username"
REPO_NAME   = "ib-cs-ml-course"
BRANCH      = "main"
```

Run:

```bash
python add_colab_badges.py
```

The script will:
- insert an **"Open in Colab"** button at the start of every notebook
- replace the username placeholder in all README files

---

## Step 3 · Push to GitHub

In the course folder:

```bash
git init
git add .
git commit -m "Initial commit: IB CS ML course"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/ib-cs-ml-course.git
git push -u origin main
```

---

## Step 4 · Verify

Open the repository on GitHub. You should see:
- ✅ A clean README with tables and badges
- ✅ Working **"Open in Colab"** buttons
- ✅ Week folders, each with its own README

---

## 📋 Distributing homework

Homework is **not** in this repository — it is released via **Google Classroom** on schedule:

1. Upload homework notebooks to a private Google Drive folder
2. In Google Classroom: **Create → Assignment**, attach the notebook
3. Choose **Make a copy for each student**
4. Set a **Schedule** date so it appears automatically when due

---

## 🔄 Updating the course

```bash
git add .
git commit -m "Update Week 3 workshop"
git push
```

> ⚠️ After adding a **new** notebook, run `add_colab_badges.py` again
> (it is idempotent: won't duplicate badges in existing notebooks).

---

[⬅ Back to home](./README.md)
