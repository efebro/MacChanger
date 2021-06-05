import subprocess
import optparse
import re
def user_input():
    parse_obje = optparse.OptionParser()
    parse_obje.add_option("-i","--interface",dest="inter",help="interface to change!")
    parse_obje.add_option("-m","--mac",dest="macadres",help="new mac address")
    return parse_obje.parse_args()

def mac_run(user_inter,user_macadres):
    subprocess.call(["ifconfig",user_inter,"down"])
    subprocess.call(["ifconfig",user_inter,"hw","ether",user_macadres])
    subprocess.call(["ifconfig",user_inter,"up"])

def control_new_mac(inter):
    ifconfig = subprocess.check_output(["ifconfig",inter])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)
    if new_mac:
        return new_mac.group()
    else:
        return None

print("Mac Changer Started...")
(user_inputs,argument) = user_input()
mac_run(user_inputs.inter,user_inputs.macadres)
final_mac = control_new_mac(user_inputs.inter)
if final_mac == user_inputs.macadres:
    print("\033[92mMac Changer Completed. New mac address :")
    print(user_inputs.macadres)
else:
    print("\033[91mMac Changer Not Completed!!!")
