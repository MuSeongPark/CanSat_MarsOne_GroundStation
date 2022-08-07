import pandas as pd
import numpy as np


columns = ["Date", "CO2", "Acceleration", "Latitude", "Longitude", "Altitude", "Ejection"]


df = pd.DataFrame(columns=columns)

new_df = ["234", "2", "34.2", "132.4", "12", np.NaN]
df.loc[len(df)] = ["date1"] + new_df


print(df)


print(new_df[:-1])


print([np.NAN] * 7)

print([None] * 7)

print(np.NaN==None)