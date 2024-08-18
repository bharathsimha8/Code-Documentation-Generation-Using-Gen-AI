import mysql.connector
import streamlit as st
import signup as signup
import pandas as pd

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="ai"
    )

def close_connection_and_cursor(connection, cursor):
    cursor.close()
    connection.close()

def data(email, name, password):
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        sql = "INSERT INTO signup(email, name, password) VALUES (%s, %s, %s)"
        val = (email, name, password)
        cursor.execute(sql, val)
        connection.commit()
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        close_connection_and_cursor(connection, cursor)

def check(email):
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM signup WHERE email=%s", (email,))
        user = cursor.fetchone()
        if user:
            return True
        else:
            return False
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        close_connection_and_cursor(connection, cursor)

def checkout(email, password):
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM signup WHERE email=%s AND password=%s", (email, password,))
        user = cursor.fetchone()
        if user:
            return True
        else:
            return False
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        close_connection_and_cursor(connection, cursor)

def hist(smail, choice, resp):
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        sql = "INSERT INTO history(mail, choice, history) VALUES (%s, %s, %s)"
        val = (smail, choice, resp)
        cursor.execute(sql, val)
        connection.commit()
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        close_connection_and_cursor(connection, cursor)

def geth(email):
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        sql = "SELECT choice, LEFT(history, 70) AS truncated_hist FROM history WHERE mail = %s ORDER BY id DESC"
        cursor.execute(sql, (email,))
        result = cursor.fetchall()
        df = pd.DataFrame(result, columns=['Choice', 'History of the Response'])
        st.write(df)
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        close_connection_and_cursor(connection, cursor)
