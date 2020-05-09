MARATHON_DISTANCE = 42.195


def calculate_km_per_hour(km_to_run, hours_took_to_finish):
    km_per_hour = km_to_run / hours_took_to_finish
    return km_per_hour


def calculate_time_to_run(distance_to_run, km_per_hour):
    hours = distance_to_run / km_per_hour
    return hours


def print_if_can_run(target_time, actual_time):
    # זה בסדר להדפיס פה, כי זה ממש המטרה של הפונקציה.
    if actual_time <= target_time:
        print("Success! You can do it!")
    else:
        print("You can't do it :(")


time = float(input("How many hours did it take to finish a 5km run? "))
km_per_hour = calculate_km_per_hour(5, time)
hours_to_finish = calculate_time_to_run(MARATHON_DISTANCE, km_per_hour)
print_if_can_run(3, hours_to_finish)
