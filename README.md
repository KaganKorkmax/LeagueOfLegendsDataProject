<h1>Motivation</h1>

For my project, I aimed to analyze my interaction with competitive gaming and performance improvement over time. Since League of Legends (LoL) is my primary game of focus, I decided to base the analysis on my match and champion data.

The motivation for this project is to gain deeper insights into my gameplay patterns, including:

The champions I play most frequently.
* My match performances.
* My rank progression across different seasons.
* By analyzing this data, I aim to identify trends in my gameplay and areas for improvement.



<h1>Tools</h1>

I used the following tools and libraries to collect, process, and analyze my data:

* Python : The primary programming language for data scraping, cleaning, and analysis.
* Selenium : For automating data scraping from the web, including match history and champion data.
* Pandas : For data cleaning, structuring, and transformation.
* Matplotlib and Seaborn : For data visualization, including bar plots, line graphs, and scatter plots.


<h1>Data Source</h1>

The data for this project comes from a single primary source:

* OP.GG Match and Champion Data : All data was scraped directly from the OP.GG website using Selenium automation scripts. This includes:
* Match Data : Match dates, K/D/A ratios, ranks, and performance metrics like CS (creep score).


<h1>Data Processing</h1>


<h2>Match Data</h2>

* Rank Mapping: Converted ranks such as "Silver 2" or "Gold 4" into numerical values for analysis.
* Filtering Invalid Matches: Dropped rows with missing or "N/A" values to focus only on valid matches.

<h2>Champion Data</h2>

* Champion Aggregation: Combined data from multiple seasons for the same champion to calculate total games played and averaged win rates.
* Filtering: Dropped champions with zero win rates or games played.

You can access my dataset and code related to it from : https://github.com/KaganKorkmax/LeagueOfLegendsDataProject/tree/main/DATA



<h1>Data Visualizations</h1>

* Seasonal Rank Progression : A bar chart showing the average rank achieved in each season.
* Total Playtime by Season : A bar chart illustrating the total hours spent playing across seasons, assuming an average game duration of 40 minutes.
* Champion Analysis : A bar chart of the top 10 most-played champions, showing games played on the x-axis and average KDA on the y-axis.
A scatter plot comparing win rates against KDA values for all champions played across seasons.
* Performance Trends Over Time : A line chart showing rank progression across individual matches in chronological order.

You can access my vizulization codes and related jpegs from : https://github.com/KaganKorkmax/LeagueOfLegendsDataProject/tree/main/Visualization


<h1>Data Analysis</h1>

* Rank Progression : Analyzed the player's rank progression over time and across seasons.
* Champion Performance : Identified the most effective champions based on win rate and KDA.
Assessed the consistency of performance across different seasons for the same champions.
* Playtime Insights : Measured the total time spent playing in each season and identified patterns in activity levels.
* Statistical Comparisons : Conducted hypothesis tests to check for significant differences in win rates or performance metrics across seasons or champions.

<h1>Conclusion</h1>

This project provided valuable insights into my gaming behavior and performance trends. By analyzing my match history and champion statistics, I identified patterns such as:

* My most effective champions.
* Peak performance periods.
* Seasonal rank progression.

The visualizations helped me better understand the areas where I can focus on improvement. The automated data collection and processing pipeline can be reused for future analyses to track progress over time.

