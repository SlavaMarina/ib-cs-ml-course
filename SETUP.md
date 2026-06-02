# 🚀 SETUP — Как опубликовать курс (для преподавателя)

Пошаговая инструкция: от распакованной папки до работающего курса на GitHub.
Время: **~15 минут** (один раз).

---

## Шаг 1 · Создайте репозиторий на GitHub

1. Зайдите на [github.com](https://github.com) → **New repository**
2. Название: `ib-cs-ml-course` (или своё — тогда поправьте в шаге 3)
3. Visibility: **Private** (для класса) или **Public** (если хотите делиться)
4. **НЕ** добавляйте README/`.gitignore` (они уже есть в этой папке)
5. Нажмите **Create repository**

---

## Шаг 2 · Активируйте Colab-бейджи

Откройте файл `add_colab_badges.py` и отредактируйте **3 строки** вверху:

```python
GITHUB_USER = "ваш-username"      # напр. "anna-teacher-tfl"
REPO_NAME   = "ib-cs-ml-course"   # как назвали репозиторий в шаге 1
BRANCH      = "main"              # обычно main
```

Запустите:

```bash
python add_colab_badges.py
```

Скрипт:
- вставит кнопку **"Open in Colab"** в начало всех 26 ноутбуков
- подставит ваш username во все README

---

## Шаг 3 · Запушьте на GitHub

В папке с курсом выполните:

```bash
git init
git add .
git commit -m "Initial commit: IB CS ML course"
git branch -M main
git remote add origin https://github.com/ВАШ-USERNAME/ib-cs-ml-course.git
git push -u origin main
```

---

## Шаг 4 · Проверьте

Откройте репозиторий на GitHub. Вы должны увидеть:
- ✅ Красивый README с таблицами и бейджами
- ✅ Кнопки **"Open in Colab"** работают (открывают ноутбук в Colab)
- ✅ Папки недель с собственными README

---

## 📋 Как раздавать ДЗ ученикам

### Вариант A — простой (Google Classroom)
1. Скопируйте ссылку "Open in Colab" нужного ДЗ-ноутбука
2. Создайте задание в Google Classroom, вставьте ссылку
3. Ученик: `Файл → Сохранить копию на Диске` → заполняет → сдаёт копию
4. Вы ревьюите копию прямо в Colab

### Вариант B — GitHub native (для продвинутых)
1. Ученики делают **Fork** репозитория
2. Для каждого ДЗ создают **branch** (напр. `hw-week1`)
3. Сдача = **Pull Request**
4. Вы ревьюите как code review — комментарии прямо в ячейках

---

## 🔄 Как обновлять курс

Если правите ноутбук:
```bash
git add .
git commit -m "Обновил Week 3 workshop"
git push
```

> ⚠️ После добавления **нового** ноутбука — запустите `add_colab_badges.py` снова
> (он идемпотентный: не дублирует бейджи в старых ноутбуках, добавит только в новые).

---

## ❓ Troubleshooting

| Проблема | Решение |
|---|---|
| Бейдж "Open in Colab" ведёт в 404 | Проверьте `GITHUB_USER`/`REPO_NAME` в `add_colab_badges.py`, перезапустите |
| Репозиторий private — Colab не открывает | Colab требует, чтобы ученик имел доступ к репо; либо сделайте public |
| Ноутбук не рендерится на GitHub | GitHub иногда тупит на больших .ipynb — откройте через [nbviewer.org](https://nbviewer.org) |
| `git push` просит пароль | Используйте Personal Access Token вместо пароля (Settings → Developer settings → PAT) |

---

[⬅ Назад к главной](./README.md)
