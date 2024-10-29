import pypyodbc # type: ignore

class Schema:
    def connector(self,server,database):
        connection=f'''
        DRIVER={{SQL SERVER}};
        SERVER={server};
        DATABASE={database};
        Trust_Connection=yes;
        '''
        con=pypyodbc.connect(connection)
        return con
    
    def drop_schema(self,connection,schema):
        try:
            cursor=connection.cursor()
        except:
            print('Invalid Connection!!')
            return
        cursor.execute(f"select schema_id from sys.schemas where name='{schema}'")
        try:
            schema_id=int(cursor.fetchall()[0][0])
        except:
            print('Schema Not Found')
            return
        cursor.execute(f"select name,type from sys.objects where type in ('U','V') and schema_id={schema_id}")
        objects=cursor.fetchall()
        for i in objects:
            try:
                if i[1]=='U ':
                    cursor.execute(f'Drop table {schema}.{i[0]}')
                elif i[1]=='V ':
                    cursor.execute(f'Drop view {schema}.{i[0]}')
            except Exception as e:
                print(e)
        cursor.execute(f'drop schema {schema}')
        cursor.commit()
        connection.close()
        print('Schema Drop Successful')
    
    def transfer_schema(self,connection,schema,schema_new):
        try:
            cursor=connection.cursor()
        except:
            raise Exception('Invalid Connection!!')
        try:
            cursor.execute(f"Create Schema {schema_new}")
        except:
            pass
        try:
            cursor.execute(f"select schema_id from sys.schemas where name='{schema}'")
            schema_id=int(cursor.fetchall()[0][0])
        except:
            raise Exception('Schema Not Found')
            return
        cursor.execute(f"select name,type from sys.objects where type in ('U','V') and schema_id={schema_id}")
        objects=cursor.fetchall()
        for i in objects:
            try:
                if i[1]=='U ':
                    cursor.execute(f'Alter Schema {schema_new} transfer {schema}.{i[0]}')
                elif i[1]=='V ':
                    cursor.execute(f'Alter Schema {schema_new} transfer {schema}.{i[0]}')
            except Exception as e:
                print(e)
        cursor.execute(f'drop schema {schema}')
        cursor.commit()
        connection.close()
        print('Schema Transfer Successful')

connection=input('Connection: ')
database=input('Database: ')
print('''
1. Drop Schema
2. Transfer Schema
3. Exit
''')

while True:
    choice=int(input('Enter your choice: '))
    match choice:
        case 1:
            obj=Schema()
            con=obj.connector(connection,database)
            schema=input('Schema: ')
            obj.drop_schema(con,schema)
        case 2:
            obj=Schema()
            con=obj.connector(connection,database)
            schema1=input('From Schema: ')
            schema2=input('To Schema: ')
            obj.transfer_schema(con,schema1,schema2)
        case 3:
            break
        case _:
            print('Invalid Value!')
