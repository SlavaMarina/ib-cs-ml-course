# 📖 Glossary — Полный справочник терминов IB CS ML

> 110+ ключевых терминов с определениями, примерами и common mistakes.
> Источники: Baumgarten (Hodder 2024), MacKenty & Stephenson (Oxford 2025), новый IB syllabus 2027.

---

## 🔤 Как пользоваться

- **Алфавитный индекс** ниже — для быстрого поиска по латинскому/русскому
- **По неделям/темам** — после индекса, удобно для повторения
- Каждая запись: краткое **определение** + **пример** + **частая ошибка** + **см. также**

---

## 🔠 Алфавитный индекс


**A** · [Accountability](#accountability)  [Accuracy](#accuracy)  [Action](#action)  [Activation function](#activation-function)  [Agent](#agent)  [Algorithmic fairness](#algorithmic-fairness)  [Amazon AI recruiting (2018)](#amazon-ai-recruiting-2018)  [Apriori algorithm](#apriori-algorithm)  [ASIC](#asic)  [Association rule mining](#association-rule-mining)  [Attention](#attention)  
**B** · [Backpropagation](#backpropagation)  [Bias](#bias)  [Bias (in ML)](#bias-in-ml)  
**C** · [Centroid](#centroid)  [Clustering](#clustering)  [CNN](#cnn)  [COMPAS](#compas)  [Confidence](#confidence)  [Confusion matrix](#confusion-matrix)  [Convolutional layer](#convolutional-layer)  [CPU](#cpu)  [Cross-validation](#cross-validation)  [Crossover](#crossover)  [Cumulative reward](#cumulative-reward)  [Curse of dimensionality](#curse-of-dimensionality)  
**D** · [Data cleaning](#data-cleaning)  [DBSCAN](#dbscan)  [Decision Tree](#decision-tree)  [Deep learning](#deep-learning)  [Dendrogram](#dendrogram)  [Dimensionality reduction](#dimensionality-reduction)  [Dropout](#dropout)  
**E** · [Edge computing](#edge-computing)  [Elbow method](#elbow-method)  [Embedded method](#embedded-method)  [Environment](#environment)  [Epoch](#epoch)  [Epsilon (ε)](#epsilon-ε)  [Epsilon-greedy](#epsilon-greedy)  [EU AI Act (2024)](#eu-ai-act-2024)  [Explainability](#explainability)  [Exploration vs exploitation](#exploration-vs-exploitation)  
**F** · [F1 Score](#f1-score)  [Feature map](#feature-map)  [Feature selection](#feature-selection)  [Filter method](#filter-method)  [Fine-tuning](#fine-tuning)  [Fitness function](#fitness-function)  [Forward propagation](#forward-propagation)  [FPGA](#fpga)  [Fully connected layer](#fully-connected-layer)  
**G** · [GDPR](#gdpr)  [Genetic algorithm](#genetic-algorithm)  [Gini impurity](#gini-impurity)  [GPU](#gpu)  [Gradient descent](#gradient-descent)  
**H** · [Hallucinations](#hallucinations)  [Hidden layer](#hidden-layer)  [Hierarchical clustering](#hierarchical-clustering)  [Hyperparameter](#hyperparameter)  
**I** · [Informed consent](#informed-consent)  [Intercept](#intercept)  [IQR method](#iqr-method)  
**K** · [K-means](#k-means)  [Kernel (Filter)](#kernel-filter)  [KNN](#knn)  
**L** · [Learning rate](#learning-rate)  [Lift](#lift)  [Linear regression](#linear-regression)  [LLM](#llm)  [Loss function](#loss-function)  
**M** · [Max pooling](#max-pooling)  [Mean imputation](#mean-imputation)  [minPts](#minpts)  [Model selection](#model-selection)  [Mutation](#mutation)  
**N** · [Netflix de-anonymization (2006)](#netflix-de-anonymization-2006)  [Normalization](#normalization)  [NPU](#npu)  
**O** · [Outlier](#outlier)  [Overfitting](#overfitting)  
**P** · [Perceptron](#perceptron)  [Policy](#policy)  [Pooling layer](#pooling-layer)  [Population](#population)  [Precision](#precision)  [Privacy](#privacy)  [Prompt engineering](#prompt-engineering)  [Pruning](#pruning)  
**Q** · [Q-learning](#q-learning)  
**R** · [RAG](#rag)  [Recall](#recall)  [Reinforcement learning](#reinforcement-learning)  [ReLU](#relu)  [Reward](#reward)  [Right to explanation](#right-to-explanation)  [R² (R-squared)](#r2-r-squared)  
**S** · [Sigmoid](#sigmoid)  [Silhouette score](#silhouette-score)  [Slope](#slope)  [Softmax](#softmax)  [Spatial hierarchies](#spatial-hierarchies)  [Spectral clustering](#spectral-clustering)  [State](#state)  [Supervised learning](#supervised-learning)  [Support](#support)  
**T** · [TOK (Theory of Knowledge)](#tok-theory-of-knowledge)  [Tokenization](#tokenization)  [TPU](#tpu)  [Transfer learning](#transfer-learning)  [Transformer](#transformer)  [Transparency](#transparency)  
**U** · [Unsupervised learning](#unsupervised-learning)  
**W** · [Weight](#weight)  [Wrapper method](#wrapper-method)  

---

## 📚 По неделям курса


### Week 1: Fundamentals

#### Supervised learning
<small>📌 `A4.1.1`</small>

> ML парадигма, в которой модель обучается на размеченных данных (input-output пары) для предсказания output на новых input.

**💡 Пример:** Email spam classifier — обучается на парах (email, spam/not-spam) и классифицирует новые email  
**⚠️ Common mistake:** Часто путают с unsupervised на классических примерах  
**🔗 См. также:** Unsupervised learning, Classification, Regression

---

#### Unsupervised learning
<small>📌 `A4.1.1`</small>

> ML парадигма для поиска паттернов в неразмеченных данных — кластеризация, ассоциативные правила.

**💡 Пример:** Market segmentation — группировка клиентов без заранее известных категорий  
**⚠️ Common mistake:** Думают, что нужны хоть какие-то метки  
**🔗 См. также:** Supervised learning, Clustering, Association rules

---

#### Reinforcement learning
<small>📌 `A4.1.1 / A4.3.6`</small>

> ML парадигма, где агент учится через взаимодействие со средой, получая награды/штрафы, цель — максимизировать cumulative reward.

**💡 Пример:** AlphaGo учится играть в Go, получая +1 за победу и -1 за проигрыш  
**⚠️ Common mistake:** Путают с GA (RL — один агент; GA — популяция)  
**🔗 См. также:** Agent, Reward, Q-learning

---

#### Deep learning
<small>📌 `A4.1.1`</small>

> Подмножество ML, использующее глубокие нейронные сети (много hidden layers), которые автоматически учат иерархические представления.

**💡 Пример:** CNN для распознавания лиц — каждый слой учится на всё более сложных признаках  
**⚠️ Common mistake:** Не любая нейросеть = deep learning; нужно минимум 2-3 hidden layers  
**🔗 См. также:** ANN, CNN, Hidden layer

---

#### Transfer learning
<small>📌 `A4.1.1`</small>

> Техника переиспользования предобученной модели для новой, но связанной задачи — экономит время и данные.

**💡 Пример:** Взять ImageNet-pretrained ResNet → fine-tune на 1000 фото своих кошек  
**⚠️ Common mistake:** Думают, что transfer learning = просто использовать готовую модель без дообучения  
**🔗 См. также:** Fine-tuning, Pre-trained model

---


### Week 1: Hardware

#### CPU
<small>📌 `A4.1.2`</small>

> Central Processing Unit — главный процессор компьютера. Несколько ядер, оптимизирован для последовательных задач.

**💡 Пример:** Intel Core i7, AMD Ryzen — у каждого 6-16 ядер  
**⚠️ Common mistake:** Думают, что CPU нельзя использовать для ML — можно, но медленнее  
**🔗 См. также:** GPU, TPU, Parallel processing

---

#### GPU
<small>📌 `A4.1.2`</small>

> Graphics Processing Unit — тысячи параллельных ядер, оптимизированных для matrix operations. Тренирует нейросети в 10-100× быстрее CPU.

**💡 Пример:** NVIDIA RTX 4090, A100 — для тренировки нейросетей  
**⚠️ Common mistake:** Думают, что GPU универсален — он плох для последовательных задач  
**🔗 См. также:** CPU, TPU, CUDA

---

#### TPU
<small>📌 `A4.1.2`</small>

> Tensor Processing Unit — ASIC от Google, специально для TensorFlow операций (matrix multiplication).

**💡 Пример:** Google использует TPU pods для тренировки GPT-уровня моделей  
**⚠️ Common mistake:** Путают с GPU — TPU специфичнее, не для графики  
**🔗 См. также:** GPU, ASIC, Google Cloud

---

#### NPU
<small>📌 `A4.1.2`</small>

> Neural Processing Unit — чип, оптимизированный для inference ML моделей на edge устройствах (смартфоны, IoT).

**💡 Пример:** Apple Neural Engine в iPhone — обрабатывает Face ID и Siri локально  
**⚠️ Common mistake:** Думают, что NPU = TPU. NPU для inference на edge, TPU для training в cloud.  
**🔗 См. также:** Edge computing, Inference

---

#### ASIC
<small>📌 `A4.1.2`</small>

> Application-Specific Integrated Circuit — чип, спроектированный под одну конкретную задачу. Максимальная эффективность.

**💡 Пример:** Tesla FSD chip — ASIC для self-driving inference; Google TPU — ASIC для ML training  
**⚠️ Common mistake:** Думают, что ASIC = универсальный чип. Наоборот — узкоспециализированный.  
**🔗 См. также:** TPU, FPGA, NPU

---

#### FPGA
<small>📌 `A4.1.2`</small>

> Field-Programmable Gate Array — перепрограммируемый чип. Гибкость между ASIC (заточен) и CPU (универсален).

**💡 Пример:** Microsoft Bing использует FPGA для search ranking  
**⚠️ Common mistake:** Путают с ASIC — FPGA можно перепрограммировать, ASIC — нет  
**🔗 См. также:** ASIC, Custom hardware

---

#### Edge computing
<small>📌 `A4.1.2`</small>

> Запуск ML inference локально на устройстве (смартфон, IoT) вместо отправки в облако. Низкая latency, приватность, offline-работа.

**💡 Пример:** Smart doorbell распознаёт лица на устройстве, фото не уходят в Amazon  
**⚠️ Common mistake:** Думают, что edge = только мобильные. Edge — это любое не-облачное устройство  
**🔗 См. также:** Cloud computing, NPU, Inference

---


### Week 1: Preprocessing

#### Data cleaning
<small>📌 `A4.2.1`</small>

> Процесс выявления и исправления (или удаления) повреждённых, неполных, дублирующихся или некорректных записей.

**💡 Пример:** Удаление дубликатов, заполнение missing values, нормализация форматов дат  
**⚠️ Common mistake:** Думают, что cleaning = только удаление missing values  
**🔗 См. также:** Missing values, Outlier, Normalization

---

#### Outlier
<small>📌 `A4.2.1`</small>

> Аномальное значение, сильно отличающееся от остальных данных. Может быть ошибкой ввода или важным сигналом.

**💡 Пример:** В датасете зарплат — значение 500K при средней 50K  
**⚠️ Common mistake:** Всегда удаляют outliers — иногда они полезны (fraud detection)  
**🔗 См. также:** IQR method, Z-score

---

#### IQR method
<small>📌 `A4.2.1`</small>

> Метод обнаружения outliers через interquartile range. Outlier если значение вне [Q1 - 1.5·IQR, Q3 + 1.5·IQR].

**💡 Пример:** В boxplot — точки за 'усами' и есть outliers по IQR методу  
**⚠️ Common mistake:** Применяют IQR к данным с не-нормальным распределением (нужны другие методы)  
**🔗 См. также:** Outlier, Z-score, Boxplot

---

#### Mean imputation
<small>📌 `A4.2.1`</small>

> Замена missing values средним значением колонки. Простой, но может вносить bias.

**💡 Пример:** Если в колонке age 10% missing, заполняем средним возрастом 35  
**⚠️ Common mistake:** Применяют к категориальным данным (нужно mode), не median при выбросах  
**🔗 См. также:** Missing values, Median imputation

---

#### Normalization
<small>📌 `A4.2.1`</small>

> Приведение значений features к одной шкале. Критично для distance-based алгоритмов (KNN) и нейросетей.

**💡 Пример:** MinMaxScaler приводит к [0, 1]; StandardScaler — к mean=0, std=1  
**⚠️ Common mistake:** Забывают нормализовать перед KNN — features с большим range доминируют distance  
**🔗 См. также:** StandardScaler, MinMaxScaler, KNN

---


### Week 2: Preprocessing

#### Feature selection
<small>📌 `A4.2.2`</small>

> Выбор только релевантных признаков для обучения. Улучшает точность, уменьшает overfitting, ускоряет обучение.

**💡 Пример:** Из 100 признаков выбрать 20 наиболее коррелированных с target  
**⚠️ Common mistake:** Применяют feature selection после dimensionality reduction, нужно наоборот  
**🔗 См. также:** Filter method, Wrapper method, Embedded method

---

#### Filter method
<small>📌 `A4.2.2`</small>

> Feature selection через статистические метрики (Pearson r, Chi-square). Быстро, но не учитывает взаимодействия фич.

**💡 Пример:** Pearson correlation: оставляем только фичи с |r| > 0.3 относительно target  
**⚠️ Common mistake:** Думают, что filter method учитывает взаимодействия — нет, только независимый rank  
**🔗 См. также:** Wrapper method, Embedded method

---

#### Wrapper method
<small>📌 `A4.2.2`</small>

> Feature selection через многократное обучение модели на разных подмножествах фич. Точнее, но медленнее.

**💡 Пример:** Recursive Feature Elimination (RFE) — итеративно удаляет наименее важные фичи  
**⚠️ Common mistake:** Используют на больших датасетах — медленно из-за многократного обучения  
**🔗 См. также:** Filter method, Embedded method

---

#### Embedded method
<small>📌 `A4.2.2`</small>

> Feature selection встроен в обучение модели (например, регуляризация Lasso, tree importance).

**💡 Пример:** Random Forest feature_importances_ — автоматически даёт ранг важности фич  
**⚠️ Common mistake:** Думают, что embedded = wrapper. Embedded — внутри модели, wrapper — снаружи.  
**🔗 См. также:** Lasso, Random Forest, Filter method

---

#### Dimensionality reduction
<small>📌 `A4.2.3`</small>

> Уменьшение числа признаков с сохранением максимума информации. Борьба с curse of dimensionality.

**💡 Пример:** PCA трансформирует 100 коррелированных фич в 10 ортогональных компонент  
**⚠️ Common mistake:** Путают с feature selection. Reduction создаёт новые фичи; selection выбирает из существующих.  
**🔗 См. также:** PCA, Feature selection, Curse of dimensionality

---

#### Curse of dimensionality
<small>📌 `A4.2.3`</small>

> Проблема: с ростом числа измерений данные становятся разреженными, distance-based алгоритмы перестают работать.

**💡 Пример:** KNN на 1000 фичах работает плохо — все точки кажутся одинаково далёкими  
**⚠️ Common mistake:** Думают, что больше фич = лучше. Часто хуже из-за curse.  
**🔗 См. также:** KNN, Dimensionality reduction

---


### Week 2: Algorithms

#### Linear regression
<small>📌 `A4.3.1`</small>

> Supervised алгоритм для regression. Y = β₀ + β₁X + ε. Находит лучшую прямую для предсказания continuous output.

**💡 Пример:** Прогноз цены дома по площади: цена = 30000 + 1500·площадь  
**⚠️ Common mistake:** Применяют к classification (нужна logistic regression) или к нелинейным зависимостям  
**🔗 См. также:** Slope, Intercept, R²

---

#### Slope
<small>📌 `A4.3.1`</small>

> Коэффициент β₁ в Y = β₀ + β₁X. Показывает, насколько меняется Y при увеличении X на 1.

**💡 Пример:** Если slope = 1500, то +1 м² → +1500$ к цене дома  
**⚠️ Common mistake:** Путают slope и intercept. Slope = наклон, intercept = точка пересечения с осью Y.  
**🔗 См. также:** Intercept, Linear regression

---

#### Intercept
<small>📌 `A4.3.1`</small>

> Коэффициент β₀ в Y = β₀ + β₁X. Значение Y при X = 0.

**💡 Пример:** Если intercept = 30000, дом площадью 0 м² 'стоил бы' 30000$ (теоретически)  
**⚠️ Common mistake:** Интерпретируют intercept буквально, когда X = 0 не имеет смысла  
**🔗 См. также:** Slope, Linear regression

---

#### R² (R-squared)
<small>📌 `A4.3.1`</small>

> Coefficient of determination. R² = 1 - SS_res/SS_tot. Доля дисперсии Y, объяснённая моделью (0 = ничего, 1 = идеально).

**💡 Пример:** R² = 0.85 → модель объясняет 85% вариации в данных  
**⚠️ Common mistake:** R² > 0.95 — часто признак overfitting, а не идеальной модели  
**🔗 См. также:** Linear regression, Overfitting

---

#### KNN
<small>📌 `A4.3.2`</small>

> K-Nearest Neighbours — classification/regression алгоритм. Предсказание = majority vote (или среднее) K ближайших соседей.

**💡 Пример:** Классификация цветка ириса: смотрим 5 ближайших размеченных образцов  
**⚠️ Common mistake:** Забывают нормализовать данные перед KNN  
**🔗 См. также:** K (parameter), Euclidean distance, Normalization

---

#### Decision Tree
<small>📌 `A4.3.2`</small>

> Древовидная структура if-else правил. Каждый узел — вопрос о фиче, листья — предсказания.

**💡 Пример:** Решение давать ли кредит: возраст > 25 → доход > 50K → дать  
**⚠️ Common mistake:** Не контролируют max_depth → дерево запоминает train data (overfitting)  
**🔗 См. также:** Gini impurity, Pruning, Random Forest

---

#### Gini impurity
<small>📌 `A4.3.2`</small>

> Метрика 'нечистоты' узла дерева. 0 = все одного класса; 0.5 = равная смесь. DT выбирает split, минимизирующий Gini.

**💡 Пример:** В узле с 80% класс А и 20% класс B: Gini = 1 - 0.8² - 0.2² = 0.32  
**⚠️ Common mistake:** Путают с entropy (другая метрика, но похожая идея)  
**🔗 См. также:** Decision Tree, Entropy

---

#### Pruning
<small>📌 `A4.3.2`</small>

> Обрезка ветвей Decision Tree для борьбы с overfitting.

**💡 Пример:** После обучения удаляем ветви, которые незначительно улучшают accuracy  
**⚠️ Common mistake:** Думают, что pruning только усложняет — наоборот, упрощает + улучшает generalization  
**🔗 См. также:** Decision Tree, Overfitting, max_depth

---


### Week 2: Tuning

#### Hyperparameter
<small>📌 `A4.3.3`</small>

> Значение, заданное ПЕРЕД обучением (не выучивается из данных). Определяет поведение алгоритма.

**💡 Пример:** K в KNN, max_depth в DT, learning_rate в нейросети  
**⚠️ Common mistake:** Путают с parameters (weights). Hyperparameters задаются вами; parameters учит модель.  
**🔗 См. также:** Grid search, Cross-validation

---

#### Cross-validation
<small>📌 `A4.3.3`</small>

> Разбиение данных на K folds. Модель обучается K раз, каждый раз другой fold = test. Среднее даёт надёжную оценку.

**💡 Пример:** 5-fold CV: данные → 5 частей → train на 4, test на 1, повторяем 5 раз, усредняем  
**⚠️ Common mistake:** Делают CV только на training, не отделяют holdout test set  
**🔗 См. также:** Hyperparameter, Holdout, Stratified

---


### Week 2: Metrics

#### Confusion matrix
<small>📌 `A4.3.3`</small>

> Таблица TP/FP/FN/TN для classification. Основа для всех метрик.

**💡 Пример:** Spam filter: 80 TP / 10 FP / 20 FN / 90 TN на 200 emails  
**⚠️ Common mistake:** Путают, где actual, а где predicted. Convention: rows = actual, cols = predicted.  
**🔗 См. также:** Precision, Recall, F1

---

#### Accuracy
<small>📌 `A4.3.3`</small>

> Доля правильных предсказаний. Accuracy = (TP + TN) / (TP + TN + FP + FN).

**💡 Пример:** 180 правильных из 200 emails → accuracy = 90%  
**⚠️ Common mistake:** Используют Accuracy при class imbalance — даёт ложное чувство хорошей модели  
**🔗 См. также:** Precision, Recall, F1, Class imbalance

---

#### Precision
<small>📌 `A4.3.3`</small>

> Из всех предсказанных positive, сколько действительно positive. P = TP / (TP + FP).

**💡 Пример:** 80 TP / 90 predicted positive → precision = 89%. Важно когда FP costly.  
**⚠️ Common mistake:** Путают с Recall. Precision = качество positive предсказаний.  
**🔗 См. также:** Recall, F1, False Positive

---

#### Recall
<small>📌 `A4.3.3`</small>

> Из всех actual positive, сколько модель нашла. R = TP / (TP + FN).

**💡 Пример:** Cancer screening: 95 actual cases, нашли 90 → recall = 95%. Важно когда FN costly.  
**⚠️ Common mistake:** Путают с Precision. Recall = полнота, чтобы не упустить positive.  
**🔗 См. также:** Precision, F1, False Negative

---

#### F1 Score
<small>📌 `A4.3.3`</small>

> Harmonic mean of Precision and Recall. F1 = 2·P·R / (P + R). Используется при class imbalance.

**💡 Пример:** P = 0.89, R = 0.80 → F1 = 0.84  
**⚠️ Common mistake:** Думают, что F1 = (P + R) / 2 — это arithmetic mean, не harmonic.  
**🔗 См. также:** Precision, Recall, Class imbalance

---


### Week 2: General

#### Overfitting
<small>📌 `A4.3.10`</small>

> Модель запомнила детали training data, плохо обобщает на новые данные. Train accuracy >> test accuracy.

**💡 Пример:** DT с max_depth=None даёт 100% train accuracy, но 60% test  
**⚠️ Common mistake:** Думают, что overfit видно только по low test accuracy. Признак — gap train vs test.  
**🔗 См. также:** Underfitting, Cross-validation, Regularization

---


### Week 3: Unsupervised

#### Clustering
<small>📌 `A4.3.4`</small>

> Unsupervised техника: группировка точек так, чтобы внутри кластера были похожи, между кластерами — различны.

**💡 Пример:** Сегментация клиентов: low-value / medium / high — без заранее заданных меток  
**⚠️ Common mistake:** Применяют к labelled data — нужно classification, а не clustering  
**🔗 См. также:** K-means, DBSCAN, Centroid

---

#### K-means
<small>📌 `A4.3.4`</small>

> Алгоритм кластеризации в 4 шага: 1) init K centroids 2) assign points to nearest 3) recalc centroids 4) repeat.

**💡 Пример:** K=3 для customer segmentation — сходится за 10-20 итераций  
**⚠️ Common mistake:** Применяют к не-сферическим кластерам (нужен DBSCAN)  
**🔗 См. также:** Centroid, Elbow method, DBSCAN

---

#### Centroid
<small>📌 `A4.3.4`</small>

> Центр кластера = среднее координат всех точек кластера. Используется в K-means.

**💡 Пример:** Кластер из точек (1,2), (3,4), (5,6) → centroid = (3, 4)  
**⚠️ Common mistake:** Путают centroid и medoid. Centroid — среднее (может не быть точкой данных); medoid — реальная точка.  
**🔗 См. также:** K-means, Cluster

---

#### Elbow method
<small>📌 `A4.3.4`</small>

> Метод выбора K в K-means. Строим график inertia vs K, ищем 'локоть' (точку резкого замедления улучшения).

**💡 Пример:** Для retail data — локоть на K=4 → используем 4 кластера  
**⚠️ Common mistake:** Думают, что есть один объективный K — часто elbow неоднозначен  
**🔗 См. также:** K-means, Silhouette score

---

#### Silhouette score
<small>📌 `A4.3.4`</small>

> Метрика качества кластеризации, от -1 до 1. Выше = кластеры более compact и separated.

**💡 Пример:** Silhouette = 0.7 → хорошее разделение; 0.3 → слабое; <0 → точка в чужом кластере  
**⚠️ Common mistake:** Доверяют только Elbow — рекомендуется использовать Elbow + Silhouette вместе  
**🔗 См. также:** K-means, Elbow method

---

#### DBSCAN
<small>📌 `A4.3.4`</small>

> Density-Based Spatial Clustering. Находит кластеры любой формы, не требует K, помечает outliers как noise.

**💡 Пример:** Кластеризация GPS точек на карте — находит формы дорог, не сферы  
**⚠️ Common mistake:** Применяют к данным разной плотности (eps один для всех — может не работать)  
**🔗 См. также:** Epsilon, minPts, K-means

---

#### Epsilon (ε)
<small>📌 `A4.3.4`</small>

> Параметр DBSCAN: радиус для поиска соседей точки.

**💡 Пример:** ε = 0.5 — точки в радиусе 0.5 единиц считаются 'соседями'  
**⚠️ Common mistake:** Подбирают ε наугад. Стандартный метод — k-distance plot.  
**🔗 См. также:** DBSCAN, minPts

---

#### minPts
<small>📌 `A4.3.4`</small>

> Параметр DBSCAN: минимальное число соседей в радиусе ε для формирования core point.

**💡 Пример:** minPts = 5 — нужно ≥5 точек в окрестности, чтобы считать core  
**⚠️ Common mistake:** Берут minPts = 2 — слишком мало, формируются 'шумные' кластеры  
**🔗 См. также:** DBSCAN, Epsilon, Core point

---

#### Hierarchical clustering
<small>📌 `A4.3.4`</small>

> Строит дерево (dendrogram) кластеров: agglomerative (bottom-up, merging) или divisive (top-down).

**💡 Пример:** Биологическая таксономия — иерархия видов  
**⚠️ Common mistake:** Применяют к большим датасетам — O(n²) или O(n³) сложность  
**🔗 См. также:** Dendrogram, K-means, Linkage

---

#### Dendrogram
<small>📌 `A4.3.4`</small>

> Древовидная диаграмма иерархической кластеризации. Срез на нужной высоте даёт нужное число кластеров.

**💡 Пример:** Дерево языков — английский ближе к немецкому, чем к русскому  
**⚠️ Common mistake:** Читают dendrogram неправильно — высота = dissimilarity, не порядок  
**🔗 См. также:** Hierarchical clustering

---

#### Spectral clustering
<small>📌 `A4.3.4`</small>

> Кластеризация на основе теории графов и eigenvectors матрицы similarity. Для non-linearly-separable данных.

**💡 Пример:** Кластеризация социальной сети — людей с общими друзьями  
**⚠️ Common mistake:** Математика вне scope IB — знать только название и применение  
**🔗 См. также:** K-means, DBSCAN

---

#### Association rule mining
<small>📌 `A4.3.5`</small>

> Поиск паттернов co-occurrence в transactional data. Например, market basket analysis.

**💡 Пример:** Купили пиво → 60% купят и чипсы (с lift = 2.5)  
**⚠️ Common mistake:** Думают, что AR = причинно-следственная связь. Это только корреляция.  
**🔗 См. также:** Apriori, Support, Confidence, Lift

---

#### Support
<small>📌 `A4.3.5`</small>

> Доля транзакций, содержащих набор товаров. Support({A,B}) = (трансакций с A и B) / (всего транзакций).

**💡 Пример:** Из 1000 чеков 50 содержат {хлеб, молоко} → Support = 0.05  
**⚠️ Common mistake:** Путают с probability — support не conditional  
**🔗 См. также:** Confidence, Lift, Apriori

---

#### Confidence
<small>📌 `A4.3.5`</small>

> Conditional probability: купили A → купят B. Confidence(A→B) = Support({A,B}) / Support({A}).

**💡 Пример:** Если 100 купили хлеб и 50 из них купили и молоко → Confidence(хлеб→молоко) = 0.5  
**⚠️ Common mistake:** Высокая confidence — НЕ всегда полезное правило, нужно ещё lift > 1  
**🔗 См. также:** Support, Lift, Apriori

---

#### Lift
<small>📌 `A4.3.5`</small>

> Сила связи vs случайность. Lift(A→B) = Confidence(A→B) / Support({B}). Lift > 1 — связь, = 1 — независимость, < 1 — anti-correlation.

**💡 Пример:** Lift({подгузники → пиво}) = 3.0 — родители покупают пиво в 3× чаще обычного  
**⚠️ Common mistake:** Думают, что lift = 1.1 — сильная связь. Обычно ищут lift ≥ 2.  
**🔗 См. также:** Support, Confidence, Apriori

---

#### Apriori algorithm
<small>📌 `A4.3.5`</small>

> Алгоритм поиска frequent itemsets для association rules. 6 шагов: thresholds → candidates → frequent → higher-order → rules → pruning.

**💡 Пример:** Market basket analysis у Walmart: Apriori нашёл правило про пиво/подгузники  
**⚠️ Common mistake:** Думают, что Apriori = single-step. Это итеративный 6-шаговый процесс.  
**🔗 См. также:** Support, Confidence, Lift

---


### Week 3: Evaluation

#### Model selection
<small>📌 `A4.3.10`</small>

> Выбор лучшего алгоритма + hyperparameters для задачи. 5 факторов: nature of problem, complexity, data, metrics, resources.

**💡 Пример:** Кредитный скоринг: сравнили LR, DT, RF через CV → выбрали RF  
**⚠️ Common mistake:** Выбирают модель по train accuracy — должны через cross-validation  
**🔗 См. также:** Cross-validation, Hyperparameter, Overfitting

---


### Week 4: ANN

#### Perceptron
<small>📌 `A4.3.8`</small>

> Один искусственный нейрон. Принимает inputs, умножает на weights, складывает с bias, применяет activation function.

**💡 Пример:** y = ReLU(x₁·w₁ + x₂·w₂ + b)  
**⚠️ Common mistake:** Думают, что perceptron = нейросеть. Perceptron — одна 'ячейка' сети.  
**🔗 См. также:** ANN, Activation function, Weight

---

#### Weight
<small>📌 `A4.3.8`</small>

> Параметр связи между нейронами, определяет важность сигнала. Учится через backpropagation.

**💡 Пример:** Между input x и hidden neuron weight w = 0.7 → x умножается на 0.7  
**⚠️ Common mistake:** Путают weight и bias. Weight — на input; bias — отдельная константа.  
**🔗 См. также:** Bias, Backpropagation, Activation

---

#### Bias
<small>📌 `A4.3.8`</small>

> Дополнительная константа, прибавляемая к weighted sum. Позволяет нейрону активироваться даже при нулевых inputs.

**💡 Пример:** y = ReLU(w·x + b) — bias смещает activation function влево/вправо  
**⚠️ Common mistake:** Путают с 'bias' в значении предвзятость (algorithmic bias) — это разные понятия!  
**🔗 См. также:** Weight, Activation function

---

#### Hidden layer
<small>📌 `A4.3.8`</small>

> Слой нейросети между input и output. Извлекает признаки. 'Hidden' = пользователь не видит его activations.

**💡 Пример:** ANN 784→128→64→10: два hidden layers (128 и 64 нейрона)  
**⚠️ Common mistake:** Думают, что больше hidden layers всегда лучше — может быть overfitting.  
**🔗 См. также:** Input layer, Output layer, Deep learning

---

#### Activation function
<small>📌 `A4.3.8`</small>

> Функция, применяемая к выходу нейрона. Вносит non-linearity, без неё сеть = линейная функция.

**💡 Пример:** ReLU, Sigmoid, Tanh, Softmax — выбор зависит от слоя/задачи  
**⚠️ Common mistake:** Используют Sigmoid в hidden layers — vanishing gradient проблема.  
**🔗 См. также:** ReLU, Sigmoid, Softmax

---

#### ReLU
<small>📌 `A4.3.8`</small>

> Rectified Linear Unit. ReLU(x) = max(0, x). Default activation для hidden layers — быстро вычисляется, нет vanishing gradient.

**💡 Пример:** Если weighted sum = -2 → ReLU выдаст 0; если +3 → выдаст 3  
**⚠️ Common mistake:** Используют ReLU в output layer для binary classification (нужен Sigmoid)  
**🔗 См. также:** Sigmoid, Softmax, Activation function

---

#### Sigmoid
<small>📌 `A4.3.8`</small>

> σ(x) = 1/(1 + e⁻ˣ). Output ∈ (0, 1). Используется в output binary classification как probability.

**💡 Пример:** Output 0.85 = 85% вероятность positive класса  
**⚠️ Common mistake:** Используют Sigmoid в deep hidden layers — vanishing gradient  
**🔗 См. также:** ReLU, Softmax, Binary classification

---

#### Softmax
<small>📌 `A4.3.8`</small>

> Преобразует logits в вероятности классов (sum = 1). Используется в output multi-class classification.

**💡 Пример:** 10 MNIST классов: softmax выдаёт [0.02, 0.01, ..., 0.85, ..., 0.03]  
**⚠️ Common mistake:** Используют Softmax для binary (можно — но проще Sigmoid с 1 нейроном)  
**🔗 См. также:** Sigmoid, Multi-class, Cross-entropy

---

#### Forward propagation
<small>📌 `A4.3.8`</small>

> Прохождение данных от input → hidden → output. На каждом узле: weighted sum + bias + activation.

**💡 Пример:** MNIST image (28×28) → flatten → Dense(128) → Dense(10) → softmax  
**⚠️ Common mistake:** Думают, что forward = обучение. Forward — только predict; обучение — backward.  
**🔗 См. также:** Backpropagation, Activation, Loss

---

#### Backpropagation
<small>📌 `A4.3.8`</small>

> Алгоритм обучения ANN. После forward pass: вычисляем error, propagate назад, рассчитываем gradients, обновляем weights.

**💡 Пример:** Loss = 0.8 → backprop вычисляет ∂Loss/∂w для каждого веса → SGD обновляет weights  
**⚠️ Common mistake:** Объясняют математически на IB — нужна КОНЦЕПЦИЯ, а не chain rule  
**🔗 См. также:** Forward propagation, Gradient descent, Loss function

---

#### Gradient descent
<small>📌 `A4.3.8`</small>

> Оптимизация: обновляем weights в направлении уменьшения loss. w_new = w_old - learning_rate · ∂L/∂w.

**💡 Пример:** SGD (Stochastic Gradient Descent) — обновление по mini-batch  
**⚠️ Common mistake:** Думают, что GD всегда находит global minimum — может застрять в local  
**🔗 См. также:** Backpropagation, Learning rate, SGD

---

#### Learning rate
<small>📌 `A4.3.8`</small>

> Hyperparameter: насколько большие шаги делает gradient descent. Обычно 0.001 - 0.01.

**💡 Пример:** lr = 0.001 → маленькие шаги, медленно но стабильно; lr = 1.0 → расходится  
**⚠️ Common mistake:** Большой LR ускоряет обучение — на деле может расходиться  
**🔗 См. также:** Gradient descent, Hyperparameter

---

#### Epoch
<small>📌 `A4.3.8`</small>

> Один полный проход через весь training dataset (forward + backward + weight update).

**💡 Пример:** MNIST 60K samples, batch=64 → 938 batches за 1 epoch  
**⚠️ Common mistake:** Путают epoch и iteration. Epoch = весь dataset; iteration = один batch.  
**🔗 См. также:** Batch size, Training loop

---

#### Loss function
<small>📌 `A4.3.8`</small>

> Функция, измеряющая отличие prediction от actual. Backprop минимизирует loss.

**💡 Пример:** MSE для regression; Cross-entropy для classification  
**⚠️ Common mistake:** Используют MSE для classification — должно быть cross-entropy  
**🔗 См. также:** Cross-entropy, MSE, Backpropagation

---


### Week 4: CNN

#### CNN
<small>📌 `A4.3.9`</small>

> Convolutional Neural Network. Использует convolution + pooling для извлечения spatial features. Стандарт для images.

**💡 Пример:** MNIST digit classification, ImageNet, face recognition  
**⚠️ Common mistake:** Используют ANN на изображениях — теряется spatial structure  
**🔗 См. также:** Convolutional layer, Kernel, Pooling

---

#### Convolutional layer
<small>📌 `A4.3.9`</small>

> Слой CNN, применяющий learnable kernels (filters) к input. Создаёт feature maps.

**💡 Пример:** Conv2D(32, (3,3)) — 32 фильтра размером 3×3  
**⚠️ Common mistake:** Думают, что kernels заранее заданы. Они учатся через backprop.  
**🔗 См. также:** Kernel, Feature map, CNN

---

#### Kernel (Filter)
<small>📌 `A4.3.9`</small>

> Маленькая матрица (3×3 или 5×5), скользящая по input. Каждый kernel детектирует свой признак (edge, texture).

**💡 Пример:** Sobel kernel детектирует вертикальные края: [[1,0,-1],[2,0,-2],[1,0,-1]]  
**⚠️ Common mistake:** Думают, что kernel один на сеть. Обычно 32-256 kernels per Conv layer.  
**🔗 См. также:** Convolutional layer, Feature map

---

#### Feature map
<small>📌 `A4.3.9`</small>

> Output convolution: 2D-карта, где каждый pixel показывает activation kernel в этой позиции.

**💡 Пример:** 10×10 input + 3×3 kernel (valid padding) → 8×8 feature map  
**⚠️ Common mistake:** Путают feature map и kernel. Kernel — фильтр; feature map — результат применения.  
**🔗 См. также:** Convolutional layer, Kernel

---

#### Pooling layer
<small>📌 `A4.3.9`</small>

> Уменьшает spatial dimensions feature map. Снижает вычислительную нагрузку + контролирует overfitting + translation invariance.

**💡 Пример:** MaxPool 2×2: 28×28 → 14×14  
**⚠️ Common mistake:** Применяют pooling к channels — pooling меняет height/width, не channels  
**🔗 См. также:** Max pooling, Average pooling

---

#### Max pooling
<small>📌 `A4.3.9`</small>

> Pooling берёт максимум из окна (например, 2×2). Сохраняет самые яркие признаки.

**💡 Пример:** Окно [[1,3],[4,2]] → max pool = 4  
**⚠️ Common mistake:** Думают, что max pooling = upsampling. Наоборот — downsampling.  
**🔗 См. также:** Pooling layer, Average pooling

---

#### Fully connected layer
<small>📌 `A4.3.9`</small>

> Каждый нейрон связан со всеми activations предыдущего слоя. Обычно в конце CNN для классификации.

**💡 Пример:** После Conv/Pool блоков: Flatten → Dense(128) → Dense(10) → softmax  
**⚠️ Common mistake:** Думают, что FC = только в ANN. CNN заканчиваются FC слоями для финальной classification.  
**🔗 См. также:** Dense layer, CNN

---

#### Spatial hierarchies
<small>📌 `A4.3.9`</small>

> Способность CNN автоматически учить иерархические признаки: early layers → edges, mid → shapes, deep → objects.

**💡 Пример:** Cat detector: layer 1 — края, layer 5 — глаза/уши, layer 10 — целая морда  
**⚠️ Common mistake:** Не упоминают точную формулировку 'spatial hierarchies' — маркер на полный балл в A4.3.9  
**🔗 См. также:** CNN, Deep learning, Feature learning

---


### Week 4: Regularization

#### Dropout
<small>📌 `A4.3.8`</small>

> Regularization техника: случайно 'выключаем' часть нейронов во время обучения. Борьба с overfitting.

**💡 Пример:** Dropout(0.3) — 30% нейронов случайно отключаются на каждом forward pass  
**⚠️ Common mistake:** Применяют dropout на inference — он только для training  
**🔗 См. также:** Overfitting, Regularization

---


### Week 5: RL

#### Agent
<small>📌 `A4.3.6`</small>

> Сущность, принимающая решения в RL. Действует в environment, наблюдает state, выбирает actions, получает rewards.

**💡 Пример:** Robot vacuum, AlphaGo, autonomous car AI, trading bot  
**⚠️ Common mistake:** Путают agent и model. Agent — система; model (Q-network) — её 'мозг'.  
**🔗 См. также:** Environment, State, Action, Reward

---

#### Environment
<small>📌 `A4.3.6`</small>

> Мир, в котором действует agent. Reagent на actions: даёт новый state и reward.

**💡 Пример:** Для AlphaGo — доска Go; для автомобиля — дорожная сеть  
**⚠️ Common mistake:** Думают, что environment всегда физический. Может быть виртуальным.  
**🔗 См. также:** Agent, State, Action

---

#### State
<small>📌 `A4.3.6`</small>

> Снимок environment в момент времени. То, что agent наблюдает для принятия решения.

**💡 Пример:** В Mario: позиция игрока, врагов, монеты, шкала жизней  
**⚠️ Common mistake:** Думают, что state = всё про мир. Это только observable часть.  
**🔗 См. также:** Agent, Environment, Action

---

#### Action
<small>📌 `A4.3.6`</small>

> Операция, которую agent может выполнить. Action space = все возможные actions.

**💡 Пример:** В Mario: {left, right, jump, fire}; в trading: {buy, sell, hold}  
**⚠️ Common mistake:** Думают, что action непрерывный. Может быть discrete (Mario) или continuous (руль).  
**🔗 См. также:** Agent, Action space

---

#### Reward
<small>📌 `A4.3.6`</small>

> Сигнал обратной связи от environment. Положительный = хорошо, отрицательный = плохо. Цель = max cumulative reward.

**💡 Пример:** +10 за монету, -100 за смерть, -0.1 за каждый шаг (поощряет короткие пути)  
**⚠️ Common mistake:** Reward design плохой → 'reward hacking' (agent эксплойтит непреднамеренно)  
**🔗 См. также:** Cumulative reward, Agent

---

#### Policy
<small>📌 `A4.3.6`</small>

> Стратегия agent: state → action. 'Если state X → делай action Y'. Стартует как random, обучается.

**💡 Пример:** Шахматный engine: 'если king атакован → защити или ходи им'  
**⚠️ Common mistake:** Думают, что policy = одно правило. Это полная функция от state space.  
**🔗 См. также:** Agent, State, Action, Q-learning

---

#### Q-learning
<small>📌 `A4.3.6`</small>

> RL алгоритм с Q-table[state][action] = expected reward. Update через Bellman equation.

**💡 Пример:** Frozen Lake: после многих эпизодов Q-table заполнится так, что agent дойдёт до цели  
**⚠️ Common mistake:** Применяют tabular Q-learning к большим state spaces (нужен DQN)  
**🔗 См. также:** Q-table, Bellman equation, DQN

---

#### Cumulative reward
<small>📌 `A4.3.6`</small>

> Сумма всех rewards за эпизод. Цель RL = максимизировать. Часто discounted (γ) для приоритета immediate rewards.

**💡 Пример:** За 100-шаговую игру: cumulative reward = +500 (агент собрал монеты, дошёл до цели)  
**⚠️ Common mistake:** Оптимизируют только immediate reward — нужен сumulative.  
**🔗 См. также:** Reward, Discount factor

---

#### Exploration vs exploitation
<small>📌 `A4.3.6`</small>

> Trade-off: пробовать новое (explore) vs использовать известное хорошее (exploit). Balance через epsilon-greedy.

**💡 Пример:** ε-greedy: с вероятностью 0.1 random action, с 0.9 — best known  
**⚠️ Common mistake:** Думают, что exploit лучше exploration — без exploration agent застрянет в local optimum.  
**🔗 См. также:** Epsilon-greedy, UCB, Q-learning

---

#### Epsilon-greedy
<small>📌 `A4.3.6`</small>

> Стратегия balance exploration/exploitation. С вероятностью ε — random action, иначе — best known.

**💡 Пример:** Старт ε=1.0 (pure exploration), decay до 0.05 (pure exploitation)  
**⚠️ Common mistake:** Используют постоянное ε — должно уменьшаться со временем (epsilon decay).  
**🔗 См. также:** Exploration, Q-learning

---


### Week 5: GA

#### Genetic algorithm
<small>📌 `A4.3.7`</small>

> Evolutionary algorithm: популяция решений эволюционирует через generations. 6 шагов: init, fitness, select, crossover, mutate, replace.

**💡 Пример:** TSP: 100 случайных маршрутов → 100 поколений → near-optimal solution  
**⚠️ Common mistake:** Путают GA с RL. RL — один agent учится; GA — популяция эволюционирует.  
**🔗 См. также:** Population, Fitness, Crossover, Mutation

---

#### Population
<small>📌 `A4.3.7`</small>

> Набор candidate solutions в GA. Эволюционирует через поколения.

**💡 Пример:** TSP с 100 случайных маршрутов на старте  
**⚠️ Common mistake:** Используют слишком маленькую population (10-20) — мало diversity  
**🔗 См. также:** Genetic algorithm, Generation

---

#### Fitness function
<small>📌 `A4.3.7`</small>

> Функция оценки 'хорошести' решения. Выше fitness = лучше решение.

**💡 Пример:** TSP: fitness = 1/total_distance (короче = лучше)  
**⚠️ Common mistake:** Думают, что fitness = loss. Fitness максимизируется, loss минимизируется.  
**🔗 См. также:** Genetic algorithm, Selection

---

#### Crossover
<small>📌 `A4.3.7`</small>

> Комбинирование двух parent solutions для создания offspring. Передаёт удачные traits.

**💡 Пример:** Parent 1: [A,B,C,D,E], Parent 2: [C,A,E,D,B] → Child: [A,B,C,E,D]  
**⚠️ Common mistake:** Думают, что crossover = просто copy от parent. Это смешивание частей обоих.  
**🔗 См. также:** Genetic algorithm, Mutation

---

#### Mutation
<small>📌 `A4.3.7`</small>

> Случайные изменения в offspring. Поддерживает diversity, предотвращает local optima.

**💡 Пример:** В route [A,B,C,D,E] swap двух городов → [A,D,C,B,E]  
**⚠️ Common mistake:** Большой mutation rate (>20%) → random search, GA теряет смысл  
**🔗 См. также:** Genetic algorithm, Crossover

---


### Week 5: Ethics

#### Accountability
<small>📌 `A4.4.1`</small>

> Кто несёт ответственность, когда AI ошибся? Developers, users, AI company, regulator?

**💡 Пример:** Tesla 2018: pedestrian killed by autonomous Uber → kто виноват? Driver/Uber/city?  
**⚠️ Common mistake:** Думают, что AI 'сам виноват'. AI — инструмент, accountability у людей.  
**🔗 См. также:** Algorithmic fairness, Ethics, Liability

---

#### Algorithmic fairness
<small>📌 `A4.4.1`</small>

> AI алгоритмы могут perpetuate biases → discriminatory outcomes в hiring, lending, justice.

**💡 Пример:** COMPAS recidivism algorithm — high false-positive для black defendants  
**⚠️ Common mistake:** Думают, что 'objective AI' = fair AI. Bias 'наследуется' из training data.  
**🔗 См. также:** Bias, COMPAS, Accountability

---

#### Bias (in ML)
<small>📌 `A4.4.1`</small>

> AI наследует biases из training data → дискриминирующие outcomes. Different from statistical bias.

**💡 Пример:** Amazon AI recruiting 2018: discriminated against women (trained on male-dominated resumes)  
**⚠️ Common mistake:** Путают technical bias (statistical) с social bias (discrimination).  
**🔗 См. также:** Algorithmic fairness, Training data

---

#### Privacy
<small>📌 `A4.4.1`</small>

> ML алгоритмы требуют огромных данных, часто personal. Issue: consent, surveillance, profiling.

**💡 Пример:** Netflix 2006: 'anonymized' данные de-anonymized через сопоставление с IMDb  
**⚠️ Common mistake:** Думают, что anonymization = privacy. Re-identification часто возможен.  
**🔗 См. также:** Anonymization, Consent, GDPR

---

#### COMPAS
<small>📌 `A4.4.1`</small>

> US recidivism algorithm. ProPublica 2016: black defendants получали higher false-positive rate. Classic bias case.

**💡 Пример:** Используется в Florida, Wisconsin судами для bail decisions  
**⚠️ Common mistake:** Думают, что COMPAS — единственный пример. Множество подобных проблем (banking, hiring).  
**🔗 См. также:** Algorithmic fairness, Bias, Accountability

---

#### Amazon AI recruiting (2018)
<small>📌 `A4.4.1`</small>

> Amazon свернул AI recruiter в 2018 — discriminated against women. Обучен на 10 годах male-dominated резюме.

**💡 Пример:** Алгоритм понижал резюме со словом 'women's' (e.g., 'women's chess club')  
**⚠️ Common mistake:** Думают, что AI создал bias. Bias был в данных — AI его 'наследовал'.  
**🔗 См. также:** Bias, Algorithmic fairness

---

#### Netflix de-anonymization (2006)
<small>📌 `A4.4.1`</small>

> Netflix release 'anonymized' dataset of user ratings. UT Austin re-identified users by matching with IMDb.

**💡 Пример:** User X с уникальной комбинацией ratings → matched с public IMDb profile  
**⚠️ Common mistake:** Думают, что privacy решает удаление имён. Re-identification возможен через unique patterns.  
**🔗 См. также:** Privacy, Anonymization

---

#### Informed consent
<small>📌 `A4.4.1`</small>

> User должен явно соглашаться на data collection AND понимать use. Required для medical, financial.

**💡 Пример:** GDPR Article 6: lawful basis для processing — consent один из 6  
**⚠️ Common mistake:** 'Click to accept terms' = НЕ informed consent. Информированность требует понимания.  
**🔗 См. также:** GDPR, Privacy, Data minimization

---

#### Transparency
<small>📌 `A4.4.1`</small>

> Видимость, как AI принимает решения. Особенно важно для high-stakes (medical, judicial, credit).

**💡 Пример:** EU AI Act требует transparency для high-risk AI systems  
**⚠️ Common mistake:** Путают transparency и explainability. Transparency — открытость; explainability — интерпретируемость.  
**🔗 См. также:** Explainability, GDPR Article 22

---

#### Explainability
<small>📌 `A4.4.1`</small>

> Способность объяснить, ПОЧЕМУ модель сделала такое предсказание. Critical для black-box моделей.

**💡 Пример:** LIME, SHAP — техники explainable AI; объясняют решение конкретного предсказания  
**⚠️ Common mistake:** Думают, что deep learning = всегда black box. Есть техники для interpretability.  
**🔗 См. также:** Transparency, LIME, SHAP

---


### Week 6: LLM

#### LLM
<small>📌 `Extended`</small>

> Large Language Model — глубокая нейросеть (transformer), обучена на терабайтах текста для понимания/генерации языка.

**💡 Пример:** GPT-4, Claude, Gemini, LLaMA — все LLMs  
**⚠️ Common mistake:** Думают, что LLM = новая парадигма ML. Это вариант ANN (transformer).  
**🔗 См. также:** Transformer, Attention, ANN

---

#### Transformer
<small>📌 `Extended`</small>

> Архитектура нейросети, основанная на self-attention. Стандарт для LLMs с 2017 (paper 'Attention is All You Need').

**💡 Пример:** GPT, BERT, T5 — все based on transformer  
**⚠️ Common mistake:** Путают transformer и RNN. Transformer — новее, parallelizable.  
**🔗 См. также:** Attention, LLM, Tokenization

---

#### Tokenization
<small>📌 `Extended`</small>

> Разбиение текста на tokens (≈ слова или sub-words). Первый шаг LLM pipeline.

**💡 Пример:** 'Machine learning' → ['Mach', 'ine', ' learn', 'ing'] (4 tokens у GPT-tokenizer)  
**⚠️ Common mistake:** Думают, что 1 token = 1 word. Tokens могут быть sub-words или characters.  
**🔗 См. также:** LLM, Embeddings

---

#### Attention
<small>📌 `Extended`</small>

> Механизм, который определяет, какие tokens 'обращают внимание' друг на друга. Сердце transformer.

**💡 Пример:** В предложении 'The cat sat on the mat' — attention связывает 'sat' с 'cat' и 'mat'  
**⚠️ Common mistake:** Думают, что attention тратит память — да, O(n²) от длины контекста  
**🔗 См. также:** Transformer, Self-attention

---

#### Hallucinations
<small>📌 `Extended`</small>

> LLM выдаёт confidently incorrect или fabricated info. Critical limitation.

**💡 Пример:** ChatGPT выдумывает несуществующие книги с реалистичными названиями  
**⚠️ Common mistake:** Думают, что hallucinations = bugs. Это fundamental свойство next-token prediction.  
**🔗 См. также:** RAG, LLM, Fine-tuning

---

#### RAG
<small>📌 `Extended`</small>

> Retrieval-Augmented Generation. Pattern: query → search retrieves docs → docs + query → LLM. Уменьшает hallucinations.

**💡 Пример:** ChatGPT с web search = базовый RAG  
**⚠️ Common mistake:** Путают RAG и fine-tuning. RAG даёт docs в context; fine-tuning меняет weights.  
**🔗 См. также:** LLM, Fine-tuning, Hallucinations

---

#### Prompt engineering
<small>📌 `Extended`</small>

> Подбор удачных prompts для готовой LLM. Не меняет модель, но влияет на output.

**💡 Пример:** Zero-shot, few-shot, chain-of-thought — стратегии prompting  
**⚠️ Common mistake:** Думают, что prompt engineering = fine-tuning. Prompt engineering не меняет model.  
**🔗 См. также:** LLM, Fine-tuning, Zero-shot

---

#### Fine-tuning
<small>📌 `Extended`</small>

> Дополнительное обучение pre-trained модели на specific domain. $1K-$10K, средняя сложность.

**💡 Пример:** GPT-3.5 fine-tuned на медицинских документах → 'MedGPT'  
**⚠️ Common mistake:** Путают с RAG. Fine-tuning меняет weights модели; RAG только добавляет контекст.  
**🔗 См. также:** LLM, Transfer learning, RAG

---


### Week 6: Regulations

#### GDPR
<small>📌 `Extended`</small>

> General Data Protection Regulation (EU, 2018). Строгие правила обработки personal data. Штрафы до €20M или 4% оборота.

**💡 Пример:** Meta получил €1.2 млрд штраф в 2023 за нарушение GDPR  
**⚠️ Common mistake:** Думают, что GDPR только в EU. Применяется ко ВСЕМ компаниям, обрабатывающим данные жителей EU.  
**🔗 См. также:** Right to explanation, Privacy, EU AI Act

---

#### EU AI Act (2024)
<small>📌 `Extended`</small>

> Первый мировой закон об AI. Делит на 4 уровня риска: unacceptable / high / limited / minimal. Штрафы до €35M.

**💡 Пример:** Social scoring (China-style) — UNACCEPTABLE и запрещён в EU  
**⚠️ Common mistake:** Думают, что AI Act только про high-risk. Все уровни регулируются по-разному.  
**🔗 См. также:** GDPR, Algorithmic fairness

---

#### Right to explanation
<small>📌 `Extended`</small>

> GDPR Article 22: user имеет право на объяснение automated decisions.

**💡 Пример:** Если AI отказал в кредите — банк ОБЯЗАН объяснить причину  
**⚠️ Common mistake:** Думают, что 'AI решил' — достаточное объяснение. Нет, нужно reasoning.  
**🔗 См. также:** GDPR, Explainability, Transparency

---


### Week 6: IB

#### TOK (Theory of Knowledge)
<small>📌 `Extended`</small>

> Обязательный компонент IB. Философские вопросы о природе знания. На CS — встраивайте в Discuss ответы для бонусных баллов.

**💡 Пример:** TOK question: 'Can AI truly know something or only process patterns?'  
**⚠️ Common mistake:** Не используют TOK-связки в ответах — теряют 1-2 балла на extended responses.  
**🔗 См. также:** IB, Discuss, Evaluate

---


## 📝 Лицензия

Этот глоссарий — часть курса IB CS ML. Свободно используйте для подготовки.

**Источники:**
- Baumgarten, P., Ganea, F., Turland, M. (2024). *Computer Science for the IB Diploma*. Hodder Education.
- MacKenty, D., Stephenson, K. (2025). *Computer Science*. Oxford University Press.
- IB Computer Science Subject Guide (first exams 2027).
