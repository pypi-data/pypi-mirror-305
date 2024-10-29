import os
import subprocess
from argparse import ArgumentParser


def cbpf_up(args):
  user = os.environ.get('CBPF_USER')
  password = os.environ.get('CBPF_PASS')
  local = args.local[0]
  remote = args.remote[0]
  cmd = f"sshpass -p {password} rsync -r -v --progress -e 'ssh -p 13900' '{local}' {user}@tiomno.cbpf.br:'{remote}'"
  subprocess.call(cmd, shell=True)
  

def cbpf_down(args):
  user = os.environ.get('CBPF_USER')
  password = os.environ.get('CBPF_PASS')
  local = args.local[0]
  remote = args.remote[0]
  cmd = f"sshpass -p {password} rsync -r -v --progress -e 'ssh -p 13900' {user}@tiomno.cbpf.br:'{remote}' '{local}'"
  subprocess.call(cmd, shell=True)
  

def cbpf_ssh(args):
  user = os.environ.get('CBPF_USER')
  password = os.environ.get('CBPF_PASS') 
  cmd = f"sshpass -p {password} ssh -p 13900 {user}@tiomno.cbpf.br"
  subprocess.call(cmd, shell=True)


def cbpf():
  parser = ArgumentParser(
    prog='cbpf', 
    description='CBPF cluster access'
  )
  
  subparser = parser.add_subparsers(dest='subprog')
  
  down = subparser.add_parser('down')
  down.add_argument('remote', nargs=1)
  down.add_argument('local', nargs='+')
  
  up = subparser.add_parser('up')
  up.add_argument('local', nargs=1) 
  up.add_argument('remote', nargs='+')
  
  subparser.add_parser('ssh')
  
  args = parser.parse_args()
  
  cmds = {
    'down': cbpf_down,
    'up': cbpf_up,
    'ssh': cbpf_ssh
  }
  
  cmds.get(args.subprog)(args)
  
  
  
  


def teiu_up(args):
  user = os.environ.get('TEIU_USER')
  password = os.environ.get('TEIU_PASS')
  local = args.local[0]
  remote = args.remote[0]
  cmd = f"sshpass -p '{password}' rsync -r -v --progress -e ssh '{local}' {user}@teiu.iag.usp.br:'{remote}'"
  subprocess.call(cmd, shell=True)


def teiu_down(args):
  user = os.environ.get('TEIU_USER')
  password = os.environ.get('TEIU_PASS')
  local = args.local[0]
  remote = args.remote[0]
  cmd = f"sshpass -p '{password}' rsync -r -v --progress -e ssh {user}@teiu.iag.usp.br:'{remote}' '{local}'"
  subprocess.call(cmd, shell=True)
  
  
def teiu_ssh(args):
  user = os.environ.get('TEIU_USER')
  password = os.environ.get('TEIU_PASS') 
  cmd = f"sshpass -p '{password}' ssh {user}@teiu.iag.usp.br"
  subprocess.call(cmd, shell=True)


def teiu():
  parser = ArgumentParser(
    prog='cbpf', 
    description='Teiu cluster access'
  )
  
  subparser = parser.add_subparsers(dest='subprog')
  
  down = subparser.add_parser('down')
  down.add_argument('remote', nargs=1)
  down.add_argument('local', nargs='+')
  
  up = subparser.add_parser('up')
  up.add_argument('local', nargs=1) 
  up.add_argument('remote', nargs='+')
  
  subparser.add_parser('ssh')
  
  args = parser.parse_args()
  
  cmds = {
    'down': teiu_down,
    'up': teiu_up,
    'ssh': teiu_ssh
  }
  
  cmds.get(args.subprog)(args)




def iguana_up(args):
  user = os.environ.get('IGUANA_USER')
  password = os.environ.get('IGUANA_PASS')
  local = args.local[0]
  remote = args.remote[0]
  cmd = f"sshpass -p '{password}' rsync -r -v --progress -e ssh '{local}' {user}@iguana.iag.usp.br:'{remote}'"
  subprocess.call(cmd, shell=True)


def iguana_down(args):
  user = os.environ.get('IGUANA_USER')
  password = os.environ.get('IGUANA_PASS')
  local = args.local[0]
  remote = args.remote[0]
  cmd = f"sshpass -p '{password}' rsync -r -v --progress -e ssh {user}@iguana.iag.usp.br:'{remote}' '{local}'"
  subprocess.call(cmd, shell=True)
  
  
def iguana_ssh(args):
  user = os.environ.get('IGUANA_USER')
  password = os.environ.get('IGUANA_PASS') 
  cmd = f"sshpass -p '{password}' ssh {user}@iguana.iag.usp.br"
  subprocess.call(cmd, shell=True)



def iguana():
  parser = ArgumentParser(
    prog='cbpf', 
    description='Iguana cluster access'
  )
  
  subparser = parser.add_subparsers(dest='subprog')
  
  down = subparser.add_parser('down')
  down.add_argument('remote', nargs=1)
  down.add_argument('local', nargs='+')
  
  up = subparser.add_parser('up')
  up.add_argument('local', nargs=1) 
  up.add_argument('remote', nargs='+')
  
  subparser.add_parser('ssh')
  
  args = parser.parse_args()
  
  cmds = {
    'down': iguana_down,
    'up': iguana_up,
    'ssh': iguana_ssh
  }
  
  cmds.get(args.subprog)(args)
  
  
if __name__ == "__main__":
  cbpf()