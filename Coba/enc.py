#!/usr/bin/python2
import sys, random
import zlib, marshal
from py_compile import compile as _compile
string_ascii = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
note ='"""\n===================================\n   Obfuscate by Mr.Gaming\n    Jangan diedit nanti error\n===================================\n"""'


def encrypt(code):
    a = ''.join(chr(x) for x in [int(ord(i)+11) for i in code])
    b = ''
    F = []
    for x in range(20):
        c = ''.join(random.choice(string_ascii) for x in range(11))
        d = random.randint(0, 1000)
        e = random.randint(0, 100)
        f = random.choice(list('^*'))
        b += str(c+'='+str(d)+f+str(d-e)+'\n')
        F.append(c)
    encripted = repr(zlib.compress('import marshal\nhentai,ecchi=None,None\nexec (lambda:(lambda:(lambda:compile({}.decode("zlib").decode("base64"),"Khairul Syabana","exec"))())())()'.format(repr((b+'\nnolep,sadboy=0,0\npiton=None\ndoujin=[]\ncode=(lambda:(lambda:(lambda:'+repr(a)+')())())()').encode('base64').encode('zlib'))).encode('hex').encode('cp1026')))
    lol = 'oppai=int(({})*0)+int(eval("\x54\x72\x75\x65"))*11\nnenen=(lambda:(lambda:(lambda:compile("".join(chr(int(i-eval("\x6f\x70\x70\x61\x69"))) for i in (lambda:(lambda:(lambda:[ord(x) for x in eval("\x63\x6f\x64\x65")])())())()),"xSODx","exec"))())())()\ndoujin.append("sagiri")\nexec nenen\ndel F,code,marshal,oppai,doujin,ecchi,hentai,nenen,piton,nolep,sadboy'.format('+'.join(F))[::-1].encode('rot13').encode('cp500')
    return note+'''
Nolep = True
if Nolep == False:
    exec str(chr(35){lol})
oppai=(lambda:(lambda:(lambda:({0}))())().decode("zlib").decode("cp1026"))()
if oppai:
    ecchi=(lambda:(False))()
    hentai=(lambda:(False))()
    exec eval("\x6f\x70\x70\x61\x69").decode("hex")
else:
    ecchi=(lambda:(True))()
    hentai=(lambda:(True))()
    exec str(sayagans)
if hentai and ecchi==False:
    piton=False
    nenen=None
    regex = (lambda x:re.findall(r"amaterasu\((.+)\)",x))(hantu)
    eval(compile(("".join(chr(x) for x in {2})+regex.decode("hex")).decode("cp500"),"?","exec"))
else:
    piton=True
    nenen=(lambda:(lambda:(lambda:{1})())())()
    eval(marshal.loads(eval("\x6e\x65\x6e\x65\x6e")))'''.format(encripted, repr(marshal.dumps(compile('if piton==True:\n\toppai=nenen\n\tnenen=oppai\n\tF=repr(marshal.dumps(oppai+nenen))\n\texec '+repr(lol)+'.decode("cp500").decode("rot13")[::-1]', 'xSODx', 'exec'))), str([random.randrange(0, 256) for x in range(50)]), lol='+str(0)'*10000)

def main(file):
    try:
        sc = open(file).read()
    except IOError:
        sys.exit('file not found !!')
    outf = ''+file.replace('/', '@')
    f = open(outf, 'wb')
    f.write(encrypt(sc))
    f.seek(len(sc))
    f.close()
    _compile(outf, outf)
    with open('__main__.pyc', 'w') as f:
        f.write(open(outf).read());f.close()
    import os
    os.system('zip xsodx.zip {0}'.format('__main__.pyc'))
    result = open('xsodx.zip').read()
    with open(outf, 'w') as f:
        f.write('{0}c^\xea\xeb\xec{1}'.format(__import__('imp').get_magic()+'\0'*4, result));f.close()
    os.remove('xsodx.zip')
    os.remove('__main__.pyc')
    print 'file saved '+outf

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        sys.exit('Usage: '+__file__+' <filename>')