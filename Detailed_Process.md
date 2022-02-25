#### Step 1  
Execute GraphQL Queries to find the token IDs of the needed tokens  
in our case UNI and WETH  
#### Step 2
Use GraphQL Queries to find its respective pair ID  
#### Step 3  
Use swaps query to find exchanges by specifying the pair ID  
This renders all the trade data of the required pair in .json format  
But as per the requirement we need it in a MySQL database  
#### Step 4
Convert all the resultant json data to Sql database over MySql workbench  
#### Step 5
Dockerize the whole process
