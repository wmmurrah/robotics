import glob
import datetime
#  time, os,
#  import dist_test as dist

log_period = 600  # seconds

logging_folder = glob.glob('/mnt/flash16/pi_data/*')[0]
dt = datetime.datetime.now()
file_name = "temp_log_{:%Y_%m_%d}.csv".format(dt)
logging_file = logging_folder + '/' + file_name
