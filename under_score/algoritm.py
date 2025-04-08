text = 'HasLomgysmt'
wovels_used_chars ='aeiou'
count = 2

while count < len(text):
    if text[count] not in (wovels_used_chars):
       text = text[:count + 1] +'_' + text[count + 1:]
       wovels_used_chars += text[count]
       count += 4
       continue
    count += 1
if text.endswith('_'):
    text = text[:-1]
print(text, wovels_used_chars)   
