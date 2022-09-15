from wxauto import *
import pandas as pd
print('preparing...')

# 获取当前微信客户端
wx = WeChat()


# 获取会话列表
wx.GetSessionList()


# 输出当前聊天窗口聊天消息
# msgs = wx.GetAllMessage
# for msg in msgs:
#     print('%s : %s'%(msg[0], msg[1]))
## 获取更多聊天记录
# wx.LoadMoreMessage()
# msgs = wx.GetAllMessage
# for msg in msgs:
#     print('%s : %s'%(msg[0], msg[1]))


# 向某人发送消息（以`文件传输助手`为例）
# msg = '你好~'
msg=[]
with open('input_msg.txt', 'r', encoding='utf-8') as infile:
  msg = infile.readlines()
  # print(msg[0])
           
df = pd.read_csv('names.csv',header=0, encoding="gbk")
for i,row in df.iterrows():
    print('-----------------------')
    # print(row[0],':',row[1])
    who = row[0]
    ret = wx.ChatWith(who)  # 打开`文件传输助手`聊天窗口
    if ret:
      print('向' + who +'发送：'+ row[1] + '，' + msg[0])
      if input('回车键确认，任意键取消') == '':
        wx.SendMsg(str(row[1]) + '，' + msg[0])
        print('发送成功')
      else:
        print('取消发送')
    else:
      continue
    # print(row[1])
# for name in configs.names.items():
#   who = name[0]
#   ret = wx.ChatWith(who)  # 打开`文件传输助手`聊天窗口
#   if ret:
#     wx.SendMsg(name[1] + '，' + str(configs.msg))

## 发送换行消息（最近很多人问换行消息如何发送，新增说明一下）
# msg = '''你好
# 这是第二行
# 这是第三行
# 这是第四行'''
# who = '文件传输助手'
# WxUtils.SetClipboard(msg)    # 将内容复制到剪贴板，类似于Ctrl + C
# wx.ChatWith(who)  # 打开`文件传输助手`聊天窗口
# wx.SendClipboard()   # 发送剪贴板的内容，类似于Ctrl + V


# # 向某人发送文件（以`文件传输助手`为例，发送三个不同类型文件）
# file1 = 'D:/test/wxauto.py'
# file2 = 'D:/test/pic.png'
# file3 = 'D:/test/files.rar'
# who = '文件传输助手'
# wx.ChatWith(who)  # 打开`文件传输助手`聊天窗口
# wx.SendFiles(file1, file2, file3)  # 向`文件传输助手`发送上述三个文件
# # 注：为保证发送文件稳定性，首次发送文件可能花费时间较长，后续调用会缩短发送时间


# # 向某人发送程序截图（以`文件传输助手`为例，发送微信截图）
# name = '微信'
# classname = 'WeChatMainWndForPC'
# wx.ChatWith(who)  # 打开`文件传输助手`聊天窗口
# wx.SendScreenshot(name, classname)  # 发送微信窗口的截图给文件传输助手
if input('回车键退出') == '':
  pass