import pandas as pd
df = pd.DataFrame({'a':list('1234'),'b':list('asdf')})
df = spark.createDataFrame(df)
display(df)
