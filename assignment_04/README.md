# Apache Beam Data Engineering Assignment

## Assignment Description
This assignment is designed to give you experience with the Apache Beam framework. You will be using the Apache Beam framework to perform data engineering tasks on a dataset of your choice. You will be required to perform the following tasks:
1) Do a complete dataset EDA in colab (preferably using D3.js visualizations). 
2) Auto EDA with your favorite tool.
3) Demonstrate apache beam in a colab including composite transform, pipeline I/O, triggers, windowing, pardo. 

### Part A: Exploratory Data Analysis
In this section of the assignment, I used exploratory data analysis to find information regarding the cost of childcare in the United States. The dataset used for this analysis is the Child Care Costs Dataset from Kaggle (This is linked in the google colab notebook). The dataset contains information about the cost of childcare in the United States, and a separate file for counties within the United States. The childcare_costs dataset contains information about childcare costs across different counties, represented by their FIPS codes, over various years.

The dataset includes a wide range of variables, including:
- Demographic details (for example, race, households, etc.)
- Economic indicators (for example, household income, employment rates, etc.)
- Specific childcare cost indicators (e.g., cost for infants, toddlers, preschool)

In this portion of the assignment, we used visualizations to show the various graphs of the dataset. 

### Part B: AutoEDA
In this portion of the assignment, I embarked on a detailed Exploratory Data Analysis (EDA) journey using a dataset of Steam games sourced from Kaggle. Here's a walkthrough of my approach:

Initiating Data Exploration:

I kicked things off by loading the dataset into a pandas DataFrame. Utilizing functions like info(), head(), and inspecting the column names, I gained initial insight into the data's structure.
I also took the time to outline each column, shedding light on the kind of information encapsulated within the dataset.
Tackling Data Cleaning and Conversion:

My focus was directed at the 'Original Price' and 'Discounted Price' columns. Recognizing the necessity for numerical analysis, I converted these columns from strings, often cluttered with 'Free' labels and currency symbols, into a more analysis-friendly numerical format.
I identified and rectified anomalies within the 'Release Date' column, ensuring it adhered to a proper datetime format. I was particularly wary of games slated for release in the future, categorizing these as anomalies and subsequently eliminating them from my dataset.
Addressing Missing Data:

I acknowledged the presence of missing data, a reality that was starkly apparent in the 'Release Date' column. I quantified these absences and embarked on a cleaning mission to purge the dataset of these problematic entries.
Revamping Review Columns:

I turned my attention to the 'Recent Reviews Number' and 'All Reviews Number' columns, which were initially populated with text data. Understanding the necessity for a quantitative analysis of review scores, I extracted numerical data from these columns.
Diving into Categorical and Text Data Analysis:

My exploration continued as I delved into categorical fields such as 'Developer', 'Publisher', and 'Popular Tags'. I aimed to unravel the diversity hidden within these categories and pinpoint the tags most commonly associated with the games. This insight was crucial as it hinted at popular game genres and features.
Crafting Visualizations:

I didn't just stop at numerical data and text. Realizing the power of visual representation, I set out to create various visualizations. Though the specific plots were not delineated in this portion of the assignment, my goal was clear: I intended to produce histograms, bar charts, and other visual aids to underscore the insights gleaned from my dataset. These visual tools were crafted to illustrate several facets, including game prices' distribution, the commonality of certain tags, and the ebb and flow of game releases over time.
Drawing Insights and Conclusions:

Lastly, I made sure to transcend mere data manipulation and technical analysis. By interpreting the statistical summaries, cleaned data, and visual elements, I converted complex analyses into digestible insights and conclusions. This step was paramount in my EDA, as it transformed the numerical and categorical analyses into tangible, understandable insights.
In summary, this portion of the assignment was an exhaustive EDA exercise, showcasing various facets such as data cleaning, transformation, analysis, visualization, and interpretation, all set within the realm of Steam games data. Through this rigorous process, I sought to gain a holistic understanding of the data's nuances, trends, and potential areas for further statistical scrutiny or predictive modeling.

### Part C: Apache Beam
Environment Setup: I started by installing the necessary package, 'apache_beam', which is essential for creating data processing pipelines. Using this, I can build scalable and efficient data processing tasks.

Loading and Initial Exploration of Data: I loaded the healthcare insurance dataset, which is in CSV format, using Pandas. The dataset is stored on my Google Drive, and I accessed it directly from there. After loading, I displayed the first few rows of the dataset using data.head() to check if it's loaded correctly and understand its structure.

Data Structure Understanding: I analyzed the columns of the dataset, which include 'age', 'sex', 'bmi', 'children', 'smoker', 'region', and 'charges'. These fields are self-explanatory and provide various attributes of the individuals covered in the insurance dataset.

Data Processing With Apache Beam:
Parsing CSV Rows: I defined a function, parse_csv, that takes a line of CSV text and parses it into a dictionary. This dictionary uses the column headers as keys and the corresponding entry in the CSV file as values. This transformation is necessary for the processing tasks ahead, where we deal with the data in a key-value pair fashion.

CSV Output Preparation: The to_csv_string function is for formatting the processed data back into a CSV-like string. This is useful when we want to output our processed data back into a CSV file.

Composite Transform Creation: One of the powerful features of Apache Beam is the ability to create custom composite transforms. I leveraged this by creating a class, CalculateAverageChargeByGroup, which inherits from beam.PTransform. This transform is designed to calculate the average charge for insurance based on a grouping key (like 'smoker' status). It performs several steps:

Extracting the key-value pairs.
Grouping the data based on the key.
Calculating the average charges for each group.
Pipeline Execution:

I initiated the creation of the pipeline with predefined options.
The pipeline begins by reading data from the CSV file, converting each line of text into a dictionary using the parse_csv function.
I used the composite transform CalculateAverageChargeByGroup to calculate the average charge, grouping by 'smoker' status for this case. This is a modular approach; we can group by any other available category by simply changing the argument.
The results, which are key-value pairs of the group and its corresponding average charge, are then formatted back into a CSV string.
Finally, these strings are written to an output CSV file. This file is saved back on my Google Drive for persistence and further analysis.
Wrap-Up:

Through this script, I demonstrated the use of Apache Beam for efficient data processing. I used various features like PTransforms, Pipeline I/O, and others to read, process, and write data. The script specifically calculates the average insurance charges based on different categorical data, showcasing the power of Apache Beam in handling and processing large datasets.

This script signifies just the start of the extensive capabilities Apache Beam offers, such as windowing and triggers, which are useful for more complex data streams and batch processing scenarios.

### Project Deliverables
All project deliverables for this assignment is located under the `assignment_04` folder. The deliverables include:
1. **README.md**: This file which contains information about the assignment and deliverables.
2. **A_EDA/childcare_costs.csv**: Dataset used for the Exploratory Data Analysis portion of the assignment.
3. **A_EDA/counties.csv**: Dataset used for the Exploratory Data Analysis portion of the assignment. This is a part of the childcare_costs dataset.
4. **B_AutoEDA/steam_games.csv**: Dataset used for the AutoEDA portion of the assignment.
5. **C_ApacheBeam/insurance.csv**: Dataset used for the Apache Beam portion of the assignment.
6. **C_ApacheBeam/output.csv-00000-of-00001**: Output as a result of running the Apache Beam pipeline.
7. **A_EDA/Part_A_EDA.ipynb**: Google Colab notebook for the Exploratory Data Analysis portion of the assignment.
8. **B_AutoEDA/Part_B_AutoEDA.ipynb**: Google Colab notebook for the AutoEDA portion of the assignment.
9. **B_AutoEDA/sweetviz_report.html**: HTML file containing the output of running the sweetviz library on the steam_games dataset.
10. **C_ApacheBeam/Part_C_ApacheBeam.ipynb**: Google Colab notebook for the Apache Beam portion of the assignment.