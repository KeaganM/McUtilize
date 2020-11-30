import os
import subprocess

if __name__ == '__main__':

    subprocess.Popen('dir /s > fileNames2.txt',cwd='test')

    # def create_eb(directory:str)

    # subprocess.run('aws --version')
    # quit()

    # os.system('aws --version')
    # # change directory
    # os.chdir('test')
    # os.system('dir /s > fileNames.txt')
    # os.system('eb init')
    # os.system('eb create test-env')
    #
    # pass
