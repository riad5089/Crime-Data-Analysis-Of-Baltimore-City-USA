# Crime-Data-Analysis-Of-Baltimore-City-USA
## Project Description
The aim of this project is to analyze crime data from the year 2023 in Baltimore City, Maryland, USA, in order to gain insights, identify patterns, understand the characteristics of victims, and examine the relationship between crime and other features.

## Objectives:

1. Web Scraping and Data Collection: I have taken data from [this website](https://data.baltimorecity.gov/datasets/baltimore::part-1-crime-data/about) and scraped 3000 data.
2. Data Preprocessing: Clean and preprocess the scraped data to handle missing values and other preprocessing steps.

3. Visualization: Utilize Tableau to create interactive visualizations. Generate pie charts, bar charts, maps and many more to highlight crime patterns, trends, and correlations within the dataset. Here is my [dashboard](https://public.tableau.com/app/profile/md.abdur.sobhan.riad/viz/Crime_analysis_16873409234090/Dashboard1?publish=yes
).

## Tableau Dashboard
1.`Total Counts` shows total number of crime and district-wise counts. Here The Total Number of Crime analysis provides an overview of the overall crime incidents recorded and District wise Count analysis represents crime incidents based on geographical districts.
<img src="Images/Screenshot_76.png" width=900 height=400>

2.`Crime Insights` shows Location and Month-Wise Crime, Gender-wise count, and Month and District-wise analysis. Location and Month-Wise Crime Analysis" simplifies crime patterns by examining where and when crimes occur and this analysis reveals trends over different months in various locations. The Gender-Wise Analysis presents the distribution of crime victims based on gender, highlighting the number of incidents involving males and females. The Month and District-wise Analysis represent crime incidents in different districts and months.
<img src="Images/Screenshot_77.png" width=900 height=400>

3.`Race wise analysis` shows Victim_Race Of Various District and Victim With Their Race(according to description). The Victim Race of Various Districts analysis shows the racial composition of crime victims across different geographical districts. The Victim with Their Race analysis delves into the relationship between crime incidents and the racial identity of the victims. 
<img src="Images/Screenshot_78.png" width=900 height=400>

4.`Weapon and Time Wise Analysis` shows Used Weapon For Crime and Time Wise Crime. The Used Weapon for Crime analysis investigates the types of weapons involved in criminal activities. The Time-Wise Crime analysis represents  crime patterns over different time periods.
<img src="Images/Screenshot_79.png" width=900 height=400>

5.`Day and Map Wise Crime` shows Day Wise analysis and Map Of Various Districts. The Day Wise Analysis explores crime incidents based on specific days of the month and the gender of the victims. And the Map Of Various Districts analysis represents crime data across districts, focusing on gender-related information to identify patterns.
<img src="Images/Screenshot_80.png" width=900 height=400>

6.`Age Wise Analysis` shows Victims With their Age, Age Of Most Victims, and Time And Age Wise Analysis. The Victims With Their Age analysis shows how many victims aged in between 20-40 and what is the race of those victims. The Age Of Most Victims analysis presents the top 10 age people who are most frequently victimized in reported crimes. And Time And Age Wise Analysis represents the relationship between the time of reported crimes and the age groups of the victims involved.
<img src="Images/Screenshot_81.png" width=900 height=400>

## Findings and Observations from the [Dashboard](https://public.tableau.com/app/profile/md.abdur.sobhan.riad/viz/Crime_analysis_16873409234090/Dashboard1?publish=yes).

1. The most occurring crime is Auto theft and the second most is Common assault.
2. Most of the victim age range in between 25-50.
3. Most of the victim races are Black and African American.
4. The analysis identifies the district of Southeast as the area with the highest number of reported crime victims.

## Build from Sources
1. Clone the repository.
```beshv
git clone https://github.com/riad5089/Crime-data-analysis.git
```
2. Install dependencies
```bash
pip freeze > requirements.txt
```
3. Download chrome webdriver from https://chromedriver.chromium.org/downloads

4. Run the scraper
```bash
Python files/crime_data.py --chromedriver_path <path_to_chromedriver>
```
5. You will get a file named Crime_data.csv containing all the required fields. Alternatively, check my scraped data here: https://github.com/riad5089/Crime-Data-Analysis-Of-Baltimore-City-USA/blob/main/Dataset/Scraped_data(Crime_analysis).csv.


