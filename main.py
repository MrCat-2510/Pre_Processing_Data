from MP_pre_processing import MultiProcessing_main
from MT_pre_processing import MultiThreading_main
from TP_pre_processing import ThreadPool_main
from PP_pre_processing import ProcessPool_main

# If pass value True, it will process the whole data

if __name__ == '__main__':
   #  MultiProcessing_main(100) # 73.156 seconds with 100 rows
   # MultiThreading_main(100) # 111.808 seconds with 100 rows
   # ThreadPool_main(100) # 95.14 seconds with 100 rows
   ProcessPool_main(10000) # 51.226 seconds with 100 rows, 3446.998 seconds with 10000 rows
   
   