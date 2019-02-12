import numpy as np
import pandas as pd
from sklearn import datasets, cluster, metrics
import seaborn as sns
# %matplotlib inline


iris = datasets.load_iris()
results = {k: cluster.KMeans(k, random_state=42).fit_predict(iris.data) for k in [3, 2, 4, 6]}


np.bincount(results[3])
metrics.confusion_matrix(iris.target, np.array([1, 0, 2])[results[3]])

1 - 16 / 150 # Acurácia

X = pd.DataFrame(iris.data, columns=iris.feature_names)

sns.pairplot(X.assign(target=iris.target_names[iris.target]),
             hue="target",
             x_vars=X.columns, y_vars=X.columns)

sns.pairplot(X.assign(predicted=np.array(["versicolor-like cluster",
                                          "setosa-like cluster",
                                          "virginica-like cluster"])[results[3]]),
             hue="predicted",
             x_vars=X.columns, y_vars=X.columns)
print(sns)
print(dir(sns))

