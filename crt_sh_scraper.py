import requests
import re
import sys



def make_request(target):
    #group by issuer make it faster in case of huge response
    params = {
        'q':target,
        'dir':'^',
        'sort': '1', 
        'group':'icaid'
        }
    req = requests.get('https://crt.sh', params=params)
    return req.text


def get_sub_domains(target):
    html = make_request('%.' + target)
    
    pattern = re.compile(r"<TD>.*\." + target)
    subs = re.findall(pattern, html)
    if subs == []:
        return target + " : Not Found"
    for i in range(len(subs)):
        subs[i] = subs[i][4:]
    subs = list(set(subs))
    return "\n".join(subs)



if len(sys.argv) == 2:
    print(get_sub_domains(sys.argv[1]))
else:
    print("\nUsage: python3 crt_sh_scraper.py <target_domain>")
    print("\nExample: python3 crt_sh_scraper.py microsoft.com")
