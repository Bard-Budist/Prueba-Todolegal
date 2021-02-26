# Test Todolegal

In this repository there is a technical test in which this statement is developed 
1. Consultar el valor de cambio de una de las siguientes opciones en 5 días diferentes de la siguiente página https://finance.yahoo.com/: Euros a dólares Pesos chilenos a dólares Soles a dólares 2. Almacenar los datos de valor de cambio en una base de datos. 3. Desarrollar un prototipo de API REST que permita consultar el valor de cambio almacenado en la base de datos 4. Al finalizar el proceso que golpee el webhook con URL ############################# con un body que incluya el valor de cambio consultado.


# Structure

For the solution of this exercise it is divided into three ways 
1. Api: Here a prototype of an api that is responsible for consulting data in a database was developed 
2. Db: Here the corresponding files were developed for managing the database as well as its main operations 
3. scrapper: Here a small scrapper was developed that is responsible for consulting the data on currencies and saving it in a database, to finally hit an endpoint with the data

## Run
- First install all packages used contain in `requirement.txt`
For this step, I divided into two processes  
1. Api: with this the api is launched for its respective use => `python3 api.py`
2. Scrapper / Populate DB: This launches the scrapper in which the data is consulted and in turn inserts it in a db => `python3 app.py`


## Requirement

packages used

## Environment Variables

HOST => Host database
PORT => Port database
USER => User database
PASSWORD => Passord database
URL_POST => Url to hit to end process
DATA_BASE => Name database
