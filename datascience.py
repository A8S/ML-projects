from sklearn import tree
#[height, weight, shoe size]
# X is a list of list
#we are giving the info of male and female with their respective physical details
X=[[181,80,40],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,51,37],[171,75,42],[181,85,43],[2000,400,5333],[120,20,16]]
#now we we are each component of the list with their respective gender
Y=['male','female','female','male','male','male','male','female','male','female','male','saksham','anant']
#declare a variable say "classi" that will classify the data feeded to the program
classi=tree.DecisionTreeClassifier()
classi=classi.fit(X,Y)
prediction=classi.predict([[2100,380,5000]])
print prediction[0]