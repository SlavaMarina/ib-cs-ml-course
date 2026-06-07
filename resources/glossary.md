# 📖 Glossary — Complete IB CS ML Term Reference

> 110+ key terms with definitions, examples, and common mistakes.
> Sources: Baumgarten (Hodder 2024), MacKenty & Stephenson (Oxford 2025), and the new IB syllabus for first exams in 2027.

---

## 🔤 How to use this glossary

- Use the **alphabetical index** below for quick lookup.
- Use the **week/topic sections** for revision after each lesson.
- Each entry gives a short **definition**, an **example**, a **common mistake**, and useful **see also** links.

---

## 🔠 Alphabetical Index

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
**N** · [Netflix de-anonymisation (2006)](#netflix-de-anonymisation-2006)  [Normalisation](#normalisation)  [NPU](#npu)  
**O** · [Outlier](#outlier)  [Overfitting](#overfitting)  
**P** · [Perceptron](#perceptron)  [Policy](#policy)  [Pooling layer](#pooling-layer)  [Population](#population)  [Precision](#precision)  [Privacy](#privacy)  [Prompt engineering](#prompt-engineering)  [Pruning](#pruning)  
**Q** · [Q-learning](#q-learning)  
**R** · [RAG](#rag)  [Recall](#recall)  [Reinforcement learning](#reinforcement-learning)  [ReLU](#relu)  [Reward](#reward)  [Right to explanation](#right-to-explanation)  [R² (R-squared)](#r2-r-squared)  
**S** · [Sigmoid](#sigmoid)  [Silhouette score](#silhouette-score)  [Slope](#slope)  [Softmax](#softmax)  [Spatial hierarchies](#spatial-hierarchies)  [Spectral clustering](#spectral-clustering)  [State](#state)  [Supervised learning](#supervised-learning)  [Support](#support)  
**T** · [TOK (Theory of Knowledge)](#tok-theory-of-knowledge)  [Tokenisation](#tokenisation)  [TPU](#tpu)  [Transfer learning](#transfer-learning)  [Transformer](#transformer)  [Transparency](#transparency)  
**U** · [Unsupervised learning](#unsupervised-learning)  
**W** · [Weight](#weight)  [Wrapper method](#wrapper-method)  

---

## 📚 By Course Week

### Week 1: Fundamentals

#### Supervised learning
<small>📌 `A4.1.1`</small>

> An ML paradigm where a model is trained on labelled data, usually input-output pairs, so it can predict outputs for new inputs.

**💡 Example:** An email spam classifier learns from pairs such as `(email, spam/not spam)` and classifies new emails.  
**⚠️ Common mistake:** Confusing it with unsupervised learning in classic scenario questions.  
**🔗 See also:** Unsupervised learning, Classification, Regression

---

#### Unsupervised learning
<small>📌 `A4.1.1`</small>

> An ML paradigm for finding patterns in unlabelled data, such as clusters or association rules.

**💡 Example:** Market segmentation groups customers without being given the customer categories in advance.  
**⚠️ Common mistake:** Thinking the algorithm needs at least some labels.  
**🔗 See also:** Supervised learning, Clustering, Association rules

---

#### Reinforcement learning
<small>📌 `A4.1.1 / A4.3.6`</small>

> An ML paradigm where an agent learns by interacting with an environment, receiving rewards or penalties, and trying to maximise cumulative reward.

**💡 Example:** AlphaGo improves by playing Go and receiving a positive result for winning and a negative result for losing.  
**⚠️ Common mistake:** Mixing it up with genetic algorithms: RL usually has one learning agent; GA evolves a population.  
**🔗 See also:** Agent, Reward, Q-learning

---

#### Deep learning
<small>📌 `A4.1.1`</small>

> A subset of ML that uses deep neural networks with multiple hidden layers to learn hierarchical representations automatically.

**💡 Example:** In a CNN for face recognition, early layers detect edges and later layers detect more complex facial features.  
**⚠️ Common mistake:** Treating any neural network as deep learning; deep learning needs several layers.  
**🔗 See also:** ANN, CNN, Hidden layer

---

#### Transfer learning
<small>📌 `A4.1.1`</small>

> Reusing a pre-trained model for a new but related task, saving training time and reducing the amount of data needed.

**💡 Example:** Fine-tuning an ImageNet-pre-trained ResNet on 1000 photos of a new animal class.  
**⚠️ Common mistake:** Thinking transfer learning is only using a ready-made model; it usually involves adaptation or fine-tuning.  
**🔗 See also:** Fine-tuning, Pre-trained model

---

### Week 1: Hardware

#### CPU
<small>📌 `A4.1.2`</small>

> Central Processing Unit: the main processor in a computer. It has a small number of flexible cores and is optimised for sequential tasks.

**💡 Example:** Intel Core i7 and AMD Ryzen processors often have 6-16 general-purpose cores.  
**⚠️ Common mistake:** Thinking CPUs cannot be used for ML. They can, but are slower for many parallel ML workloads.  
**🔗 See also:** GPU, TPU, Parallel processing

---

#### GPU
<small>📌 `A4.1.2`</small>

> Graphics Processing Unit: a processor with many parallel cores, well suited to matrix operations and neural network training.

**💡 Example:** NVIDIA RTX 4090 or A100 GPUs are used to train neural networks much faster than CPUs.  
**⚠️ Common mistake:** Thinking a GPU is always better; it is poor for many sequential tasks.  
**🔗 See also:** CPU, TPU, CUDA

---

#### TPU
<small>📌 `A4.1.2`</small>

> Tensor Processing Unit: a Google ASIC designed for tensor operations such as matrix multiplication, especially in TensorFlow workloads.

**💡 Example:** Google uses TPU pods for large-scale deep learning training.  
**⚠️ Common mistake:** Confusing TPU with GPU. A TPU is more specialised and is not for graphics.  
**🔗 See also:** GPU, ASIC, Google Cloud

---

#### NPU
<small>📌 `A4.1.2`</small>

> Neural Processing Unit: a chip optimised for ML inference on edge devices such as phones, laptops, and IoT devices.

**💡 Example:** Apple Neural Engine processes Face ID and some Siri tasks locally on an iPhone.  
**⚠️ Common mistake:** Treating NPU and TPU as the same thing. NPUs are mainly for edge inference; TPUs are mainly for large cloud workloads.  
**🔗 See also:** Edge computing, Inference

---

#### ASIC
<small>📌 `A4.1.2`</small>

> Application-Specific Integrated Circuit: a chip designed for one specific task, giving very high efficiency.

**💡 Example:** Tesla FSD chips are ASICs for self-driving inference; Google TPUs are ASICs for ML workloads.  
**⚠️ Common mistake:** Calling an ASIC a general-purpose chip. It is the opposite: specialised.  
**🔗 See also:** TPU, FPGA, NPU

---

#### FPGA
<small>📌 `A4.1.2`</small>

> Field-Programmable Gate Array: a reprogrammable chip, giving flexibility between fixed ASICs and general-purpose CPUs.

**💡 Example:** Microsoft has used FPGAs to accelerate search ranking.  
**⚠️ Common mistake:** Confusing FPGA with ASIC. An FPGA can be reprogrammed; an ASIC cannot.  
**🔗 See also:** ASIC, Custom hardware

---

#### Edge computing
<small>📌 `A4.1.2`</small>

> Running ML inference locally on or near the device that produces the data, instead of sending everything to the cloud.

**💡 Example:** A smart doorbell recognises faces on the device, so images do not need to leave the home.  
**⚠️ Common mistake:** Thinking edge means only mobile phones. Any non-cloud device can be an edge device.  
**🔗 See also:** Cloud computing, NPU, Inference

---

### Week 1: Preprocessing

#### Data cleaning
<small>📌 `A4.2.1`</small>

> Finding and fixing, removing, or replacing corrupted, incomplete, duplicated, or invalid records.

**💡 Example:** Removing duplicates, filling missing values, and standardising date formats.  
**⚠️ Common mistake:** Thinking cleaning only means removing missing values.  
**🔗 See also:** Missing values, Outlier, Normalisation

---

#### Outlier
<small>📌 `A4.2.1`</small>

> An unusual value that is very different from most other data points. It may be an error or an important signal.

**💡 Example:** In a salary dataset, 500K when the average is 50K may be an outlier.  
**⚠️ Common mistake:** Always deleting outliers; sometimes they matter, such as in fraud detection.  
**🔗 See also:** IQR method, Z-score

---

#### IQR method
<small>📌 `A4.2.1`</small>

> A method for detecting outliers using the interquartile range. A value is an outlier if it is outside `[Q1 - 1.5·IQR, Q3 + 1.5·IQR]`.

**💡 Example:** In a boxplot, points beyond the whiskers are often IQR outliers.  
**⚠️ Common mistake:** Applying IQR blindly to all distributions; some data need different methods.  
**🔗 See also:** Outlier, Z-score, Boxplot

---

#### Mean imputation
<small>📌 `A4.2.1`</small>

> Replacing missing values with the mean of the column. It is simple, but can introduce bias.

**💡 Example:** If 10% of ages are missing, replace them with the mean age, such as 35.  
**⚠️ Common mistake:** Using it for categorical data, or using the mean when the median would handle outliers better.  
**🔗 See also:** Missing values, Median imputation

---

#### Normalisation
<small>📌 `A4.2.1`</small>

> Scaling features to a comparable range. This is important for distance-based algorithms such as KNN and for neural networks.

**💡 Example:** MinMaxScaler maps values to `[0, 1]`; StandardScaler maps them to mean 0 and standard deviation 1.  
**⚠️ Common mistake:** Forgetting to normalise before KNN, so large-range features dominate the distance.  
**🔗 See also:** StandardScaler, MinMaxScaler, KNN

---

### Week 2: Preprocessing

#### Feature selection
<small>📌 `A4.2.2`</small>

> Choosing only the relevant features for training. It can improve accuracy, reduce overfitting, and speed up training.

**💡 Example:** From 100 features, keep the 20 most strongly related to the target.  
**⚠️ Common mistake:** Applying feature selection after dimensionality reduction; selection normally comes first.  
**🔗 See also:** Filter method, Wrapper method, Embedded method

---

#### Filter method
<small>📌 `A4.2.2`</small>

> Feature selection using statistical measures such as Pearson correlation or chi-square. It is fast, but ignores feature interactions.

**💡 Example:** Keep features with `|r| > 0.3` against the target.  
**⚠️ Common mistake:** Thinking a filter method understands interactions; it ranks features independently.  
**🔗 See also:** Wrapper method, Embedded method

---

#### Wrapper method
<small>📌 `A4.2.2`</small>

> Feature selection by repeatedly training a model on different feature subsets. It is often more accurate, but slower.

**💡 Example:** Recursive Feature Elimination (RFE) removes the least useful features step by step.  
**⚠️ Common mistake:** Using it on very large datasets without considering the training cost.  
**🔗 See also:** Filter method, Embedded method

---

#### Embedded method
<small>📌 `A4.2.2`</small>

> Feature selection built into model training, such as Lasso regularisation or tree-based feature importance.

**💡 Example:** Random Forest `feature_importances_` gives a ranking of useful features.  
**⚠️ Common mistake:** Mixing embedded and wrapper methods. Embedded selection happens inside the model.  
**🔗 See also:** Lasso, Random Forest, Filter method

---

#### Dimensionality reduction
<small>📌 `A4.2.3`</small>

> Reducing the number of features while keeping as much information as possible. It helps with the curse of dimensionality.

**💡 Example:** PCA turns 100 correlated features into 10 orthogonal components.  
**⚠️ Common mistake:** Confusing it with feature selection. Reduction creates new features; selection keeps existing ones.  
**🔗 See also:** PCA, Feature selection, Curse of dimensionality

---

#### Curse of dimensionality
<small>📌 `A4.2.3`</small>

> As the number of dimensions grows, data becomes sparse and distance-based algorithms become less useful.

**💡 Example:** KNN often performs badly with 1000 features because all points can seem similarly far away.  
**⚠️ Common mistake:** Assuming more features always help. They often hurt without selection or reduction.  
**🔗 See also:** KNN, Dimensionality reduction

---

### Week 2: Algorithms

#### Linear regression
<small>📌 `A4.3.1`</small>

> A supervised regression algorithm. `Y = β₀ + β₁X + ε`. It finds the best straight line for predicting a continuous output.

**💡 Example:** Predicting house price from area: `price = 30000 + 1500·area`.  
**⚠️ Common mistake:** Using it for classification or for strongly non-linear relationships.  
**🔗 See also:** Slope, Intercept, R²

---

#### Slope
<small>📌 `A4.3.1`</small>

> The coefficient `β₁` in `Y = β₀ + β₁X`. It shows how much `Y` changes when `X` increases by 1.

**💡 Example:** If slope = 1500, then +1 square metre adds about $1500 to the predicted house price.  
**⚠️ Common mistake:** Confusing slope and intercept. Slope is the rate of change; intercept is the value when `X = 0`.  
**🔗 See also:** Intercept, Linear regression

---

#### Intercept
<small>📌 `A4.3.1`</small>

> The coefficient `β₀` in `Y = β₀ + β₁X`. It is the predicted value of `Y` when `X = 0`.

**💡 Example:** If intercept = 30000, a house with area 0 would theoretically be predicted at $30000.  
**⚠️ Common mistake:** Interpreting the intercept literally when `X = 0` has no real meaning.  
**🔗 See also:** Slope, Linear regression

---

#### R² (R-squared)
<small>📌 `A4.3.1`</small>

> Coefficient of determination. `R² = 1 - SS_res/SS_tot`. It is the proportion of variance in `Y` explained by the model.

**💡 Example:** `R² = 0.85` means the model explains about 85% of the variation in the data.  
**⚠️ Common mistake:** Treating very high R² as always good; it can also be a sign of overfitting.  
**🔗 See also:** Linear regression, Overfitting

---

#### KNN
<small>📌 `A4.3.2`</small>

> K-Nearest Neighbours: a classification or regression algorithm. Prediction is based on the majority vote or average of the K nearest labelled examples.

**💡 Example:** Classifying an iris flower by looking at the 5 nearest labelled flowers.  
**⚠️ Common mistake:** Forgetting to normalise data before KNN.  
**🔗 See also:** K (parameter), Euclidean distance, Normalisation

---

#### Decision Tree
<small>📌 `A4.3.2`</small>

> A tree of if-else rules. Each internal node asks a feature question; each leaf gives a prediction.

**💡 Example:** Loan decision: age > 25, then income > 50K, then approve.  
**⚠️ Common mistake:** Not controlling `max_depth`, so the tree memorises training data.  
**🔗 See also:** Gini impurity, Pruning, Random Forest

---

#### Gini impurity
<small>📌 `A4.3.2`</small>

> A measure of how mixed a decision-tree node is. `0` means one pure class; higher values mean more mixed classes.

**💡 Example:** A node with 80% class A and 20% class B has `Gini = 1 - 0.8² - 0.2² = 0.32`.  
**⚠️ Common mistake:** Confusing it with entropy. They are different metrics with a similar purpose.  
**🔗 See also:** Decision Tree, Entropy

---

#### Pruning
<small>📌 `A4.3.2`</small>

> Cutting branches from a decision tree to reduce overfitting.

**💡 Example:** After training, remove branches that add little validation accuracy.  
**⚠️ Common mistake:** Thinking pruning makes the model more complex; it usually simplifies it.  
**🔗 See also:** Decision Tree, Overfitting, max_depth

---

### Week 2: Tuning

#### Hyperparameter
<small>📌 `A4.3.3`</small>

> A value set before training that controls algorithm behaviour. It is not learned from the data.

**💡 Example:** `K` in KNN, `max_depth` in a decision tree, or `learning_rate` in a neural network.  
**⚠️ Common mistake:** Confusing hyperparameters with parameters such as weights. You set hyperparameters; the model learns parameters.  
**🔗 See also:** Grid search, Cross-validation

---

#### Cross-validation
<small>📌 `A4.3.3`</small>

> Splitting data into K folds. The model trains K times, each time testing on a different fold, then averages the results.

**💡 Example:** In 5-fold CV, train on 4 parts and test on 1 part, repeating until each part has been the test fold.  
**⚠️ Common mistake:** Using CV but never keeping a final holdout test set.  
**🔗 See also:** Hyperparameter, Holdout, Stratified

---

### Week 2: Metrics

#### Confusion matrix
<small>📌 `A4.3.3`</small>

> A table of true positives, false positives, false negatives, and true negatives for classification.

**💡 Example:** A spam filter may have 80 TP, 10 FP, 20 FN, and 90 TN on 200 emails.  
**⚠️ Common mistake:** Mixing up actual and predicted axes. A common convention is rows = actual, columns = predicted.  
**🔗 See also:** Precision, Recall, F1

---

#### Accuracy
<small>📌 `A4.3.3`</small>

> The proportion of correct predictions. `Accuracy = (TP + TN) / (TP + TN + FP + FN)`.

**💡 Example:** 180 correct predictions out of 200 emails gives 90% accuracy.  
**⚠️ Common mistake:** Using accuracy with class imbalance, where it can give a false sense of model quality.  
**🔗 See also:** Precision, Recall, F1, Class imbalance

---

#### Precision
<small>📌 `A4.3.3`</small>

> Of all predicted positive cases, how many are actually positive. `P = TP / (TP + FP)`.

**💡 Example:** 80 TP out of 90 predicted positives gives precision of 89%. It matters when false positives are costly.  
**⚠️ Common mistake:** Confusing it with recall. Precision measures the quality of positive predictions.  
**🔗 See also:** Recall, F1, False Positive

---

#### Recall
<small>📌 `A4.3.3`</small>

> Of all actual positive cases, how many the model found. `R = TP / (TP + FN)`.

**💡 Example:** In cancer screening, finding 90 out of 95 actual cases gives recall of about 95%.  
**⚠️ Common mistake:** Confusing it with precision. Recall measures how complete the positive detection is.  
**🔗 See also:** Precision, F1, False Negative

---

#### F1 Score
<small>📌 `A4.3.3`</small>

> The harmonic mean of precision and recall. `F1 = 2·P·R / (P + R)`. It is useful with class imbalance.

**💡 Example:** `P = 0.89`, `R = 0.80` gives `F1 ≈ 0.84`.  
**⚠️ Common mistake:** Thinking F1 is the arithmetic mean `(P + R) / 2`; it is harmonic.  
**🔗 See also:** Precision, Recall, Class imbalance

---

### Week 2: General

#### Overfitting
<small>📌 `A4.3.10`</small>

> A model has memorised details of the training data and performs poorly on new data. Train accuracy is much higher than test accuracy.

**💡 Example:** A decision tree with `max_depth=None` gets 100% train accuracy but 60% test accuracy.  
**⚠️ Common mistake:** Looking only at low test accuracy. The key sign is the gap between train and test performance.  
**🔗 See also:** Underfitting, Cross-validation, Regularisation

---

### Week 3: Unsupervised

#### Clustering
<small>📌 `A4.3.4`</small>

> An unsupervised technique that groups points so items inside a cluster are similar and items in different clusters are different.

**💡 Example:** Customer segmentation into low-value, medium-value, and high-value groups without predefined labels.  
**⚠️ Common mistake:** Applying it to labelled prediction tasks; those need classification.  
**🔗 See also:** K-means, DBSCAN, Centroid

---

#### K-means
<small>📌 `A4.3.4`</small>

> A clustering algorithm: initialise K centroids, assign points to the nearest centroid, recalculate centroids, and repeat.

**💡 Example:** `K = 3` for customer segmentation, often converging after 10-20 iterations.  
**⚠️ Common mistake:** Applying it to non-spherical clusters, where DBSCAN may be better.  
**🔗 See also:** Centroid, Elbow method, DBSCAN

---

#### Centroid
<small>📌 `A4.3.4`</small>

> The centre of a cluster, calculated as the mean coordinates of all points in the cluster. Used in K-means.

**💡 Example:** Points `(1,2)`, `(3,4)`, `(5,6)` have centroid `(3,4)`.  
**⚠️ Common mistake:** Confusing centroid and medoid. A centroid is a mean; a medoid is a real data point.  
**🔗 See also:** K-means, Cluster

---

#### Elbow method
<small>📌 `A4.3.4`</small>

> A method for choosing K in K-means by plotting inertia against K and looking for the point where improvement slows sharply.

**💡 Example:** In retail data, an elbow at `K = 4` suggests four clusters.  
**⚠️ Common mistake:** Thinking there is always one objective K. The elbow can be ambiguous.  
**🔗 See also:** K-means, Silhouette score

---

#### Silhouette score
<small>📌 `A4.3.4`</small>

> A clustering quality metric from -1 to 1. Higher values mean clusters are more compact and better separated.

**💡 Example:** `0.7` is strong, `0.3` is weak, and a negative score suggests poor assignment.  
**⚠️ Common mistake:** Trusting only the elbow method. Use elbow and silhouette together when possible.  
**🔗 See also:** K-means, Elbow method

---

#### DBSCAN
<small>📌 `A4.3.4`</small>

> Density-Based Spatial Clustering. It finds clusters of any shape, does not require K, and marks outliers as noise.

**💡 Example:** Clustering GPS points on a map can reveal road-shaped groups rather than spheres.  
**⚠️ Common mistake:** Using it on data with very different densities, where one `eps` value may not work.  
**🔗 See also:** Epsilon, minPts, K-means

---

#### Epsilon (ε)
<small>📌 `A4.3.4`</small>

> The DBSCAN radius used to search for a point's neighbours.

**💡 Example:** `ε = 0.5` means points within radius 0.5 count as neighbours.  
**⚠️ Common mistake:** Choosing ε by guesswork. A k-distance plot is a better method.  
**🔗 See also:** DBSCAN, minPts

---

#### minPts
<small>📌 `A4.3.4`</small>

> The DBSCAN minimum number of neighbours inside radius ε needed to form a core point.

**💡 Example:** `minPts = 5` means at least 5 nearby points are needed for a core point.  
**⚠️ Common mistake:** Choosing `minPts = 2`, which often creates noisy clusters.  
**🔗 See also:** DBSCAN, Epsilon, Core point

---

#### Hierarchical clustering
<small>📌 `A4.3.4`</small>

> Clustering that builds a tree, or dendrogram, either bottom-up by merging clusters or top-down by splitting them.

**💡 Example:** Biological taxonomy is a hierarchy of related species.  
**⚠️ Common mistake:** Using it on very large datasets without considering its high computational cost.  
**🔗 See also:** Dendrogram, K-means, Linkage

---

#### Dendrogram
<small>📌 `A4.3.4`</small>

> A tree diagram for hierarchical clustering. Cutting the tree at a chosen height gives a chosen number of clusters.

**💡 Example:** A language tree may show English closer to German than to Japanese.  
**⚠️ Common mistake:** Reading the horizontal order as important. The height represents dissimilarity.  
**🔗 See also:** Hierarchical clustering

---

#### Spectral clustering
<small>📌 `A4.3.4`</small>

> Clustering based on graph theory and eigenvectors of a similarity matrix. Useful for non-linearly separable data.

**💡 Example:** Clustering a social network by people who share many friends.  
**⚠️ Common mistake:** Going too deep into the maths for IB; know the idea and use case.  
**🔗 See also:** K-means, DBSCAN

---

#### Association rule mining
<small>📌 `A4.3.5`</small>

> Finding co-occurrence patterns in transactional data, often used in market basket analysis.

**💡 Example:** Customers who buy coffee may also buy biscuits, with `lift = 2.5`.  
**⚠️ Common mistake:** Treating an association rule as causation. It is correlation, not proof of cause.  
**🔗 See also:** Apriori, Support, Confidence, Lift

---

#### Support
<small>📌 `A4.3.5`</small>

> The proportion of transactions containing an itemset. `Support({A,B}) = transactions with A and B / all transactions`.

**💡 Example:** If 50 of 1000 receipts contain `{bread, milk}`, support is 0.05.  
**⚠️ Common mistake:** Treating support as conditional probability. It is not conditional.  
**🔗 See also:** Confidence, Lift, Apriori

---

#### Confidence
<small>📌 `A4.3.5`</small>

> Conditional probability for a rule: if A is bought, B is also bought. `Confidence(A→B) = Support({A,B}) / Support({A})`.

**💡 Example:** If 100 customers buy bread and 50 of them also buy milk, `Confidence(bread→milk) = 0.5`.  
**⚠️ Common mistake:** Assuming high confidence always means a useful rule; check lift as well.  
**🔗 See also:** Support, Lift, Apriori

---

#### Lift
<small>📌 `A4.3.5`</small>

> The strength of an association compared with random chance. `Lift(A→B) = Confidence(A→B) / Support({B})`.

**💡 Example:** `Lift(coffee→biscuits) = 3.0` means biscuits are bought three times more often with coffee than usual.  
**⚠️ Common mistake:** Treating `lift = 1.1` as strong. Strong rules often need a higher lift, such as 2 or more.  
**🔗 See also:** Support, Confidence, Apriori

---

#### Apriori algorithm
<small>📌 `A4.3.5`</small>

> An algorithm for finding frequent itemsets and association rules: set thresholds, create candidates, keep frequent itemsets, build rules, and prune.

**💡 Example:** Market basket analysis can use Apriori to find rules between products.  
**⚠️ Common mistake:** Thinking Apriori is a single-step algorithm; it is iterative.  
**🔗 See also:** Support, Confidence, Lift

---

### Week 3: Evaluation

#### Model selection
<small>📌 `A4.3.10`</small>

> Choosing the best algorithm and hyperparameters for a task, based on problem type, complexity, data, metrics, and resources.

**💡 Example:** For credit scoring, compare logistic regression, decision trees, and random forests with cross-validation.  
**⚠️ Common mistake:** Choosing a model by training accuracy instead of validation or cross-validation performance.  
**🔗 See also:** Cross-validation, Hyperparameter, Overfitting

---

### Week 4: ANN

#### Perceptron
<small>📌 `A4.3.8`</small>

> One artificial neuron. It takes inputs, multiplies them by weights, adds a bias, and applies an activation function.

**💡 Example:** `y = ReLU(x₁·w₁ + x₂·w₂ + b)`.  
**⚠️ Common mistake:** Calling a perceptron a full neural network. It is one unit inside a network.  
**🔗 See also:** ANN, Activation function, Weight

---

#### Weight
<small>📌 `A4.3.8`</small>

> A learned connection parameter between neurons that controls the importance of a signal.

**💡 Example:** If input `x` connects to a hidden neuron with weight `w = 0.7`, the input is multiplied by 0.7.  
**⚠️ Common mistake:** Confusing weight and bias. A weight is attached to an input; bias is an added constant.  
**🔗 See also:** Bias, Backpropagation, Activation

---

#### Bias
<small>📌 `A4.3.8`</small>

> An extra constant added to the weighted sum, allowing a neuron to activate even when inputs are zero.

**💡 Example:** In `y = ReLU(w·x + b)`, bias shifts the activation function left or right.  
**⚠️ Common mistake:** Confusing neural-network bias with social or algorithmic bias. They are different ideas.  
**🔗 See also:** Weight, Activation function

---

#### Hidden layer
<small>📌 `A4.3.8`</small>

> A neural-network layer between input and output. It extracts features; it is "hidden" because users do not directly see its activations.

**💡 Example:** ANN `784→128→64→10` has two hidden layers: 128 and 64 neurons.  
**⚠️ Common mistake:** Assuming more hidden layers always help; they can also cause overfitting.  
**🔗 See also:** Input layer, Output layer, Deep learning

---

#### Activation function
<small>📌 `A4.3.8`</small>

> A function applied to a neuron's output. It adds non-linearity; without it, the whole network behaves like a linear function.

**💡 Example:** ReLU, sigmoid, tanh, and softmax are common activation functions.  
**⚠️ Common mistake:** Using sigmoid in deep hidden layers, which can cause vanishing gradients.  
**🔗 See also:** ReLU, Sigmoid, Softmax

---

#### ReLU
<small>📌 `A4.3.8`</small>

> Rectified Linear Unit. `ReLU(x) = max(0, x)`. It is a common default activation for hidden layers.

**💡 Example:** If weighted sum is -2, ReLU returns 0; if it is +3, ReLU returns 3.  
**⚠️ Common mistake:** Using ReLU in the output layer for binary classification, where sigmoid is usually needed.  
**🔗 See also:** Sigmoid, Softmax, Activation function

---

#### Sigmoid
<small>📌 `A4.3.8`</small>

> `σ(x) = 1/(1 + e⁻ˣ)`. The output is between 0 and 1, so it is useful for binary classification probabilities.

**💡 Example:** Output `0.85` means an estimated 85% probability for the positive class.  
**⚠️ Common mistake:** Using sigmoid in deep hidden layers, where vanishing gradients can slow learning.  
**🔗 See also:** ReLU, Softmax, Binary classification

---

#### Softmax
<small>📌 `A4.3.8`</small>

> Converts logits into class probabilities that sum to 1. Used in multi-class classification output layers.

**💡 Example:** For 10 MNIST classes, softmax may output `[0.02, 0.01, ..., 0.85, ..., 0.03]`.  
**⚠️ Common mistake:** Using softmax for binary classification when sigmoid with one output neuron is simpler.  
**🔗 See also:** Sigmoid, Multi-class, Cross-entropy

---

#### Forward propagation
<small>📌 `A4.3.8`</small>

> Passing data from input to hidden layers to output. At each neuron: weighted sum, bias, activation.

**💡 Example:** MNIST image `(28×28)` → flatten → Dense(128) → Dense(10) → softmax.  
**⚠️ Common mistake:** Thinking forward propagation is training. It is prediction; training also needs backpropagation.  
**🔗 See also:** Backpropagation, Activation, Loss

---

#### Backpropagation
<small>📌 `A4.3.8`</small>

> The ANN training algorithm: after a forward pass, calculate error, propagate it backward, calculate gradients, and update weights.

**💡 Example:** Loss = 0.8, so backpropagation calculates `∂Loss/∂w` for each weight and SGD updates the weights.  
**⚠️ Common mistake:** Giving too much calculus in an IB answer; the concept matters more than the chain rule.  
**🔗 See also:** Forward propagation, Gradient descent, Loss function

---

#### Gradient descent
<small>📌 `A4.3.8`</small>

> An optimisation method that updates weights in the direction that reduces loss: `w_new = w_old - learning_rate · ∂L/∂w`.

**💡 Example:** Stochastic Gradient Descent updates weights using a mini-batch.  
**⚠️ Common mistake:** Thinking gradient descent always finds the global minimum; it may get stuck in a local minimum.  
**🔗 See also:** Backpropagation, Learning rate, SGD

---

#### Learning rate
<small>📌 `A4.3.8`</small>

> A hyperparameter controlling the step size in gradient descent. Common values are around 0.001 to 0.01.

**💡 Example:** `lr = 0.001` gives small, stable steps; `lr = 1.0` may diverge.  
**⚠️ Common mistake:** Assuming a larger learning rate always trains faster. It can make training unstable.  
**🔗 See also:** Gradient descent, Hyperparameter

---

#### Epoch
<small>📌 `A4.3.8`</small>

> One complete pass through the whole training dataset, including forward and backward passes and weight updates.

**💡 Example:** MNIST has 60K samples; with batch size 64, one epoch is about 938 batches.  
**⚠️ Common mistake:** Confusing epoch and iteration. An epoch is the whole dataset; an iteration is one batch.  
**🔗 See also:** Batch size, Training loop

---

#### Loss function
<small>📌 `A4.3.8`</small>

> A function that measures how different a prediction is from the actual value. Backpropagation minimises loss.

**💡 Example:** Mean squared error for regression; cross-entropy for classification.  
**⚠️ Common mistake:** Using MSE for classification when cross-entropy is usually the correct choice.  
**🔗 See also:** Cross-entropy, MSE, Backpropagation

---

### Week 4: CNN

#### CNN
<small>📌 `A4.3.9`</small>

> Convolutional Neural Network. It uses convolution and pooling to extract spatial features. It is standard for image tasks.

**💡 Example:** MNIST digit classification, ImageNet classification, and face recognition.  
**⚠️ Common mistake:** Using a plain ANN for images and losing spatial structure.  
**🔗 See also:** Convolutional layer, Kernel, Pooling

---

#### Convolutional layer
<small>📌 `A4.3.9`</small>

> A CNN layer that applies learnable kernels, or filters, to the input and creates feature maps.

**💡 Example:** `Conv2D(32, (3,3))` uses 32 filters of size `3×3`.  
**⚠️ Common mistake:** Thinking kernels are fixed by the programmer. They are learned through backpropagation.  
**🔗 See also:** Kernel, Feature map, CNN

---

#### Kernel (Filter)
<small>📌 `A4.3.9`</small>

> A small matrix, often `3×3` or `5×5`, that slides over the input. Each kernel detects a feature such as an edge or texture.

**💡 Example:** A Sobel kernel can detect vertical edges: `[[1,0,-1],[2,0,-2],[1,0,-1]]`.  
**⚠️ Common mistake:** Thinking there is only one kernel in a network; a convolutional layer often has many.  
**🔗 See also:** Convolutional layer, Feature map

---

#### Feature map
<small>📌 `A4.3.9`</small>

> The output of a convolution: a 2D map where each value shows how strongly a kernel activated at that position.

**💡 Example:** A `10×10` input with a `3×3` kernel and valid padding produces an `8×8` feature map.  
**⚠️ Common mistake:** Confusing feature map and kernel. The kernel is the filter; the feature map is the result.  
**🔗 See also:** Convolutional layer, Kernel

---

#### Pooling layer
<small>📌 `A4.3.9`</small>

> A layer that reduces the spatial dimensions of a feature map, reducing computation and helping control overfitting.

**💡 Example:** MaxPool `2×2` changes `28×28` to `14×14`.  
**⚠️ Common mistake:** Applying pooling to channels; pooling normally changes height and width, not channels.  
**🔗 See also:** Max pooling, Average pooling

---

#### Max pooling
<small>📌 `A4.3.9`</small>

> A pooling operation that takes the maximum value from a small window, such as `2×2`.

**💡 Example:** Window `[[1,3],[4,2]]` gives max pool value `4`.  
**⚠️ Common mistake:** Thinking max pooling is upsampling. It is downsampling.  
**🔗 See also:** Pooling layer, Average pooling

---

#### Fully connected layer
<small>📌 `A4.3.9`</small>

> A layer where every neuron is connected to all activations from the previous layer. Often used near the end of a CNN.

**💡 Example:** After convolution and pooling: Flatten → Dense(128) → Dense(10) → softmax.  
**⚠️ Common mistake:** Thinking fully connected layers only exist in plain ANNs. CNNs often end with them.  
**🔗 See also:** Dense layer, CNN

---

#### Spatial hierarchies
<small>📌 `A4.3.9`</small>

> The ability of CNNs to learn hierarchical spatial features: early layers detect edges, middle layers detect shapes, and deeper layers detect objects.

**💡 Example:** A cat detector may learn edges first, then eyes and ears, then the whole face.  
**⚠️ Common mistake:** Not using the phrase "spatial hierarchies" in A4.3.9 answers. It is a strong exam signal.  
**🔗 See also:** CNN, Deep learning, Feature learning

---

### Week 4: Regularisation

#### Dropout
<small>📌 `A4.3.8`</small>

> A regularisation technique that randomly switches off some neurons during training to reduce overfitting.

**💡 Example:** `Dropout(0.3)` disables 30% of neurons during each training forward pass.  
**⚠️ Common mistake:** Applying dropout during inference; it is for training only.  
**🔗 See also:** Overfitting, Regularisation

---

### Week 5: RL

#### Agent
<small>📌 `A4.3.6`</small>

> The decision-making entity in reinforcement learning. It acts in an environment, observes states, chooses actions, and receives rewards.

**💡 Example:** Robot vacuum, AlphaGo, autonomous car AI, or trading bot.  
**⚠️ Common mistake:** Confusing agent and model. The agent is the whole system; the model may be its "brain".  
**🔗 See also:** Environment, State, Action, Reward

---

#### Environment
<small>📌 `A4.3.6`</small>

> The world in which an agent acts. It responds to actions by giving a new state and a reward.

**💡 Example:** For AlphaGo, the Go board; for a car, the road network.  
**⚠️ Common mistake:** Thinking the environment must be physical. It can be virtual.  
**🔗 See also:** Agent, State, Action

---

#### State
<small>📌 `A4.3.6`</small>

> A snapshot of the environment at a moment in time: what the agent observes before making a decision.

**💡 Example:** In a game, state may include player position, enemies, coins, and lives.  
**⚠️ Common mistake:** Thinking state means the whole real world. It is usually only the observable part.  
**🔗 See also:** Agent, Environment, Action

---

#### Action
<small>📌 `A4.3.6`</small>

> An operation an agent can perform. The action space is the set of all possible actions.

**💡 Example:** In a game: `{left, right, jump, fire}`; in trading: `{buy, sell, hold}`.  
**⚠️ Common mistake:** Thinking actions must be continuous. They can be discrete or continuous.  
**🔗 See also:** Agent, Action space

---

#### Reward
<small>📌 `A4.3.6`</small>

> Feedback from the environment. Positive is desirable, negative is undesirable, and the goal is to maximise cumulative reward.

**💡 Example:** `+10` for a coin, `-100` for dying, `-0.1` for each step to encourage short paths.  
**⚠️ Common mistake:** Poor reward design can cause reward hacking, where the agent exploits unintended behaviour.  
**🔗 See also:** Cumulative reward, Agent

---

#### Policy
<small>📌 `A4.3.6`</small>

> The agent's strategy: a mapping from state to action. It may start random and improve during learning.

**💡 Example:** A chess policy chooses a move based on the current board state.  
**⚠️ Common mistake:** Thinking a policy is one rule. It is a full function over the state space.  
**🔗 See also:** Agent, State, Action, Q-learning

---

#### Q-learning
<small>📌 `A4.3.6`</small>

> An RL algorithm using a Q-table where `Q[state][action]` estimates expected reward, updated using the Bellman equation.

**💡 Example:** In Frozen Lake, after many episodes the Q-table guides the agent to the goal.  
**⚠️ Common mistake:** Applying tabular Q-learning to huge state spaces, where methods like DQN are needed.  
**🔗 See also:** Q-table, Bellman equation, DQN

---

#### Cumulative reward
<small>📌 `A4.3.6`</small>

> The sum of all rewards in an episode. RL tries to maximise it, often using a discount factor for future rewards.

**💡 Example:** In a 100-step game, cumulative reward might be +500 if the agent collects coins and reaches the goal.  
**⚠️ Common mistake:** Optimising only immediate reward instead of cumulative reward.  
**🔗 See also:** Reward, Discount factor

---

#### Exploration vs exploitation
<small>📌 `A4.3.6`</small>

> The trade-off between trying new actions and using the best-known action. Epsilon-greedy is one way to balance it.

**💡 Example:** ε-greedy may take a random action with probability 0.1 and the best-known action with probability 0.9.  
**⚠️ Common mistake:** Thinking exploitation is always better; without exploration, the agent may get stuck.  
**🔗 See also:** Epsilon-greedy, UCB, Q-learning

---

#### Epsilon-greedy
<small>📌 `A4.3.6`</small>

> A strategy for balancing exploration and exploitation: with probability ε choose a random action, otherwise choose the best-known action.

**💡 Example:** Start with `ε = 1.0` for exploration, then decay to `0.05` for mostly exploitation.  
**⚠️ Common mistake:** Keeping ε constant forever; it often needs to decrease over time.  
**🔗 See also:** Exploration, Q-learning

---

### Week 5: GA

#### Genetic algorithm
<small>📌 `A4.3.7`</small>

> An evolutionary algorithm where a population of candidate solutions evolves over generations through selection, crossover, mutation, and replacement.

**💡 Example:** TSP: 100 random routes evolve over 100 generations towards a near-optimal route.  
**⚠️ Common mistake:** Confusing GA with RL. RL learns through one agent; GA evolves a population.  
**🔗 See also:** Population, Fitness, Crossover, Mutation

---

#### Population
<small>📌 `A4.3.7`</small>

> A set of candidate solutions in a genetic algorithm. It evolves over generations.

**💡 Example:** A TSP population may start with 100 random routes.  
**⚠️ Common mistake:** Using a population that is too small, giving too little diversity.  
**🔗 See also:** Genetic algorithm, Generation

---

#### Fitness function
<small>📌 `A4.3.7`</small>

> A function that scores how good a candidate solution is. Higher fitness means a better solution.

**💡 Example:** For TSP, `fitness = 1 / total_distance`, so shorter routes have higher fitness.  
**⚠️ Common mistake:** Treating fitness like loss. Fitness is maximised; loss is minimised.  
**🔗 See also:** Genetic algorithm, Selection

---

#### Crossover
<small>📌 `A4.3.7`</small>

> Combining two parent solutions to create offspring, passing useful traits from both parents.

**💡 Example:** Parent 1 `[A,B,C,D,E]` and Parent 2 `[C,A,E,D,B]` may produce Child `[A,B,C,E,D]`.  
**⚠️ Common mistake:** Thinking crossover just copies one parent; it mixes information from both.  
**🔗 See also:** Genetic algorithm, Mutation

---

#### Mutation
<small>📌 `A4.3.7`</small>

> Random changes to offspring. Mutation maintains diversity and helps avoid local optima.

**💡 Example:** In route `[A,B,C,D,E]`, swap two cities to get `[A,D,C,B,E]`.  
**⚠️ Common mistake:** Using a very high mutation rate, which turns the algorithm into random search.  
**🔗 See also:** Genetic algorithm, Crossover

---

### Week 5: Ethics

#### Accountability
<small>📌 `A4.4.1`</small>

> Who is responsible when AI causes harm: developers, users, the company, or regulators?

**💡 Example:** If an autonomous vehicle causes a crash, responsibility may involve the driver, company, designers, and regulators.  
**⚠️ Common mistake:** Saying "the AI is responsible". AI is a tool; accountability stays with people and organisations.  
**🔗 See also:** Algorithmic fairness, Ethics, Liability

---

#### Algorithmic fairness
<small>📌 `A4.4.1`</small>

> The concern that AI systems can perpetuate bias and create discriminatory outcomes in hiring, lending, justice, and other areas.

**💡 Example:** The COMPAS recidivism algorithm showed higher false-positive rates for Black defendants.  
**⚠️ Common mistake:** Assuming "objective AI" means fair AI. Bias can be inherited from training data.  
**🔗 See also:** Bias, COMPAS, Accountability

---

#### Bias (in ML)
<small>📌 `A4.4.1`</small>

> Social or data bias inherited by an AI system, which can lead to discriminatory outcomes. This is different from statistical bias.

**💡 Example:** Amazon's 2018 recruiting tool discriminated against women after training on male-dominated CV data.  
**⚠️ Common mistake:** Confusing technical bias with social bias.  
**🔗 See also:** Algorithmic fairness, Training data

---

#### Privacy
<small>📌 `A4.4.1`</small>

> ML systems often need large amounts of personal data, raising issues of consent, surveillance, profiling, and re-identification.

**💡 Example:** In the Netflix Prize case, "anonymised" ratings could be matched with public IMDb profiles.  
**⚠️ Common mistake:** Thinking anonymisation always guarantees privacy. Re-identification is often possible.  
**🔗 See also:** Anonymisation, Consent, GDPR

---

#### COMPAS
<small>📌 `A4.4.1`</small>

> A US recidivism algorithm. ProPublica reported in 2016 that it had higher false-positive rates for Black defendants.

**💡 Example:** It has been used in some courts for bail and sentencing decisions.  
**⚠️ Common mistake:** Treating COMPAS as the only bias example. Similar issues occur in banking, hiring, and healthcare.  
**🔗 See also:** Algorithmic fairness, Bias, Accountability

---

#### Amazon AI recruiting (2018)
<small>📌 `A4.4.1`</small>

> Amazon stopped using an AI recruiting tool in 2018 after it showed bias against women, caused by training on male-dominated CV data.

**💡 Example:** The system downgraded CVs containing terms such as "women's chess club".  
**⚠️ Common mistake:** Saying the AI invented the bias. The bias came from the data and was amplified by the model.  
**🔗 See also:** Bias, Algorithmic fairness

---

#### Netflix de-anonymisation (2006)
<small>📌 `A4.4.1`</small>

> Netflix released an "anonymised" dataset of user ratings. Researchers re-identified users by matching rating patterns with IMDb.

**💡 Example:** A unique rating pattern can reveal a public profile even when names are removed.  
**⚠️ Common mistake:** Thinking privacy is solved by deleting names. Unique patterns can still identify people.  
**🔗 See also:** Privacy, Anonymisation

---

#### Informed consent
<small>📌 `A4.4.1`</small>

> Users should clearly agree to data collection and understand how their data will be used, especially in medical and financial contexts.

**💡 Example:** Under GDPR Article 6, consent is one lawful basis for processing personal data.  
**⚠️ Common mistake:** Treating "click to accept terms" as informed consent. Understanding matters.  
**🔗 See also:** GDPR, Privacy, Data minimisation

---

#### Transparency
<small>📌 `A4.4.1`</small>

> Openness about how an AI system makes decisions, especially in high-stakes areas such as medicine, justice, and credit.

**💡 Example:** The EU AI Act requires transparency duties for some AI systems.  
**⚠️ Common mistake:** Confusing transparency and explainability. Transparency is openness; explainability is making decisions understandable.  
**🔗 See also:** Explainability, GDPR Article 22

---

#### Explainability
<small>📌 `A4.4.1`</small>

> The ability to explain why a model made a particular prediction. It is especially important for black-box models.

**💡 Example:** LIME and SHAP help explain individual predictions.  
**⚠️ Common mistake:** Assuming all deep learning is impossible to interpret. Explainability methods exist.  
**🔗 See also:** Transparency, LIME, SHAP

---

### Week 6: LLM

#### LLM
<small>📌 `Extended`</small>

> Large Language Model: a deep neural network, usually transformer-based, trained on very large text datasets to understand and generate language.

**💡 Example:** GPT-4, Claude, Gemini, and LLaMA are all LLMs.  
**⚠️ Common mistake:** Treating LLMs as a new ML paradigm. They are a type of ANN, usually based on transformers.  
**🔗 See also:** Transformer, Attention, ANN

---

#### Transformer
<small>📌 `Extended`</small>

> A neural-network architecture based on self-attention. It became the standard architecture for LLMs after the 2017 paper "Attention Is All You Need".

**💡 Example:** GPT, BERT, and T5 are transformer-based models.  
**⚠️ Common mistake:** Confusing transformers with RNNs. Transformers are more parallelisable.  
**🔗 See also:** Attention, LLM, Tokenisation

---

#### Tokenisation
<small>📌 `Extended`</small>

> Splitting text into tokens, which may be words, sub-words, or characters. It is an early step in the LLM pipeline.

**💡 Example:** "Machine learning" may become tokens such as `["Mach", "ine", " learn", "ing"]`.  
**⚠️ Common mistake:** Thinking one token always equals one word. Tokens can be smaller or larger.  
**🔗 See also:** LLM, Embeddings

---

#### Attention
<small>📌 `Extended`</small>

> The mechanism that decides which tokens should attend to, or use information from, other tokens. It is central to transformers.

**💡 Example:** In "The cat sat on the mat", attention can link "sat" to "cat" and "mat".  
**⚠️ Common mistake:** Forgetting that attention has a memory cost, often `O(n²)` with sequence length.  
**🔗 See also:** Transformer, Self-attention

---

#### Hallucinations
<small>📌 `Extended`</small>

> Confidently incorrect or fabricated information produced by an LLM. This is a key limitation.

**💡 Example:** An LLM may invent book titles or citations that look realistic.  
**⚠️ Common mistake:** Treating hallucinations as simple bugs. They are linked to next-token prediction and uncertainty.  
**🔗 See also:** RAG, LLM, Fine-tuning

---

#### RAG
<small>📌 `Extended`</small>

> Retrieval-Augmented Generation: search retrieves relevant documents, then the documents and query are given to the LLM.

**💡 Example:** A chatbot with web search is a basic RAG-style system.  
**⚠️ Common mistake:** Confusing RAG and fine-tuning. RAG adds context; fine-tuning changes weights.  
**🔗 See also:** LLM, Fine-tuning, Hallucinations

---

#### Prompt engineering
<small>📌 `Extended`</small>

> Designing effective prompts for an existing LLM. It changes the output without changing model weights.

**💡 Example:** Zero-shot, few-shot, and chain-of-thought prompting are prompt strategies.  
**⚠️ Common mistake:** Calling prompt engineering fine-tuning. Prompting does not retrain the model.  
**🔗 See also:** LLM, Fine-tuning, Zero-shot

---

#### Fine-tuning
<small>📌 `Extended`</small>

> Additional training of a pre-trained model on a specific domain or task.

**💡 Example:** Fine-tuning a general LLM on medical documents to make it better at medical text tasks.  
**⚠️ Common mistake:** Confusing it with RAG. Fine-tuning changes model weights; RAG adds retrieved context.  
**🔗 See also:** LLM, Transfer learning, RAG

---

### Week 6: Regulations

#### GDPR
<small>📌 `Extended`</small>

> General Data Protection Regulation: EU law from 2018 with strict rules for processing personal data and large potential fines.

**💡 Example:** GDPR can apply to companies outside the EU if they process data about people in the EU.  
**⚠️ Common mistake:** Thinking GDPR only matters for EU companies. It can apply much more widely.  
**🔗 See also:** Right to explanation, Privacy, EU AI Act

---

#### EU AI Act (2024)
<small>📌 `Extended`</small>

> The EU's AI law. It groups AI systems by risk level: unacceptable, high, limited, and minimal risk.

**💡 Example:** Social scoring systems like state-level citizen scoring are treated as unacceptable risk in the EU.  
**⚠️ Common mistake:** Thinking the AI Act only covers high-risk systems. Different risk levels have different rules.  
**🔗 See also:** GDPR, Algorithmic fairness

---

#### Right to explanation
<small>📌 `Extended`</small>

> Under GDPR-related automated decision rights, users may need a meaningful explanation of automated decisions that affect them.

**💡 Example:** If an automated system rejects a loan application, the bank may need to explain the reason.  
**⚠️ Common mistake:** Saying "the AI decided" as if that is a sufficient explanation. It is not.  
**🔗 See also:** GDPR, Explainability, Transparency

---

### Week 6: IB

#### TOK (Theory of Knowledge)
<small>📌 `Extended`</small>

> A required IB component about the nature of knowledge. In CS, TOK links can strengthen Discuss and Evaluate answers.

**💡 Example:** TOK question: "Can AI truly know something, or does it only process patterns?"  
**⚠️ Common mistake:** Ignoring TOK links in extended responses and missing easy marks.  
**🔗 See also:** IB, Discuss, Evaluate

---

## 📝 Licence

This glossary is part of the IB CS ML course. You may use it freely for revision and preparation.

**Sources:**
- Baumgarten, P., Ganea, F., Turland, M. (2024). *Computer Science for the IB Diploma*. Hodder Education.
- MacKenty, D., Stephenson, K. (2025). *Computer Science*. Oxford University Press.
- IB Computer Science Subject Guide (first exams 2027).
