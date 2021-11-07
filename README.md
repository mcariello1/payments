# Payments
# Prequisites
Must be running on python 3.7+ 
# Executing
`python3 payment_engine.py transactions.csv > client_accounts.csv`

Basics:
Application runs as intended , reads and writes data to csv if following proper execution
Completeness: 
All cases are handled, there are tests that use a set of expected combinations that can occur. Client objects are typed ensuring that the correct parameters are input into client functionality
Safety:
Even though python3 doesnt really privatize objects I made account data a private object so the processing engine would not be able to access clients data except for the client object
Efficiency:
O(n) in space in time . Data is streamed and changes are being made to client accounts as csv is being parsed
Maintainability
Code is modular , clean, and typed. Each individual component of functionality can be updated and apply for all clients and csvs. 

