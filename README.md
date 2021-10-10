# FIFA-FOOTBALL-PLAYER-RATING-PREDICTION

[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)]( https://fifa-soccer-player-rating-pred.herokuapp.com/)&nbsp;
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)&nbsp;
<img src="https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg">&nbsp;
![GitHub repo size](https://img.shields.io/github/repo-size/Shashank-Sundi/FIFA-FOOTBALL-PLAYER-RATING-PREDICTION)&nbsp;
![Lines of code](https://img.shields.io/tokei/lines/github/Shashank-Sundi/FIFA-FOOTBALL-PLAYER-RATING-PREDICTION?style=flat)

Machine Learning Project for predicting the Ratings of football players in FIFA 


<img src="static\images\guglielmo-basile-ikz8R6LGbK8-unsplash.jpg" alt="FIFA" />

## Deployment

The model has been deployed using REST API using flask, on Heroku : 
 https://fifa-soccer-player-rating-pred.herokuapp.com/

<hr>

  ## Original Dataset and Python Notebook

Database File : https://www.kaggle.com/hugomathien/soccer

Python Notebook : https://github.com/Shashank-Sundi/NOTEBOOKS/blob/main/Football%20Player%20Rating%20Prediction.ipynb

<hr>

## Project Description

| PROBLEM | MODELS USED  |LIBRARIES USED   |
| :-------- | :------- | :------------------------- |
| **Predicting the ratings of players in FIFA**| `XGBOOST,LINEAR-REG ,KMEANS ,KNN ,RANDOM FOREST ,DECISION TREE ,SVR ` | **Sklearn , Seaborn ,Pandas ,Scipy ,Sqlite3, math ,Xgboost** |

<hr>

## Project Execution

### (A) **Analysis in Jupyter Notebook**

| **Step**|**Execution of the project was carried out as given in the following steps :** |
| :--------|:-------- | 
|1|Extracted data table (PLAYER_ATTRIBUTES) form the SQL database using Sqlite3 |
|2| Validated data types of the features and analysed the statistical properties of the features
|3| Checked for null values in feature vectors. Implemented Random Sample and fequent category imputation imputation with categorical feature vectors. Imputed null values in numerical feature vectors using KNN imputer
|4| Encoded the categorical feature vectors using frequency encoding and one-hot encoding
|5| Performed EDA on data - checked the distribution of data using NPP, KDE plots ; checked for outliers via boxplots
|6| Visualised the correlation heatmap and removed highly correlated feature vectors from the data
|7| Clustered the data into 4 clusters ( based on elbow curve ) , using K-Means clustering , to train different models on each cluster 
|8|Trained and tested various models on each of the clusters ; chose the model which gave highest r2 score .
|9| Apparently xgboost gave highest r2 for all the data clusters . This also implies that there was no need to cluster the data at all
|10| Exported the xgboost model


### (B) **Building the Application in Python (in PyCharm)**

| **Step**|**Execution of the project was carried out as given in the following steps :** |
| :--------|:-------- | 
|1| Built Log Writer module , for writing the log messages in a centralised log file
|2| Built the Data Formatter module , for aggregating the inputs from the html form ; converting the input to a dataframe
|3| Buil the Valaidator module , to validate the data types of inputs , column names , length etc.
|4| Built the Preprocessing module ,for imputation , encoding and other transformations
|5| Built REST API using Flask framework ; created routes for home page and prediction , by calling all the required modules 
|6| Created the requirements.txt , Procfile , etc. and all other requirements to be satisfied for deployment.
|7| Built html pages for data input and results prediction
|8| Deployed the model on Heroku via Git Bash terminal

<hr>

## Screenshots

### **Enter the required inputs in home page and press predict button**

<img src="static\images\Homepagee.PNG" alt="FIFA" style="height: 300px; width:700px;"/>

### **The Prediction Page**

<img src="static\images\predpage.PNG" alt="FIFA" style="height: 300px; width:700px;"/>

<hr>
  
## Contact


<a href="https://www.linkedin.com/in/shashank-sundi-4b78561b1"> ![alt text](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)</a>&emsp;
<a href="https://www.instagram.com/shashank_sundi13/">![alt text](https://img.shields.io/badge/Shashank_Sundi-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)</a>&emsp;
<a href="mailto:sundi.sn@gmail.com">![alt text](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)</a>

<hr>
