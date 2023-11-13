import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAY_DATA = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

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
    city = str(input('Enter name of the city (chicago, new york city, washington):'))
    while (city.lower().strip() not in CITY_DATA):
        print('Entered city is not correct. Name of city should be one of the following (chicago, new york city, washington)')
        city = str(input('Enter name of the city (chicago, new york city, washington):'))

    # TO DO: get user input for month (all, january, february, ... , june)
    month = str(input('Enter month (january,february, march, april, may, june, all):'))
    while (month.lower().strip() not in MONTH_DATA):
        print('Entered month is not correct. Month should be one of the following (january,february, march, april, may, june, all)')
        month = str(input('Enter month (january,february, march, april, may, june, all):'))
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input('Enter day of week(all,monday,tuesday,... sunday):'))
    while (day.lower().strip() not in DAY_DATA):
        print('Entered day is not correct. Day should be one of the following (all, monday, tuesday, ... sunday)')
        day = str(input('Enter day of week(all,monday,tuesday,... sunday):'))

    print('-'*40)
    return city.lower().strip(), month.lower().strip(), day.lower().strip()


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
    # load data from city
    df = pd.read_csv(CITY_DATA[city.lower().strip()])
    if (city == 'washington'):
        print(df.columns)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTH_DATA.index(month.lower().strip()) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'].str.lower() == day.lower().strip()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most common month is {}'.format(MONTH_DATA[popular_month-1]))
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day of week is {}'.format(popular_day))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is {}'.format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is {}'.format(popular_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    popular_combination_start_end_stations = df.groupby(['Start Station','End Station']).size().idxmax()
    print('The most frequent combination of start station and end station trip is {}'.format(popular_combination_start_end_stations))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is {}'.format(total_travel_time))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is {}'.format(mean_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:\n{}'.format(user_types))


    # TO DO: Display counts of gender
    if ('Gender' in df.columns):
        user_genders = df['Gender'].value_counts()
        print('Counts of gender:\n{}'.format(user_genders))
    else:
        print('This dataset does not contain Gender column')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if ('Birth Year' in df.columns):
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode().iloc[0]

        print('Earliest Birth Year: {}'.format(earliest_birth_year))
        print('Most Recent Birth Year: {}'.format(most_recent_birth_year))
        print('Most Common Birth Year: {}'.format(most_common_birth_year))
    else:
        print('This dataset does not contain Birth Year column')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
    Display raw data by asking user enter yes/no. Repeating display 5 rows if user enter yes and stop/not display when user enter no or something else.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    start_loc = 0
    total_rows = len(df.index)
    while ((view_data.lower().strip() == 'yes') & (start_loc < total_rows)):
        print('Ok, displaying raw data ...')
        print(df.iloc[start_loc:start_loc + 5 if (start_loc + 5) < total_rows else total_rows ])
        if (start_loc + 5 < total_rows):
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
        else:
            print("All {} rows of raw data displayed!".format(total_rows))
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
