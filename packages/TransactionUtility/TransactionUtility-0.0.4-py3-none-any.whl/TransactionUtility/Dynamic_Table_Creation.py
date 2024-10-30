import cx_Oracle
from collections import defaultdict
import loggerutility as logger

class Dynamic_Table_Creation:
        
    def check_table_exists(self, table_name, connection):
        if not connection:
            return False
        cursor = connection.cursor()
        try:
            cursor.execute(f"SELECT COUNT(*) as CNT FROM USER_TABLES WHERE TABLE_NAME = :table_name", table_name=table_name)
            count = cursor.fetchone()[0]
            cursor.close()
            return count > 0
        except cx_Oracle.Error as error:
            logger.log(f"Error checking APP_NAME existence: {error}")
            return False
        
    def check_column_exists(self, table_name, column_name, connection):
        if not connection:
            return False
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                    SELECT COUNT(*) as CNT FROM all_tab_columns 
                    WHERE table_name = :table_name AND column_name = :column_name
                """,
                table_name=table_name,
                column_name=column_name
            )
            count = cursor.fetchone()[0]
            cursor.close()
            return count > 0
        except cx_Oracle.Error as error:
            logger.log(f"Error checking if column {column_name} exists in {table_name}: {error}")
            return False

    
    def create_new_table(self, table_lst, connection):
        for table_name, columns in table_lst.items():
            logger.log(f"In table_name ::: {table_name}")
            logger.log(f"In columns ::: {columns}")
            columns_sql = []

            table_name = table_name
            for single_col in columns:

                col_name = single_col['db_name']
                col_type = single_col['col_type'].upper()
                db_size = single_col.get('db_size', None)
                is_key = single_col.get('key', False)
                mandatory = single_col.get('mandatory', 'false')

                col_def = ''
                if col_type == 'CHAR' and db_size:
                    if db_size == '0':
                        col_def = f"{col_name} {col_type}(10)"  
                    else:
                        col_def = f"{col_name} {col_type}({db_size})"
                
                elif col_type == 'DECIMAL':
                    if db_size != '0':
                        col_def = f"{col_name} DECIMAL({db_size}, 2)"  
                    else:
                        col_def = f"{col_name} DECIMAL(5, 2)"  
                
                elif col_type == 'DATETIME':
                    col_def = f"{col_name} DATE" 

                else:
                    col_def = f"{col_name} {col_type}"  

                if mandatory == True:
                    col_def += " PRIMARY KEY"
                    
                if col_def != '':
                    columns_sql.append(col_def)

            columns_sql_str = ", ".join(columns_sql)
            
            create_table_sql = f"CREATE TABLE {table_name} ({columns_sql_str})"
            logger.log(f"create_table_sql ::: {create_table_sql}")

            cursor = connection.cursor()
            try:
                cursor.execute(create_table_sql)
                logger.log(f"Table {table_name} created successfully.")
            except cx_Oracle.Error as error:
                logger.log(f"Error creating table {table_name}: {error}")

    def alter_table_add_columns(self, table_name, single_col, connection):

        col_name = single_col['db_name']
        col_type = single_col['col_type'].upper()
        db_size = single_col.get('db_size', 10)
        is_key = single_col.get('key', False)
        mandatory = single_col.get('mandatory', 'false')

        col_def = ''
        if col_type == 'CHAR' and db_size:
            if db_size == '0':
                col_def = f"{col_name} {col_type}(10)"  
            else:
                col_def = f"{col_name} {col_type}({db_size})"
        
        elif col_type == 'DECIMAL':
            if db_size != '0':
                col_def = f"{col_name} DECIMAL({db_size}, 2)"  
            else:
                col_def = f"{col_name} DECIMAL(5, 2)"  
        
        elif col_type == 'DATETIME':
            col_def = f"{col_name} DATE" 

        else:
            col_def = f"{col_name} {col_type}"  

        if mandatory == True:
            col_def += " PRIMARY KEY"

        alter_table_sql = f"ALTER TABLE {table_name} ADD ({col_def})"
        logger.log(f"{alter_table_sql}")

        cursor = connection.cursor()
        try:
            cursor.execute(alter_table_sql)
            logger.log(f"Column {col_name} added successfully to table {table_name}.")
        except cx_Oracle.Error as error:
            logger.log(f"Error adding column {col_name} to table {table_name}: {error}")
            return False

    def create_alter_table(self, data, connection):
        logger.log(f"Start of Dynamic_Table_Creation Class")
        if "transaction" in data and "sql_models" in data['transaction']:
            for index,sql_models in enumerate(data["transaction"]["sql_models"]):
                columns = sql_models["sql_model"]["columns"]
                table_json = defaultdict(list)
                for column in columns:
                    column = column['column']
                    table_name = column['table_name']
                    column_name = column['db_name']
                    exists = self.check_table_exists(table_name.upper(), connection)
                    logger.log(f"table_name ::: {table_name}")
                    logger.log(f"exists ::: {exists}")
                    if exists:
                        logger.log(f"column_name ::: {column_name}")
                        column_exist = self.check_column_exists(table_name.upper(), column_name.upper(), connection)
                        logger.log(f"column_exist ::: {column_exist}")
                        if not column_exist:
                            logger.log(f"Inside column_exist ::: {table_name.upper(), column}")
                            self.alter_table_add_columns(table_name.upper(), column, connection)
                    else:
                        table_json[table_name.upper()].append(column)
                logger.log(f"outside forloop ::: {dict(table_json)}")
                self.create_new_table(dict(table_json), connection)
            
            logger.log(f"End of Dynamic_Table_Creation Class")
            return f"Success"

