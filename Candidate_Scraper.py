import os
from urllib import request


import time


# find link element 

# get download link
download_link='https://www.data.gouv.fr/fr/datasets/r/8597b9e5-162b-472a-a27e-fe1b25eb0c35'

destination_filename=os.path.join(os.curdir,"Candidates_data.xlsx")
response=request.urlretrieve(download_link,destination_filename)
time.sleep(3)
