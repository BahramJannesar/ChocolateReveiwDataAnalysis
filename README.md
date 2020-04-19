### Whats is Chocolate ?
Chocolate is a preparation of roasted and ground [cacao](https://en.wikipedia.org/wiki/Theobroma_cacao) seeds that is made in the form of a liquid, paste, or in a block, which may also be used as a flavoring ingredient in other foods. The earliest signs of use are associated with Olmec sites (within what would become Mexico’s post-colonial territory) suggesting consumption of chocolate beverages, dating from 19 centuries BCE.The majority of Mesoamerican people made chocolate beverages, including the Maya and Aztecs.The word chocolate is derived from the Spanish word chocolate, deriving in turn from the Classical Nahuatl word xocolātl.

![Chocolate](https://github.com/BahramJannesar/Chocolate_reveiw_data_analysis/blob/master/image/istock-522735736.jpg)

### Cholocate Review 
Chocolate is one of the most popular candies in the world . because of this , the most important part of this bussiness is chocolate review , Up to 10 reputable sites,paid attention to the chocolate review issue like these website :

* http://www.chocolatereviews.co.uk/

* https://www.c-spot.com/

* http://flavorsofcacao.com/index.html

### Chocolate Review Data Analysis
According to our research, many people have done analyzes on chocolate review like [Exploratory Data Analysis with Chocolate](https://www.kaggle.com/thedatabeast/exploratory-data-analysis-with-chocolate) , but all of  their datasets are imperfect .

This website was launched by Brady Brelinski , has a very dirty dataset for chocolate review [dataset](http://flavorsofcacao.com/chocolate_database.html) , we scrape this data and presented a new analysis on it .

We have multiple questions to answer, in the below list we answer most important informations that possible to answer.
1. Where are the best cocoa beans grown?
2. Which countries produce the highest-rated bars?
3. Who create best Chocolate bars?

In this analysis we want to find out which atrributes lead us to create best chocolate taste. only possible measure in our dataset is Rating. In continue we'll start to EDA(Exploratory data analysis) with plotting columns againt each other and numeric stats.

### Data Set

#### Columns before cleaning dataset :

* REF
* Company (Manufacturer)
* Company Location
* Review Date
* Country of Bean Origin
* Specific Bean Origin or Bar Name
* Cocoa Percent
* Ingredients
* Most Memorable Characteristics
* Rating

![before cleaning](https://github.com/BahramJannesar/Chocolate_reveiw_data_analysis/blob/master/image/table_before_cleaning.png)

#### Columns after cleaning dataset :

* ref
* company
* company_location
* review_date
* country_of_bean_origin
* specific_bean_origin_or_bar_name
* cocoa_percent
* rating
* counts_of_ingredients
* beans	cocoa_butter
* vanilla
* lecithin
* salt
* sugar
* sweetener_without_sugar
* first_taste
* second_taste
* third_taste
* fourth_taste


![before cleaning](https://github.com/BahramJannesar/Chocolate_reveiw_data_analysis/blob/master/image/table1.png)


![before cleaning](https://github.com/BahramJannesar/Chocolate_reveiw_data_analysis/blob/master/image/table2.png)

Due to the dirty and indistinguishable dataset of taste, we had to separate and create a special data set for the tastes to analyze the data information.

convert these colmuns to the readable columns :

#### before converting 

* First taste
* Second taste
* Third taste
* Fourth taste

![before cleaning](https://github.com/BahramJannesar/Chocolate_reveiw_data_analysis/blob/master/image/tastte%20table.png)

#### after converting :

* taste	
* count of taste

![before cleaning](https://github.com/BahramJannesar/Chocolate_reveiw_data_analysis/blob/master/image/taste_table12.png)














