import temperatures
import pprint

if __name__ == "__main__":

    # To avoid having the list of temps in the answers I have imported this from the other file (we will
    # cover this later)
    temps = temperatures.temps

    # Ex 1 Create a separate list of temperatures for each of the locations

    # Create empty lists that will hold the values
    times = []
    chicken_temps = []
    barn_temps = []
    greenhouse_temps = []

    # We are going to loop over the temperatures and split on the comma (,) to give us each of the fields in a list
    # i.e. we will get [dates, chicken_temp, barn_temp, greenhouse_temp]
    for temp in temps:
        temp_tokens = temp.split(sep=",")

        # Dates is index 0, chicken is 1, barn is 2, greenhouse is 3
        chicken_temps.append(float(temp_tokens[1]))
        barn_temps.append(float(temp_tokens[2]))
        greenhouse_temps.append(float(temp_tokens[3]))

    # We will print one of them so that we can see that it has done what we want
    print("Chicken temps: %s" % chicken_temps)

    # Wait for input
    input()
    # Ex 2 Create a list of the times to the nearest minute
    # We loop over the dates again this time building up the times

    for temp in temps:
        # Split as above and get the first field for the date
        date_field = temp.split(sep=",")[0]

        # now we are going to use slicing to get the times
        time_string = date_field[-15:]

        # split this string again
        hour, minute, seconds = time_string.split(sep=":")

        # we now rejoin the components
        calc_time = "%s:%s" % (hour, minute)

        times.append(calc_time)

    # Again print to ensure it is as we expect
    print("Times: %s" % times)

    # Wait before continuing
    input()
    # Ex 3 Find the highest temperature for each of the Barn, Greenhouse and Chickens

    chicken_max = -100
    for temp in chicken_temps:
        if temp > chicken_max:
            chicken_max = temp

    barn_max = -100
    for temp in barn_temps:
        if temp > barn_max:
            barn_max = temp

    greenhouse_max = -100
    for temp in greenhouse_temps:
        if temp > greenhouse_max:
            greenhouse_max = temp
    print("Max values: Chicken: %s, Barn: %s, Greenhouse: %s" % (chicken_max, barn_max, greenhouse_max))

    # Wait before continuing
    input()

    # Actually there is an easier way of doing this using the max() built-in function
    chicken_max = max(chicken_temps)
    barn_max = max(barn_temps)
    greenhouse_max = max(greenhouse_temps)

    print("Max values: Chicken: %s, Barn: %s, Greenhouse: %s" % (chicken_max, barn_max, greenhouse_max))

    # Wait before continuing
    input()

    # Ex 4 Find the lowest temps for each of the above

    chicken_min = 100
    for temp in chicken_temps:
        if temp < chicken_min:
            chicken_min = temp

    barn_min = 100
    for temp in barn_temps:
        if temp < barn_min:
            barn_min = temp

    greenhouse_min = 100
    for temp in greenhouse_temps:
        if temp < greenhouse_min:
            greenhouse_min = temp
    print("Min values: Chicken: %s, Barn: %s, Greenhouse: %s" % (chicken_min, barn_min, greenhouse_min))

    # Wait before continuing
    input()

    # And again there is a easier way to do this using min() built-in function
    chicken_min = min(chicken_temps)
    barn_min = min(barn_temps)
    greenhouse_min = min(greenhouse_temps)
    print("Min values: Chicken: %s, Barn: %s, Greenhouse: %s" % (chicken_min, barn_min, greenhouse_min))

    # Wait before continuing
    input()

    # Ex 5 Calculate the Mean, Median and Mode for each location
    #       http://www.bbc.co.uk/bitesize/ks2/maths/data/mode_median_mean_range/read/1/

    # Mean is just the sum of the temps divided by the number (i.e. length of list)
    barn_mean = sum(barn_temps) / len(barn_temps)
    chicken_mean = sum(chicken_temps) / len(chicken_temps)
    greenhouse_mean = sum(greenhouse_temps) / len(chicken_temps)

    print("Mean temps: Chicken: %s, Barn: %s, Greenhouse: %s" % (chicken_mean, barn_mean, greenhouse_mean))

    # Wait before continuing
    input()

    # To calculate the mode we are going to use a dictionary to count the occurences of each temperature
    # i.e. the temp will be the key and the value will be how many times that value appears
    barn_temps_counter = {}

    # We loop over each temperature in turn
    for temp in barn_temps:

        # If the temperature is already in the keys then we increase the count by 1
        if temp in barn_temps_counter:
            barn_temps_counter[temp] += 1
        # Otherwise (the temp is not in the dictionary therefore) we create the entry and set it to be 1
        else:
            barn_temps_counter[temp] = 1

    # we then need two variables
    # 1st a list to hold the temps that has the most counts
    barn_modal_temp = []

    # 2nd the number of times that temperature occurs
    barn_modal_count = 0

    # we then loop over the keys of the dictionary (i.e. the temps)
    for temp in barn_temps_counter:

        # We get teh number of times the temperature occurs
        temp_count = barn_temps_counter[temp]

        # The count obtained (i.e. temp_count) is equal to the current model count (barn_modal_temp) then we add the temperature to the
        # list of temperatures (i.e. barn_modal_temp)
        if temp_count == barn_modal_count:
            barn_modal_temp.append(temp)

        # If the count is greater that the current model count then
        elif temp_count > barn_modal_count:
            # We now set the current model count to be the count obtained
            barn_modal_count = temp_count
            # Empty the list of temperatures by creating a new list
            barn_modal_temp = []
            # Now add the new temp to the barn_modal temperature list
            barn_modal_temp.append(temp)

    # We could then use the same method to calculate the mode values for other temps

    print("Barn Temp Mode: %s which occurs: %s times" % (barn_modal_temp, barn_modal_count))

    # Wait before continuing
    input()

    # Find the median value

    # work out how long the array is
    barn_length = len(barn_temps)

    # we need to handle even and odd sets differently
    if barn_length % 2 == 0:

        # This is the more complicated case, we have to find the two in the middle and take the mean of that value
        # (Corrected from the discussions during the course)
        mid_point = barn_length // 2

        val_1 = barn_temps[mid_point - 1]
        val_2 = barn_temps[mid_point]

        barn_median = (val_1 + val_2) / 2
    else:
        # If it is odd then the mean is the value at the length//2 index of the sorted list
        barn_median = sorted(barn_temps)[barn_length // 2]

    print("Barn median: %s" % barn_median)

    # Wait before continuing
    input()

    # Ex 6 Create a dictionary using this data

    # What dictionary you create is upto you but I am going to create a dictionary of dictionary where the first is keyed by
    # location and the second by the time

    # Create empty map
    temps = {}
    temps["barn"] = {}
    temps["chicken"] = {}
    temps["greenhouse"] = {}

    for time in times:
        # We get the index of the time
        index = times.index(time)

        temps["barn"][time] = barn_temps[index]
        temps["chicken"][time] = chicken_temps[index]
        temps["greenhouse"][time] = greenhouse_temps[index]

    print("Temps map:")
    # pprint.pprint will allow us to "pretty print" the map
    pprint.pprint(temps)
