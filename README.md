# CS361

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



