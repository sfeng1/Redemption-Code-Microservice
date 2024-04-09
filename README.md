## Redemption Code Microservice:

## See video demo here: https://youtu.be/G3btwIePNoM 

This is a simple microservice that allows managers to input and retrieve redemption codes via a local MySQL database instance. 
Managers can assign tags to batches of ingested codes and retrieve those codes in requested quantities based on those tags. 
This microservice can also be called by an external entity to verify the validity of a redemption code. 

## How to Setup Verify Mircroservice: 
Download the following files in the zip:
  1. UX.py - this is my main project
  2. verify.py - this is the microservice for you to call
  3. redeemcode.sql - this is a simple script to create a table in the mysql database 
  4. Codes.csv - sample codes to import into the mysql database

Start by installing mysql workbench and setting up a local database server.  
Run the query in the redeemcode.sql file in mysql workbench to create a table. 

Switch over to python and install pandas, mysql.connector, and flask if you haven't already.  
Open UX.py and update the database credentials at the top (variables in the mysql.connector.connect( ) function).  

Place Codes.csv in the same directory as UX.py.  
Run UX.py and go through the flow (ingestion) to import all the data in Codes.csv into your local database.

Move verify.py to the same directory as UX.py (just to make the import easier in Python).  
Finally, open verify.py and run it to create a web app at the address printed into the console.  
By default the web app address is localhost at http://127.0.0.1:5000/.    
Now you can use the communication contract below to send a get call to get a response from the service. 

IMPORTANT NOTES:  
Make sure you are running verify.py and UX.py at the same time, verify.py uses a function in UX.py to access the database.  


## Communication Contract:

### To call this service: 
Send GET request to flask URL address embdded in code with the prmotional code you would like to verify.  
Example using the default address, the call would be:  
GET http://localhost:5000/code{parameter}  
GET http://localhost:5000/code?code=example 

Response: "Valid" or "Invalid"

### Requests from this service: 
The service will send a GET request to your service via the agreed upon URL with the code to be verified by your service.  
Example using the default address, the call would be:  
GET {yourURL}/code{parameter}  
GET http://localhost:5000/code?code=example 

Expected Response: "Valid" or "Invalid"

## UML:

![sequence](https://github.com/sfeng1/CS361/assets/114194642/072be415-4465-4399-8ca3-f0f03d29f726)



