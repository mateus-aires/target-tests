import pandas as pd

# Filtering data to only include billing values above zero
df = pd.read_json("dados.json")
billing_df = df[df['valor'] > 0].reset_index(drop=True)

# Getting the answer by implementing my own functions:
def get_media(df, label):
  sum = 0
  n = len(df)
  for i in range(n):
    sum += df[label][i]
  return sum / n


def get_billing_info(df, label):
  series = df[label]

  biggest = 0
  media = get_media(df, label)
  smallest = series[0]
  drop_indexes = []

  for i in range(len(series)):
    if series[i] < smallest:
      smallest = series[i]
    if series[i] > biggest:
      biggest = series[i]
    if series[i] <= media:
      drop_indexes.append(i)

  result = series.drop(labels = drop_indexes)

  return {'Smallest': smallest,
          'Biggest': biggest,
          'Above billing average days': result}

print(get_billing_info(billing_df, 'valor'))

# Getting the answer by using already implemented pandas functions

def get_billing_info2(df, label):
  series = df[label]

  biggest = series.max()
  media = series.mean()
  smallest = series.min()

  result = series[series > media]

  return {'Smallest': smallest,
          'Biggest': biggest,
          'Above billing average days': result}


print(get_billing_info2(billing_df, 'valor'))
