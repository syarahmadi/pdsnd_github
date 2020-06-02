
import time
import pandas as pd
import numpy as np



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
      print('Hello! Let\'s explore some US bikeshare data!')
      print('Would you like to see data for Chicago, New York, or Washington?')
      city=input().lower()
      while city not in ['chicago','new york city','washington']:
        print('Entered city is invalid, try again')
        city=input().lower()
      print('Awesome, you chose {}'.format(city))
      df = pd.read_csv(CITY_DATA[city])
      print('Would you like to filter the data by month, day, both or not at all?\n (Please enter month, day, both or none)')
      word=input().lower()
      while word not in ['month', 'day', 'both','none']:
        print('Please enter month, day, both or none')
        word=input().lower()
      if word in ['month', 'both']:
        print('Which month - January, February, March, April, May, or June?')
        month=input().lower()
        while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
          print('please enter January, February, March, April, May, or June')
          month=input().lower()
      else:
        month='all'
      if word in ['day', 'both']:
        print('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? \n please give it as integer, Sunday=1')
        #print('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?')
        day=int(input())
        while day not in [1,2,3,4,5,6,7]:
        #while day not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
          #print('please enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday.')
          print('please enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday.\n please give it as integer, Sunday=1')
          day=int(input())
      else:
        day='all'
      return city, month, day
      #---------------------------------

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
    df = pd.read_csv(CITY_DATA[city])
    # load data file into a dataframe
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day
    if month!= 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
    return df
