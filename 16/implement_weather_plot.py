from weather import Weather
import matplotlib.pyplot as plt


def make_index_key_pair(weather_data):
    """
    Input: weather data (dict - key: header, value: data points)
    Output: display list of keys with corresponding index so user can choose which key to pick using the index"""
    print("-----")
    print("You have chosen to plot:")
    index_to_key = {}
    i = 0
    for key in weather_data.keys():
        index_to_key[i] = key
        print('{0:<2} - {1}'.format(i, key))
        i += 1
    print("-----")

    return index_to_key


def invalid_index(indices, weather_data, index_key_pair):
    """
    :param indices: indices that user has input as a way to select the keys in weather data dict
    :param weather_data: dict of weather data (key: header, value: data points)
    :param index_key_pair: dict of index to key (key: index, value: weather data key)
    :return: True if any index was found to be invalid, False if none is invalid
    """
    if len(indices) != 2:
        print("You did not enter two numbers.")
        return True
    for position, index in enumerate(indices):
        # Test for non-integer index
        try:
            index_int = int(index)
        except ValueError:
            print(index.lstrip() + " is not an integer")
            return True
        else:

            # Test for index not belonging to available indices
            if index_int not in index_key_pair:
                print(index.lstrip() + ' does not belong to the available indices')
                return True
            else:

                # Test whether key corresponding to index has non-numeric data points in weather data
                weather_key = index_key_pair[index_int]
                data_values = weather_data[weather_key]
                sample_value = data_values[0]
                try:
                    float(sample_value)
                except ValueError:
                    print(weather_key + ' does not contain numerical values')
                    return True

                # Modify chosen index in place with the integer value of index
                else:
                    indices[position] = index_int

    # When for loop ends (on invalid input), return False to break input loop
    return False


def select_keys_for_shading(weather_data):
    """
    Input: weather data (dict)
    Output: available keys to be selected for in-between shading, each with a corresponding index so user can choose
    """
    # Return (and also display for user) the available keys and their corresponding index
    index_key_pair = make_index_key_pair(weather_data)

    continue_flag = True
    while continue_flag:
        # Prompt user to input 2 indices/keys to draw shading between
        chosen_indices = input("Please select the 2 plots you want to shade using the corresponding numbers: ")
        chosen_indices = chosen_indices.split(',')

        # Prompt user for input again if invalid indices were found, otherwise continue the program with chosen indices
        # already converted to integers
        continue_flag = invalid_index(chosen_indices, weather_data, index_key_pair)

    # Convert chosen indices to chosen keys
    chosen_keys = [index_key_pair[index] for index in chosen_indices]
    return chosen_keys


def main():
    filenames = ["death_valley_2014.csv", "sitka_weather_2014.csv"]

    for filename in filenames:
        # Create Weather object from corresponding CSV file
        location_weather = Weather(filename)

        # Get weather data from CSV file
        location_weather.set_weather_data()

        # Assign dates (list) and weather data (dict) attributes to shorter variables
        dates = location_weather.dates
        weather_data = location_weather.weather_data

        # Do not plot shading if user had initially chosen less than 2 categories (aside from date)
        if len(weather_data) < 2:
            print("Number of available data categories is less than that required for plotting shading (2). "
                  "Shading not plotted.")
        else:
            is_shading = input("Do you want to plot shading between any 2 lines (y/n)? ")
            if is_shading.lower() == 'y':
                # Ask user to pick 2 keys to shade between and store those keys
                chosen_keys_for_shading = select_keys_for_shading(weather_data)

                # From the 2 chosen keys, generate 2 lists of data points between which shading can be drawn
                data1, data2 = [weather_data[key] for key in chosen_keys_for_shading]

                # Plot shading
                plt.fill_between(dates, data2, data1, facecolor='blue', alpha=0.1)

        # Plot weather data originally chosen by user
        if len(filenames) > 1:
            location_weather.plot_weather_data(multiple=True)
        else:
            location_weather.plot_weather_data()

    plt.show()


main()
