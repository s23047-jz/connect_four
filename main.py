"""
Authors:
    Jakub Żurawski: https://github.com/s23047-jz/NAI/

"""
import os
import json
import pandas as pd

from classes.movie_engine import MovieEngine


def convert_excel_data_to_json():
    """
    Reads data from excel file and save them as json file.
    """
    data_path = os.path.join('data')
    excel_data = pd.read_excel(os.path.join(data_path, 'movie_data.xlsx'), header=None)

    data_dict = {}
    for row in excel_data.itertuples(index=False, name=None):
        name = row[0]
        movies_dict = dict()
        for i in range(1, len(row), 2):
            movie_name = row[i]
            score = row[i + 1]

            if pd.notna(movie_name) and pd.notna(score):
                movies_dict[movie_name] = score
        data_dict[name] = movies_dict


    with open(os.path.join(data_path, "movie_data.json"), "w", encoding="utf-8") as json_file:
        json.dump(data_dict, json_file, ensure_ascii=False, indent=2)


def main():
    # convert_excel_data_to_json()
    # movie_engine = MovieEngine("Paweł Czapiewski", 5, 5, "euclidean")
    movie_engine = MovieEngine("Daniel Klimowski", 5, 5, "euclidean")
    movie_engine.init()


if __name__ == "__main__":
    main()
