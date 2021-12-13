from typing import Dict, List, Union

import psycopg2

from project.db.config_database import ConfigDatabase

class AccessDataBase(ConfigDatabase):

    def __init__(self) -> None:
        self.logger.debug('Init Class AccessDataBase')
        conn = psycopg2.connect(**self.postgres_access)
        cursor = conn.cursor()
        query = f'''CREATE TABLE IF NOT EXISTS {self.table_name}(
                    message_id SERIAL PRIMARY KEY NOT NULL,
                    message_title varchar(30) NOT NULL UNIQUE,
                    author_name varchar(30) NOT NULL,
                    message_text varchar(200) NOT NULL,
                    creation_date date NOT NULL)'''
        cursor.execute(query)
        cursor.close()
        conn.commit()

        cursor = conn.cursor()
        query = f'''CREATE TABLE IF NOT EXISTS {self.applicants_table}(
                    applicant_id SERIAL PRIMARY KEY NOT NULL,
                    name varchar(100) NOT NULL,
                    email varchar(50) NOT NULL,
                    university varchar(100) NOT NULL,
                    faculty varchar(100) NOT NULL,
                    department varchar(100) NOT NULL,
                    graduation_year int NOT NULL,
                    gpa varchar(100) NOT NULL,
                    doc_birthdate text NULL,
                    doc_bsc_cert text NULL,
                    doc_r_letters text NULL,
                    status int NOT NULL,
                    program_id int NOT NULL,
                    creation_date date NOT NULL)'''
        cursor.execute(query)
        cursor.close()
        conn.commit()


        cursor = conn.cursor()
        query = f'''CREATE TABLE IF NOT EXISTS {self.programs_table}(
                    program_id SERIAL PRIMARY KEY NOT NULL,
                    name varchar(100) NOT NULL,
                    creation_date date NOT NULL)'''
        cursor.execute(query)
        cursor.close()
        conn.commit()

        cursor = conn.cursor()
        query = f'''CREATE TABLE IF NOT EXISTS {self.reviewers_table}(
                    reviewer_id SERIAL PRIMARY KEY NOT NULL,
                    name varchar(100) NOT NULL,
                    creation_date date NOT NULL)'''
        cursor.execute(query)
        cursor.close()
        conn.commit()


        cursor = conn.cursor()
        query = f'''CREATE TABLE IF NOT EXISTS {self.scores_table}(
                    id SERIAL PRIMARY KEY NOT NULL,
                    reviewer_id int NOT NULL,
                    applicant_id int NOT NULL,
                    score int NOT NULL,
                    creation_date date NOT NULL)'''
        cursor.execute(query)
        cursor.close()
        conn.commit()
        self.logger.debug('CLASS AccessDataBase INITIATED')


    def init_data(self):
        conn = psycopg2.connect(**self.postgres_access)
        cursor = conn.cursor()
        query = f'''INSERT INTO {self.programs_table} (name,creation_date) VALUES ('College of engineering, Computer Dept.','2000-12-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()

        cursor = conn.cursor()
        query = f'''INSERT INTO {self.programs_table} (name,creation_date) VALUES ('College of engineering, Electronics Dept.','2000-12-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()

        cursor = conn.cursor()
        query = f'''INSERT INTO {self.programs_table} (name,creation_date) VALUES ('College of engineering, Industrial Dept.','2000-12-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()

        cursor = conn.cursor()
        query = f'''INSERT INTO {self.reviewers_table} (name,creation_date) VALUES ('A','2000-12-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()

        cursor = conn.cursor()
        query = f'''INSERT INTO {self.reviewers_table} (name,creation_date) VALUES ('B','2000-12-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()

        cursor = conn.cursor()
        query = f'''INSERT INTO {self.reviewers_table} (name,creation_date) VALUES ('C','2000-12-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()

        cursor = conn.cursor()
        query = f'''INSERT INTO {self.reviewers_table} (name,creation_date) VALUES ('D','2000-12-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()

        cursor = conn.cursor()
        query = f'''INSERT INTO {self.applicants_table} (name, email, university, faculty, department, graduation_year, gpa, doc_birthdate, doc_bsc_cert, doc_r_letters, status,program_id, creation_date) VALUES('Student 1', 's1@gmail.com', 'Alexandria University', 'College of engineering', 'Computer Dept', 2019, '3.5', 'a', 'a', 'a', 0,1, '2021-12-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()

        cursor = conn.cursor()
        query = f'''INSERT INTO {self.applicants_table} (name, email, university, faculty, department, graduation_year, gpa, doc_birthdate, doc_bsc_cert, doc_r_letters, status,program_id, creation_date) VALUES('Student 2', 's2@gmail.com', 'AASTMT', 'College of engineering', 'Electronics Dept', 2020, '3.5', 'a', 'a', 'a', 0,3, '2021-10-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()

        cursor = conn.cursor()
        query = f'''INSERT INTO {self.applicants_table} (name, email, university, faculty, department, graduation_year, gpa, doc_birthdate, doc_bsc_cert, doc_r_letters, status,program_id, creation_date) VALUES('Student 3', 's3@gmail.com', 'Ain Shams University', 'College of engineering', 'Mechanics Dept', 2021, '3.9', 'a', 'a', 'a', 0,2, '2021-11-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()


        cursor = conn.cursor()
        query = f'''INSERT INTO {self.applicants_table} (name, email, university, faculty, department, graduation_year, gpa, doc_birthdate, doc_bsc_cert, doc_r_letters, status,program_id, creation_date) VALUES('Student 4', 's4@gmail.com', 'Alexandria University', 'College of engineering', 'Computer Dept', 2019, '3.5', 'a', 'a', 'a', 0,1, '2021-12-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()

        cursor = conn.cursor()
        query = f'''INSERT INTO {self.applicants_table} (name, email, university, faculty, department, graduation_year, gpa, doc_birthdate, doc_bsc_cert, doc_r_letters, status,program_id, creation_date) VALUES('Student 5', 's5@gmail.com', 'AASTMT', 'College of engineering', 'Electronics Dept', 2020, '3.5', 'a', 'a', 'a', 0,3, '2021-10-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()

        cursor = conn.cursor()
        query = f'''INSERT INTO {self.applicants_table} (name, email, university, faculty, department, graduation_year, gpa, doc_birthdate, doc_bsc_cert, doc_r_letters, status,program_id, creation_date) VALUES('Student 6', 's6@gmail.com', 'Ain Shams University', 'College of engineering', 'Mechanics Dept', 2021, '3.9', 'a', 'a', 'a', 0,2, '2021-11-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()


        cursor = conn.cursor()
        query = f'''INSERT INTO {self.applicants_table} (name, email, university, faculty, department, graduation_year, gpa, doc_birthdate, doc_bsc_cert, doc_r_letters, status,program_id, creation_date) VALUES('Student 7', 's7@gmail.com', 'Alexandria University', 'College of engineering', 'Computer Dept', 2019, '3.5', 'a', 'a', 'a', 0,1, '2021-12-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()

        cursor = conn.cursor()
        query = f'''INSERT INTO {self.applicants_table} (name, email, university, faculty, department, graduation_year, gpa, doc_birthdate, doc_bsc_cert, doc_r_letters, status,program_id, creation_date) VALUES('Student 8', 's8@gmail.com', 'AASTMT', 'College of engineering', 'Electronics Dept', 2020, '3.5', 'a', 'a', 'a', 0,3, '2021-10-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()

        cursor = conn.cursor()
        query = f'''INSERT INTO {self.applicants_table} (name, email, university, faculty, department, graduation_year, gpa, doc_birthdate, doc_bsc_cert, doc_r_letters, status,program_id, creation_date) VALUES('Student 9', 's9@gmail.com', 'Ain Shams University', 'College of engineering', 'Mechanics Dept', 2021, '3.9', 'a', 'a', 'a', 0,2, '2021-11-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()

        cursor = conn.cursor()
        query = f'''INSERT INTO {self.applicants_table} (name, email, university, faculty, department, graduation_year, gpa, doc_birthdate, doc_bsc_cert, doc_r_letters, status,program_id, creation_date) VALUES('Student 10', 's10@gmail.com', 'Alexandria University', 'College of engineering', 'Computer Dept', 2019, '3.5', 'a', 'a', 'a', 0,1, '2021-12-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()

        cursor = conn.cursor()
        query = f'''INSERT INTO {self.applicants_table} (name, email, university, faculty, department, graduation_year, gpa, doc_birthdate, doc_bsc_cert, doc_r_letters, status,program_id, creation_date) VALUES('Student 11', 's11@gmail.com', 'AASTMT', 'College of engineering', 'Electronics Dept', 2020, '3.5', 'a', 'a', 'a', 0,3, '2021-10-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()

        cursor = conn.cursor()
        query = f'''INSERT INTO {self.applicants_table} (name, email, university, faculty, department, graduation_year, gpa, doc_birthdate, doc_bsc_cert, doc_r_letters, status,program_id, creation_date) VALUES('Student 12', 's12@gmail.com', 'Ain Shams University', 'College of engineering', 'Mechanics Dept', 2021, '3.9', 'a', 'a', 'a', 0,2, '2021-11-16 12:21:13')'''
        cursor.execute(query)
        cursor.close()


        conn.commit()
        self.logger.debug('data initiated')


    def get_applicants(self):
        self.logger.debug('GETTING APPLICANTS')
        conn = psycopg2.connect(**self.postgres_access)
        self.logger.debug('DB CONNECTED')
        cursor = conn.cursor()
        select_query = f"select a.*,p.name as program_name from {self.applicants_table} a , {self.programs_table} p where p.program_id =a.program_id "
        cursor.execute(select_query)
        self.logger.debug('QUERY EXECUTED')
        applicants = cursor.fetchall()
        cursor.close()
        conn.commit()
        self.logger.debug('RETURNING APPLICANTS')
        return applicants

    def get_applicant_byId(self,applicant_id):
        self.logger.debug('GETTING APPLICANT BY ID')
        conn = psycopg2.connect(**self.postgres_access)
        self.logger.debug('DB CONNECTED')
        cursor = conn.cursor()
        select_query = f"select a.*,p.name as program_name from {self.applicants_table} a , {self.programs_table} p where p.program_id =a.program_id AND a.applicant_id={applicant_id}"
        cursor.execute(select_query)
        self.logger.debug('QUERY EXECUTED')
        applicant = cursor.fetchone()
        cursor.close()
        conn.commit()
        self.logger.debug('RETURNING APPLICANT ID ')
        return applicant


