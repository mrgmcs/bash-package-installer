from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='',
                                 host='127.0.0.1',
                                 database='info')

cursor = cnx.cursor()
#create tables
tables =["users", "posts", "comments"]

user_table= """id int(11), 
name varchar(255), 
email varchar(255), 
password varchar(255),
remember_token varchar(100),
created_at timestamp,
updated_at timestamp
"""
posts_table= """id int(11),
user_id int(11),
title varchar(250),
text text
"""
comments_table="""id int(11),
user_id int(11),
post_id(11),
text text
"""
#add user info columns
cursor.execute(f"CREATE TABLE {tables[0]} ({user_table});")
#add posts info columns
cursor.execute(f"CREATE TABLE {tables[1]} ({posts_table});")
#add comment info columns
cursor.execute(f"CREATE TABLE {tables[2]} ({comments_table});")

cnx.close()