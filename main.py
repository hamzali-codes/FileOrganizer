import shutil
from pathlib import Path


def Task2(task_continue,second_task):    
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
        return task_continue,second_task
                    


def Task3(task_continue,third_task):
    task_continue = False
    f = Path(input("Enter the folder path to copy files from: "))
    if f.exists():
        file_types = input("Select all file or Select file types: (Type 'all' if u want all file to be transefered else type (jpg,png,pdf,csv..etc) ").lower()
        new_f = input('Do u want to create a new folder for the files: (yes/no): ').lower()
        if new_f == 'yes':
            folder_name = input('Enter your folder name: ')
            fc = Path(input("Enter the path where u want the folder: "))
            if fc.exists():
                if file_types == 'all':
                    new_folder_path = fc/folder_name
                    new_folder_path.mkdir(exist_ok=True)
                    try:
                        shutil.move(f,new_folder_path)
                        print(f'Success your files were successfuly transefered to your path: {fc}')
                        third_task = False
                        task_continue = True
                    except Exception as e:
                        print(f'Error Transferring Files: {e}')
                        third_task = False
                        task_continue = True
                        
                else:
                    ft = '*.'+file_types
                    new_folder_path = fc/folder_name
                    new_folder_path.mkdir(exist_ok=True)
                    try:
                        for file in f.glob(ft):
                          shutil.move(file,new_folder_path)
                    except Exception as e:
                        print(f'Something went wrong: {e}')
                    third_task = False
                    task_continue = True
                    
                    
            else:
                print('Invalid path entered Please try again!')
    
                
        elif new_f == 'no':
            fc = Path(input('Enter the path of your folder wheru u want the files to be transfered: '))
            if fc.exists():
                if file_types=='all':
                    try: 
                        shutil.move(f,fc)
                        print(f'Success your files were successfuly transefered to your path: {fc}')
                        third_task = False
                        task_continue = True
                    except Exception as e:
                        print(f'Error Transferring Files: {e}')
                        third_task = False
                        task_continue = True
                else:
                    try:
                        for file in f.glob(ft):
                          shutil.move(file,fc)
                    except Exception as e:
                        print(f'Something went wrong: {e}')
                    third_task = False
                    task_continue = False
                    
                    
            else:
                print("Invalid Input Please Try again!")
                    
        else:
            print('Invalid Input!')
    
    else:
        print('Invalid path enterd Please try again!')
        
    return task_continue,third_task






print('Hello and Welcome to our File Organizer.\nWe will help u Organize your Files.')
task_continue = True
while task_continue:
    task = int(input(
        'What do u want to do?\n1.Organize Files\n2.Copy a folder\n3.Move files from one folder to another\nSelect (1, 2 or 3): '
    ))
  
    second_task = True
    third_task = True
    while second_task:
        if task == 2: 
            task_continue,second_task = Task2(task_continue,second_task)
        elif task == 3:
            task_continue,third_task = Task3(task_continue,third_task)
                    
 