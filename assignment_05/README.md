# Assignment 05: Data preparation and Processing
### Assignment Description
Using popular kaggle data sets, perform the following tasks:
- EDA
- data preparation
- processing

For this assignment, we will need to perform the following tasks:
1. Pick a data set for each of the different dataset types below (selecting a mixture of imbalanced data sets and balanced data sets):

   - tabular diverse set of data types like nyc taxi
   - timeseries
   - spatio temporal
   - image (use kerascv or popular package)
   - audio
   - video (action recognition)
   - graph data set (pick any popular like citation etc.,.)
2. For each of the data sets listed above, perform the following actions:
   A. Perform Detailed EDA.
   B. Perform detailed Data preprocessing/cleaning. (You can use autoEDA and autoDS together with your manual insights and autoML, such as sagemaker or Azure).
   C. Perform clustering and anomaly eliminations in the data sets.  Perform all steps in data preparation including feature processing and feature selection. 
   D. Build various ML models using autoML including ensemble model 
   E. Write one medium paper of how you leveraged GPT-4 code interpreter to perform all of these steps for each of the datasets and your experience in doing so. 
3. Submit the link to the medium article and GitHub Repository. 

## Project Deliverables
Please see below for the list of project deliverables for this assignment. Please note that all deliverables are located within the 'assignment_05' folder of this repository:
1. [`assignment_05/README.md`](https://github.com/schumbar/SJSU_CMPE255/blob/main/assignment_05/README.md): Contains description and instructions for this assignment.
2. [`assignment_05/a_tabular_data.ipynb`](https://github.com/schumbar/SJSU_CMPE255/blob/main/assignment_05/a_tabular_data.ipynb): Google Colab notebook for working with tabular data.
3. [`assignment_05/b_timeseries_data.ipynb`](https://github.com/schumbar/SJSU_CMPE255/blob/main/assignment_05/b_timeseries_data.ipynb): Google Colab notebook for working with time series data.
4. [`assignment_05/c_spatio_temporal_data.ipynb`](https://github.com/schumbar/SJSU_CMPE255/blob/main/assignment_05/c_spatio_temporal_data.ipynb): Google Colab notebook for working with spatio-temporal data.
5. [`assignment_05/d_image.ipynb`](https://github.com/schumbar/SJSU_CMPE255/blob/main/assignment_05/d_image.ipynb): Google Colab notebook for working with image data.
6. [`assignment_05/e_audio.ipynb`](REPLACEME): Google Colab notebook for working with audio data.
7. [`assignment_05/f_video_data.ipynb`](https://github.com/schumbar/SJSU_CMPE255/blob/main/assignment_05/f_video_data.ipynb): Google Colab notebook for working with video data.
8. [`assignment_05/g_graph_data.ipynb`](https://github.com/schumbar/SJSU_CMPE255/blob/main/assignment_05/g_graph_data.ipynb): Google Colab notebook for working with graph data.


# ChatGPT Prompts:
### Prompt for ChatGPT - Task 1: Loading Data and Preliminary Inspection

"Please provide a Python script that I can run in a Google Colab notebook. This script should do the following:



# ChatGPT Prompts:
### Prompt for ChatGPT - Task 1: Loading Data and Preliminary Inspection

"Please provide a Python script that I can run in a Google Colab notebook. This script should do the following:

1. Load a dataset from a CSV file. Although the specific CSV file will be determined later, assume it's named 'dataset.csv' for now.
2. Display the first few rows of the dataset so I can understand what kind of data I'm dealing with.
3. Perform an initial inspection of the data and provide statistics. I want to see a summary that includes data types, any missing values, and basic statistics for numerical columns (like mean, median, mode, standard deviation, and count).
4. Identify potential issues in the dataset that I should be aware of, such as columns with many missing values, possible outliers, or columns that might require encoding or transformation (for example, date-time columns or categorical variables)."

---

### Prompt for ChatGPT - Task 2: Detailed Exploratory Data Analysis (EDA)

"Generate a Python script suitable for a Google Colab environment that conducts a comprehensive Exploratory Data Analysis (EDA) on my 'dataset.csv'. The script should include the following components:

1. **Data Visualization:**
   - Generate histograms for all numerical variables to understand their distributions.
   - Create box plots for numerical variables to identify potential outliers.
   - If there are categorical variables, produce bar charts to see the distribution of each category.
   - Construct scatter plots for potential predictor variables against the target variable (if defined) to observe any apparent relationships.

2. **Correlation Analysis:**
   - Calculate the correlation matrix for the numerical variables in the dataset.
   - Display a heatmap of the correlation matrix with annotations to make it easier to read the correlation coefficients.

3. **Advanced Statistical Summaries:**
   - Perform a descriptive statistical analysis, providing an overview beyond the basics (mean, median, etc.), like skewness, kurtosis, and range for numerical columns.
   - If the dataset is large, create a random sample of rows to make this computation more manageable and note this sampling in the script's comments.

4. **Narrative Analysis:**
   - After each major step (like visualizations, correlation analysis), add comments explaining the findings. These comments should guide the reader on what to observe in the outputs, highlighting any notable points such as high correlation between variables, unusual distributions, or potential data quality issues.

5. **Recommendations for Further Steps:**
   - Based on the EDA, make suggestions for the next steps in data preprocessing. This might include strategies for handling outliers, missing values, variable transformations, or encoding techniques for categorical variables.

Please make sure the script is well-commented, explaining the purpose of each code section, to ensure clarity on what each step is meant to achieve."

---
### Prompt for ChatGPT - Task 3: Data Cleaning and Preprocessing

"Create a detailed Python script for use in Google Colab that focuses on cleaning and preprocessing the data from 'dataset.csv'. The script should systematically address common data quality issues and prepare the data for machine learning. Here are the specific tasks I need the script to perform:

1. **Handling Missing Data:**
   - Identify any columns with missing data.
   - Implement strategies to deal with the missing data. This might include imputation, using methods like mean, median, or mode replacement, or more complex techniques where necessary. If rows or columns are to be dropped due to excessive missing values, please justify these actions.

2. **Addressing Outliers:**
   - Use suitable methods to detect and handle outliers within the dataset. This could involve statistical techniques (like Z-score, IQR) or data transformations. Please provide a rationale for the chosen method.

3. **Normalizing and Scaling:**
   - Apply appropriate normalization or scaling techniques to the numerical data to ensure that all numerical features are on a comparable scale. Explain why the particular method was chosen (e.g., Min-Max scaling, Standard scaling).

4. **Encoding Categorical Variables:**
   - If there are categorical variables, convert them into a format suitable for machine learning models using encoding techniques like one-hot encoding or label encoding.

5. **Feature Selection/Reduction:**
   - Discuss and implement methods for feature selection or reduction, especially if the dataset has a large number of features. Techniques might include statistical methods, selection by model performance, or the use of domain knowledge.

6. **Data Partitioning:**
   - Finally, split the dataset into training and testing sets, ensuring a suitable distribution of data points in each. Typically, a common split ratio is 80:20 (training:testing), but use what is considered best practice for the current data scenario.

Please ensure that each step is accompanied by comments explaining both what the code is doing and why it is necessary, providing insights into the decisions being made. Also, if certain steps like outlier detection or data imputation require more nuanced handling due to the specifics of the dataset, please highlight these considerations."

---

### Revised Prompt for ChatGPT - Task 4: Building Machine Learning Models (Focusing on Ensemble and Including AutoML)

"I need a comprehensive Python script for Google Colab that guides me through the process of building multiple machine learning models, with a specific focus on ensemble methods, and includes the use of AutoML tools. The dataset 'dataset.csv' has been preprocessed in previous steps. Here's what I need:

1. **Baseline Model Building:**
   - Start by creating simple baseline models (like a linear model or a basic decision tree) for the problem at hand (classification/regression/etc.). This step is to quickly check the 'raw' performance of straightforward models on the dataset.

2. **Advanced Model Building with Ensemble Focus:**
   - Develop ensemble models, such as Random Forest, Gradient Boosting, AdaBoost, or even a custom ensemble of different model types. Explain the choice of models based on the dataset's characteristics or problem type.
   - Tune hyperparameters for these ensemble models to improve performance, using methods like grid search or random search. Discuss why certain hyperparameters are being focused on during tuning.

3. **Performance Evaluation:**
   - Implement a robust evaluation strategy, using appropriate metrics for the problem type (accuracy, precision, recall, F1-score for classification; MSE, RMSE, MAE for regression, etc.). Compare the performance of the different models, emphasizing the impact of ensemble methods on the results.

4. **Introduction to AutoML:**
   - Provide an overview of how AutoML can be leveraged for this scenario, discussing its potential benefits and limitations. Mention if AutoML tools typically include ensemble methods in their processes.

5. **Using AutoML Tools:**
   - Guide me through using an AutoML tool (like Google's AutoML, Azure AutoML, or AWS SageMaker) to automatically build and select the best model. Highlight whether these tools are employing ensemble methods and how they contribute to the final model selection.

6. **Comparing Models:**
   - After building models with AutoML, compare their performance against manually developed models, particularly ensemble models. Highlight the pros and cons of each approach and discuss any significant performance differences, with insights into why ensemble models performed as they did.

7. **Final Selection:**
   - Based on the performance comparison, suggest which model(s) might be best to proceed with for deployment or further optimization. Discuss the rationale behind this choice, focusing on aspects beyond raw performance, such as interpretability, scalability, and maintenance. If ensemble models are recommended, provide additional context on why they stand out.

Please ensure the script includes detailed comments and explanations, discussing the strategic choices being made at each step. This explanation should provide insights into why specific models or ensemble techniques are chosen, how they function, and how they align with best practices in machine learning."

---

This revised prompt ensures ChatGPT understands the emphasis on ensemble methods, guiding the script to not only use these techniques but also to provide educational commentary on why and how these methods are effective. After running the models and evaluations, you'll have a solid foundation for deciding the best strategies for your project's final stages, whether that involves deployment, further optimizations, or additional research.

---

### Prompt for ChatGPT - Task 5: Comprehensive Conclusion for Notebook and Medium Article

"I need a detailed conclusion section for my Google Colab notebook that I plan to adapt into a Medium article. This conclusion should thoroughly recap the machine learning project, highlighting the key steps undertaken, the rationale behind methodological choices, insights derived from the analysis, and potential future directions. Here's what the conclusion needs to encompass:

1. **Project Overview:**
   - Provide a succinct recap of the project's objectives and the dataset used, touching on its source, nature, and key features.

2. **Exploratory Data Analysis (EDA):**
   - Summarize the EDA process, including the types of visualizations and statistical analyses performed. Highlight any surprising discoveries or expected patterns confirmed during this phase. Discuss how the EDA influenced subsequent preprocessing steps.

3. **Data Cleaning and Preprocessing:**
   - Recap the main challenges faced during data cleaning (e.g., missing data, outliers) and the strategies employed to address them. Include the reasoning behind chosen imputation methods, encoding strategies, or any transformations applied.

4. **Model Building (Including Ensemble and AutoML):**
   - Discuss the various models built, with a special emphasis on ensemble methods. Why were these models chosen, and how were they configured and tuned? Also, describe your experience using AutoML tools, highlighting any advantages or limitations encountered.

5. **Model Evaluation and Selection:**
   - Summarize the performance results of the models tested. Which metrics were used, and why? How did the models fare against each other, and what was surprising or expected about these outcomes?

6. **Insights and Learnings:**
   - Reflect on the project's key takeaways. What did this journey teach you about the dataset, the problem scope, or machine learning in general? Were there any 'eureka' moments or steep learning curves?

7. **Future Implications and Next Steps:**
   - Based on your project's outcomes, what are the potential real-world implications or applications? What steps would you recommend taking next, either in terms of model deployment, further testing, or additional features to explore?

8. **Narrative for Medium:**
   - Craft the conclusion in a narrative suitable for a broad audience, explaining complex concepts accessibly and engagingly. The tone should be informative but approachable, ensuring both technical and non-technical readers can grasp the project's essence.

9. **Visuals and References:**
   - Recommend any visuals (charts, significant code snippets, etc.) that would enhance the conclusion's impact or clarity. Also, suggest any external sources or references that readers could consult for further information or context.

Please ensure this conclusion is detailed and coherent, serving as a standalone summary that encapsulates the depth and breadth of the work undertaken in this project."
