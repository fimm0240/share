from pykiwoom.kiwoom import *


class Account(Kiwoom):
    def __init__(self):
        super().__init__()
        self.CommConnect(block=True)
        pass

    def getmyinfo(self):
        self.account_num = self.GetLoginInfo("ACCOUNT_CNT")
        self.accounts = self.GetLoginInfo("ACCNO")
        self.user_id = self.GetLoginInfo("USER_ID")
        self.user_name = self.GetLoginInfo("USER_NAME")
        self.keyboard = self.GetLoginInfo("KEY_BSECGB")
        self.firewell = self.GetLoginInfo("FIREW_SECGB")
        pass

    def getmarketinfo(self):
        # 1: kospi, 3: ELW, 4: Mutualfund, 5: preemptive right, 6: REITs 9: Heier fund, 10: kosdaq, 30: K-OTC 50: KONEX
        self.kospi = self.GetCodeListByMarket('0')
        self.kosdaq = self.GetCodeListByMarket('10')
        self.etf = self.GetCodeListByMarket('8')
        pass

    def getcodename(self, info: str):
        print(self.GetMasterCodeName(info))
        pass

    def getconnection(self):
        print(self.GetConnectState())
        pass

    def getlistedstockcnt(self, info: str):
        print(f'Volume of stock {self.GetMasterCodeName(info)} is {self.GetMasterListedStockCnt(info)}')
        pass

    def getconstruction(self, info: str):
        print(f'Investment supervision for {self.GetMasterCodeName(info)}: {self.GetMasterConstruction(info)}')
        pass


if __name__ == '__main__':
    acc = Account()
    acc.getmyinfo()
    acc.getmarketinfo()
    acc.getcodename(acc.kospi[50])
    acc.getconnection()
    acc.getlistedstockcnt(acc.kospi[510])
    acc.getconstruction(acc.kospi[500])


