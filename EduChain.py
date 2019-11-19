'''每个区块链都包含时间、自己的哈希值、上一区块的哈希值、难度、随机值、交易数据
每个区块的哈希值=计算（一系列的值+上一区块的哈希值）
'''

import time  #获取目前的时间
import hashlib
import json

class Block():

    def __init__(self, msg , previous_hash):
        self.time_stamp = time.asctime(time.localtime(time.time()))#获取这个区块产生的时间
        self.previous_hash = previous_hash#获取上一个区块的哈希值
        self.msg = msg#我们的信息
        self.nonce = 1
        self.hash =self.get_hash()#自己的哈希值

    def get_hash(self):#计算哈希值的功能
        data = self.time_stamp +self.msg +self.previous_hash + str(self.nonce)#将各种信息相加
        hash256 = hashlib.sha256()
        hash256.update(data.encode('gb2312'))#计算这个哈希值
        return hash256.hexdigest()

    def mine(self, diffculty):
        target =''
        for each_num in range(0,diffculty):
            target = target +'0'
        while(int(self.hash[0:diffculty] != target)):
            self.nonce = self.nonce + 1
            self.hash= self.get_hash()
        print('Mined a new block')

class EduChain():

    def __init__(self, diffculty):#初始化区块链
        self.list = [] #创建一个空列表
        self.diffculty =  diffculty
    def add_block(self , block):#添加区块
        block.mine(self.diffculty)
        self.list.append(block)

    def show(self):#打印所有区块
        json_res = json.dumps(self.list, default=self.block_dict)
        print(json_res)
    def block_dict(self , block):
        return block.__dict__

    def isChainValid(self):
        for i in range(1, len(self.list)):
            current_block = self.list[i]
            previous_block = self.list[i-1]
            if(current_block.hash != current_block.get_hash()):
                print('Current Block is not equal')
                return False
            if(current_block.previous_hash != previous_block.hash):
                print('Previous hash is not equal')
                return False
            print('All the blocks are correct')
            return True

c = EduChain(3)
c.add_block(Block('first', '0'))
c.add_block(Block('second', c.list[len(c.list)-1].hash))
c.show()
c.isChainValid()
