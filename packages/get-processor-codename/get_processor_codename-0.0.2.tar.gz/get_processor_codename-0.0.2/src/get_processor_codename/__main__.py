# get-processor-codename
# version 0.0.2
# by SamuelLouf <https://github.com/samuellouf/>

import os, platform, subprocess, re, util

def getProcessorName(replace_symbols=False):
  def removeUnusefulSpaces(string):
    string = string.replace('  ', ' ')

    if string[0] == ' ':
      string = string[1:string.__len__()]
    
    if string[-1] == ' ':
      string = string[0:-1]

    string = string.replace('(C)', '©').replace('(R)', '®').replace('(TM)', '™')
    return string

  if platform.system() == "Windows":
    return removeUnusefulSpaces(platform.processor())
  elif platform.system() == "Darwin":
    os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
    command ="sysctl -n machdep.cpu.brand_string"
    return removeUnusefulSpaces(subprocess.check_output(command).strip())
  elif platform.system() == "Linux":
    command = "cat /proc/cpuinfo"
    all_info = subprocess.check_output(command, shell=True).decode().strip()
    for line in all_info.split("\n"):
      if "model name" in line:
        return removeUnusefulSpaces(re.sub( ".*model name.*:", "", line,1))
  return ""

def getProcessorCodeName(name):
  if 'CPU' in name:
    name = name.split(' CPU')[0]
  name = name[0:-1]
  results = util.intel_ark_lookup(name)
  if results.__len__() != 1 and type(results) == list:
    m = None
    for result in results:
      if result['name'] == name:
        m = result
    if m:
      results = m
  elif results.__len__() != 1:
    results = results[0]
  
  return results
