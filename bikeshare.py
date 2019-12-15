import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Function to get user's input in order to filter the data
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # User input for city (chicago, new york city, washington)
    # While loop and try statement to handle invalid inputs 
    while True:
        try:
            city_choice = input("\nWould you like to see data for Chicago, New York or Washington?\n").lower()
            if city_choice == 'chicago' or city_choice == 'new york' or city_choice == 'washington':
                # Creation of a dictionary to make sure that the city is correctly determined
                cities = {'chicago':'chicago', 'new york':'new york city', 'washington':'washington'}
                city = cities[city_choice]
                print("\nLet\'s see {}\'s data!".format(city.title()))
                break
            else: 
                print("\nYour input didn\'t match any option, please do it again!")
        except:
            print('\nThat\'s not a valid answer... Let\'s try again!')

    # Date filter
    # While loop and try statement to handle invalid inputs 
    while True:
        try:
            filter_date = (input("\nWould you like to filter data by month or by day? Enter \'both\' if you want both filters and \'none\' if you don\'t want any at all:\n").lower())  
            if filter_date == 'month' or filter_date == 'day' or filter_date == 'both' or filter_date == 'none':
                break
            else: 
                print("\nYour input did not match any option, please do it again!")
        except:
            print('\nThat\'s not a valid answer... Let\'s try again!')  

    # Get user input in case they want to filter by month
    if filter_date == 'month':
        day = 'all'
        print("\nData will be filtered by {}!".format(filter_date))
        # While loop and try statement to handle invalid inputs
        while True:
            try:
                month = input("\nWhich month, between January and June, would you like to see the data for?\n").lower()
                if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june':
                    print('\nYou will see data for {}!'. format(month.title()))
                    break
                else: 
                    print("\nYour input didn\'t match any option, please do it again!")
            except:
                print('\nThat\'s not a valid answer... Let\'s try again!')                      

    # Get user input in case they want to filter by day
    elif filter_date == 'day':
        month = 'all'
        print("\nThe data will be filtered by {}!".format(filter_date))
        # While loop and try statement to handle invalid inputs
        while True:
            try:
                day_choice = input("\nWhich day would you like to see data for, M, Tu, We, Th, F, Sa or Su?:\n ").lower()
                if day_choice == 'm' or day_choice == 'tu' or day_choice == 'we' or day_choice == 'th' or day_choice == 'f' or day_choice == 'sa' or day_choice == 'su':
                    days = {'m':'Monday', 'tu':'Tuesday', 'we':'Wednesday', 'th':'Thursday', 
                            'f':'Friday', 'sa':'Saturday', 'su':'Sunday'}
                    day = days[day_choice].lower()
                    print('You will see the data for {}!'.format(days[day_choice]))
                    break
                else: 
                    print("\nYour input did not match any option, please do it again!")
            except:
                print('\nThat\'s not a valid answer... Lets try again!') 
                
    # Get double input if the user want to filter by both, month and day
    elif filter_date == 'both':
        print("\nYou will get data filtered by month and day!")
        # While loop and try statement to handle invalid inputs for month and day input
        while True:
            try:
                month = input("\nWhich month, between January and June, would you like to see data for?\n").lower()
                if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june':
                    break
                else: 
                    print("\nYour input did not match any option, please do it again!")
            except:
                print('\nThat\'s not a valid answer... Let\'s try again!')
                
        while True:
            try:            
                day_choice = input("\nWhich day would you like to see data for, M, Tu, We, Th, F, Sa or Su?:\n ").lower()  
                if day_choice == 'm' or day_choice == 'tu' or day_choice == 'we' or day_choice == 'th' or day_choice == 'f' or day_choice == 'sa' or day_choice == 'su':
                    days = {'m':'Monday', 'tu':'Tuesday', 'we':'Wednesday', 'th':'Thursday', 
                            'f':'Friday', 'sa':'Saturday', 'su':'Sunday'}
                    day = days[day_choice].lower()
                    print('\nYou will see data for each {} of {}!'.format(days[day_choice], month.title()))
                    break
                else: 
                    print("\nYour input did not match any option, please do it again!")
            except:
                print('\nThat\'s not a valid answer... Let\'s try again!')
    
    # If the user don't want to apply any filter, they will obtain data for all months and days
    elif filter_date == 'none':
        print("\nYou don\'t want any filter at all so... Let\'s see all the information!")
        month = 'all'
        day = 'all'

    print('-'*40)
    return city, month, day

# Function to load data according to the filters specified
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        data - Pandas DataFrame containing city data filtered by month and day
    """
    # data = dataframe
    data = pd.read_csv(CITY_DATA[city])

    # Conversion of the Start Time column to Date format
    data['Start Time'] = pd.to_datetime(data['Start Time'])

    # Getting the month and day of the week from the Start Time Date 
    data['month'] = data['Start Time'].dt.month
    data['day_of_week'] = data['Start Time'].dt.weekday_name

    # Filter by month if applicable 
    if month != 'all':
        # Use the index of the months list to get the corresponding int 
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # Filter by month to create the new dataframe
        data = data[data['month'] == month]
        
    # Filter by day of week if aplicable 
    if day != 'all':
        data = data[data['day_of_week'] == day.title()]    

    return data

# Function to obtain the most popular month, day of week and hour from the Start Time 
def time_stats(data):
    """
    Displays statistics on the most frequent times of travel.
    
    Arg:
        data - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Convert the Start Time column to datetime
    data['Start Time'] = pd.to_datetime(data['Start Time'])
    
    # Extract month from the Start Time column to create a month column
    data['month'] = data['Start Time'].dt.month
    # Find the most popular month
    popular_month = data['month'].mode()[0]
    print('Most Popular Start Month:', popular_month)

    # Extract the day from the Start Time column to create a day column
    data['day_of_week'] = data['Start Time'].dt.weekday_name
    # Find the most popular day of the week
    popular_day = data['day_of_week'].mode()[0]
    print('Most Popular Start Day:', popular_day)

    # Extract hour from the Start Time column to create an hour column
    data['hour'] = data['Start Time'].dt.hour
    # Find the most popular hour
    popular_hour = data['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Function to obtain the most popular Start and End Station, as well as the one with both combined
def station_stats(data):
    """
    Displays statistics on the most popular stations and trip.
    
    Arg:
       data - Pandas DataFrame containing city data filtered by month and day 
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    # Calculate value counts for each start station
    count_start_st = data['Start Station'].value_counts()
    # Get the most popular one
    max_value_start_st = count_start_st.max()
    popular_start_st = count_start_st.idxmax()
    print('The most commonly used start station is {}, used {} times.'.format(popular_start_st, max_value_start_st))

    # Display most commonly used end station
    count_end_st = data['End Station'].value_counts()
    max_value_end_st = count_end_st.max()
    popular_end_st = count_end_st.idxmax()
    print('The most commonly used end station is {}, used {} times.'.format(popular_end_st, max_value_end_st))

    # Display most frequent combination of start station and end station trip
    data['Combined Stations'] = data['Start Station'] + data['End Station']
    count_comb_st = data['Combined Stations'].value_counts()
    max_value_comb = count_comb_st.max()
    popular_comb = count_comb_st.idxmax()
    print('The most frequent combination is {}, used {} times.'.format(popular_comb, max_value_comb))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
# Function to calculate the total duration of the trips as well as the average
def trip_duration_stats(data):
    """
    Displays statistics on the total and average trip duration.
    
    Arg:
        data - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...')
    start_time = time.time()

    # Display total time of travel for the filters applied
    total_trip_dur = data['Trip Duration'].sum()

    # Calculate the average time (total duration divided by the number of trips)
    mean_trip_dur = data['Trip Duration'].mean()
    
    print("\nThe total duration of all the trips is {} seconds, and the average is {} seconds.".format(total_trip_dur, mean_trip_dur))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
          
# Function to obtain users' data
def user_stats(city, data):
    """
    Displays statistics on bikeshare users.

    Arg:
        data - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating User Stats...')
    start_time = time.time()

    # Display counts of user types
    count_users = data['User Type'].value_counts()
    print("\nThe count of each type of user is:\n", count_users)
    
    # Just New York and Chicago have data for user's gender and year of birth 
    if city != 'washington':
        # Display counts of gender
        count_gender = data['Gender'].value_counts()
        print("\nThe count of each gender is:\n", count_gender)

        # Display earliest, most recent, and most common year of birth
        yob = data['Birth Year']    # yob = year of birth
        earliest_yob = yob.min()
        most_recent_yob = yob.max()
        # Most common yob
        popular_yob = yob.mode()[0]
        print("\nThe earliest year of birth is: {}".format(earliest_yob))
        print("The most recent year of birth is: {}".format(most_recent_yob))
        print("The most common year of birth is: {}".format(popular_yob))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)            
        
# Main function, where the functions call is made 
def main():
    while True:
        city, month, day = get_filters()
        data = load_data(city, month, day)

        # User input to decide if they want to display just 5 rows or the complete database
        answer = input("\nWould you like to see the first 5 rows of raw data? Enter 'no' if you want to see it all.\n").lower()
        if answer == 'yes':
            print(data.head())
            count = 0
            # for loop to ask the user if they want to see 5 more rows, until they say 'no'
            for head_data in range(len(data.index)):
                raw_data = input("\nWould you like to see 5 more rows of raw data?\n").lower()
                if raw_data == 'yes':
                    #print(data.head(5 + count))
                    head_data = count + 5
                    print(data[:][head_data:(head_data+5)])
                    print(head_data)
                    count += 5
                else:
                    break
        else:
            print(data)
        
        time_stats(data)
        station_stats(data)
        trip_duration_stats(data)
        user_stats(city, data)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

