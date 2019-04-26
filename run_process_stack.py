def format_script(source, tablename, db, database):

	start_time = datetime.datetime.now() #need for process time u_printing

	filename = source+'_'+tablename+' UPDATE'
	sql = "ALTER INDEX ALL ON "+source+'_'+tablename+" REBUILD;"

	u_print("UPDATING INDEXES ON... "+tablename)
	query_database2(filename, sql, db, database)

	finish_time = datetime.datetime.now() #need for process time u_printing
	u_print('Time Taken: '+str(finish_time - start_time))

def run_process_stack(db, database):

	source = 'he'

	tablename = 'sys_user'
	format_script(source, tablename, db, database)
	tablename = 'incident_alert'
	format_script(source, tablename, db, database)
	tablename = 'incident'
	format_script(source, tablename, db, database)
	tablename = 'incident_task'
	format_script(source, tablename, db, database)
	tablename = 'sc_request'
	format_script(source, tablename, db, database)
	tablename = 'sc_req_item'
	format_script(source, tablename, db, database)
	tablename = 'sc_task'
	format_script(source, tablename, db, database)
	tablename = 'change_request'
	format_script(source, tablename, db, database)
	tablename = 'change_task'
	format_script(source, tablename, db, database)
	tablename = 'problem'
	format_script(source, tablename, db, database)
	tablename = 'problem_task'
	format_script(source, tablename, db, database)
	tablename = 'task_sla'
	format_script(source, tablename, db, database)
	tablename = 'sc_cat_item'
	format_script(source, tablename, db, database)

	source = 'croydon'
	
	tablename = 'sys_user'
	format_script(source, tablename, db, database)
	tablename = 'incident'
	format_script(source, tablename, db, database)
	tablename = 'sc_request'
	format_script(source, tablename, db, database)
	tablename = 'sc_req_item'
	format_script(source, tablename, db, database)
	tablename = 'sc_task'
	format_script(source, tablename, db, database)
	tablename = 'problem'
	format_script(source, tablename, db, database)
	tablename = 'problem_task'
	format_script(source, tablename, db, database)
	tablename = 'task_sla'
	format_script(source, tablename, db, database)
	tablename = 'sc_cat_item'
	format_script(source, tablename, db, database)

	source = 'mhclg'
	
	tablename = 'sys_user'
	format_script(source, tablename, db, database)
	tablename = 'incident'
	format_script(source, tablename, db, database)
	tablename = 'sc_request'
	format_script(source, tablename, db, database)
	tablename = 'sc_req_item'
	format_script(source, tablename, db, database)
	tablename = 'sc_task'
	format_script(source, tablename, db, database)
	tablename = 'problem'
	format_script(source, tablename, db, database)
	tablename = 'problem_task'
	format_script(source, tablename, db, database)
	tablename = 'task_sla'
	format_script(source, tablename, db, database)
	tablename = 'sc_cat_item'
	format_script(source, tablename, db, database)

	source = 'fsa'
	
	tablename = 'sys_user'
	format_script(source, tablename, db, database)
	tablename = 'incident'
	format_script(source, tablename, db, database)
	tablename = 'sc_request'
	format_script(source, tablename, db, database)
	tablename = 'sc_req_item'
	format_script(source, tablename, db, database)
	tablename = 'sc_task'
	format_script(source, tablename, db, database)
	tablename = 'problem'
	format_script(source, tablename, db, database)
	tablename = 'problem_task'
	format_script(source, tablename, db, database)
	tablename = 'task_sla'
	format_script(source, tablename, db, database)
	tablename = 'sc_cat_item'
	format_script(source, tablename, db, database)