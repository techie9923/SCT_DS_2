titan dt is dataset taken from kaggle  https://www.kaggle.com/c/titanic/data
titan.py is pyhton file

📌 Titanic Data Analysis (EDA) Project
This project performs data cleaning and exploratory data analysis (EDA) on the classic Titanic dataset (uploaded as titan dt.xlsx).
We explore relationships between passenger features and survival outcomes using Python, pandas, seaborn, and matplotlib.

✅ 📖 Objectives
Clean the Titanic dataset by handling missing values.
Explore and visualize important patterns in the data.
Understand relationships between passenger features (age, fare, class, sex) and survival.

✅ 🗂️ Dataset
The dataset contains details of Titanic passengers such as:
PassengerId
Survived (0 = No, 1 = Yes)
Pclass (Passenger Class)
Name
Sex
Age
SibSp (siblings/spouses aboard)
Parch (parents/children aboard)
Ticket
Fare
Cabin
Embarked (port of embarkation)

✅ 🧹 Data Cleaning Steps
Missing Age values were replaced with the mean age.
The Cabin column was dropped because it had too many missing values.
Rows with missing Embarked values were removed.
These steps ensure our analysis uses a clean, consistent dataset without null entries in key columns.

✅ 📊 Exploratory Data Analysis (EDA)
We created multiple plots to understand trends and relationships in the data:

🔹 1. Correlation Heatmap
Shows numeric correlations between variables.
Reveals that Fare and Pclass are correlated, and Pclass correlates with survival.

🔹 2. Age Distribution
Histogram showing the distribution of passenger ages.
Identifies the most common age ranges on board.

🔹 3. Survival by Sex
Count plot comparing survival rates of males and females.
Highlights higher survival rates among female passengers.

🔹 4. Age vs Fare (Colored by Survival)
Scatter plot visualizing the relationship between age and ticket fare.
Colors indicate survival, showing trends by socio-economic status.

🔹 5. Fare by Passenger Class
Box plot comparing ticket prices across classes.
Shows clear differences in fare distribution between 1st, 2nd, and 3rd class.

✅ 💻 Technologies Used
Python
pandas
numpy
matplotlib
seaborn


✅ 📈 Key Insights
Higher passenger class strongly correlates with higher fares.
First-class passengers paid much more and had better survival rates.
Female passengers had a higher survival probability.
Children (younger ages) also show some trend toward higher survival, reflecting the "women and children first" policy.
