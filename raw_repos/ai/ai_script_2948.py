def create_userid(firstname, lastname):
    userid = firstname[0] + lastname[:5]
    return userid

userid = create_userid("John", "Smith")
print(userid) # Output: JSmith