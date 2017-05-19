# Clustering_Foods_Based_On_Taste_Profiles
Using a data set of taste similarities to cluster differnt types of food. 
README
Project2
You can run the code using by navigating to the project2 outer folder and executing the python3 main.py command. This will execute the clustering code and plot the out put. I made the assumption that you have the srep-00196-s2.csv file in the folder. I have included it in the folder downloaded from Janux web site.  

THE CODE:
To keep track of what was actually happening I selected to save the data files as I manipulated the data into the numpy arrays. You end up with cleaned data called data and a pivot file that creates a distance matrix. Each row of the distance matrix is compressed together to create a feature vector used to cluster.  I settled on Kmeans clustering with 7 clusters. I also completed an hierarchical clustering that is commented out. For speed and as a result of the massive amount of data we use sklearns minibatch. After we cluster the data and since the vectors have over 1000 features I used PCA to convert to two dimensions. These dimensions are then plotted and out put for review. 

RESULTS
You will see the 7 clusters and description in the legend. The clusters are all fairly defined except the 6 and 7 cluster they are very closely related.   
1. These are your nuts, seeds and oils from these
2.These are citrus flavors highly acidic. You also see foods in here that tend to be cooked in high citrus flovors 
3.This is meats and high fat foods
4.These are smoked and roasted meats
5.Your fruits and berries 
6.Wines and coffee raw tea floavors
7.This contains some darker teas beer boiled meats. It is very close to cluster 6  
