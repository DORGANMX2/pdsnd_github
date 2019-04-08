import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nChoose a city between Chicago, New York City, and Washington:\n> ').lower()  
        if city not in cities:
            print('\n"{}" is not found in our records.'.format(city))
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhat month would you like to filter your data by?  \nJanuary, February, March, April, May, or June?.  \nType All to filter data by all months.\n> ').lower()
        if month not in months:
            print('\n"{}" is not found in our records.'.format(month))
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhat day would you like to filter your data by?  \nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?  \nType All to filter by all days.\n> ').lower()
        if day not in days:
            print('\n"{}" is not found in our records.'.format(day))
            continue
        else:
            break

   
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime     
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
   
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe        
        df = df[df['month'] == month]
    
    # filter by day of week if applicable
    if day != 'all': 
        df = df[df['day_of_week'] == day.title()] 
        
     
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    # find the most popular month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month: {}'.format(popular_month))
 

    # TO DO: display the most common day of week
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract day from the Start Time column to create a day column
    df['day'] = df['Start Time'].dt.day
    # find the most popular day
    popular_day = df['day'].mode()[0]
    print('Most Popular Day: {}'.format(popular_day))

    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Hour: {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station: {}'.format(common_start_station))
    print('Start Station Counts: {}\n'.format(df['Start Station'].value_counts()[common_start_station]))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station: {}'.format(common_end_station))
    print('End Station Counts: {}\n'.format(df['End Station'].value_counts()[common_end_station]))
    
    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}".format(most_common_start_end_station[0], most_common_start_end_station[1]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
     # display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types: \n{}\n'.format(user_types))
    
    try:
         # To manage errors from missing data in Washington file
         # TO DO: Display counts of gender
         gender_types = df['Gender'].value_counts() 
  
         # TO DO: Display earliest, most recent, and most common year of birth
         earliest_birth_year = df['Birth Year'].min()
    
         most_recent_birth_year = df['Birth Year'].max()
    
         common_birth_year = df['Birth Year'].mode()[0]
    
    except KeyError:
         # print error statement for missing data
         print('Gender data not available. \nCannot display statistics.\n')
    
         print('Birth Year data not available.  \nCannot display statistics.')
    
    else:
         # display counts of gender
         print(gender_types)
         # display earliest birth year
         print('Earliest Birth Year:', earliest_birth_year.min())
         # display most recent birth
         print('Most Recent Birth Year:', most_recent_birth_year.min())
         # display most popular birth
         print('Most Popular Birth Year:', common_birth_year)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """ Accesses csv and displays 5 rows of its raw data if user types "yes" """
 
 
    raw_data_request = input('\nWould you like to see 5 rows of raw data?  (Yes or No)\n> ').lower()
    if raw_data_request == 'yes':
        print('\nAccessing Raw Data...\n')
        start_time = time.time()
        # index number = 0
        i = 0
        # this while loop cycles through raw data in csv and displays it
        while True:
            print(df.iloc[i:i + 5])
            i += 5
            print("\nThis took %s seconds." % (time.time() - start_time))
            more_data_request = input('\nWould you like to see 5 more rows of raw data?  (Yes or No)\n> ').lower()
            # breaks out of loop if user doesn't type "yes"
            if more_data_request != 'yes':
                break
 
 
    print('-'*40)      
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        """ Asks user to restart program and clears screen if yes """

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'yes':
            # detects user os
            os_type = platform.system()
            # clears screen: OSX & Linux
            if os_type in ('Darwin', 'Linux'):
                os.system('clear')
            # clears screen: Windows    
            elif os_type == 'Windows':
                os.system('cls')
            # continues without clearing screen if unknown OS is detected
            else:
                continue
        elif restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
