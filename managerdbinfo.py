db_info = {
    'host': '10.10.10.175',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'dbmanager',
    'autocommit': True,
    'charset': 'utf8mb4',
}
sql = "select * from db_info"



'''
host = None, user = None, password = "",
database = None, port = 0, unix_socket = None,
charset = '', sql_mode = None,
read_default_file = None, conv = None, use_unicode = None,
client_flag = 0, cursorclass = Cursor, init_command = None,
connect_timeout = 10, ssl = None, read_default_group = None,
compress = None, named_pipe = None,
autocommit = False, db = None, passwd = None, local_infile = False,
max_allowed_packet = 16 * 1024 * 1024, defer_connect = False,
auth_plugin_map = None, read_timeout = None, write_timeout = None,
bind_address = None, binary_prefix = False, program_name = None,
server_public_key = None
'''