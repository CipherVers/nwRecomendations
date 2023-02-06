import json
import pandas as pd

jsonFiles = ["yelp_academic_dataset_business.json",
             "yelp_academic_dataset_checkin.json",
             "yelp_academic_dataset_review.json",
             "yelp_academic_dataset_tip.json",
             "yelp_academic_dataset_user.json"]
             
#This code loops through each JSON file in the jsonFiles list, reads each JSON line, converts it to a dictionary, and stores it in the batch list. It then converts the batch list to a dataframe and stores that dataframe as a csv file in the data folder. Finally, it prints out the dataframe. 

for jsonFile in jsonFiles:
    #Replace the .json extension with .csv
    csv_file = jsonFile.replace("json","csv")
    #Open the JSON file
    with open(jsonFile,"r") as yelp_f:
        #Create an empty list to store the JSON dictionaries by line
        batch = []
        #Loop through each line in the JSON file
        for line in yelp_f.readlines():
            #Convert the line to a dictionary
            jessy = json.loads(line)
            #Store the dictionary in the batch list
            batch.append(jessy)
        #Convert the batch list to a dataframe
        df = pd.DataFrame(batch)
        #Save the dataframe as a csv file in the data folder
        df.to_csv("data/"+csv_file)
        #Print out the dataframe
        print(df)