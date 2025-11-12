import shutil
from pathlib import Path


def Task2():
    global task_continue,second_task,task
    if task == 2:     
            task_continue = False
            folder_path = Path(input('Enter the folder path to copy: '))
            if folder_path.exists():
                copied_folder_path = Path(input('Enter the path where u want folder to be copied: '))
                if copied_folder_path.exists():
                    copied_folder_name = input('Enter the copied folder name: ')
                    full_copied_folder_path = copied_folder_path/copied_folder_name
                    if full_copied_folder_path.exists():
                        print('Folder already exists!')
                        second_task = False
                    else:
                        try:
                          shutil.copytree(folder_path, full_copied_folder_path)
                          print('Success your folder was successfully copied!')
                        except Exception as e:
                          print(f"Error copying folder: {e}")   # error = Error copying folder: [WinError 183] Cannot create a file when that file already exists: 'C:\\Users\\User\\Desktop\\CopiedFolder'

                        second_task = False
                else:
                    print("Invalid Path entered Try Again!")
                    continue_task2 = input('Do u want to continue with task2? (Yes/No): ')
                    if continue_task2.lower() == 'no':
                        task_continue = True
                        second_task = False
                        
            else:
                print('Invalid Path entered Try Again!')
                continue_task2 = input('Do u want to continue with task2? (Yes/No): ')
                if continue_task2.lower() == 'no':
                    task_continue = True
                    second_task = False
                    
print('Hello and Welcome to our File Organizer.\nWe will help u Organize your Files.')
task_continue = True
while task_continue:
    task = int(input(
        'What do u want to do?\n1.Organize Files\n2.Copy a folder\n3.Move files from one folder to another\nSelect (1, 2 or 3): '
    ))
  
    second_task = True
    while second_task:
        Task2()
                    
 