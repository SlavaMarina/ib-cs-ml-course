# 🎓 IB Computer Science — Machine Learning Course

> Полный 6-недельный курс подготовки к **ML-части IB Computer Science** (Topic A4, first exams 2027). HL focus. 26 интерактивных Jupyter-ноутбуков.

![Notebooks](https://img.shields.io/badge/notebooks-26-blue) ![Syllabus](https://img.shields.io/badge/A4_coverage-17%2F17-success) ![Level](https://img.shields.io/badge/level-HL-orange) ![Exams](https://img.shields.io/badge/first_exams-2027-informational)

---

## 📖 О курсе

Этот курс покрывает **все 17 syllabus statements** из Topic A4 (Machine Learning) нового IB CS syllabus. Каждая неделя построена по схеме: **Лекция → Теоретическое ДЗ → Семинар (практика) → Практическое ДЗ**.

Все ноутбуки запускаются в **Google Colab** (одна кнопка, ничего ставить не надо) или локально в Jupyter.

## 🚀 Как начать

1. Нажмите бейдж **Open in Colab** рядом с любым ноутбуком ниже
2. В Colab: `Файл → Сохранить копию на Диске` (чтобы сохранять свой прогресс)
3. Запускайте ячейки сверху вниз (`Shift+Enter`)
4. Для ДЗ — заполняйте ячейки с пометкой `# === ВАШ КОД ===` или текстовые блоки

> 💡 **Ученикам:** делайте копию ноутбука себе на Drive перед началом работы — иначе прогресс не сохранится.

## 📅 Календарь курса

| Неделя | Тема | Покрытие |
|---|---|---|
| **1** | Основы + Hardware + Data Cleaning | 3 statements |
| **2** | Supervised Learning + метрики | 5 statements |
| **3** | Unsupervised + Model Selection | 3 statements |
| **4** | Neural Networks (ANN + CNN) | 2 statements |
| **5** | RL + GA + Ethics + Mock | 4 statements |
| **6** | Final Mile (LLM, Mock Paper, Flashcards) | exam prep |
| 🎁 Bonus | Kaggle Competition + Debate Kit | дополнительно |

## ✅ Покрытие syllabus (17/17)

| Statement | Тема | Неделя |
|---|---|---|
| `A4.1.1` | Describe types of ML and real-world applications | 1 |
| `A4.1.2` | Describe hardware used in ML (CPU/GPU/TPU/etc.) | 1 |
| `A4.2.1` | Data cleaning (HL) | 1 |
| `A4.2.2` | Feature selection (HL) | 2 |
| `A4.2.3` | Dimensionality reduction (HL) | 2 |
| `A4.3.1` | Linear regression | 2 |
| `A4.3.2` | Classification (KNN, Decision Trees) | 2 |
| `A4.3.3` | Hyperparameter tuning + evaluation metrics | 2 |
| `A4.3.4` | Clustering algorithms | 3 |
| `A4.3.5` | Association rule learning | 3 |
| `A4.3.6` | Reinforcement learning | 5 |
| `A4.3.7` | Genetic algorithms | 5 |
| `A4.3.8` | Artificial Neural Networks (ANN) | 4 |
| `A4.3.9` | Convolutional Neural Networks (CNN) | 4 |
| `A4.3.10` | Model selection | 3 |
| `A4.4.1` | Ethical implications of ML | 5 |
| `A4.4.2` | Reassessing ethics as tech evolves | 5 |

## 📚 Содержание

### Неделя 1: [Основы ML, Hardware и очистка данных](./week1_fundamentals/)

*Syllabus: `A4.1.1`, `A4.1.2`, `A4.2.1`*

| Ноутбук | Открыть | Описание |
|---|---|---|
| **Урок 1 · Лекция** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week1_fundamentals/Week1_Lesson1_Lecture.ipynb) | Типы ML + Hardware: 6 типов процессоров, edge vs cloud, 5 сценариев применения |
| **ДЗ 1 · Теория** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week1_fundamentals/Week1_HW1_Theory.ipynb) | Сопоставление парадигм ML, выбор hardware, worked example |
| **Урок 2 · Семинар** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week1_fundamentals/Week1_Lesson2_Workshop.ipynb) | Полный pipeline очистки данных на 2 реальных датасетах |
| **ДЗ 2 · Практика** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week1_fundamentals/Week1_HW2_Practice.ipynb) | Самостоятельная очистка грязного датасета + отчёт |

### Неделя 2: [Supervised Learning + метрики](./week2_supervised/)

*Syllabus: `A4.2.2`, `A4.2.3`, `A4.3.1`, `A4.3.2`, `A4.3.3`*

| Ноутбук | Открыть | Описание |
|---|---|---|
| **Урок 3 · Лекция** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week2_supervised/Week2_Lesson3_Lecture.ipynb) | Linear regression, KNN, Decision Trees + feature selection + метрики |
| **ДЗ 1 · Теория** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week2_supervised/Week2_HW1_Theory.ipynb) | Расчёт метрик вручную, confusion matrix, выбор алгоритма |
| **Урок 4 · Семинар** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week2_supervised/Week2_Lesson4_Workshop.ipynb) | KNN + DT на реальных данных, grid search, cross-validation |
| **ДЗ 2 · Практика** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week2_supervised/Week2_HW2_Practice.ipynb) | Полный supervised pipeline с тюнингом гиперпараметров |

### Неделя 3: [Unsupervised Learning + выбор модели](./week3_unsupervised/)

*Syllabus: `A4.3.4`, `A4.3.5`, `A4.3.10`*

| Ноутбук | Открыть | Описание |
|---|---|---|
| **Урок 5 · Лекция** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week3_unsupervised/Week3_Lesson5_Lecture.ipynb) | Clustering (4 алгоритма), association rules, model selection |
| **ДЗ 1 · Теория** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week3_unsupervised/Week3_HW1_Theory.ipynb) | Ручной расчёт support/confidence/lift, выбор алгоритма кластеризации |
| **Урок 6 · Семинар** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week3_unsupervised/Week3_Lesson6_Workshop.ipynb) | Customer segmentation (K-means+Elbow+Silhouette), DBSCAN, Apriori |
| **ДЗ 2 · Практика** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week3_unsupervised/Week3_HW2_Practice.ipynb) | Mini-IA: retail analytics (clustering + правила + churn) |

### Неделя 4: [Нейронные сети — ANN, CNN, Backpropagation](./week4_neural_networks/)

*Syllabus: `A4.3.8`, `A4.3.9`*

| Ноутбук | Открыть | Описание |
|---|---|---|
| **Урок 7 · Лекция** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week4_neural_networks/Week4_Lesson7_Lecture.ipynb) | ANN структура, activation functions, backprop, CNN архитектура |
| **ДЗ 1 · Теория** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week4_neural_networks/Week4_HW1_Theory.ipynb) | Forward pass вручную, ReLU vs Sigmoid, CNN spatial hierarchies |
| **Урок 8 · Семинар** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week4_neural_networks/Week4_Lesson8_Workshop.ipynb) | Brain in Code: NumPy ANN + Keras CNN на MNIST |
| **ДЗ 2 · Практика** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week4_neural_networks/Week4_HW2_Practice.ipynb) | Architecture Lab: эксперименты с глубиной + ReLU vs Sigmoid |

### Неделя 5: [RL, Генетические алгоритмы, Этика, Mock Exam](./week5_rl_ga_ethics/)

*Syllabus: `A4.3.6`, `A4.3.7`, `A4.4.1`, `A4.4.2`*

| Ноутбук | Открыть | Описание |
|---|---|---|
| **Урок 9 · Лекция** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week5_rl_ga_ethics/Week5_Lesson9_Lecture.ipynb) | RL + GA + Ethics (8 типов проблем, 6 case studies) |
| **ДЗ 1 · Теория** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week5_rl_ga_ethics/Week5_HW1_Theory.ipynb) | RL case study, GA fitness, эссе 200 слов по этике |
| **Урок 10 · Семинар** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week5_rl_ga_ethics/Week5_Lesson10_Workshop.ipynb) | Mock Exam Section B + N-Queens GA + Q-learning GridWorld |
| **ДЗ 2 · Capstone** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week5_rl_ga_ethics/Week5_HW2_Practice.ipynb) | Дизайн ML-системы для социальной проблемы (100 баллов) |

### Неделя 6: [Final Mile — LLM, TOK, Regulations, Mock, Flashcards](./week6_final_mile/)

*Syllabus: `LLM`, `TOK`, `GDPR`, `AI Act`*

| Ноутбук | Открыть | Описание |
|---|---|---|
| **Урок 11 · Лекция** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week6_final_mile/Week6_Lesson11_Lecture_LLM.ipynb) | LLM/GenAI + TOK integration + GDPR/AI Act/regulations |
| **Quiz · Самопроверка** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week6_final_mile/Week6_Quiz_Battery.ipynb) | 50 multiple-choice вопросов с авто-проверкой (Section A практика) |
| **Mock · Экзамен** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week6_final_mile/Week6_Mock_Paper1.ipynb) | Полный 2-часовой Paper 1 (Section A + B) + markscheme |
| **Flashcards · Повторение** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/week6_final_mile/Week6_Flashcards.ipynb) | 108 интерактивных карточек + day-before-exam checklist |

### 🎁 [Bonus — Kaggle Competition + Class Debate Kit](./bonus/)

| Ноутбук | Открыть | Описание |
|---|---|---|
| **Kaggle Quest** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/bonus/Bonus_Kaggle_Competition_Journey.ipynb) | 6-недельный геймифицированный трек: от первого submission до class leaderboard |
| **Debate Kit** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlavaMarina/ib-cs-ml-course/blob/main/bonus/Bonus_Class_Debate_Kit.ipynb) | 8 готовых дебатов с аргументами, кейсами, killer questions, scoring rubric |

## 🗂 Структура репозитория

```
ib-cs-ml-course/
├── week1_fundamentals/
│   ├── Week1_Lesson1_Lecture.ipynb
│   ├── Week1_HW1_Theory.ipynb
│   ├── Week1_Lesson2_Workshop.ipynb
│   ├── Week1_HW2_Practice.ipynb
│   └── README.md
├── week2_supervised/
│   ├── Week2_Lesson3_Lecture.ipynb
│   ├── Week2_HW1_Theory.ipynb
│   ├── Week2_Lesson4_Workshop.ipynb
│   ├── Week2_HW2_Practice.ipynb
│   └── README.md
├── week3_unsupervised/
│   ├── Week3_Lesson5_Lecture.ipynb
│   ├── Week3_HW1_Theory.ipynb
│   ├── Week3_Lesson6_Workshop.ipynb
│   ├── Week3_HW2_Practice.ipynb
│   └── README.md
├── week4_neural_networks/
│   ├── Week4_Lesson7_Lecture.ipynb
│   ├── Week4_HW1_Theory.ipynb
│   ├── Week4_Lesson8_Workshop.ipynb
│   ├── Week4_HW2_Practice.ipynb
│   └── README.md
├── week5_rl_ga_ethics/
│   ├── Week5_Lesson9_Lecture.ipynb
│   ├── Week5_HW1_Theory.ipynb
│   ├── Week5_Lesson10_Workshop.ipynb
│   ├── Week5_HW2_Practice.ipynb
│   └── README.md
├── week6_final_mile/
│   ├── Week6_Lesson11_Lecture_LLM.ipynb
│   ├── Week6_Quiz_Battery.ipynb
│   ├── Week6_Mock_Paper1.ipynb
│   ├── Week6_Flashcards.ipynb
│   └── README.md
├── bonus/
│   ├── Bonus_Kaggle_Competition_Journey.ipynb
│   ├── Bonus_Class_Debate_Kit.ipynb
│   └── README.md
├── resources/
└── README.md
```

## 🛠 Технические требования

Все библиотеки предустановлены в Google Colab. Для локального запуска:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn mlxtend tensorflow ipywidgets
```

| Библиотека | Используется в |
|---|---|
| numpy, pandas, matplotlib, seaborn | все недели |
| scikit-learn | недели 2-3 (supervised, clustering) |
| mlxtend | неделя 3 (association rules) |
| tensorflow / keras | неделя 4 (нейросети), bonus Kaggle |
| ipywidgets | неделя 6 (quiz, flashcards) |

## 📦 Источники

Контент основан на двух официальных учебниках IB CS (2027):
- Baumgarten, Ganea & Turland — *Computer Science for the IB Diploma* (Hodder/Hachette)
- MacKenty & Stephenson — *Computer Science* (Oxford 2025)

---

> ⚙️ **Преподавателю:** перед публикацией запустите `python add_colab_badges.py` (укажите свой GitHub username) — это активирует все Colab-бейджи. См. инструкцию в скрипте.
