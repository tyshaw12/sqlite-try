import sqlite3
import pandas as pd

database = '1'



# Builds tables
def build_tables(database):
    conn = sqlite3.connect(database) 
    c = conn.cursor()
    # Builds products
    c.execute('''
          CREATE TABLE IF NOT EXISTS products
          ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT)
          ''')
    # Builds prices
    c.execute('''
          CREATE TABLE IF NOT EXISTS prices
          ([product_id] INTEGER PRIMARY KEY, [price] INTEGER)
          ''')
                     
    conn.commit()
    
    
    
# Inserts into tables
def insert_info(database):
    conn = sqlite3.connect(database) 
    c = conn.cursor()
    # Insert into products in product_id, product_name format seen in VALUES
    c.execute('''
          INSERT INTO products (product_id, product_name)

                VALUES
                (1,'Computer'),
                (2,'Printer'),
                (3,'Tablet'),
                (4,'Desk'),
                (5,'Chair')
          ''')
    # Insert into prices in product_id, price format seen in VALUES  
    c.execute('''
          INSERT INTO prices (product_id, price)

                VALUES
                (1,800),
                (2,200),
                (3,300),
                (4,450),
                (5,150)
          ''')

    conn.commit()
    
    
    
# Edits information (hard-coded for prices)
def edit_info(database):
    conn = sqlite3.connect(database) 
    c = conn.cursor()
                   
    c.execute('''
          UPDATE prices SET price = 500 WHERE product_id = 1
          
          ''')

    conn.commit()
    
    
    
# Edits information (hard-coded for prices product_id = 1)
def delete_info(database):
    conn = sqlite3.connect(database) 
    c = conn.cursor()
                   
    c.execute('''
          DELETE FROM prices WHERE product_id = 1
          
          ''')

    conn.commit()
    
    
    
# Queries the price table
def query_prices(database):
    conn = sqlite3.connect(database) 
    c = conn.cursor()
                   
    c.execute('''
          SELECT
          *
          FROM prices
          ''')

    df = pd.DataFrame(c.fetchall(), columns=['product_id','price'])
    print(df)
    
        
        
#Queries the product table
def query_product(database):
    conn = sqlite3.connect(database) 
    c = conn.cursor()
                   
    c.execute('''
          SELECT
          *
          FROM products
          ''')

    df = pd.DataFrame(c.fetchall(), columns=['product_id','product'])
    print(df)

# Queries and joins both tables
def query_both(database):
    conn = sqlite3.connect(database) 
    c = conn.cursor()
                   
    c.execute('''
          SELECT
          a.product_name,
          b.price
          FROM products a
          LEFT JOIN prices b ON a.product_id = b.product_id
          ''')

    df = pd.DataFrame(c.fetchall(), columns=['product_name','price'])
    print(df)
    
def video_test_first():    
    print()
    print()
    print()
    print()
    print()
    print()
    database = '1'
    build_tables(database)
    insert_info(database)
    query_prices(database)
    query_product(database)
    query_both(database)

def video_test_second():
    print()
    print()
    print()
    print()
    print()
    print()
    database = '1'
    query_prices(database)
    edit_info(database)
    query_prices(database)
    
def video_test_third():
    print()
    print()
    print()
    print()
    print()
    print()
    database = '1'
    query_prices(database)
    delete_info(database)
    query_prices(database)


def demo():
    #video_test_first()
    #video_test_second()
    video_test_third()
#demo()
edit_info('1')
query_both('1')



#def choice_first():
    #print(f'Options: \n 1. Create \n 2. Insert \n 3. Query \n 4. Delete')
    #print()
    #type = input("What would you like to do with SQL? ")
    #return type

#def build_tables_input():
    #database = input("What is the name of the database? ")
    #table_name = input("What would you like to name the table? ")
    #pri_key_name = input("What is the primary key? ")
    #pri_key_type = input("What is the primary key datatype? ")
    #column_name = input("What would you like to name the column? ")
    #column_type = input("What is the column datatype? ")
    #return database, table_name, pri_key_name, pri_key_type, column_name, column_type

#def build_tables_user(database, table_name, pri_key_name, pri_key_type, column_name, column_type):
    #conn = sqlite3.connect(database.lower()) 
    #c = conn.cursor()
    #table_name = table_name
    #CREATE TABLE IF NOT EXISTS prices
          #([product_id] INTEGER PRIMARY KEY, [price] INTEGER)
          #''')
    #c.execute("CREATE TABLE IF NOT EXISTS "+table_name+pri_key_name+pri_key_type+"PRIMARY KEY"+","+column_name+column_type)
    #c.execute("CREATE TABLE IF NOT EXISTS "+table_name+pri_key_name+pri_key_type+" PRIMARY KEY,")
    #conn.commit() 
    
    
#def execute():
    #type = choice_first()
    #type = ('create')
    #if type.lower() == 'create':
        #database = input("What is the name of the database? ")
        #table_name = input("What would you like to name the table? ")
        #pri_key_name = input("What is the primary key? ")
        #pri_key_type = input("What is the primary key datatype? ")
        #column_name = input("What would you like to name the column? ")
        #column_type = input("What is the column datatype? ")
        #database = ("1")
        #table_name = ("TEST_TABLE")
        #pri_key_name = ("([TEST_KEY])")
        #pri_key_type = ("INTEGER")
        #column_name = ("[TEST_COL]")
        #primary_key = "PRIMARY KEY, [price] INTEGER"
        #column_type = ("INTEGER")
        #create_table = (f'''CREATE TABLE IF NOT EXISTS {table_name} {pri_key_name} {pri_key_type} PRIMARY KEY, {column_name} {column_type}''')
        #build_tables_user(database, table_name, pri_key_name, pri_key_type, column_name, column_type)
        #conn = sqlite3.connect(database.lower()) 
        #c = conn.cursor()
        #table_name = table_name
    #CREATE TABLE IF NOT EXISTS prices
          #([product_id] INTEGER PRIMARY KEY, [price] INTEGER)
          #''')
    c.execute("CREATE TABLE IF NOT EXISTS "+table_name+pri_key_name+pri_key_type+"PRIMARY KEY"+","+column_name+column_type)
        #c.execute(create_table)
        #c.execute(create_table+table_name+pri_key_name+pri_key_type+primary_key)
        #conn.commit() 
        #conn = sqlite3.connect(database) 
        #c = conn.cursor()          
        #c.execute("SELECT "+pri_key_name+column_name+" FROM "+table_name)

        #df = pd.DataFrame(table_name.fetchall(), columns=[pri_key_name, column_name])
        #print(df)
#execute()
        
    
    
#def query_one(database):
    #conn = sqlite3.connect(database) 
    #c = conn.cursor()
                   
    #c.execute('''
          #SELECT
          #price
          #FROM prices
          #WHERE product_id = 1
          #''')

    #df = pd.DataFrame(c.fetchall(), columns=['product_name','price'])
    #print(df) 
    
#def query_all_one(database):
    #conn = sqlite3.connect(database) 
    #c = conn.cursor()
                   
    #c.execute('''
          #SELECT
         # *
          #FROM prices
          #''')

    #df = pd.DataFrame(c.fetchall(), columns=['product_name','price'])
    #print(df)