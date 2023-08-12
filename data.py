import pandas as pd
import re
import sheets

data = pd.read_csv(sheets.url)
data['Handle'] = data['Handle'].str.strip().str.lower()


def emailToRoll(email):
    if matches := re.search(r"^(.+)@iiitl\.ac\.in", email, re.IGNORECASE):
        return matches.group(1)


data.drop(['Timestamp'], axis=1, inplace=True)
data['Email Address'] = data['Email Address'].apply(emailToRoll)
data.rename(columns={'Email Address': 'Roll Number'}, inplace=True)

grouped = data.groupby('Contest ID')

cid_data = {}

for name, group in grouped:
    group.drop(['Contest ID'], axis=1, inplace=True)
    cid_data[name] = group

__all__ = ['cid_data']
