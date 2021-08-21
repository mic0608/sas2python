import pandas as pd

df = pd.DataFrame({'lob':list('qwerasdf),'life':list('12345678')})
spark.createDataFrame(df).write.mode('overwrite').parquet('/FileStore/table/life')
