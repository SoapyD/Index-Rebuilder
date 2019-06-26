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


	source = 'lfliveextract'
	
	tablename = 'session_reduction'
	format_script(source, tablename, db, database)
	tablename = 'nps_reduction'
	format_script(source, tablename, db, database)


def run_heat_process_stack(db, database):

	source = 'heat'

	tablename = 'changes'
	format_script(source, tablename, db, database)
	tablename = 'employee_data'
	format_script(source, tablename, db, database)
	tablename = 'escalations'
	format_script(source, tablename, db, database)
	tablename = 'incidents'
	format_script(source, tablename, db, database)
	tablename = 'organisations'
	format_script(source, tablename, db, database)
	tablename = 'problems'
	format_script(source, tablename, db, database)
	tablename = 'service_requests'
	format_script(source, tablename, db, database)
	tablename = 'tasks'
	format_script(source, tablename, db, database)

	source = 'contacts'

	tablename = 'answer'
	format_script(source, tablename, db, database)
	tablename = 'completedsurvey'
	format_script(source, tablename, db, database)
	tablename = 'completedsurveyresponse'
	format_script(source, tablename, db, database)
	tablename = 'fsa_sessionincident'
	format_script(source, tablename, db, database)
	tablename = 'he_sessionincident'
	format_script(source, tablename, db, database)
	tablename = 'mhclg_sessionincident'
	format_script(source, tablename, db, database)
	tablename = 'croydon_sessionincident'
	format_script(source, tablename, db, database)	
	tablename = 'sessionincident'
	format_script(source, tablename, db, database)
	tablename = 'session'
	format_script(source, tablename, db, database)
	tablename = 'sessionpostback'
	format_script(source, tablename, db, database)

	tablename = 'telephony'
	format_script(source, tablename, db, database)


	tablename = 'lflive'
	format_script(source, tablename, db, database)
	tablename = 'nps'
	format_script(source, tablename, db, database)