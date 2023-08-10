#!/usr/bin/python3
import time
import base64
import json
import pickle
import argparse
import requests
import os
# import bs4
from bs4 import BeautifulSoup


# added a load of the Processed challenges
def getProcd(fname):
    # this will create an empty file first time through.
    if not os.path.exists(fname):
        f = open(fname, "w")
        f.close()
    f = open(fname, "r")
    d = f.read().splitlines()
    f.close()
    a = []
    a = sorted([int(j) for i in d for j in i.split(",") if j.strip() and int(j) not in a])
    return a


# added a save of the Processed challenges
def saveProcd(a, fname):
    f = open(fname, "w")
    a.sort()
    f.writelines(",".join([str(_) for _ in a]))
    f.close()


def getUserArgs():
    parser = argparse.ArgumentParser(
        description="Download all of the correct submission by a user on HackerRank. By @Gambit0970"
    )
    parser.add_argument(
        "uname", metavar="uname", help="Username of the HackerRank account"
    )
    parser.add_argument(
        "password", metavar="password", help="Password of the HackerRank account"
    )

    u_args = parser.parse_args()
    return u_args.uname, u_args.password


def createSession():
    return requests.Session()


def getToken(main_session, site):
    main_session.headers[
        "User-Agent"
    ] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0"
    response = main_session.get(site)
    text = BeautifulSoup(response.text, features="lxml")
    csrf_tag = text.find("meta", {"id": "csrf-token"})
    return csrf_tag["content"]


def wwwLogin(main_session, site, login_data):
    response = main_session.post(site, data=login_data)
    response_data = json.loads(response.text)
    if response_data["status"]:
        print("[*] Login Successful")
    else:
        print("[*] Login Failed")
    return response_data["status"]


def getModels(main_session, site):
    print("[*] Getting Questions")
    question_models = []
    cursor = ""
    done = False
    while not done:
        resp = main_session.get(site.format(cursor=cursor))
        resp_data = json.loads(resp.text)
        cursor = resp_data["cursor"]
        for model in resp_data["models"]:
            if model["ch_slug"] not in question_models:
                question_models.append(model["ch_slug"])
        if resp_data["last_page"]:
            done = True
    return question_models


def getSubmissions(main_session, site, qs):
    print("[*] Getting Submissions")
    thisSubs = {}
    for q in qs:
        resp = main_session.get(site.format(q))
        resp_data = json.loads(resp.text)
        for sub in resp_data["models"]:
            if sub["status"] == 'Accepted':
                sub_data = {}
                sub_data['name'] = sub['challenge']['slug']
                sub_data['folder'] = ""
                sub_data['code'] = ""
                sub_data['language'] = sub['language']
                thisSubs[sub['id']] = sub_data
    return thisSubs


def getCode(main_session, site, qs):
    print("[*] Getting code")
    for q in qs:
        print(site.format(qs[q]['name'], q))
        rerun = True
        while rerun:
            resp = main_session.get(
                site.format(qs[q]['name'], q)
            )
            resp_data = json.loads(resp.text)
            # kept crashing here as there were some returned without Language data - think they timed out
            # so looped any that error and save procd file to enable restart
            try:
                qs[q]['folder'] = resp_data["model"]["track"]["slug"]
                qs[q]['code'] = resp_data["model"]["code"]
            except:
                print(f"Error getting data: {site.format(qs[q]['name'], q)} {resp_data}")
                print("Sleeping for a 60 seconds!")
                time.sleep(60)
            else:
                rerun = False
    return qs

def buildCodeFiles(subs):
    print("[*] Building code files")
    EXTENSIONS = {
        "cpp": "cpp",
        "python3": "py",
        "python": "py",
        "pypy": "py",
        "pypy3": "py",
        "bash": "sh",
    }
    mainDir = 'Submissions/'
    if not os.path.isdir(mainDir):
        os.mkdir(mainDir)
    for sub in subs:
        count = 1
        subDir = '{}{}/{}'.format(mainDir,subs[sub]['language'],subs[sub]['folder'])
        if not os.path.isdir(subDir):
            os.makedirs(subDir)
        if subs[sub]['language'] in EXTENSIONS.keys():
            fileExt = EXTENSIONS[subs[sub]['language']]
        else:
            fileExt = subs[sub]['language']
        fileName = '{}/{}.v{}.{}'.format(subDir,subs[sub]['name'],count,fileExt)
        while os.path.isfile(fileName):
            count += 1
            fileName = '{}/{}.v{}.{}'.format(subDir, subs[sub]['name'], count, fileExt)
        print(fileName)
        with open(fileName, "w") as f:
            f.write(subs[sub]['code'])
        f.close()



# get login credentials from passed args
UNAME, PASSWORD = getUserArgs()
# set up main variables
login_data = {
    "login": UNAME,
    "password": PASSWORD,
    "remember_me": False,
    "fallback": True,
}
procf = "procd.txt"
mainSite = "https://www.hackerrank.com/"
login = mainSite + "auth/login"

# get processed submission ids
procd = getProcd(procf)
# initiate session & get token from site
session = createSession()
session.headers["X-CSRF-Token"] = getToken(session, login)
if wwwLogin(session, login, login_data):
    modelSite = mainSite + f"rest/hackers/{UNAME}/" + "recent_challenges?limit=100&cursor={cursor}&response_version=v2"
    qModels = getModels(session, modelSite)
    siteHead = mainSite + "rest/contests/master/challenges/{}/submissions/"
    subSite = siteHead + "?offset=0&limit=1000"
    subs = getSubmissions(session, subSite, qModels)
    filtered = {}
    for sub in subs:
        if sub not in procd:
            procd.append(sub)
            procd.sort()
            filtered[sub] = subs[sub]
    codeSite = siteHead + '{}'
    subs = getCode(session, codeSite, filtered)
    buildCodeFiles(subs)
    saveProcd(procd, procf)

print("[*] Completed!!!")