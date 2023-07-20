import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from scipy.stats import pearsonr
path = r'C:\Users\Preston Conner\Desktop\ucibikedata\archive\day.csv'
df = pd.read_csv(path)
#prelimary stuff

#understanding the data
df.columns
df.shape
print(df.info)
print(df.describe())
df.dtypes
print(df.head)
#column count of 731, check for missing values
df.isnull().sum()
#does not have missing values
#Count is rentals so that is target variable

#the variables we are interested in finding potential correlations are:
#count, temp, season, month, holiday, weekday, weathersit, windspeed
#got rid of atemp because it is the same as temp and has same correlation value as each other

#data cleaning process
#going to check outliers with the count and temp variables
#thought process is that these variables are floats/integers and are target variables
#using (IQR) interquartile range method for atemp outliers
Q1 = df['temp'].quantile(0.25)
Q3 = df['temp'].quantile(0.75)
IQR = Q3-Q1
#bounds for outliers
upperbound = Q3 + 1.5*IQR
lowerbound = Q1 - 1.5*IQR
print(lowerbound)
print(upperbound)
print(df.describe())
#the min/max of temp do not reach the bounds, therefore no outstanding outliers
#using (IQR) interquartile range method for count outliers
Q1 = df['cnt'].quantile(0.25)
Q3 = df['cnt'].quantile(0.75)
IQR = Q3-Q1
#bounds for outliers
upperboundcnt = Q3 + 1.5*IQR
lowerboundcnt = Q1 - 1.5*IQR
print(lowerboundcnt)
print(upperboundcnt)
print(df.describe())
#the min/max of temp do not reach the bounds, therefore no outstanding outliers

#second check possible outliers using a Zscore test
#Zscore for temp
z_scores = np.abs((df['temp'] - df['temp'].mean())/ df['temp'].std())
#z score formula
z_score_threshold = 2
z_score_outliers = df[z_scores >z_score_threshold]
print(z_score_outliers)
num_temp_outliers = z_score_outliers.shape[0]
print("Outliers: " + str(num_temp_outliers))
#there are 6 outliers in temp, now to omit them
df_without_tempoutliers = df[~(z_scores > z_score_threshold)]
print(df_without_tempoutliers)
#check omit happened
df_without_tempoutliers.shape
#now use new data frame for z score with count

#Zscore for count
z_scores = np.abs((df_without_tempoutliers['cnt'] - df_without_tempoutliers['cnt'].mean())/ df_without_tempoutliers['cnt'].std())
z_score_threshold = 2
z_score_outliers = df_without_tempoutliers[z_scores >z_score_threshold]
print(z_score_outliers)
num_cnt_outliers = z_score_outliers.shape[0]
print("Outliers: " + str(num_cnt_outliers))
#there are 10 outliers, now to omit
df_without_outliers = df_without_tempoutliers[~(z_scores > z_score_threshold)]
print(df_without_outliers)
#check omit happened

#temp is normalized (divided by 41) so reverting that for better readibility on plots
df_without_outliers['temp'] = (df_without_outliers['temp'] * 41).round().astype(int)
print(df_without_outliers)

#Adding a new column that converts celcius into farenheit
df_without_outliers['temp_farenheit'] = (df_without_outliers['temp'] * 9/5) + 32
print(df_without_outliers)
df_without_outliers.head()
print(df_without_outliers.describe())
#now use new data frame for rest of data analysis
#data is cleaned

#create data visuals for insights on patterns and relations
#heat map is great to quickly find correlations between all variables of interest
#specifically looking at variables correlation to cnt
variables_of_interest = ['cnt', 'temp', 'season', 'holiday', 'weekday', 'weathersit', 'windspeed']
wanted_variables_df = df_without_outliers[variables_of_interest]
correlation_matrix = wanted_variables_df.corr()
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 4))
ax = sns.heatmap(correlation_matrix, fmt='.2f', annot=True, cmap='coolwarm')
plt.xticks(rotation=90)
plt.yticks(rotation=0)
ax.set_title('Correlation Matrix of Variables of Interest')
#to fix matplotlib functions not changing seaborn heatmap
plt.draw()
plt.savefig("Heatmap of Correlation between Variables of Interest")
plt.pause(0.001)
plt.show()

#print list of corr
correlation_matrix_list = df_without_outliers[variables_of_interest].corr()
correlation_to_count = correlation_matrix_list['cnt']
print(correlation_to_count)
#temp: 0.617 & season: 0.406
#temp- moderate postive correlation
#season- weak positive correlation
#holiday is -0.06 so near 0

#Pearsons correlation test for statistical signficance
#for temp and cnt
temp = df_without_outliers['temp']
cnt = df_without_outliers['cnt']
corr_coef, p_value = pearsonr(temp, cnt)
print("Correlation Coefficient:", corr_coef)
print("P-value:", p_value)
#very good and strong support for correlation between pearson and temp
#for season and cnt
season = df_without_outliers['season']
cnt = df_without_outliers['cnt']
corr_coef, p_value = pearsonr(season, cnt)
print("Correlation Coefficient:", corr_coef)
print("P-value:", p_value)
#statistically significant

#it would still be helpful to see distributions of different time frames (seasons and months)
#Count = Rentals for future reference

#Box Plot and Violin Plot joint- Rentals and season
#joint
sns.set_style("whitegrid")
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,10))
#boxplot
sns.boxplot(x='season', y='cnt', data=df_without_outliers, palette='gist_ncar', ax=ax1)
ax1.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
ax1.set_xlabel('Season')
ax1.set_ylabel('Rentals')
ax1.set_title('Relationship between Daily Rentals and Seasons')
#violin plot 
sns.violinplot(x='season', y='cnt', data=df_without_outliers, xticklabels=['Spring', 'Summer', 'Fall', 'Winter'], palette='gist_ncar', ax=ax2)
ax2.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
ax2.set_xlabel('Season')
ax2.set_ylabel('Rentals')
#joint final
plt.savefig("RentalsbySeasonPlots")
plt.subplots_adjust(hspace=0.3, wspace=0.0)
plt.show()

#Box and Violin Plot Joint- Rentals and month
#joint
sns.set_style("whitegrid")
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,10))
#box plot
sns.boxplot(x='mnth', y='cnt', data=df_without_outliers, palette='gist_ncar', ax=ax1)
ax1.set_xlabel('Month')
ax1.set_ylabel('Rentals')
ax1.set_title('Relationship between Daily Rentals and Months')
#violin plot
sns.violinplot(x='mnth', y='cnt', data=df_without_outliers, palette='gist_ncar', ax=ax2)
ax2.set_xlabel('Month', fontsize=12)
ax2.set_ylabel('Rentals', fontsize=12)
ax2.yaxis.set_label_coords(-0.1, 0.5)
#set xticks as abbrev months
months = pd.to_datetime(df_without_outliers['dteday']).dt.strftime('%b').unique()
ax1.set_xticklabels(months)
ax2.set_xticklabels(months)
#joint final
plt.subplots_adjust(hspace=0.3, wspace=0.0)
plt.savefig("RentalsbyMonthPlots")
plt.show()

#Rentals and weathersituation
#box plot of rentals by weathersit
sns.set_style("whitegrid")
plt.figure(figsize=(8, 6))
boxplot_colors = ['lightblue', 'lightgreen', 'lightcoral']
boxplot = sns.boxplot(x='weathersit', y='cnt', data=df_without_outliers, palette=boxplot_colors)
legend_colors = ['lightblue', 'lightgreen', 'lightcoral']
labels = ['Clear/Partly Cloudy', 'Misty/Cloudy', 'Light Rain, Rain, Thunderstorm']
patches = [mpatches.Patch(color=legend_colors[i], label=labels[i]) for i in range(len(labels))]
plt.legend(handles=patches, title='Weather Situation Key')
plt.xlabel('Weather Situation')
plt.ylabel('Rentals')
plt.savefig("RentalsbyWeathersit")
plt.title('Relationship between Daily Rentals and Weather Situation')

#scatterplot with line of fit temp relation to rentals
sns.regplot(x='temp', y='cnt', data=df_without_outliers, scatter_kws={'alpha':0.2}, line_kws={'color':'red', 'linewidth':2})
plt.xlabel('Temperature (Celcius)')
plt.ylabel('Rentals')
plt.title('Relationship between Daily Rentals and Temperature (Celcius)')
plt.savefig("RentalsbyTemp ScatterwithLine")
plt.show()

#subset temp and cnt into seasons into different data frames
#because both have correlation and statistical signifiance and lead to greater insights
#create 4 more different data frames for each season
df_spring = df_without_outliers[df_without_outliers['season'] == 1].copy()
df_summer = df_without_outliers[df_without_outliers['season'] == 2].copy()
df_fall = df_without_outliers[df_without_outliers['season'] == 3].copy()
df_winter = df_without_outliers[df_without_outliers['season'] == 4].copy()
#check changes took place
df_spring.count()

#Conducts Pearson test for each season
seasons_dataframes = [df_spring, df_summer, df_fall, df_winter]
season_names = ['Spring', 'Summer', 'Fall', 'Winter']

for i, season_df in enumerate(seasons_dataframes):
    season_name = season_names[i]
    temp = season_df['temp']
    cnt = season_df['cnt']
    corr_coef, p_value = pearsonr(temp, cnt)
    print(f"Correlation for {season_name}:")
    print("Correlation Coefficient:", corr_coef)
    print("P-value:", p_value)
    
#spring moderate strong correlation
#summer moderate correlation
#fall very weak correlation
#winter moderate correlation
print(df_spring.describe())
print(df_summer.describe())
print(df_fall.describe())
print(df_winter.describe())

#cnt and temp 4 joint scatter plot for each season
#seasonality time series analysis
sns.set_style("whitegrid")
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8, 10))
#df_spring
sns.scatterplot(x='temp', y='cnt', data=df_spring, ax=ax1)
sns.regplot(x='temp', y='cnt', data=df_spring, ax=ax1, scatter_kws={'alpha':0.2}, line_kws={'color':'red', 'linewidth':2})
ax1.set_xlabel('Temperature')
ax1.set_ylabel('Rentals')
ax1.set_title('Spring')
#df_summer
sns.scatterplot(x='temp', y='cnt', data=df_summer, ax=ax2)
sns.regplot(x='temp', y='cnt', data=df_summer, ax=ax2, scatter_kws={'alpha':0.2}, line_kws={'color':'red', 'linewidth':2})
ax2.set_xlabel('Temperature')
ax2.set_ylabel('Rentals')
ax2.set_title('Summer')
#df_fall
sns.scatterplot(x='temp', y='cnt', data=df_fall, ax=ax3)
sns.regplot(x='temp', y='cnt', data=df_fall, ax=ax3, scatter_kws={'alpha':0.2}, line_kws={'color':'red', 'linewidth':2})
ax3.set_xlabel('Temperature')
ax3.set_ylabel('Rentals')
ax3.set_title('Fall')
#df_winter
sns.scatterplot(x='temp', y='cnt', data=df_winter, ax=ax4)
sns.regplot(x='temp', y='cnt', data=df_winter, ax=ax4, scatter_kws={'alpha':0.2}, line_kws={'color':'red', 'linewidth':2})
ax4.set_xlabel('Temperature')
ax4.set_ylabel('Rentals')
ax4.set_title('Winter')
#adjust spacing, bigger title, and save
fig.suptitle('Variation in Daily Rentals per day by Temperature (Celcius) in Different Seasons')
plt.subplots_adjust(hspace=0.4, wspace=0.5)
plt.savefig("JointSeasons RentalsbyTemp")
plt.show()

#Find relationship of casual and registered users
df_monthly_breakup = df_without_outliers.groupby('mnth')[['casual', 'registered']].sum()
df_monthly_breakup['total'] = df_monthly_breakup['casual'] + df_monthly_breakup['registered']
df_monthly_breakup['casual_percentage'] = df_monthly_breakup['casual'] / df_monthly_breakup['total'] * 100
df_monthly_breakup['registered_percentage'] = df_monthly_breakup['registered'] / df_monthly_breakup['total'] * 100
#check everything looks right
print(df_monthly_breakup.head(13))

#stacked bar to show relation of casual and registered
plt.figure(figsize=(10, 6))
plt.bar(df_monthly_breakup.index, df_monthly_breakup['casual_percentage'], label='Casual', color='skyblue')
plt.bar(df_monthly_breakup.index, df_monthly_breakup['registered_percentage'], bottom=df_monthly_breakup['casual_percentage'], label='Registered', color='orange')
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(df_monthly_breakup.index, months)
plt.xlabel('Month')
plt.ylabel('Percentage')
plt.title('Percentage Breakdown of Casual and Registered Users by Month')
plt.legend()
plt.savefig('Userbreakdown by month')
plt.show()

print(df_without_outliers.head())
