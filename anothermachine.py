from sklearn.linear_model import Perceptron
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

plan = pd.read_excel(r'C:/Users/ileoo/Desktop/ia/belezafinal.xlsx')
y = plan["deciprimeira"]
x = plan.drop('deciprimeira', axis=1)

x = PolynomialFeatures(interaction_only=True).fit_transform(x).astype(int)
clf = Perceptron(fit_intercept=False, max_iter=10, tol=None,shuffle=False).fit(x, y)
clf.predict(x)
print(clf.score(x, y))