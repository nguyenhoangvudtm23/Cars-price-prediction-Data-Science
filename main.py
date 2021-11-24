import pandas as pd

df = pd.read_csv('cars_final_v2.csv')

# Replace labels in vEengineType
df['vEengineType'].value_counts()
df['vEengineType'] = pd.factorize(df.vEengineType)[0]
# Replace labels in vehicleTransmission
df['vehicleTransmission'].value_counts()
df['vehicleTransmission'] = pd.factorize(df.vehicleTransmission)[0]
# Process slash labels in weightTotal
df['weightTotal'].value_counts()
df['weightTotal'] = df['weightTotal'].replace(to_replace='-', value=0)
# Replace nan values in wheelbase
df['wheelbase'].value_counts()
df['wheelbase'].isna().sum()
df['wheelbase'] = df['wheelbase'].replace(to_replace=np.nan, value=0)
# Width does not have anything to replace
