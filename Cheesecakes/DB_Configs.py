
DRIVER_NAME= "SQL SERVER"
SERVER_NAME = r""
DATABASE_NAME = "" #

conn_string = f"""
        Driver={{{DRIVER_NAME}}};
        Server={SERVER_NAME};
        Database={DATABASE_NAME};
        Trust_Connection=yes;
    """