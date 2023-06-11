import yaml
import networkx as nx
import config
import loader

def build(name, path, filename_builds, filename_task):
    path = config.get_path(path)
    
    tasks_list = None
    
    for _build in loader.load_file(path + filename_builds)['builds']:
        if _build['name'] == name:
            tasks_list = _build['tasks']
            break
    if tasks_list is None:
        return 'No build data'
    
    task_data = loader.load_file(path + filename_task)['tasks']
    
    tasks_list = dependencies_graph(task_data, tasks_list)
    
    if tasks_list is None:
        return 'Tasks graph has cycle'
    
    result = 'Build info:\n * name: {}\n * tasks: {}'.format(
        name,
        ', '.join(tasks_list)
        )
    return result
    
def task(name, path, filename):
    path = config.get_path(path)
    
    data = loader.load_file(path + filename)['tasks']
    
    dependencies = None
    for _task in data:
        if _task['name'] == name:
            dependencies = _task['dependencies']
            break
    if dependencies is None:
        return 'No task data'
        
    result = 'Task info:\n * name: {}\n * dependencies: {}'.format(
        name,
        ', '.join(dependencies)
        )
    
    return result
        
def dependencies_graph(data, tasks):
    
    graph = nx.DiGraph()
    graph.add_nodes_from([i['name'] for i in data])
    graph.add_edges_from(
        [
            (_task['name'], dependency)
            for _task in data
            for dependency in _task["dependencies"]
        ]
    )
    
    subgraph = nx.DiGraph()
    subgraph.add_nodes_from(tasks)    
    [
        subgraph.add_nodes_from(nx.descendants(graph, _task))
        for _task in tasks
    ]
    
    [
        subgraph.add_edge(*edge)
        for edge in graph.edges
        if edge[0] in subgraph.nodes()
    ]
            
    try:
        return list(nx.topological_sort(subgraph))[::-1]
    except nx.exception.NetworkXUnfeasible:
        return None