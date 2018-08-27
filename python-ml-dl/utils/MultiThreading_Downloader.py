# coding: utf-8

##############################################################
# Usage : python Multi_Threading_Downloader.py <URL List file>
# <URL List file> format:
# 	Line 1: URL 1
# 	Line 2: URL 2
# 	Line 3: URL 3
# 	Line 4: URL 4
# Processing:
# Multiple threads (worker) will get a URL from URL Queue
# (Thread-Safe) and executing the downloading for it.
# One URL for one getting
##############################################################

import time
import requests
import os


#################################################
# Parsing arguments and setup download directory
#################################################
import sys
argvs = sys.argv
argc = len(argvs)
#print(argvs)

if (argc != 2):
    print("Usage : {0} {0}".format(argvs[0], " URL List file"))
    sys.exit()

# Reading URL list file name from argument[1]
url_list_filename = argvs[1]
if (not os.path.isfile(url_list_filename)):
    print("ERORR: File is not exist")
    sys.exit()

#Create saved directory from URL list file name
SAVE_DIR = ".\\{0}_Download".format(url_list_filename[:url_list_filename.rfind(".")])
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)
print("SAVE DIR :{0}".format(SAVE_DIR))

#######################################################
# Creating logging for tracking error when downloading
#######################################################
import logging

# create logger
logger = logging.getLogger('multi_thread_downloader')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
#ch = logging.NullHandler()
#ch.setLevel(logging.CRITICAL)
ch_f = logging.FileHandler('{0}_LOG.log'.format(url_list_filename[:url_list_filename.rfind(".")]), mode='a', encoding='utf-8')
ch_f.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)
ch_f.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)
logger.addHandler(ch_f)

########################################################################
# if logging MODULE is not available, please use following dummy class
# by remove following comments
########################################################################
#class VirtualLogger:
#    def warning(self, strLog):
#        print("WARN     :", strLog)
#    def info(self, strLog):
#        print("INFO     :", strLog)
#    def debug(self, strLog):
#        print("DEBUG    :", strLog)
#    def error(self, strLog):
#        print("ERROR    :", strLog)
#    def critical(Self, strLog):
#        print("CRITICAL :",strLog)        
#logger = VirtualLogger()

# 'application' code
#logger.debug('debug message')
#logger.info('info message')
#logger.warning('warn message')
#logger.error('error message')
#logger.critical('critical message')

####################################
# Initialize some global variables
####################################
import queue
# A URL Queue 
# (I have known thaThread-Safe after gooling)
URL_Queue = queue.Queue()

import threading
# A array of Thread
threadPools = []

# Global stop flag
isStop = False

# Download file and save it
def downloadFile(URL, saveFilePath, workerName="000"):
    # Use proxy setting if nesscessary
    proxies = {}    
    try:
        start_time = time.time()
        response = requests.get(URL, proxies=proxies)
        with open(saveFilePath, 'wb') as f:
            for chunk in response.iter_content():
                f.write(chunk)
        logger.info("{0}: Completed. It took :{1}, by {2}".format(URL, time.time() - start_time, workerName))
    except Exception as inst:
        logger.error("{0}: failured. Exception :{1}, by {2}".format(URL, inst, workerName))


# The function which is assigned to each worker
def Download_Worker_Func():
    logger.info("Worker :{0} started".format(threading.currentThread().getName()))
    while (not isStop):
        try:
            # Waiting for 3 second til get a URL from URL Queue
            OriginalURL = URL_Queue.get(timeout=3)
        except queue.Empty:
            OriginalURL = None
            
        # If URL Qeueu is empty, just break loop
        if (OriginalURL == None):
            if URL_Queue.empty():
                break
            else:
                continue
        
        # Extracting save name from given URL
        saveFileName = OriginalURL[OriginalURL.rfind("/")+1:]
        # And make file full path
        saveFileFullPath = "{0}\\{1}".format(SAVE_DIR, saveFileName)

        # Skip downloading if the file is already existing
        if (os.path.isfile(saveFileFullPath)):
            #logger.debug("{0}: Already existing, skipped".format(OriginalURL))
            1
        else:
            downloadFile(OriginalURL, saveFileFullPath, threading.currentThread().getName() )

        # Just sleep 0.5 seconds ( it is good for scheduling)
        time.sleep(0.05)

    logger.info("Worker :{0} finished".format(threading.currentThread().getName()))

# Create new worker
def Create_New_Download_Worker(workerId):
    newWorker = threading.Thread(target=Download_Worker_Func, name=workerId)
    newWorker.start()
    return newWorker

# Load URL list into URL Queue
def Load_URL_List_file(urlListFile):
    with open(urlListFile,'r',encoding='utf8') as f:
        for line in f:
            print(line.strip())
            URL_Queue.put(line.strip())

####################################
# Now it MAIN
####################################
Load_URL_List_file(url_list_filename)

# Create all workers for downloading
# Any value if you want, recommend 5~10
N_THREADs_MAX = 5
for i in range(N_THREADs_MAX):
    download_worker = Create_New_Download_Worker("Worker_{0:0d}".format(i + 1))
    threadPools.append(download_worker)

#####################################################
# Some monitoring command is providing
# via standard input while all worker is hardworking
# 
# Type HELP for display availalbe commands
####################################################
while (True):
    try:
        input_lines = sys.stdin.readline()
        print("Command :", input_lines)

        # If "QUIT" is anywhere in inputted command, just quit all
        if ("QUIT" in input_lines.upper()):
            print("Quiting...")
            
            # Thread finish
            isStop = True
            for worker in threadPools:
                worker.join()
            # Exiting loop
            break
        else:
            cmd=input_lines.strip()
            if (len(cmd) == 0):
                cmd = "HELP"
            # Monitoring command
            if ("INFO" == cmd.upper()):
                print("Queue size :{0}".format(URL_Queue.qsize()))
                print("N Workers  :{0}".format(len(threadPools)))
            # HELP command
            if ("HELP" == cmd.upper()):
                print("INFO, HELP ...")
    except KeyboardInterrupt:# In case of Ctrl + C is pressed
        print("Forcing exiting all thread....")
        # Thread finish
        isStop = True
        for worker in threadPools:
            worker.join()
        # Exiting loop
        break
