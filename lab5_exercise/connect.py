from flask import Flask
import psycopg2
import sys
import datetime
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

app = Flask(__name__)
dbhost = 'localhost'
dbport = '5433'
dbname = 'clonyjr'
dbuser='clonyjr'
dbpass=''
conn_string = "host=" + dbhost + " dbname=" + dbname + " user=" + dbuser + ' port=' + dbport


@app.route("/")
def index():
    try:
        
        df1 = pd.read_csv('queryWeather.csv')
        dfg1 = pd.DataFrame(df1,columns=['weather', 'trip_seconds'])
        fig1 = px.bar(dfg1,
        x='weather',
        y='trip_seconds',
        title='How the weather affects a trip duration?',
        barmode='stack')
    
        df = pd.read_csv('queryBestFare.csv')
        dfg = pd.DataFrame(df,columns=['company', 'trip_miles', 'bestfare'])
        fig = px.bar(dfg,
        x='company',
        y='bestfare',
        title='Best Companies fares (per mile) on November 2016',
        barmode='stack')

        fig.show()
        fig1.show()
        return "VERIFICAR AS OUTRAS PÁGINAS CRIADAS"
    except PX.Error as error:
        print("ERROR NO PLOTLY", error)
        return "ERROR"
    return "VERIFICAR AS OUTRAS PÁGINAS CRIADAS"


if __name__ == "__main__":
    app.run()
    
 #FUNCTION USED TO PROCESS THE DATA ON THE POSTGRESQL, TO USE MUST HAVE A POSTGRESQL INSTALLED WITH A DATABASE CALLED CLONYJR AND THE FOLLOWING TABLES: chicago_taxi_dataset, weathercondition AND trip_weather
def etl():
    print(conn_string)
    try:
        conn = psycopg2.connect(conn_string)
        print("Connected!")
        cursorweather = conn.cursor()
        cursorchicago = conn.cursor()
        cursorinsert = conn.cursor()
        countinsercoes = 0

        sql_chicagotaxi_query = "select * from chicago_taxi_dataset where trip_start_timestamp between  '2016-11-01 00:00:00' and '2016-12-07 23:59:00'  order by trip_start_timestamp"
        sql_weather_query = "select * from weathercondition order by time"
        postgres_insert_query = """ INSERT INTO trip_weather (trip_id, weather_id) VALUES (%s,%s)"""

        cursorchicago.execute(sql_chicagotaxi_query)
        taxi_records = cursorchicago.fetchall()

        for row in taxi_records:
            tripchicago_id = row[0]
            taxistartmoment = row[2]
            taxiendmoment = row[3]
            cursorweather.execute(sql_weather_query)
            weather_records = cursorweather.fetchall()
            for row in weather_records:
                weathermoment_id = row[0]
                weathermoment = row[1]
                if(weathermoment>taxistartmoment):
                    if (weathermoment-taxistartmoment) <= (datetime.timedelta(hours=1)):
                        
                        print("inserindo dados na tabela: " + postgres_insert_query,(tripchicago_id, weathermoment_id))
                        countinsercoes += 1
                        cursorinsert.execute(postgres_insert_query,(tripchicago_id, weathermoment_id))
                        conn.commit()
                        if(weathermoment>taxiendmoment):
                            if(weathermoment-taxiendmoment) <= (datetime.timedelta(hours=1)):
                                    print("inserindo dados na tabela: ")
                                    countinsercoes += 1
                                    cursorinsert.execute(postgres_insert_query,(tripchicago_id, weathermoment_id))
                                    conn.commit()
                elif (weathermoment < taxistartmoment):
                    if(taxistartmoment-weathermoment) <= (datetime.timedelta(hours=1)):
                        
                        print("inserindo dados na tabela")
                        cursorinsert.execute(postgres_insert_query,(tripchicago_id, weathermoment_id))
                        conn.commit()
                        countinsercoes += 1
                        if (weathermoment < taxiendmoment):
                            if(taxiendmoment-weathermoment) <= (datetime.timedelta(hours=1)):
                                
                                print("inserindo dados na tabela")
                                cursorinsert.execute(postgres_insert_query,(tripchicago_id, weathermoment_id))
                                conn.commit()
                                countinsercoes += 1

                
    except psycopg2.Error as error:
        print("Error in update operation", error)
        print(psycopg2.__version__)
        print(error.pgerror)
        print(error.diag.message_detail)
        
    finally:
        # closing database connection.
        if (conn):
            cursorweather.close()
            cursorchicago.close()
            cursorinsert.close()
            conn.close()
            print("PostgreSQL connection is closed")
            print("O total de inserções no banco foi de: " + str(countinsercoes))
        
