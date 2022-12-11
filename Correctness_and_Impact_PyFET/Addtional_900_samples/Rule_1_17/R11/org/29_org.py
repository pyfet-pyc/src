class __init__(*args, **kwargs):
    super(Chatroom, self).__init__(*args, **kwargs)
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