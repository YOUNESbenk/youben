# Hash_DecVitable
# Version 1.0.0
# Coded by YOUNES BENKALAI in python 2.7.13

import os
import sys
import hashlib
import datetime
from optparse import OptionParser


def face():                                                 #Whene the script start
    if  os.name=="nt": os.system('cls')
    else : os.system('clear')
    print(''.rjust(56,'#'))
    print ('#'+''.center(54)+'#')
    print ('# Hash_DecVitable'.ljust(55)+'#')
    print ('# Version 1.0.1'.ljust(55)+'#')
    print ('# Coded by YOUNES BENKALAI in python 2.7.13'.ljust(55)+'#')
    print (''.rjust(56,'#'))
    print(''.rjust(56,'_')+"\n")
    print("* Describe: This Script Decrypt all hash type ".ljust(55)+'*'+ "\n* usage: python decvitable.py -s [HASH] -t [HASH_TYPE] ".ljust(56)+'*')
    print(''.rjust(56, '_'))
    if sys.version_info.major!=2 or sys.version_info.minor!=7:
        print("Requires Python version 2.7")
def loop(characters,size):                                 #Method for create a list of Prospects
    if size==0:
        yield []
    else:
        for x in xrange(len(characters)):
            for y in loop(characters[:x] + characters[x:] , size - 1):
                yield [characters[x]]+y
def hashstring(hashtype,string):                           #this method for compare the hash
    ht=str(hashtype)
    stringhached=hashlib.new(ht)
    stringhached.update(string)
    result=stringhached.hexdigest()
    return result
def bruteforceMethod(hash,hashty):                         #method for do a bruteforce
    stime = datetime.datetime.now()
    cont=0
    characters=list('aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789')
    maxlen=xrange(0,25)
    stringbuilder=''
    result=0
    for length in maxlen:
        for x in loop(characters,length):
            stringtest=stringbuilder+''.join(x)
            cont =cont+1
            if hashstring(hashty,stringtest)==hash:
                time=str(datetime.datetime.now() - stime  ).split('.')[0]
                print(str("THE result is:  <<< "+stringtest+ " >>>-----------!!!CRACKED!!!-------------AFTER: "+time+"\n"))
                raw_input("Press Enter to exit.....")
                sys.exit()
            else:
		result=result+1
		if result==100000:
			print(str(cont)+"__ TESTED NOT YET PLEASE WAIT __")
			result=0

    print ("!!!!!!!!SORRY HASH DONT CRACKED!!!!!!!!")

def main():                                                 #main method

    face()
    parser=OptionParser()
    parser.add_option("-t","--type",dest="type",help="Hash type")
    parser.add_option("-s","--hash",dest="hash",help="Hash")
    (options,args)=parser.parse_args()
    try:
        bruteforceMethod(options.hash,options.type)
    except:
        print("")

if __name__=="__main__":main()
