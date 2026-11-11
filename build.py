# Fabrique index.html (page complète) à partir de app.html
s = open('app.html', encoding='utf-8').read()
head, rest = s.split('</style>', 1)
out = ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       + head + '</style>\n<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)} body{margin:0} [hidden]{display:none!important}</style>\n</head>\n<body>'
       + rest + '</body>\n</html>\n')
open('index.html', 'w', encoding='utf-8').write(out)
