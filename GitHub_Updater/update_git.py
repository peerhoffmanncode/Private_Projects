###
### GitHub CMD Line update script
### Usage:
###
### <script name> -repro=

import os
import sys

def execute_git_cmd(init_new_repro, repro, addfile, commit_msg, branch, push):
    if repro == "" or addfile == "":
        print("")
        print("no Repo is set, or no files are selected!")
        print("use:")
        print("<scritname.py> -repro=<repro name> -addfile=* -commit_msg=<your msg> -branch=<your branch> -commit&push -init)")
        print("")
        quit() 
    else:
        # git init
        if init_new_repro: exec_cmd("git init")
        # git add files
        exec_cmd("git add " + addfile)
        # git commit -m "first commit"
        exec_cmd("git commit -m \"" + commit_msg + "\"")
        # git branch -M main
        exec_cmd("git branch -M " + branch)
        # git remote add origin https://github.com/peerhoffmanncode/update_git.git
        exec_cmd("git remote add origin https://github.com/peerhoffmanncode/" + repro + ".git")
        # git push -u origin main
        exec_cmd("git push -u origin " + branch)
        print("")
        print("done... exiting!")
        print("")

def find_args_and_vals(system_arg: list) -> list:
    
    return_list_arg = []
    return_list_val = []
    
    for i in system_arg:
        i = i.strip()
        if i == "push" or i == "init":
            arg = i.strip()
            val = ""
            return_list_arg.append(arg)
            return_list_val.append(val)
        else:
            try:
                arg = str(i[:i.index("=")]).strip()
                val = str(i[i.index("=")+1:]).strip()
                return_list_arg.append(arg.lower())
                return_list_val.append(val.lower())
            except ValueError:
                pass

    return return_list_arg, return_list_val


def exec_cmd(command):
    handle = os.popen(command)
    return

__name__ == "__main__"

arglst, valuelst = find_args_and_vals(sys.argv)

# set default values
repro = addfile = ""
push = True
init_new_repro = True
commit_msg = "first commit"
branch = "main"

# set values for the found args
for i, arg in enumerate(arglst):
    if "repro" in arg:
        repro = valuelst[i]
    if "addfile" in arg:
        addfile = valuelst[i]
    if "commit_msg" in arg:
        commit_msg = valuelst[i]
    if "push" in arg:
        push = True
    if "init" in arg:
        init_new_repro = True

# execute Git
execute_git_cmd(init_new_repro, repro, addfile, commit_msg, branch, push)
