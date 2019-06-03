#-*-coding:utf-8-*-
from xml.etree import ElementTree as et
import yaml
import json
import sys,requests,json,time,random
reload(sys)
sys.setdefaultencoding("utf8")

def addCase(projectId,name):
  data = {"id":projectId,"name":name}
  headers = {'Content-Type': 'application/json'}
  url = 'http://127.0.0.1:5000/api/IAT/addCase'
  res = requests.post(url, headers=headers, data=json.dumps(data))
  response = res.json()
  if response["code"] == 0:
    return response["content"]["id"]
  return None

def addSample(caseId,info):
  data = {
    "id": caseId,
    "info": info
  }
  headers = {'Content-Type': 'application/json'}
  url = 'http://127.0.0.1:5000/api/IAT/updateSample'
  res = requests.post(url, headers=headers, data=json.dumps(data))
  try:
    response = res.json()
    print(response["msg"])
  except Exception as e:
    print(e)
    print("数据异常：",data)

def runbuild(userId,projectId,fileName):
  with open(fileName, encoding='UTF-8') as config_file:
    configs = yaml.safe_load(config_file)

  for path, info in configs['paths'].items():
    method = (list(info.keys())[0])
    rest_api = {}
    testname = '未知服务'
    for k, v in list(info.values())[0].items():
      if k == 'operationId':
        testname=v
      if k == 'parameters':
        for i in v:
          rest_api.update({i.get('name').replace('\'', '"'):''})

    info = {
      "asserts": {
        "assertData": [{
          "id": int(round(time.time() * 1000)),
          "value": "\"code\":0"
        }],
        "assertsType": 1
      },
      "extract": {
        "extractData": [],
        "extractType": 0
      },
      "method": method,
      "name": testname,
      "params": rest_api,
      "paramType": 'json',
      "path": path,
      "user_id": userId,
      "preShellType": 0,
      "preShellData": "",
      "postShellType": 0,
      "postShellData": "",
    }
    caseId = addCase(projectId, testname)
    if caseId:
      addSample(caseId, info)

    # print testname
    # print method
    # print paramType
    # print path
    # print params
    # print "==============="

if "__main__" == __name__:
  # fileName = 'testData.jmx'
  # projectId = 66
  # userId = 44
  userId = sys.argv[1]
  projectId = sys.argv[2]
  fileName = sys.argv[3]
  runbuild(userId,projectId,fileName)
