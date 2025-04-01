import os
fi = input('Input file: ')
hehe = f'''fi="{fi}"\nc=exec\ndef h(*args):\n    pass\ndef cc(*args):\n    if str(args[0])[0] != '<':\n        print(args[0])\n        open('deobf-'+fi, 'w', encoding='utf8').write("# Decoded by NguyenXuanTrinh\\n\\n"+args[0])\n        print('Done! Wrote in '+'deobf-'+fi)\n        __import__('os').remove(__file__)\n    else:\n        return c(*args)\ninput=h\nexec=cc\n'''
hic = hehe + open(fi, 'r', encoding='utf8').read()
open('temp.py', 'w', encoding='utf8').write(hic)
os.system('python temp.py')
