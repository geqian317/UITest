"""关键字驱动框架的主入口"""

import logging
import os

from excel_driver import excel_read

if __name__ == '__main__':
    # 生成日志器
    log=logging.getLogger('./config/log.ini')
    # excel数据驱动
    # excel_read.read_run(log)
    # 读取测试用例集
    cases=[]
    # 读取指定路径下的所有文件
    for path,dir,files in os.walk('./test_data/'):
        for file in files:
            # 获取文件后缀名
            #print(file)
            file_type=os.path.splitext(file)[1]
            if file_type==".xlsx" and 'test' in file:
                excel_path=path+file
                cases.append(excel_path)
                #print(excel_path)
            else:
                log.info('文件类型错误:{}'.format(file))
        #print(cases)
    # 调用excel_run进行关键字驱动自动化测试
    for case in cases:
        log.info('运行{}自动化测试用例'.format(case))
        #print(case)
        excel_read.read_run(case,log)



