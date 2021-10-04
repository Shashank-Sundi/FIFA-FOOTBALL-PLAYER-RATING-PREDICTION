from Log_writer import logger
from flask import request
import pandas as pd
import numpy as np

class data_formater:
    def __init__(self):
        self.log_writer=logger.App_Logger()

    def format_data(self):
        self.log_writer.log("Prediction Process Started")
        self.log_writer.log("Started to format the data input from the html form")
        try:
            if request.form['potential']=="": potential = np.nan
            else:potential=float(request.form['potential'])

            if request.form['foot']=="":foot = np.nan
            else: foot=int(request.form['foot'])

            if request.form['attacking_work_rate']=="":attacking_work_rate=np.nan
            else:attacking_work_rate=request.form['attacking_work_rate']

            if request.form['defensive_work_rate'] =="":defensive_work_rate=np.nan
            else:defensive_work_rate=request.form['defensive_work_rate']

            if request.form['crossing']=="":crossing=np.nan
            else:crossing=float(request.form['crossing'])

            if request.form['finishing']=="":finishing=np.nan
            else:finishing=float(request.form['finishing'])

            if request.form['heading_accuracy']=="":heading_accuracy=np.nan
            else:heading_accuracy=float(request.form['heading_accuracy'])

            if request.form['volleys']=="":volleys=np.nan
            else:volleys=float(request.form['volleys'])

            if request.form['curve']=="":curve=np.nan
            else:curve=float(request.form['curve'])

            if request.form['free_kick_accuracy']=="":free_kick_accuracy=np.nan
            else:free_kick_accuracy=float(request.form['free_kick_accuracy'])

            if request.form['long_passing']=="":long_passing=np.nan
            else:long_passing=float(request.form['long_passing'])

            if request.form['ball_control']=="":ball_control=np.nan
            else:ball_control=float(request.form['ball_control'])

            if request.form['sprint_speed']=="":sprint_speed=np.nan
            else:sprint_speed=float(request.form['sprint_speed'])

            if request.form['agility']=="":agility=np.nan
            else:agility =float(request.form['agility'])

            if request.form['reactions']=="":reactions=np.nan
            else:reactions=float(request.form['reactions'])

            if request.form['balance']=="":balance=np.nan
            else:balance=float(request.form['balance'])

            if request.form['shot_power']=="":shot_power=np.nan
            else:shot_power=float(request.form['shot_power'])


            if request.form['jumping']=="":jumping=np.nan
            else:jumping=float(request.form['jumping'])

            if request.form['stamina']=="":stamina=np.nan
            else:stamina=float(request.form['stamina'])

            if request.form['strength']=="":strength=np.nan
            else:strength=float(request.form['strength'])

            if request.form['long_shots']=="":long_shots=np.nan
            else:long_shots=float(request.form['long_shots'])

            if request.form['aggression']=="":aggression=np.nan
            else:aggression=float(request.form['aggression'])

            if request.form['interceptions']=="":interceptions=np.nan
            else:interceptions=float(request.form['interceptions'])

            if request.form['positioning']=="":positioning=np.nan
            else:positioning=float(request.form['positioning'])

            if request.form['vision']=="":vision=np.nan
            else:vision=float(request.form['vision'])

            if request.form['penalties']=="":penalties=np.nan
            else:penalties=float(request.form['penalties'])

            if request.form['sliding_tackle']=="":sliding_tackle=np.nan
            else:sliding_tackle=float(request.form['sliding_tackle'])

            if request.form['gk_kicking']=="":gk_kicking=np.nan
            else:gk_kicking=float(request.form['gk_kicking'])

            if request.form['gk_reflexes']=="":gk_reflexes=np.nan
            else:gk_reflexes=float(request.form['gk_reflexes'])

            self.log_writer.log("Collected inputs from HTML form")


            data=[[potential,foot,attacking_work_rate,defensive_work_rate,crossing,finishing,heading_accuracy,
                   volleys,curve,free_kick_accuracy,long_passing,ball_control,sprint_speed,
                   agility,reactions,balance,shot_power,jumping,stamina,strength,long_shots
                   ,aggression,interceptions,positioning,vision,penalties,sliding_tackle,gk_kicking,gk_reflexes]]

            self.log_writer.log("Aggregated data inputs from user")

            data=pd.DataFrame(data,columns=['potential', 'preferred_foot', 'attacking_work_rate',
                               'defensive_work_rate', 'crossing', 'finishing', 'heading_accuracy',
                               'volleys', 'curve', 'free_kick_accuracy', 'long_passing',
                               'ball_control', 'sprint_speed', 'agility', 'reactions', 'balance',
                               'shot_power', 'jumping', 'stamina', 'strength', 'long_shots',
                               'aggression', 'interceptions', 'positioning', 'vision', 'penalties',
                               'sliding_tackle', 'gk_kicking','gk_reflexes'])

            self.log_writer.log("Raw data aggregated and converted to DataFrame")
            return data

        except Exception as e:
            self.log_writer.log("ERROR occured while formatting raw data.")
            return print(e)




