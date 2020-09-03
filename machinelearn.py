import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import accuracy_score

plan = pd.read_excel(r'C:/Users/ileoo/Desktop/ia/belezafinal.xlsx')
y = plan["deciprimeira"]
x = plan.drop('deciprimeira', axis=1)
#tr2 ct1
x_treino, x_teste, y_treino, y_test = train_test_split(x, y, test_size = 0.3)

modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)

resultado = modelo.score(x_teste, y_test)
print("porcentagem {}".format(resultado))

y_pred = y_test.replace([3, 2], 1)
print(accuracy_score(y_test, y_pred))
