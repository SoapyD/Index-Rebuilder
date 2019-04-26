
import os
path = os.getcwd() #get the current path
string_pos = path.index('Python') #find the python folder
base_path = path[:string_pos]+'Python\\' #create a base filepath string
exec(open(base_path+"Functions\\functions.py").read()) #load the master password file

exec(open("run_process_stack.py").read())

global error_count

u_print('########################################')
u_print('RUNNING INDEX REBUILDER PROCESS')
u_print('########################################')

start_time = datetime.datetime.now() #need for process time u_printing


db = 1
database = ''

#run the servicenow index updates 
#run_process_stack(db, database)

run the heat index updates
run_heat_process_stack(db, database)


finish_time = datetime.datetime.now()
u_print('')
u_print('########################################')
u_print('PROCESS COMPLETE')

u_print('Number of Errors: '+str(error_count))
u_print('Start: '+str(start_time))
u_print('End: '+str(finish_time))
u_print('Time Taken: '+str(finish_time - start_time))
u_print('########################################')

save_process(start_time, finish_time, str(finish_time - start_time), "Index-Rebuilder", 'daily')