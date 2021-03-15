# DS_Prod_QA

# SQUAD QA Bot.md

 ![](https://img.shields.io/github/release/pandao/editor.md.svg) 


**Table of Contents**

[TOCM]


##About the Project
We are working with the SQUAD dataset which is  a reading comprehension dataset, consisting of questions posed by crowd workers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable.  

With the Squad dataset, our intention is to train a model that can quickly answer queries. A lot of times people must skim through whole articles/books/pages to be able to retrieve answers to simple questions such as "When did Socrates die?". This is tedious and time-consuming. Instead, imagine if you had an application available to you that takes an article, a set of questions and simply returns you the answer to each of your questions. Simple and quick, right? 

##Infrastructure
On the infrastructure side, instead of locally experimenting and then facing difficulty later when shifting to the cloud, we immediately jumped to using Azure as one of the mediums in our project.

    We started off by establishing a simple Blob Storage where we wrote the appropriate script to upload the Squad Dataset in the unlikely case, it is removed from the internet. We then proceeded to our actual storage medium that would store datapoints and be utilized for serving as the source of data to our models. Initially, we chose SQL and dumped our records into Azure SQL Database. However, upon a bit of exploration, we found out that NoSQL databases are generally used in big data given their faster retrieval speeds and ability to scale easier comparatively. Thus, we shifted to using Azure Cosmos DB that is a NoSQL Database. The data was split into its train and test components and uploaded into two different containers in Azure Cosmos. 
    Then, we moved onto forming an API, using the Fast Api, that would serve as the medium of interaction between the users and the models. For test purposes, we wrapped a pre-trained models using the Fast Api and configured it to respond to live scenarios. What does that mean? In a live scenario, people, rather than reading through whole articles, feed the specific article into the API along with the questions they want answered. The API would, in turn, feed the received data into the model and return the predicted answers to the user(s). We incorporated this functionality into our Fast Api. The User enters the title of the article on Wikipedia along with their questions and the api returns the predicted answer.
    Last but not the least, we deployed this API, with the embedded model in it, using the docker. The image file has uploaded in the repository. Therefore, it is easily experimentable. 
##Experimental Models
On the model experimentation side, we achieved the following:

    Understanding the data and getting an insight into the data to get comfortable with the dataset. 
    Converted dataset available in JSON format into standard panda’s data frame. 
    Performed basic text analytics. 
    Perform sentence embeddings that provide vectorized semantic sentence representations. This is done using InferScent. 
    Calculate cosine similarity and Euclidean distance with each sentence in the context and predict the output with minimum distance. 
    Using these distance vector and cosine similarity, made feature vector. 
    Apply Multinomial Logistic regression, Random Forest Classifier, and XGBClassifier on that feature vector. 

Method Used  | Train Accuracy | Test Accuracy
------------- | -------------
Multinomial Logistic regression   | Train Accuracy | 0.4276022086466165
Multinomial Logistic regression  | Test Accuracy | 0.4317434210526316
Random Forest    | Train Accuracy | 0.7173695958646616
Random Forest   | Test Accuracy | 0.5330122180451128
XGBoost   | Train Accuracy | 0.6573073308270677
XGBoost  | Test Accuracy | 0.5615601503759399 

##Way Forward
###Infrastructure
On the infrastructure side, the following are the aims:
-	Create the needed link and pipeline between the Data Storage and Api. 
The pipeline would facilitate real-time and immediate provision of data to whichever type of model that needs to be trained. The pipeline would, further, facilitate re-training of the models once new data keeps entering the Data Storage. 
- Investigate Dagster and Azure Pipelines for the construction of this path. 
- Extend the pipeline to work end-to-end. That is to say, from the provision of data to training and re-training of models and finally, to the automated deployment of the latest model. 

###Experimentation Models
-	We will be using BERT (Bidirectional Encoder Representations from Transformers) pre-trained model, fine-tune it as per our data and add a custom model to it to increase its benchmark accuracy on our dataset.
The accuracy we achieved in our model above is low as many advanced techniques are already applied with greater accuracy, but using these models we have learnt and explore our dataset at a lower level which will help in fine-tuning and enhancing accuracy in later steps

#Thank you
