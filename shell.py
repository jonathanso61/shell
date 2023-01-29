import getpass
import os
import platform
import sys
import shutil
from threading import Semaphore
from time import sleep


if platform.system() == 'Windows':
    PLATFORM = True
    import msvcrt
    semaphore = Semaphore()
    ROOT = 'C:\\'
else:
    PLATFORM = False
    ROOT = '/'
    import fcntl
    semaphore = Semaphore()


def access(file=None, command=None, function=None):
    semaphore.acquire()
    try:
        if PLATFORM:
            file = open(file, 'r+')
            msvcrt.locking(file.fileno(), msvcrt.LK_RLCK, 1)
            function(command)
        else:
            file = open(file, 'r+')
            fcntl.flock(file, fcntl.LOCK_EX | fcntl.LOCK_NB)
            function(command)
    except Exception as e:
        print('Um processo esta executando este arquivo')
    finally:
        if PLATFORM:
            msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, 1)
            file.close()
        else:
            fcntl.flock(file, fcntl.LOCK_UN)
            file.close()
        semaphore.release()
        sleep(1)


def access_copy(file=None, name=None, function=None):
    semaphore.acquire() 
    try:
        if PLATFORM:
            file = open(file, 'r+')
            msvcrt.locking(file.fileno(), msvcrt.LK_RLCK, 1)
            function(name, file)
        else:
            file = open(file, 'r+')
            fcntl.flock(file, fcntl.LOCK_EX | fcntl.LOCK_NB)
            function(name, file)
    except Exception as e:
        print('Um processo esta executando este arquivo')
    finally:
        if PLATFORM:
            msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, 1)
            file.close()
        else:
            fcntl.flock(file, fcntl.LOCK_UN)
            file.close()
        semaphore.release()
        sleep(1)


def ver():
    print(platform.system())
    semaphore.release()


def dir(command):
    if PLATFORM:
        os.system('dir {0}'.format(command))
    else:
        os.system('ls {0}'.format(command))
    semaphore.release()


def exit():
    sys.exit(0)
    semaphore.release()


def mkdir(path):
    os.mkdir(path)
    semaphore.release()


def rm_d(path):
    os.rmdir(path)
    semaphore.release()


def current_dir():
    return os.getcwd()
    semaphore.release()


def rm_a(path):
    if PLATFORM:
        os.system('del {0}'.format(path))
    else:
        os.system('rm -a {0}'.format(path))
    semaphore.release()


def mv(file, path):
    shutil.move(file, path)
    semaphore.release()


def cp(file, path):
    shutil.copy(file, path)
    semaphore.release()


def cat(path):
    file = open(path, 'r+')
    print(file.read())
    file.close()
    semaphore.release()


def edit(path):
    if PLATFORM:
        os.system('notepad {0}'.format(path))
    else:
        os.system('nano {0}'.format(path))
    semaphore.release()


def cd(path):
    os.chdir(path)
    semaphore.release()


if __name__ == '__main__':
    print("USER: {0}".format(getpass.getuser()))
    print("""
        ███████████████████████████████
        ████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬████
        ██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
        █╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
        █╬╬╬███████╬╬╬╬╬╬╬╬╬███████╬╬╬█
        █╬╬██╬╬╬╬███╬╬╬╬╬╬╬███╬╬╬╬██╬╬█
        █╬██╬╬╬╬╬╬╬██╬╬╬╬╬██╬╬╬╬╬╬╬██╬█
        █╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
        █╬╬╬╬█████╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬█
        █╬╬█████████╬╬╬╬╬╬╬█████████╬╬█
        █╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
        █╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
        █╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
        █╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
        █╬╬╬▓▓▓▓╬╬╬╬╬╬╬█╬╬╬╬╬╬╬▓▓▓▓╬╬╬█
        █╬╬▓▓▓▓▓▓╬╬█╬╬╬█╬╬╬█╬╬▓▓▓▓▓▓╬╬█
        █╬╬╬▓▓▓▓╬╬██╬╬╬█╬╬╬██╬╬▓▓▓▓╬╬╬█
        █╬╬╬╬╬╬╬╬██╬╬╬╬█╬╬╬╬██╬╬╬╬╬╬╬╬█
        █╬╬╬╬╬████╬╬╬╬███╬╬╬╬████╬╬╬╬╬█
        █╬╬╬╬╬╬╬╬╬╬╬╬╬███╬╬╬╬╬╬╬╬╬╬╬╬╬█
        ██╬╬█╬╬╬╬╬╬╬╬█████╬╬╬╬╬╬╬╬█╬╬██
        ██╬╬██╬╬╬╬╬╬███████╬╬╬╬╬╬██╬╬██
        ██╬╬▓███╬╬╬████╬████╬╬╬███▓╬╬██
        ███╬╬▓▓███████╬╬╬███████▓▓╬╬███
        ███╬╬╬╬▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬███
        ████╬╬╬╬╬╬╬╬╬╬███╬╬╬╬╬╬╬╬╬╬████
        █████╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬█████
        ██████╬╬╬╬╬╬╬╬███╬╬╬╬╬╬╬╬██████
        ███████╬╬╬╬╬╬╬███╬╬╬╬╬╬╬███████
        ████████╬╬╬╬╬╬███╬╬╬╬╬╬████████
        █████████╬╬╬╬╬███╬╬╬╬╬█████████
        ███████████╬╬╬╬█╬╬╬╬███████████
        ███████████████████████████████

    """)
    while True:
        try:
            if current_dir == ROOT:
                command = input('> ')
            else:
                command = input('{0}/> '.format(current_dir().replace('\\', '/').replace('C:/', '').replace('//', '/')))
            semaphore.acquire()
            if command.split(' ')[0] == 'dir':
                dir(command.split(' ')[1])

            elif command.split(' ')[0] == 'exit':
                exit()

            elif command.split(' ')[0] == 'ver':
                ver()

            elif command.split(' ')[0] == 'mkdir':
                mkdir(command.split(' ')[1])

            elif command.split(' ')[0] == 'rm' and command.split(' ')[1] == '-r':
                rm_d(command.split(' ')[2])

            elif command.split(' ')[0] == 'rm' and command.split(' ')[1] == '-a':
                rm_a(command.split(' ')[2])

            elif command.split(' ')[0] == 'mv':
                mv(command.split(' ')[1], command.split(' ')[2])

            elif command.split(' ')[0] == 'cp':
                access_copy(file=command.split(' ')[2], function=cp, name=command.split(' ')[1])
            elif command.split(' ')[0] == 'cat':
                cat(command.split(' ')[1])

            elif command.split(' ')[0] == 'edit':
                access(command=command.split(' ')[1], function=edit, file=command.split(' ')[1])

            elif command.split(' ')[0] == 'cd':
                cd(command.split(' ')[1])
            else:
                print("'{0}' Comando nao foi encontrado!".format(command))
        except PermissionError as e:
            pass
        except Exception as e:
            pass
        except KeyboardInterrupt as e:
            pass
