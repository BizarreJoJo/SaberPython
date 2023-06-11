'''
Usage:
    app.py list builds [<path>]
    app.py list tasks [<path>]
    app.py get build <build_name> [<path>]
    app.py get task <task_name> [<path>]    
    app.py path <path>
    app.py reset
      
'''
from docopt import docopt
import list
import get
import config
import os

def main():
    args = docopt(__doc__)
    
    _path_check = path_check(args['<path>'])
    if _path_check[0]:
        response = _path_check[1]
        
    elif args['list']:       

        if args['builds']:
            response = list.get_list(
                args['<path>'],
                'List of available builds:',
                'builds.yaml',
                'builds')
            
        elif args['tasks']:
            response = list.get_list(
                args['<path>'],
                'List of available tasks:',
                'tasks.yaml',
                'tasks')

    elif args['get']:        

        if args['build']:            
            response = get.build(
                args['<build_name>'],
                args['<path>'],
                'builds.yaml',
                'tasks.yaml')
        elif args['task']:
            response = get.task(
                args['<task_name>'],
                args['<path>'],
                'tasks.yaml'
                )

    elif args['path']:       
        
        response = config.save(args['<path>'])
        
    elif args['reset']:       
        
        response = config.reset()
        
    print(response)

def path_check(path):      
    if path and not os.path.isdir(path):
        return (True, 'Incorrect directory')
    return (False, None)

if __name__ == '__main__':
    main()