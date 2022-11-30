# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 11:57:17 2022

@author: gperalta
"""

import nfl_data_py as nfl

#pbp2022 = nfl.import_pbp_data([2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022])
#weekly = nfl.import_weekly_data([2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022])

pbp = nfl.import_pbp_data([2021])

#%%
pbp_sample.to_csv('C:/Users/gperalta/Downloads/PBP_2021.csv')
#weekly.to_csv('C:/Users/gperalta/Downloads/Weekly_2010_2022')

#%%
import pandas as pd

data = pd.read_csv('C:/Users/gperalta/Downloads/pbp_sample.csv').copy()

#%%
pbp = data[['game_id','old_game_id','home_team','away_team','season_type','week','posteam','posteam_type','defteam',
           'game_date','sp','play_type','yards_gained','pass_length','yards_after_catch','field_goal_result',
           'extra_point_result','two_point_conv_result','td_team','epa','air_epa','yac_epa','comp_air_epa',
           'comp_yac_epa','wpa','vegas_wpa','air_wpa','yac_wpa','comp_air_wpa','comp_yac_wpa','third_down_converted',
           'fourth_down_converted','interception','penalty','fumble_lost','qb_hit','rush_attempt','pass_attempt',
           'sack','touchdown','penalty_team','penalty_yards','season','away_score','home_score','location','result',
           'div_game','roof','surface','success']]

#%%