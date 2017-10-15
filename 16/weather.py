import csv
from datetime import datetime
import matplotlib.pyplot as plt
from random import randint


class Weather:
    def __init__(self, filename):
        self.filename = filename
        self.dates = None
        self.weather_data = None

    def set_weather_data(self):
        """
        :param filename: Name of weather-related csv file to be parsed for weather info
        :return: 3 lists: lists of user-chosen weather-related info
        """
        def display_headers(headers):
            """
            Input: header list to be displayed
            Output: display all headers with indices next to them so user can see which index to choose"""
            print("Below are the weather information for your location")
            print("-----")
            for index, header in enumerate(headers):
                print('{0:<2} - {h}'.format(index, h=header))
            print("-----")

        def invalid_indices(indices, headers):
            """
            Input: list of index/indices
            Output: True if any of the indices are in the wrong format (positive integers) or does not belong to the
            list of available indices; False otherwise, along with the indices list as integers
            """
            indices_int = []
            available_indices = range(len(headers))
            for index in indices:
                try:
                    index_int = int(index)
                except ValueError:
                    print(index.lstrip() + " is not an integer")
                    return [True]
                else:
                    if index_int not in available_indices:
                        print(index.lstrip() + " does not belong to available indices")
                        return [True]
                    else:
                        indices_int.append(index_int)
            return [False, indices_int]

        def select_headers(headers):
            """
            Input: list of available headers that user can choose from
            Output: indices of the headers that user has selected, starting with date/time index"""
            while True:
                date_index = [input("Please select the number correspond to the date/time info: ")]
                date_index = invalid_indices(date_index, headers)
                if date_index[0]:
                    continue
                else:
                    date_index = date_index[1]
                    while True:
                        selected_indices = input("Please select the numbers correspond to the weather info you want "
                                                 "to export (separated by comma): ")
                        split_indices = selected_indices.split(",")
                        split_indices = invalid_indices(split_indices, headers)
                        if split_indices[0]:
                            continue
                        else:
                            split_indices = split_indices[1]
                            if 0 in split_indices:
                                print("One of your indices were zero.")
                                continue
                            return date_index + split_indices

        def export_data(reader_object, headers, indices):
            weather_data = {}
            date = []
            date_index = indices[0]

            for row in reader_object:
                for position, index in enumerate(indices):
                    value = row[index]
                    # print("value before checking:", value)
                    if not value:
                        if index == date_index:
                            break
                        else:
                            header = headers[index]
                            print("Missing " + header + " value on " + row[date_index])
                            del date[-1]
                            previous_indices = indices[1:position]
                            previous_headers = [headers[index] for index in previous_indices]
                            for header in previous_headers:
                                if header in weather_data:
                                    del weather_data[header][-1]
                            break
                    else:
                        if index == date_index:
                            value = datetime.strptime(value, "%Y-%m-%d")
                            date.append(value)
                        else:
                            header = headers[index]
                            try:
                                value = float(value)
                            except ValueError:
                                pass
                            finally:
                                if header in weather_data:
                                    weather_data[header].append(value)
                                else:
                                    weather_data[header] = [value]
            self.dates = date
            self.weather_data = weather_data

        with open(self.filename) as file_object:
            print("=====")
            print("Opening " + self.filename)
            # Convert file object into CSV reader object
            reader_object = csv.reader(file_object)

            # Collect header of CSV file and display them so that user can choose which headers to plot
            headers = next(reader_object)
            headers = [header.strip() for header in headers]
            display_headers(headers)
            indices = select_headers(headers)

            # Collect data from the rest of the CSV object with the headers that user has chosen
            # Store data in dates (list) and weather_data (dict) attributes of Weather class
            export_data(reader_object, headers, indices)

    def plot_weather_data(self, multiple=False):
        """
        Input: list of dates and weather information dictionary
        Output: plot showing weather information versus date
        """
        for key, values in self.weather_data.items():
            if multiple:
                key = self.filename[:-4] + ": " + key
            try:
                float(values[0])
            except ValueError:
                plt.xlabel(key + " does not contain numerical data, and won't be plotted")
            else:
                plt.plot(self.dates, values, label=key)
                plt.legend(shadow=True)


if __name__ == '__main__':
    sitka_2014 = Weather("sitka_weather_2014.csv")
    sitka_2014.set_weather_data()
    sitka_2014.plot_weather_data()
