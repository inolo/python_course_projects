# python_course_projects
Project 2: 

SQLite and DATABASE QUERIES in python. 


Sqlite: SQLite is a easy to use local database that stores as a file on your computer and you can access it like a regular database to create tables, query data, and so on. 


In this project I want you to query three different phrases from a table called SECRET_CODE. 

The columns in this table are CODE and CODE_NUMBER.

First you have to connect to the database and find out how to return a result from a query and then use that data. 



LEVEL 1:

I want you to query the CODE in this order by CODE_NUMBER. [75,202,233]

Get all the phrases, join them together and then send it to me what the phrase is. 


LEVEL 2: 

I also created another table called SUCCESS_MESSAGE this table has two columns SUCCESS_MESSAGE and SUCCESS_HASH.

To get the success message you have to HASH the phrase from step one using the SHA256 hashing algorithm and then query the table by the hash. 

HASH: A hash is a formula/algorithm that is applied to an input and will give you a unique output. It is used to securely store data and verify data.

Once you can query the table send me what the success message is.

(This one is a bit hard but use google when you run into hashing issues, such as string encoding and digesting.)


EXTRA_BONUS:

IF YOU GET SQL AND HOW IT WORKS YOU CAN GET AROUND THIS EASILY WITHOUT USING THE HASH
