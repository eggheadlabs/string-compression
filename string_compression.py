# Compress a string by encoding their consecutive appearances
# Example: AAABBCCDDDAAAAAAAA ==> 3A2B2C3D8A

# s = "AAABBCCDDDAAAAAAAA"          # static example string, or input any string below
s = input('input a sting with letters: ')   # input any string
s = s + " "

l = []
cnt = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        cnt += 1
    else:
        l.append(str(cnt) + s[i-1])
        cnt = 1     # rest the cnt

print(''.join(l)) 