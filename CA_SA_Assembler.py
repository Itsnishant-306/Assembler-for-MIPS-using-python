import re
import pandas as pd
#with open('/content/drive/MyDrive/Colab Notebooks/assembler-2.txt',"r") as r:
  #data=r.read()
data='''meen: .word 91
nishant: .word 85
typr: nor $s0, $s1,$s1
addi $s0, $s1,0x154
bltz $s1,typr
bne $s1,$s1,typr
pol: j typr
syscall
lui $t1,0x1001
ppo: jal ppo
'''
register={
    '$zero':0,
    '$at':1,
    '$v0':2,
    '$v1':3,
    '$a0':4,
    '$a1':5,
    '$a2':6,
    '$a3':7,
    '$t0':8,
    '$t1':9,
    '$t2':10,
    '$t3':11,
    '$t4':12,
    '$t5':13,
    '$t6':14,
    '$t7':15,
    '$s0':16,
    '$s1':17,
    '$s2':18,
    '$s3':19,
    '$s4':20,
    '$s5':21,
    '$s6':22,
    '$s7':23,
    '$t8':24,
    '$t9':25,
    '$k0':26,
    '$k1':27,
    '$gp':28,
    '$sp':29,
    '$fp':30,
    '$ra':31
}
inst={'add':0, 'sub':0,'addi':8,'and':0,'or':0,'xor':0,'nor':0,'andi':12,'ori':13,'xori':14,'lui':0b001111}
function={'add':32,'sub':34,'and':36,'or':37,'xor':38,'nor':39}
l=re.split('\n', data)
for i in range (0,len(l)):#to remove unnecessary empty lines
  try:
    l.remove ("")
  except(ValueError):
    break
def itype():
  global line
  global hexaa
  for keys in inst:#take here for function RIJ format
    if(line[0]==keys):
      opcode=(inst[keys])<<26
      break
  else:
    raise Exception("error in inst")
  for keys in register:
    if(line[1]==keys):
      rs=(register[keys])<<16
      break
  else:
    raise Exception ("error in keyword")
  for keys in register:
    if(line[2]==keys):
      rt=(register[keys])<<21
      break
  else:
    raise Exception("error in keyword")
  if(int(line[3],16)<65536 or int(line[3])<65536):
    if(line[3][0:2]=="0x"):
      hexaa=((opcode+rs+rt+int(line[3],16)))
    else:
      hexaa=((opcode+rs+rt+int(line[3])))
  else:
    raise Exception("error number is greater than 65536")
def branchtype():#to edit branch offset
  global line
  global hexaa
  global i
  global symbolfinal
  for j in range(0,len(symbolfinal)):
    if(line[3]==symbolfinal[j][1][0]):
      jta=int(symbolfinal[j][0][0][2:],16)#convert to hex instead of int
      jta=bin(jta)
      jta=jta[6:(len(jta)-1)]
      jta =int(int(jta,2)/4)
      print(jta)
      if jta>0:
        jta=jta+1
      else:
        jta=jta+0x00010000
      offset=int(jta-(i))
      print(offset)
      break
  else:
    raise Exception("symbol not found")
  for keys in register:#take here for function RIJ format
    if(line[1]==keys):
      opcode1=(register[keys])<<21
      break
  else:
    raise Exception ("error in keyword")
  for keys in register:#take here for function RIJ format
    if(line[2]==keys):
      opcode2=(register[keys])<<16
      break
  else:
    raise Exception ("error in keyword")
  if line[0]=='bltz':
    hexaa=(offset) + opcode1+opcode2+0x04000000#0032xxxx
  if line[0]=='beq':
    hexaa=(offset) + opcode1+opcode2+0x10000000#0032xxxx
  if line[0]=='bne':
    hexaa=(offset) + opcode1+opcode2+0x14000000#0032xxxx

def rtype():
  global line
  global hexaa
  for keys in inst:#take here for function RIJ format
    if(line[0]==keys):
      opcode=(inst[keys])<<26
      break
  else:
    raise Exception("error in inst")
  for keys in register:
    if(line[1]==keys):
      rd=(register[keys])<<11
      break
  else:
    raise Exception ("error in keyword")
  for keys in register:
    if(line[2]==keys):
      rs=(register[keys])<<21
      break
  else:
    raise Exception("error in keyword")
  for keys in register:
    if(line[3]==keys):
      rt=(register[keys])<<16
      break
  else:
    raise Exception("error in keyword")
  for keys in function:
    if(line[0]==keys):
      fun=(function[keys])
      break
  hexaa=((opcode+rd+rs+rt+fun))
def jtype():
  global line
  global hexaa
  #global symbolfinal
  if(line[0]=='j'):
    op=((2))<<26
  if(line[0]=='jal'):
    op=((0b000011))<<26
    for i in range(0,len(symbolfinal)):
      if(line[1]==symbolfinal[i][1][0]):
        jta=int(symbolfinal[i][0][0][2:],16)#convert to hex instead of int
        jta=bin(jta)
        jta=jta[6:(len(jta)-2)]
        jta =int(jta, 2)
        break
    else:
      raise Exception("symbol not found")
    hexaa=(op+jta)
sline=[]
symbol=[]
symbolfinal=[]
remember=[]
datauser=[]
du=0
sf=0
for i in range(0,len(l)):#for symbol and .word
  a=str(l[i])
  line=re.split(', |_|-|,| ', a)
  sline.append(line)
  if(sline[i][0][len(sline[i][0])-1])==':':
    symbol=(sline[i][0][:(len(sline[i][0][:len(sline[i][0])-1]))])
    sline[i]=sline[i][1:]
    if sline[i][0]=='.word':
      temp=[hex(0x10000000+(4*du))],[hex(int(sline[i][1]))],[(symbol)]
      datauser.append(temp)
      remember.append(i)
      du=du+1
    else:
      temp=[hex(0x80000000+(4*(i-du)))],[(symbol)]
      sf=sf+1
      symbolfinal.append(temp)
print("symbol table")
print(pd.DataFrame(symbolfinal))
print("data table")
print(pd.DataFrame(datauser))
i=0
f = open("demofile2.txt", "w")
for i in range(du,len(l)):#for instruction
  hexaa=0
  if sline[i][0]=='addi' or sline[i][0]=='andi' or sline[i][0]=='ori' or sline[i][0]=='xori':
    line=sline[i]
    itype()
  elif sline[i][0]=='add' or sline[i][0]=='sub' or sline[i][0]=='nor' or sline[i][0]=='and' or sline[i][0]=='or' or sline[i][0]=='xor':
    line=sline[i]
    rtype()
  elif sline[i][0]=='j' or sline[i][0]=='jal':
    line=sline[i]
    jtype()
  elif sline[i][0]=='bne' or sline[i][0]=='beq' or sline[i][0]=='bltz':
    line=sline[i]
    if line[0]=='bltz':
      line=sline[i]
      line = line[:2] + ['$zero'] + line[2:]
    branchtype()
  elif sline[i][0]=='lui':
    line=sline[i]
    line = line[:2] + ['$zero'] + line[2:]
    itype()
  elif sline[i][0]=='jr' and sline[i][1]=='$ra':
    hexaa=65011720
  elif sline[i][0]=='syscall':
    hexaa=0x0000000c
  else:
    raise Exception("instruction not correct")
  f = open("demofile2.txt", "a")#from here to end file write
  f.seek(2)
  f.write('{:08X}:{:08X}\n'.format(0x80000000+(4*i)-(du*4),hexaa))
  f.close()
  print('{:08X}:{:08X}'.format(0x80000000+(4*i)-(du*4),hexaa))