__author__ = 'mohamed'
from models import *
import simplejson
from  autodeploy_client.Client import Client
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
def checkServers(request):
    res = {}
    for server in Server.objects.all():
        c = Client("git", server.ip, server.port)
        state = c.CheckUp()
        if state:
            res[server.name] = "UP"
        else:
            res[server.name] = "DOWN"
    return HttpResponse(simplejson.dumps(res))

@csrf_protect
def clone(request):
    scm = str(request.GET["scm"])
    ip = str(request.GET["ip"])
    port = int(request.GET["port"])
    project=Project.objects.get(name=request.GET["project_name"])
    c = Client(scm,ip,port,project.sshKey.key)
    res = c.Clone(project.repo, project.working_dir)
    return HttpResponse(res)

@csrf_protect
def deploy(request):
    server = Server.objects.get(name=request.session["deploy_server"])
    project = Project.objects.get(name=request.session["deploy_project"])
    D= Deployment_Server()
    c = Client(str(project.repo_type), server.ip, server.port)
    D.project = project
    D.server = server
    if "tag" in request.GET:
        res = c.SwitchTag(project.working_dir, request.GET["tag"])
        D.update_type="tag"
        D.update_version=request.GET["tag"]
    elif "commit" in request.GET:
        if request.GET["commit"] != "HEAD":
            res=c.SwitchCommit(project.working_dir,request.GET["commit"])
        D.update_type="commit"
        D.update_version = request.GET["commit"]
    res = c.Deploy(project.working_dir, project.configFile)
    if not "ERR:" in res:
        D.datetime=timezone.now()
        D.has_new_version=False
        D.save()
        if "http://" not in project.deployment_link:
            return HttpResponse(res+",,http://"+server.DNS+project.deployment_link)
        else:
            return HttpResponse(res+",,"+project.deployment_link)