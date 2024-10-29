from io import StringIO 
import datetime 
import time
import os
import psutil
import inspect
import glob 
import logging
import pandas as pd
import boto3
import re
import pytz

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def pandas_to_s3_csv(df, bucket, key, save_index=False):
    """
    Inputs:
        df: pd.DataFrame: Pandas DataFrame to save (will not save index)
        bucket: str: S3 bucket to save to (i.e. draft-kings-2022)
        key: str: everything excluding the bucket (i.e. games/BoxScoreTraditionalV2)
        save_index: bool : whether or not to save the Pandas Index. 
    """
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=save_index)
    s3_client = boto3.client('s3')
    s3_client.put_object(Bucket=bucket, Key=key, Body=csv_buffer.getvalue())


def get_current_chicago_time():
    """
    Returns datetime object of the current chicago time, needs to be adjusted during DST
    """
    chicago_tz = pytz.timezone('America/Chicago')

    # Get the current time in Chicago timezone
    current_time_chicago = datetime.datetime.now(chicago_tz)
    return current_time_chicago

def run_query(query, conn, disable_game_date_check=False):
    start = time.time()
    df = pd.read_sql_query(query, conn)
    end = time.time()
    n = end - start 
    rows, cols = df.shape
    if not disable_game_date_check:
        if 'GAME_DATE' in df.columns:
            df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'])
    logging.info(f'Returned {rows} rows, {cols} cols, took {n} seconds.')
    return df

def run_query_from_file(file, conn, disable_game_date_check=False):
    """
    Input:
        file: str - name of file containing SQL query
        conn: SQLAlchemy object - database connection object
    Output:
        df: pandas Dataframe containing the queries output
    """
    s = time.time()
    with open(file, 'r') as f:
        q = f.read().strip()
    df = pd.read_sql_query(q, conn)
    if not disable_game_date_check:
        if 'GAME_DATE' in df.columns:
            df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'])
    e = time.time()
    t = '{:.1f}'.format(e-s)

    logging.info(f'Successfully Queried Data from {file}, took {t} seconds.')
    return df 


def write_to_db(df, table_name, conn):
    start = time.time()
    df.to_sql(table_name, conn, if_exists='append', index=False)
    end = time.time()
    rows, cols = df.shape
    n = end - start 
    logging.info(f'Saved {rows} rows, {cols} cols to table {table_name}, took {n} seconds')


def get_todays_df(df, today_column='GAME_DATE'):
    return df[df[today_column].dt.date == datetime.date.today()]


def time_function(func):
    """
    Decorator that reports the execution time of a function and memory usage.
    """
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        t = '{:.1f}'.format(end-start)
        logging.info(f"Memory usage: {psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2} MB, at Function {func.__name__}. Took {end-start} seconds.")
        return result
    return wrap


def time_function_simple(func):
    """
    Decorator that reports the execution time of a function
    """
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        t = '{:.1f}'.format(end-start)

        
        bound_args = inspect.signature(func).bind(*args, **kwargs)
        bound_args.apply_defaults()
        target_args = dict(bound_args.arguments)
        
        kv = ', '.join([f'{x[0]}={x[1]}' for x in list(zip(target_args.keys(), target_args.values()))])

        logging.info(f'Function {func.__name__} took {t} seconds, ran with arguments {kv}')
        return result
    return wrap

def get_most_recent_file_from_directory(directory, use_s3=False, bucket_name=''):
    """
    Input:
        directory: str - (i.e. '/Users/t2/Desktop') or the S3 prefix ('i.e. data/trailing-game-features')
        use_s3: bool - Whether to read from S3 bucket instead of disk. Use in conjunction with
            bucket_name
        bucket_name: str - the AWS S3 bucket name
    Output:
        str - fully-qualified filename, i.e. /Users/t2/Desktop/fantasy/GitDK/DraftKings/data/aggregated_data/2022-01-03_13:06:14.319307.csv
    """
    if use_s3:
        return get_most_recent_file_from_s3_bucket(directory, bucket_name=bucket_name)
    else:
        list_of_files = glob.glob(f'{directory}/*')
        return max(list_of_files, key=os.path.getctime)


def get_most_recent_file_from_s3_bucket(prefix, bucket_name='draft-kings-2022'):
    """
    Input:
        prefix: str - (i.e. data/trailing-games-features/) Note: do not include bucket-name
        bucket_name: str - S3 bucket name (i.e. 'my-aws-s3-bucket')
    Output:
        str - fully-qualified filename, i.e. s3://my-aws-s3-bucket/data/2022-01-03_13:06:14.319307.csv
    """
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name)
    
    # Extract files and their last modified timestamps
    files = response['Contents']

    most_recent_file = sorted(
        list(filter(lambda x: x['Key'].startswith(prefix), files)), 
        key=lambda x: x['LastModified'], 
        reverse=True)[0]['Key']
    return os.path.join(f's3://{bucket_name}', most_recent_file)


def write_pandas_csv(df, file, index=False):
    rows, cols = df.shape
    start = time.time()
    df.to_csv(file, index=index)
    end = time.time()
    logging.info(f"Saved {rows} rows, {cols} cols to {file}, took {end-start} seconds")


def save_pandas_df(df, file, index=False, format='parquet'):
    rows, cols = df.shape
    start = time.time()
    if format == 'parquet':
        df.to_parquet(file, index=index)
    elif format == 'csv':
        df.to_csv(file, index=index)
    else:
        raise Exception(f'format {format} saving is not implemented yet.')
    end = time.time()
    logging.info(f"Saved {rows} rows, {cols} cols to {file}, took {end-start} seconds")

def read_pandas_df(file, format='parquet'):
    start = time.time()
    if format == 'parquet':
        df = pd.read_parquet(file)
    elif format == 'csv':
        df = pd.read_csv(file)
    else:
        raise Exception(f'Reading in from format {format} is not implemented yet.')
    if 'GAME_DATE' in df.columns:
        df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'])
    end = time.time()
    rows, cols = df.shape 
    logging.info(f"Read in {rows} rows and {cols} columns from file {file}, took {end-start} seconds")
    return df 

def read_pandas_csv(file):
    start = time.time()
    df = pd.read_csv(file)
    end = time.time()
    rows, cols = df.shape 
    logging.info(f"Read in {rows} rows and {cols} columns from file {file}, took {end-start} seconds")
    return df 

def find_latest_run(p):
    """
    Look in a log directory and return the latest file. all files must be in format:
         "%Y-%m-%d_%H:%M:%S.log"
    :param p: str - Path
    :return: most recent datetime object. If there are no files in the directory,
        this will default to January 4, 2005.
    """
    dates = []
    for file in os.listdir(p):
        with open(os.path.join(p, file), 'r') as f:
            x = f.read()
        # ignore empty file
        if len(x) == 0:
            continue

        date_info = file.split('.')[0]
        date = datetime.datetime.strptime(date_info, "%Y-%m-%d_%H:%M:%S")
        dates.append(date)

    if len(dates) == 0:
        # Default to arbitrary date, January 4, 2005
        return datetime.datetime(2005, 1, 4)

    most_recent = sorted(dates, reverse=True)[0]
    return most_recent


def normalize_name(input_string):
    input_string = input_string.lower()

    # if its this kind of suffix
    spaces = input_string.split(' ')
    if spaces[-1] in ['jr', 'ii', 'iii', 'iv', 'sr', 'jr.', 'sr.']:
        input_string = ' '.join(spaces[:-1])

    # if there's a last name first for whatever reason, then swap first and last names
    names = input_string.split(',')
    if len(names) == 2:
        input_string = names[1] + ' ' + names[0]

    clean_pattern = r"[.'’]|\(.*?\)"
    # Define the regex pattern to match periods, commas, and apostrophes
    cleaned_string = re.sub(clean_pattern, '', input_string)
    # remove non-ASCII characters (i.e. for  "Luka Dončić" -> Luka Doncic)
    cleaned_string = cleaned_string.replace("č", "c").replace('ć', 'c').strip()

    # get rid of middle names
    names = cleaned_string.split(' ')
    if len(names) > 2:
        cleaned_string = names[0] + ' ' + names[-1]

    name_stems = {
        'matthew': 'matt',
        'nicolas': 'nic',
        'gregory': 'greg',
        'aleksandar': 'alex',
        'spencer': 'spence',
        'joshua': 'josh',
        'nicholas': 'nic',
        'nick': 'nic',
        'christian': 'chris',
        'cameron': 'cam',
        'robert': 'rob',
        'herbert': 'herb',
        'obadiah': 'obi',
        'mohamed': 'mo',
        'maurice': 'mo',
        'moe': 'mo'
    }
    # stem first names
    names = cleaned_string.split(' ')
    cleaned_string = name_stems.get(names[0], names[0]) + ' ' + names[1]

    return cleaned_string.strip()

def flip_first_last_name(name):
    names = name.split(' ')
    assert len(names) == 2
    return names[1] + ' ' + names[0]

def first_initial_last_name(name):
    names = name.split(' ')
    return names[0][0] + ' ' + ' '.join(names[1:])

def join_with_playerid(source, target, join_col_name=['PLAYER_NAME']):
    """
    Take in a source dataframe that has PLAYER_NAME with unmapped player-ids, 
    and joins it with another dataframe that has both PLAYER_NAME and NBA_PLAYER_ID.
    
    Returns the successful joins and failed joins
    """
    comb = source.merge(target, how='left', left_on=join_col_name, right_on=join_col_name)
    succ = comb[comb['NBA_PLAYER_ID'].notnull()]
    fail = comb[comb['NBA_PLAYER_ID'].isna()].drop(columns=['NBA_PLAYER_ID'])
    return succ, fail

def clean_and_join(source, target, join_col_name=['PLAYER_NAME'], try_flip_last_names=True,
                   try_first_initial_last_name=True):
    source['normalized_name'] = source['PLAYER_NAME'].apply(normalize_name)
    target['normalized_name'] = target['PLAYER_NAME'].apply(normalize_name)

    new_join_col_names = [x if x != 'PLAYER_NAME' else 'normalized_name' for x in join_col_name]

    success, failure = join_with_playerid(
        source, 
        target.drop(columns='PLAYER_NAME'),
        join_col_name=new_join_col_names
    )

    if try_flip_last_names:
        failure['normalized_name'] = failure['normalized_name'].apply(flip_first_last_name)
        success2, failure = join_with_playerid(failure, target.drop(columns='PLAYER_NAME'),
                                               join_col_name=new_join_col_names)
        success = pd.concat([success, success2]) 
        failure['normalized_name'] = failure['normalized_name'].apply(flip_first_last_name)

    if try_first_initial_last_name:
        target['normalized_name'] = target['normalized_name'].apply(first_initial_last_name)
        success2, failure = join_with_playerid(failure, target.drop(columns='PLAYER_NAME'),
                                               join_col_name=new_join_col_names)
        success = pd.concat([success, success2])

    source = source.drop(columns=['normalized_name'])
    target = target.drop(columns=['normalized_name'])
    return success.drop(columns=['normalized_name']), failure.drop(columns=['normalized_name'])


def remove_ambiguity_of_team_name(success_df, failure_df):
    """
    Since the Odds-Api doesn't provide the team-name of each player, but does
        provide the event-id, we consider that each player can be part of either
        home or away team. Because of this, there are false positive "failures"
        which were successfully mapped in the other team. This function removes
        the false positives.
    :param success_df: successful mappings df
    :param failure_df: failed mappings df
    :return: failure_df
    """
    failure_df = success_df.drop(columns=['NBA_TEAM_ID', 'location']).merge(
        failure_df,
        how='right'
    )
    return failure_df[failure_df['NBA_PLAYER_ID'].isnull()].drop(
        columns=['NBA_PLAYER_ID'])


def map_player_ids_with_several_targets(source, target_list, join_col_name=['PLAYER_NAME'],
        try_flip_last_names=True, try_first_initial_last_name=True,
        remove_ambiguous_game_team_names=False):
    """
    Given existing sets of name mappings, try to map the source names with the ones
    we already have.

    :param source: dataframe that has player-names needing to be mapped
    :param target_list: priority ordered list of dataframes that contain PLAYER_NAME and NBA_PLAYER_ID
        mappings
    :param join_col_name: List[str] - the list of columns that define a successful join.
    :param try_flip_last_names: bool - Sometimes the data has James, Lebron instead of Lebron James. If true, then try flip-flopping
    :param try_first_initial_last_name: bool - Sometimes the data has L. James. Try to map on this
    :param remove_ambiguous_game_team_names: bool - For sources where I know the game and player-name, but not the team-name
        then each player can be associated with 2 possible teams. If a player maps successfully in one, he'll probably fail for 
        the other team. Therefore just remove the false positive failed row.
    :return: successful mappings, unsuccessful mappings
    """
    final_mappings = []
    failure = source
    for target in target_list:
        success, failure = join_with_playerid(failure, target, join_col_name=join_col_name)
        if remove_ambiguous_game_team_names:
            failure = remove_ambiguity_of_team_name(success, failure)

        final_mappings.append(success)
        if failure.shape[0] == 0:
            return pd.concat(final_mappings), failure

    for target in target_list:
        success, failure = clean_and_join(
            failure, target, join_col_name=join_col_name,
            try_flip_last_names=try_flip_last_names,
            try_first_initial_last_name=try_first_initial_last_name)
        if remove_ambiguous_game_team_names:
            failure = remove_ambiguity_of_team_name(success, failure)

        final_mappings.append(success)
        if failure.shape[0] == 0:
            break
    return pd.concat(final_mappings), failure