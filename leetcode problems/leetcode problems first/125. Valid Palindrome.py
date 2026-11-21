s = "A man, a plan, a canal: Panama"
String = []

for i in range(len(s)):
    if( s[i].isalnum()):
        g = s[i].lower()
        String.append(g)

print(String)
n = len(String) 
for i in range(n // 2):
    if(String[i] != String[n - 1 - i]):
        print(String[i])
        print(String[n - 1 - i])



