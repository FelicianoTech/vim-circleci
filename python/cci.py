import json
import subprocess
import webbrowser

from circleci.circleci import api


class Project:

    def __init__(self, vcs, org, repo):

        self.vcs = vcs
        self.org = org
        self.repo = repo

def config_validate():
    result = subprocess.run([ "circleci" , "config", "validate"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode == 0:
        print( "The CircleCI config file is valid." )
    else:
        print( "The CircleCI config file is invalid." )


def load_projects():
    
    # Notes:

    # git symbolic-ref --shortHEAD
    # This will give us the current branch name, or return error on a dettached HEAD -- Git v1.8 or later

    result = subprocess.run([ "git", "remote", "show"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    git_remotes = result.stdout.strip().split()

    projects = []

    for remote in git_remotes:

        result = subprocess.run([ "git", "remote", "get-url", remote], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        project_path = result.stdout.strip()

        if project_path.endswith( ".git" ):
            project_path = project_path[:-4]

        if project_path.startswith( "git@" ):
            project_path = project_path.split( ":" )[1]

        if project_path.startswith( "https://" ):
            project_path = project_path.split( "/" )[4:]



        project_path = project_path.split("/")

        # Hardcoding "github" for now. Need to be able to detect Bitbucket in the future.
        projects.append( Project( "github", project_path[0], project_path[1] ))

    return projects


def get_token():

    result = subprocess.run([ "circleci", "diagnostic"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    lines = result.stdout.splitlines()

    for line in lines:
        if line.startswith( "Config found:" ):
            config_path = line[14:].strip()
            break

    with open( config_path ) as f:
        for line in f:
            if line.startswith( "token" ):
                return line[7:].strip()


def vim_open():

    projects = load_projects()

    cci_api = api.Api( get_token() )

    for project in projects:
    
        builds = cci_api.get_project_build_summary( project.org, project.repo, 1, 0, None, "master")

        # This project isn't on CircleCI so skip it.
        if len( builds ) == 0:
            continue

        webbrowser.open( "https://circleci.com/gh/" + project.org + "/" + project.repo, 2 )


def vim_status():

    projects = load_projects()

    cci_api = api.Api( get_token() )

    for project in projects:
    
        builds = cci_api.get_project_build_summary( project.org, project.repo, 1, 0, None, "master")

        # This project isn't on CircleCI so skip it.
        if len( builds ) == 0:
            continue

        print( "Latest build status: " + builds[0]["status"] + "; Project: " + project.org + "/" + project.repo + "; Build #" + str( builds[0]["build_num"] ))
