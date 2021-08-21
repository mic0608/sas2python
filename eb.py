import pandas as pd

df = pd.DataFrame({'lob':list('qwerasdf),'eb':list('12345678')})
spark.createDataFrame(df).write.mode('overwrite').parquet('/FileStore/table/eb')

                              
for i in range(10000000):
  a=i
