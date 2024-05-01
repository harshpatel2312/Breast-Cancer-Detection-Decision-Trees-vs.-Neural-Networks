# Breast-Cancer-Detection-Decision-Trees-vs.-Neural-Networks
This research aims to compare the performance of two machine learning algorithms, Decision Trees (DT) and Neural Networks (NN), in detecting breast cancer from medical imaging data. Breast cancer is a significant health concern globally, and early detection plays a crucial role in successful treatment. Machine learning algorithms offer promising solutions for early detection, but their performance varies.

Objectives:

Evaluate the accuracy, precision, and recall of Decision Trees and Neural Networks in detecting breast cancer.
Test the hypothesis: "There is a significant difference in the accuracy of cancer detection between DT and NN algorithms."
Methodology:

Dataset: Utilizing a publicly available repository containing medical imaging data, including images from patients diagnosed with breast cancer and healthy individuals.
Experimental Design: The dataset is randomly divided into training (66%) and testing (34%) sets. Each machine learning model is built 30 times based on different random samples of the dataset.
Performance Evaluation: Metrics such as accuracy, precision, and recall are used to evaluate the performance of DT and NN models.
Statistical Analysis: Hypothesis testing using the t-test to determine significant differences in accuracy between the two algorithms.
Results:

Mean accuracy of Decision Trees: 0.7113 (Standard Deviation: 0.0346)
Mean accuracy of Neural Networks: 0.6756 (Standard Deviation: 0.0353)
Hypothesis testing p-value: 0.00021017384189646725
Conclusion:
The results indicate a significant difference in the performance of Decision Trees and Neural Networks in detecting breast cancer. Decision Trees outperformed Neural Networks in terms of mean accuracy. These findings provide insights into the efficacy of machine learning algorithms for breast cancer detection and can contribute to the optimization of diagnostic processes for improved patient care.

Deliverables:

Journal paper summarizing the project's objectives, methodology, results, and conclusions.
Python file containing experimental code and results.
