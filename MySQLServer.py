#!/usr/bin/env python3
"""
MySQLServer.py - Task 1
Script to create the alx_book_store database in MySQL server
"""

import mysql.connector


def create_database():
    """
    Creates the alx_book_store database if it doesn't exist
    """
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Change this to your MySQL username
            password=''   # Change this to your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            
    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")
        
    finally:
        # Close database connection
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == "__main__":
    create_database()
