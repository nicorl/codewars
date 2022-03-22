def domain_name(url):
    print(url)
    if (url.find('www') == -1):
        if (url.find('//') == -1):
            inicio = 0
            x = 0
        else:
            inicio = url.find('//')
            x = 2
    else: 
        inicio = url.find('www')
        x = 4
    sincomienzo = url[inicio+x:]
    punto = sincomienzo.find('.')
    print(sincomienzo[:punto])
    return sincomienzo[:punto]

print(domain_name("www.xakep.ru"))
print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("https://youtube.com"))
print(domain_name("http://www.lalala.com"))
print(domain_name("icann.com"))
