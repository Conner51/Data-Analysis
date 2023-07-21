# Data-Analysis
Bike Sharing Data Analysis with Python

Introduction
This data analysis project was undertaken as part of my self learning journey to learn data analysis using Python. The dataset used for this project is the "Bike Sharing Dataset" obtained from the UCI Machine Learning Repository (Link: Bike Sharing Dataset).

The purpose of this project was to gain hands-on experience in data analysis techniques and explore insights from the bike sharing dataset. Through this analysis, I aimed to understand patterns and trends in bike sharing behavior, as well as to practice data manipulation, visualization, and really just how to utilize s in Python.

Dataset Overview
The "Bike Sharing Dataset" contains rental data of a bike-sharing system with attributes such as the number of bikes rented, weather conditions, time, date, and more.

Dataset Features:

instant: Record index
dteday: Date of the data
season: Season (1: spring, 2: summer, 3: fall, 4: winter)
yr: Year (0: 2011, 1: 2012)
mnth: Month (1 to 12)
hr: Hour of the day (0 to 23)
holiday: Binary (1 if the day is a holiday, 0 otherwise)
weekday: Day of the week (0 to 6)
workingday: Binary (1 if the day is a working day, 0 otherwise)
weathersit: Weather situation (1: Clear, 2: Mist + Cloudy, 3: Light Snow/Rain, 4: Heavy Rain)
temp: Normalized temperature on a scale of 0 to 1
atemp: Normalized feeling temperature on a scale of 0 to 1
hum: Normalized humidity on a scale of 0 to 1
windspeed: Normalized wind speed on a scale of 0 to 1
cnt: Count of total bike rentals (target variable)
Data Analysis Steps
Data Loading: Read and explore the dataset to understand its structure and features.
Data Preprocessing: Handle missing values, convert categorical variables, and perform feature scaling.
Exploratory Data Analysis: Visualize the data to identify patterns and relationships between variables.
Feature Selection: Identify significant features that influence bike rentals.
Machine Learning: Build and train a predictive model to forecast bike rentals.
Evaluation: Assess the model's performance and discuss the results.
Key Findings
- There is a strong direct relationship between temperature and Daily rentals.
- Positive correlation between temperature and Daily rentals for Spring, Summer, and Winter seasons.
- For Fall season, there was no correlation between temperature and Daily rentals.
- Fall season was the only season that was not statistically significant in terms of its relationship with Daily rentals.
- Weak positive correlation between seasons (Spring, Summer, Winter) and Daily rentals (excluding Fall).
- Near-zero correlation between holidays and Daily rentals.
- Near-zero correlation between weekdays and Daily rentals.
- The busiest months were the middle months of the year (June, July, August, September, and October).
- Summer and Fall were the most popular seasons for daily rentals, with Winter trailing closely behind.
- Most rentals occurred when the weather was cloudy or less, and there was a clear drop-off in rentals when any sort of rain was happening.
- Around 20% and less of users were casual users vs. registered users.
- January, February, November, and December were low usage months for casual users.

Conclusion
This specific data analysis, being my first, has really opened my eyes as to why Python is such a popular tool. After getting past the intitial learning curve, it really is a great platform to manipulate large data sets.
Also I really believe in learning my doinig so this has truly heleped me grasp Python byhandling real-world data, performing data manipulation, and drawing meaningful insights from the data.
That said definitely was not easy for my first go around, just had to throw some music on and pain stakingly work through the errors.

That said this project has also made me realize how high of a ceiling there is when it comes to the possibilities in Python. I really want to focus on machine model learning in the future.
I look forward to furthering my data analysis skills and tackling more complex projects in the future. Your feedback and suggestions on this project are highly appreciated.
