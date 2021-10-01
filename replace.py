def replace_ch(str):
    ch=str[0]

    str=str.replace(ch,'$')
    str=ch+str[1:]

    return str
print(replace_ch('aishani'))

print(replace_ch('restart'))