import pytest
import list
import get
import config
import yaml
import os

def test_list_build(create_sample_data):
    
    result = list.get_list(
        '',
        '',
        'sample_builds.yaml',
        'builds'
        )
    assert len(result) == 30, 'Wrong answer'
    
def test_list_tasks(create_sample_data):
    result = list.get_list(
        '',
        '',
        'sample_tasks.yaml', 
        'tasks'
        )
    assert len(result) == 60, 'Wrong answer'
    
def test_get_build(create_sample_data):
    result = get.build(
        'build1',
        '',
        'sample_builds.yaml',
        'sample_tasks.yaml'
        )
    assert len(result) == 114, 'Wrong answer'
    
def test_get_task(create_sample_data):
    result = get.task(
        'task1',
        '',
        'sample_tasks.yaml'
    )
    assert len(result) == 12, 'Wrong answer'

def test_path():
    result = config.get_path('tests')
    assert len(result) == 6, 'Wrong answer'
    
    result = config.get_path('')
    assert len(result) == 0, 'Wrong answer'
    
def test_build_cycle(create_sample_data):
    result = get.build(
        'build1',
        '',
        'sample_builds.yaml',
        'sample_tasks_cycle.yaml'
        )
    assert result == 'Tasks graph has cycle', 'Wrong answer'

sample_builds = {
    'builds': [{
        'name': 'build1',
        'tasks': [
            'task11',
            'task12'
        ]
    }, {
        'name': 'build2',
        'tasks': ['task2']
    }, {
        'name': 'build2',
        'tasks': []
    }]
}
    
sample_tasks = {
    'tasks':[{
        'name': 'task11',
        'dependencies':[
            'task21'
            'task22'
        ]},{
            'name': 'task12',
            'dependencies':[
                'task21',
                'task23'
            ]
        },{
            'name': 'task13',
            'dependencies':[]
        },{
            'name': 'task21',
            'dependencies':[
                'task31',
                'task32',
                'task22'
            ]
        },{
            'name': 'task22',
            'dependencies':[
                'task32'
            ]
        },{
            'name': 'task23',
            'dependencies':[
                'task33'
            ]
        }
    ]
}

sample_tasks_cycle = {
        'tasks':[{
            'name': 'task11',
            'dependencies':[
                'task21'
                'task22'
            ]},{
                'name': 'task12',
                'dependencies':[
                    'task21',
                    'task23'
                ]
            },{
                'name': 'task13',
                'dependencies':[]
            },{
                'name': 'task21',
                'dependencies':[
                    'task31',
                    'task32',
                    'task22'
                ]
            },{
                'name': 'task22',
                'dependencies':[
                    'task32',
                    'task12'
                ]
            },{
                'name': 'task23',
                'dependencies':[
                    'task33'
                ]
            }
        ]
    }

import pytest

@pytest.fixture
def create_sample_data():
    
    with open('sample_builds.yaml', 'w') as f:
        yaml.dump(sample_builds, f)
    with open('sample_tasks.yaml', 'w') as f:
        yaml.dump(sample_tasks, f)
    with open('sample_tasks_cycle.yaml', 'w') as f:
        yaml.dump(sample_tasks_cycle, f)
        
    yield
    
    os.remove('sample_builds.yaml')
    os.remove('sample_tasks.yaml')
    os.remove('sample_tasks_cycle.yaml')