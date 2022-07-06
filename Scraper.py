import os
import time
import pandas as pd
import numpy as np
from urllib import request
download_link='https://www.data.gouv.fr/fr/datasets/r/3cf49bf4-c171-4328-b002-fea995cb85d8'
# download the data to the folder Data_First_Round
destination_filename=os.path.join(os.curdir,"Data_First_Round","Candidates_data.xlsx")
response=request.urlretrieve(download_link,destination_filename)




