import pexpect as px
child=px.spawn('ssh nabila@192.168.149.128')
child.expect("password:")
child.sendline('83098nabeela')
print(child.before)
print("hello")
child.close()