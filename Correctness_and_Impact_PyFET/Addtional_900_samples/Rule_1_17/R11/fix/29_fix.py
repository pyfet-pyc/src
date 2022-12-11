class __init__(FET_one_star_arg, FET_two_star_arg):
    super(Chatroom, self).__init__(FET_one_star_arg, FET_two_star_arg)
    memberList = ContactList()
    userName = self.get('UserName', '')
    refSelf = ref(self)
    def init_fn(parentList, d):
        d.chatroom = refSelf() or \
            parentList.core.search_chatrooms(userName=userName)
    memberList.set_default_value(init_fn, ChatroomMember)
    if 'MemberList' in self:
        for member in self.memberList:
            memberList.append(member)
    self['MemberList'] = memberList