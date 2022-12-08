# sqlite-try


# Overview

I made this as a way to learn about SQLite3 in Python and how to use it to create relational databases. I love dealing with data and wanted to learn how to use SQLite queries to deal with it in Python.

The software currently just runs basic insert, query, modify, and delete commands. My hope is to make it a user run application that will create local SQLite databases.

I wrote this software to learn about SQLite3 and how it functions within Python. I know SQL fairly well but writing it out to possibly abstract the SQL language.

[Software Demo Video](https://youtu.be/SpbReHrz6qs)

# Relational Database

I am building a simple relational database that takes prices and products, then joins them together. They follow the third rule of normalization. 

The structure of the tables is very simple. The price table has 2 columns. Product_id and price. The product tables has 2 columns. Product_id and product_name. When these are joined it merges the two on product_id. This means that the price matches up with the product.

# Development Environment

I used VScode as my development environment. 

I also used Python with the libraries SQLite3 and Pandas

SQLite3 - Automatically installed with Python

Pandas - !pip install pandas - pip install pandas

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Tutorials Point](https://www.tutorialspoint.com/sqlite/sqlite_update_query.htm)
* [Data To Fish](https://datatofish.com/create-database-python-using-sqlite3/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Fully abstract each SQL command to be totally custom
* Connect this through a web app
* Build my local SQL database with Destiny guns through SQLite
