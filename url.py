import pyshorteners as sh

link = 'https://www.youtube.com/channel/UCKZZPrWs00tqy4pTYCaAPkg'

s = sh.Shortener()
x = (s.tinyurl.short(link))

print(x)
