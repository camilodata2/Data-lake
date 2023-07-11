from cargue.conect import *
def load_file(file_name):
    table_name = file_name.split('.')[0]
    client.upload_file(
        Filename="target/{}".format(file_name),
        Bucket="cyberdata-bucket",
        Key="course_etl_target/{}".format(file_name),
    )

    sentence = '''copy public.{} from 's3://cybertdata-bucket{}' credentials 'aws_access_key_id={};aws_secret_access_key={}' csv delimiter '|' region 'us-east-2b' ignoreheader 1'''.format(
        table_name, file_name, os.environ.get('AWS_ACCESS_KEY_ID'), os.environ.get('AWS_SECRET_ACCESS_KEY')
    )
    try:
        cursor.execute(sentence)
        print('ok tabla '+ table_name)
    except:
        print('error en la tabla '+table_name)


list_files = os.listdir('target/')
for _ in list_files:
    load_file(_)

conn.commit()

conn.close()
