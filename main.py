import os
import db

def list_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            #print(os.path.join(root, file))
            #print(file)
            parts1 = file.split("(")
            print(parts1[0])
            parts2 = parts1[1].split(")")
            print(parts2[0])
            with open(os.path.join(root, file), 'r') as file:
               for line in file:
                   line = line.replace("'","\"")
                   num = db.check_sql(line)
                   if len(num)== 0:
                       #print(file)
                       db.insert_sql(line)
                       num2 = db.check_sql(line)
                       db.insert_ip(str(num2[0][0]), parts1[0], parts2[0])
                   else:
                       num2 = db.check_sql(line)
                       db.insert_ip(str(num2[0][0]), parts1[0], parts2[0])


if __name__ == '__main__':
    directory = '//172.16.9.10/pc-inf'
    list_files(directory)


