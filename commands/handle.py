import commands.cmds as cmds

def handle(self, chat_raw):
    self.logger.info("Handling command: " + chat_raw + " (for player" + self.fquid + ")")
    _atmp1 = chat_raw.split(" ")
    _atmp2 = list(_atmp1[0])
    del _atmp2[0]
    del _atmp1[0]
    cmdobj = {
        "base": _atmp2,
        "args_raw": _atmp1,
        "scope": self,
        "chat_raw": chat_raw
    }
    cmds.InvalidCommand.begin(self, cmdobj) if _atmp2 not in cmds.baseList else cmds.baseList[_atmp2].begin(self, cmdobj)