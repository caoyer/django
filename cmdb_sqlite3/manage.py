#!/usr/bin/env python
import os
import sys
import sqlite3
import json

BASE = os.path.dirname(os.path.abspath(__file__))
print(BASE)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmdb.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    #while False:
    while True:
        try:
            db = sqlite3.connect('mysite.db')
            cursor = db.cursor()
            cursor.execute("select id,username from auth_user where is_superuser=?",('1',))
            user = cursor.fetchone()
            print("------ Table -----------")
            if not user:
                print("请设置管理用户")
                command = []
                command.append(sys.argv[0])
                command.append('createsuperuser')
                execute_from_command_line(command)
            break

        except Exception as e:
            print(str(e))
            print("--------- b ----------")
            if 'table' in str(e):
                command = []
                command.append(sys.argv[0])
                cmd_exec = ["makemigrations", "migrate"]
                for cmd in cmd_exec:
                    command.append(cmd)
                    print("------ %s -------", command)
                    execute_from_command_line(command)
                    command.pop() 
    
    execute_from_command_line(sys.argv)

