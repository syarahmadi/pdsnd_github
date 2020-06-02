
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
