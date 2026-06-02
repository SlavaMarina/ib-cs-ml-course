#!/usr/bin/env python3
"""
============================================================================
  add_colab_badges.py
============================================================================
  Что делает этот скрипт:
    1. Вставляет кнопку "Open in Colab" в начало КАЖДОГО ноутбука
    2. Заменяет placeholders (__GH_USER__ / __REPO__) во ВСЕХ README.md
       на ваш реальный GitHub username и название репозитория

  Запускается ОДИН РАЗ после клонирования/распаковки репозитория,
  ПЕРЕД тем как запушить на GitHub.

  ─────────────────────────────────────────────────────────────────────────
  ИНСТРУКЦИЯ:
    1. Отредактируйте 2 строки ниже (GITHUB_USER и REPO_NAME)
    2. Запустите:  python add_colab_badges.py
    3. Запушьте репозиторий на GitHub
    4. Все кнопки "Open in Colab" заработают автоматически
  ─────────────────────────────────────────────────────────────────────────
"""

# ╔═══════════════════════════════════════════════════════════════════════╗
# ║  👇 ОТРЕДАКТИРУЙТЕ ЭТИ 3 СТРОКИ ПОД СЕБЯ                                 ║
# ╚═══════════════════════════════════════════════════════════════════════╝
GITHUB_USER = "SlavaMarina"        # ваш GitHub username, напр. "anna-teacher-tfl"
REPO_NAME   = "ib-cs-ml-course"      # название репозитория на GitHub
BRANCH      = "main"                 # ветка (обычно main, иногда master)
# ───────────────────────────────────────────────────────────────────────────

import json
import os
import glob

# Папка, где лежит этот скрипт = корень репозитория
ROOT = os.path.dirname(os.path.abspath(__file__))

COLAB_LOGO = "https://colab.research.google.com/assets/colab-badge.svg"


def make_badge_cell(rel_path):
    """Создаёт markdown-ячейку с Colab-бейджем для ноутбука по пути rel_path."""
    url = f"https://colab.research.google.com/github/{GITHUB_USER}/{REPO_NAME}/blob/{BRANCH}/{rel_path}"
    badge_md = (
        f"<a href=\"{url}\" target=\"_blank\">"
        f"<img src=\"{COLAB_LOGO}\" alt=\"Open In Colab\"/></a>"
    )
    return {
        "cell_type": "markdown",
        "metadata": {"colab_badge": True},   # маркер, чтобы не дублировать
        "source": [badge_md],
    }


def inject_badges():
    """Вставляет бейдж в начало каждого .ipynb (идемпотентно)."""
    notebooks = glob.glob(os.path.join(ROOT, "**", "*.ipynb"), recursive=True)
    # Игнорируем checkpoints
    notebooks = [nb for nb in notebooks if ".ipynb_checkpoints" not in nb]

    count = 0
    for nb_path in sorted(notebooks):
        rel_path = os.path.relpath(nb_path, ROOT).replace(os.sep, "/")
        with open(nb_path, "r", encoding="utf-8") as f:
            nb = json.load(f)

        cells = nb.get("cells", [])

        # Идемпотентность: удаляем старый бейдж, если он уже есть (первая ячейка)
        if cells and cells[0].get("metadata", {}).get("colab_badge"):
            cells.pop(0)

        # Вставляем свежий бейдж первой ячейкой
        cells.insert(0, make_badge_cell(rel_path))
        nb["cells"] = cells

        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, ensure_ascii=False, indent=1)
        count += 1
        print(f"  🔖 {rel_path}")

    print(f"\n✅ Бейджи вставлены в {count} ноутбуков")


def patch_readmes():
    """Заменяет placeholders в README.md на реальные значения."""
    readmes = glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)
    count = 0
    for md_path in readmes:
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "__GH_USER__" in content or "__REPO__" in content:
            content = content.replace("__GH_USER__", GITHUB_USER)
            content = content.replace("__REPO__", REPO_NAME)
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            rel = os.path.relpath(md_path, ROOT)
            print(f"  📝 {rel}")
    print(f"\n✅ Обновлено README-файлов: {count}")


if __name__ == "__main__":
    print("=" * 60)
    print(f"  GitHub user : {GITHUB_USER}")
    print(f"  Repo name   : {REPO_NAME}")
    print(f"  Branch      : {BRANCH}")
    print("=" * 60)

    if GITHUB_USER == "your-username":
        print("\n⚠️  ВНИМАНИЕ: вы не изменили GITHUB_USER!")
        print("   Откройте этот файл и впишите свой GitHub username в строку 38.")
        print("   Бейджи будут указывать на несуществующий репозиторий.\n")
        resp = input("Всё равно продолжить? (y/n): ").strip().lower()
        if resp != "y":
            print("Отменено. Отредактируйте GITHUB_USER и запустите снова.")
            raise SystemExit(0)

    print("\n[1/2] Вставка Colab-бейджей в ноутбуки...")
    inject_badges()

    print("\n[2/2] Патч README-файлов...")
    patch_readmes()

    print("\n" + "=" * 60)
    print("🎉 ГОТОВО! Теперь:")
    print("   git add .")
    print('   git commit -m "Add Colab badges"')
    print("   git push")
    print("=" * 60)
