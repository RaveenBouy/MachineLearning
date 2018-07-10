from sklearn import tree
from sklearn.svm.libsvm import predict
from sklearn import svm
from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors.nearest_centroid import NearestCentroid

#Sample set - Features are : Height, Weight, Shoe_Size
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
    [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], 
    [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

#Classifiers
classifier_tree = tree.DecisionTreeClassifier() # Using the decission tree classifer to classify our data(female or male) 
classifier_svm  = svm.SVC() # Support vector machine classifier
classifier_sgd  = SGDClassifier(loss="hinge", penalty="l2") # Stochastic Gradient descent classifier 
classifier_mlc  = MLPClassifier(solver='lbfgs', alpha=1e-5, 
                    hidden_layer_sizes=(5, 2), random_state=1) # Neural Network classifier
classifier_nn   = NearestCentroid() # Using Nearest neighbor classifier


#Training models
classifier_tree = classifier_tree.fit(X,Y)  # Training the tree on the sample data set.
classifier_svm  = classifier_svm.fit(X,Y)   # Training the SVM on the sample data set.
classifier_sgd  = classifier_sgd.fit(X,Y)   # Training the SGD on the sample data set.
classifier_mlc  = classifier_mlc.fit(X,Y)   # Training the sample set on multi-layer perceptron algorithm.
classifier_nn   = classifier_nn.fit(X,Y)    # Training the NN classider on given data

print("Welcome to gender classifier. Please fillout the following:")

UIHeight    = input("Height :")
UIWeight    = input("Weight :")
UIShoeSize  = input("Shoe_Size :")

#Predicting the given value
prediction_tree = classifier_tree.predict([[UIHeight, UIWeight, UIShoeSize]])
prediction_svm  = classifier_svm.predict([[UIHeight, UIWeight, UIShoeSize]])
prediction_sgd  = classifier_sgd.predict([[int(UIHeight), int(UIWeight), int(UIShoeSize)]])
prediction_mlp  = classifier_mlc.predict([[int(UIHeight), int(UIWeight), int(UIShoeSize)]])
prediction_nn   = classifier_nn.predict([[UIHeight,UIWeight,UIShoeSize]])

#Printing the prediction
print("Decision Tree : Gender = ",prediction_tree)
print("Support Vector Machines : Gender = ", prediction_svm)
print("Stochastic gradient descent : Gender = ", prediction_sgd)
print("Multi-Layer Perceptron : Gender = ", prediction_mlp)
print("Nearest Neighbor : Gender = ", prediction_nn)

#Based on the provied few sample data, Nearest neighbour algorithm was the most successful candidate. Decision tree, the runners up.