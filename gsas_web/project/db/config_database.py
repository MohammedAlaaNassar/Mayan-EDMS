import configparser
import logging
import logging.config
import os

class ConfigDatabase:
    logging.config.fileConfig('project/db/resources/configs/logging.conf',)
    logger = logging.getLogger('AccessDataBase')
    logger.debug('logging.conf got')
    db_info = configparser.ConfigParser()
    db_info.read('project/db/resources/database.ini')
    logger.debug('database.ini got')
    postgres_access = {value[0]: value[1] for value in db_info.items('POSTGRES_CONNECT')}
    if new_value := os.environ.get('DATABASE_HOST'):
        postgres_access['host'] = new_value
    if new_value := os.environ.get('DATABASE_PASSWORD'):
        postgres_access['password'] = new_value
    if new_value := os.environ.get('DATABASE_DATABASE'):
        postgres_access['database'] = new_value
    if new_value := os.environ.get('DATABASE_USER'):
        postgres_access['user'] = new_value
    table_name = db_info.get('MESSAGES_TABLE', 'table_name')
    applicants_table = db_info.get('APPLICANTS_TABLE', 'applicants_table')
    programs_table = db_info.get('PROGRAMS_TABLE', 'programs_table')
    scores_table = db_info.get('SCORES_TABLE', 'scores_table')
    reviewers_table = db_info.get('REVIEWERS_TABLE', 'reviewers_table')

    logger.debug('DATABASE INFO CONFIGURED')