from sklearn import tree

#Features are : Height, Weight, Shoe_Size

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
    [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], 
    [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

classifier = tree.DecisionTreeClassifier() # Using the decissiontree classifer to classify our data(female or male) 

classifier = classifier.fit(X,Y) # Training the tree on the above given data set.

print("Welcome to gender classifier. Please fillout the following:")

UIHeight    = input("Height :")
UIWeight    = input("Weight :")
UIShoeSize  = input("Shoe_Size :")

prediction  = classifier.predict([[UIHeight,UIWeight,UIShoeSize]])

print("Gender = ",prediction)