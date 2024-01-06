import pandas as pd
from constants import FILE_PATH
from io_utils import write_txt

#added index_col=0 to drop the index column
data = pd.read_csv(FILE_PATH, index_col=0)
#drop the null rows from data horizontaly (where all collumns are null, in this case context)
#empty rows in a collumn a treated as np.nan (float) => error when joining the list by \n
data = data.dropna(axis=0, how="all")
#transform context data to list to join with a new line delimiter
data = data["context"].tolist()
for i, row in enumerate(data):
    #write output to txt file
    write_txt(f"staging/extracted/context{i}.txt", row)