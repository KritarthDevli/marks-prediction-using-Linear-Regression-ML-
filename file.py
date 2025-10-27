from sklearn.linear_model import LinearRegression #importing the model

X=[[1],[2],[3],[4],[5]] #old data of students
y=[40,50,65,75,90]

model=LinearRegression()
model.fit(X,y)

hours=float(input("Enter total hours you studies :"))
predicted_marks=model.predict([[hours]])

print(f"Based on {hours} you may score around {predicted_marks}, Thank you")
