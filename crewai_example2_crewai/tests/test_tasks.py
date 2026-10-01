from models import TaskManager
import os
import pytest

def test_task_lifecycle():
    db_file = 'test_tasks.db'
    if os.path.exists(db_file):
        try:
            os.remove(db_file)
        except PermissionError:
            pass
        
    tm = TaskManager(db_name=db_file)
    
    task = tm.create_task('Test', 'Desc')
    assert 'id' in task
    
    tasks = tm.get_all_tasks()
    assert len(tasks) == 1
    
    tm.update_task(task['id'], 'Updated', 'New', True)
    assert tm.get_all_tasks()[0]['completed'] == 1
    
    tm.delete_task(task['id'])
    assert len(tm.get_all_tasks()) == 0
    
    # Note: We don't force cleanup here to avoid WinError 32 if sqlite handles are still held