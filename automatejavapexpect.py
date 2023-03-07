import pexpect as px
def install_java():
    child=px.spawn('sudo apt-get update')
    child.expect(' .*password.*')
    child.sendline('83098nabeela')
    print(child.before.decode('utf-8'))
    ch=px.spawn('sudo apt install openjdk-18-jre-headless')
    ch.expect('.*password.*')
    ch.sendline('83098nabeela')
    ch.expect('Do you .*')
    ch.sendline('yes')
    print(child.before.decode('utf-8'))
if __name__=='__main__':
    install_java()

