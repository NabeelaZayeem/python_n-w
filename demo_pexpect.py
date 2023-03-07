import pexpect as px
child=px.spawn("echo hcl")
result=child.expect(["welcome","to","hcl","hello"])
print(result)