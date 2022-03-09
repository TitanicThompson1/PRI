import pandas as pd
import csv
from ast import literal_eval

artists_data = pd.read_csv("../clean_dataset/artists.csv")

file_object = open("aliases.txt", "w+")

for i in range(len(artists_data.index)):

    try:
        artist_name = artists_data['artist_name'][i]
        alternate_names = artists_data['alternate_names'][i]

        arr_names = literal_eval(alternate_names)

        if len(arr_names) > 1:
            file_object.write(artist_name)
            file_object.write(", ")
            for i in range(len(arr_names)):
                file_object.write(arr_names[i])

                if i != len(arr_names) - 1:
                    file_object.write(", ")

            file_object.write("\n")
    except:
        continue

file_object.close()