# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 11:57:17 2022

@author: gperalta
"""

import nfl_data_py as nfl

pbp = nfl.import_pbp_data([2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022])
weekly = nfl.import_weekly_data([2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022])

#%%
pbp.to_csv('C:/Users/gperalta/Downloads/PBP_2010_2022')
weekly.to_csv('C:/Users/gperalta/Downloads/Weekly_2010_2022')