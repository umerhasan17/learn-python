Seaborn plot error because pandas column is always an object. Create dataframes with numpy array forces all data to be of type objects. 

Error:
```
TypeError: Neither the `x` nor `y` variable appears to be numeric.
```
Solution:
```
cocodet_per_class['data']['Instances'] = pd.to_numeric(cocodet_per_class['data']['Instances'])
```
