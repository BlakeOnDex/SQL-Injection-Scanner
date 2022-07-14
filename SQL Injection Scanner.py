# SQL Injection
import requests, argparse, sys
from colorama import *

Parser = argparse.ArgumentParser()
Parser.add_arguments("-u", "--url", help="url", Required=True)
Parser.add_arguments("-p", "--payloads", help="payloads list", Required=True)
args = Parser.parse_args()

def fuzz(url, payloads):
    for payload in open(payloads, "r").readlines():
        new_url =url.replace('{fuzz}', payload)
        request = requests.get(new_url)
        if request.elapsed.total_seconds > 7:
            print(Style.BRIGHT + Fore.RED + "Timeout detected with", new_url)
        else:
            print(Style.BRIGHT + Fore.CYAN + "Not work with this payload :", payload)
def verif(url):
    url_test = url.replace("{fuzz}", "")
    req = requests.get(url.test)
    if req.elapsed.total_seconds > 6:
        sys.exit(Style.BRIGHT + Fore.RED + "Please make sure you have a good connection to run the scanner")
    else:
        fuzz(args.url, args.payloads)
if not '{fuzz}' in args.url:
    sys.exit(Style.BRIGHT + Fore.RED + "Missing {fuzz} parameter !")
else:
     verif(args.url)





            
