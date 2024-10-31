Description 
-------------
 This project made for verify mobile number in Thailand and verify Email pattern

Feature 
-------------
#### Verify
- verify_mobile_number
- verify_email
- verify_thai_number
- verify_citizenid_format
- verify_datetime_format
#### Convert
- convert_num_th_to_global
#### Clean
- clean_car_plateno **(Inprogress)**
#### Utils
- DatabaseManager
##### Connector
- postgres_connector
- mysql_connector
- sqlite_connector
##### Extract
- extract_api

Installing
----------
    pip install aidataup

Change log 
-------------
#### Version

##### v0.0.5 
- **[2024/10/31]** Hotfix add pysqlite3-binary dependencies
##### v0.0.4 
- **[2024/10/31]** Add DatabaseManager and connection
##### v0.0.3 
- **[2024/10/24]** Add function verify citizenid and datetime with fix format pattern (%Y-%m-%d, %d/%m/%Y, %d-%m-%Y, %Y/%m/%d)
##### v0.0.2 
- **[2024/10/22]** Add function convert and verify Thai numbers to arabic number 
##### v0.0.1 
- **[2024/10/22]** Initial verify telephone and mobile number in Thailand 

Documentation
-------------
Official documentation for aidataup will coming soon...

Usage
-------------
##### Example use
    python -m venv test_pylib
    test_pylib\Scripts\activate
    pip install aidataup

##### Python code
    from aidataup import *
    print(verify_email("1234@mail.com")) #--- Verify Email
    print(verify_mobile_number("0841333333")) #--- Verify Thailand Mobile number pattern


