states=[]
try:
    read_file=open("..//data/states.txt",'r')
    for l in read_file:
        states.append(l.strip())
    print('\n',states)
except Exception as e:
    print(e)
finally:
    read_file.close()

st=[]
print('\n')
print("Printing unique names , 'not duplicates'")
for s in states:
    if s not in st:
        st.append(s)
print(st)