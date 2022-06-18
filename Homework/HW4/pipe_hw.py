# 由于多进程在Jupyter Notebook中可能无法运行，这里采用魔法方法writefile将此代码块保存为本地py文件

import time
from multiprocessing import Process, Pipe

def pipe_reader(pipe):
    with open('trade.log') as f:
        content = f.read()
    pipe.send(content)
    pipe.close()
    #raise NotImplementedError # TODO: 补全利用pipe发送信息部分

def pipe_writer(pipe):
    f2 = open('trade_with_time.log', 'w')
    f2.write(time.asctime())
    f2.write("\n")
    f2.write(pipe.recv())
    #raise NotImplementedError # TODO: 从pipe的另一端接收信息，在文件开头添加时间，并写入trade_with_time.log
    
if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    pp = Process(target=pipe_reader, args=(parent_conn,))
    pc = Process(target=pipe_writer, args=(child_conn,))
    pp.start()
    pc.start()
    pp.join()
    pc.join()
    #raise NotImplementedError # 创建Pipe，创建并执行两个子进程
