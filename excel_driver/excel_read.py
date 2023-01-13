
# excel的读写
import openpyxl

from webkey.web_key import web_key


def read_run(path,log):
   excel = openpyxl.load_workbook(path)
   try:
      # 读取所有的sheet页
      for sheet in excel.sheetnames:
         # 读取sheet也中的所有内容
         temp_sheet=excel[sheet]
         log.info('--------{}-------'.format(sheet))
         for value in temp_sheet.values:
            # 读取用例中的内容
            if type(value[0]) is int:
               log.info('正在执行{}'.format(value[5]))
               # 提取测试数据
               data={}
               data['name']=value[2]
               data['value']=value[3]
               data['txt']=value[4]
               data['expect']=value[6]
               # 清除为none的数据
               for key in list(data.keys()):
                  if data[key] is None:
                     del data[key]
               print(value[1])
               # 实例化关键字驱动
               if value[1]=='open_browser':
                  key=web_key(value[4],log)
               elif "assert" in value[1]:
                  status=getattr(key,value[1])(**data)
                  if status:
                     excel_confi.write(temp_sheet.cell,value[0]+2,8)
                  else:
                     excel_confi.write(temp_sheet.cell,value[0]+2,8,status=2)
                  excel.save(path)
               else:
                  # 常规操作
                  getattr(key,value[1])(**data)
   except Exception as e:
      log.exception('运行异常:{}'.format(e))
   finally:
      excel.close()




