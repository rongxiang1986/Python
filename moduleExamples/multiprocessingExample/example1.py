import time
import math
import pandas as pd
import multiprocessing
import numpy as np


df = pd.DataFrame(np.random.rand(10, 1))
results = []

def split_dataframe_by_position(df, splits_n):
    """Takes a dataframe and an integer of the number of splits to create.
       Returns a list of dataframes."""
    dataframes = []
    index_to_split = math.ceil(len(df)/splits_n)
    # splits
    start = 0
    end = index_to_split
    for split in range(splits_n):
         temporary_df = df.iloc[start:end, :]
         dataframes.append(temporary_df)
         start += index_to_split
         end += index_to_split
    return dataframes

def processData(df, num):
    """Does some compute intensive operation on the data frame.
       Returns a list."""
    time.sleep(1)
    print("processData\n")
    df = df + num
    return df


def collect_results(result):
    """Uses apply_async's callback to setup up a separate Queue for each process"""
    print("subprocess")
    results.append(result)


if __name__ == "__main__":
    start_time = time.time()

    # Repeats the compute intensive operation on 10 data frames concurrently
    processes_num = multiprocessing.cpu_count()
    df_list = split_dataframe_by_position(df, processes_num)
    print([len(item) for item in df_list])

    pool = multiprocessing.Pool(processes=processes_num)
    for i in range(processes_num):
        res = pool.apply_async(processData, args=(df_list[i], 2), callback=collect_results)
        print(res)
        print("res.get()", res.get())
    pool.close()
    pool.join()

    # Converts list of lists to a data frame
    print(results)
    df = pd.concat(results)
    print(df)
    print(df.shape)
    print("--- %s seconds ---" % (time.time() - start_time))