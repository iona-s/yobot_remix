class ClanBattleError(ValueError): ...


class UserError(ClanBattleError): ...


class GroupError(ClanBattleError): ...


class InputError(ClanBattleError): ...


class UserNotInGroup(UserError):
    def __init__(self, msg='未加入公会，请先发送“加入公会”', *args):
        super().__init__(msg, *args)


class GroupNotExist(GroupError):
    def __init__(self, msg='本群未初始化，请发送“创建X服公会”', *args):
        super().__init__(msg, *args)
