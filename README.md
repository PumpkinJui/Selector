# Selector

Made with **LOVE**❤ by PumpkinJui

> A simple program which can randomly select one name in a name list.
> 
> 一个简洁的程序，可以从给定的名称列表中抽取一个名称。

## 程序版本

- Internal：为满足我自己使用需求而制作的版本。

- Public：适用于绝大多数人的绝大多数需求的推广版本。

- Version 1.0 Release 仅包含 Internal 版本。

## 使用方法

1. 下载程序。可以在 [本项目的 Releases 页面](https://github.com/PumpkinJui/Selector/releases) 下载打包的 EXE 版本。

2. - 对于 Public 版本：
     
     - 如果您需要给出名称列表，请在程序的目录下新建一个 list.txt 文件，然后将列表写入。每一行写入列表中的一个元素。
       
       - 列表读取后将会在程序内部自动去重。
       
       - 列表中如果存在空行，空行将被计为一个元素。
       
       - 列表中的所有空格将会正常显示。
         即，形如 “a b” 和 “ab     ” 的元素将会按它们现在的样子显示。
       
       - 这是一个拥有四个元素的名称列表示例文件：
         
         > 0
         > 1
         > 2
         > 3
     
     - 如果您没有给出名称列表，程序将自动使用一个包含 0~9 十个整数的列表运行。
   
   - 对于 Internal 版本：
     名称列表已被直接写入程序代码中——您没有选择。

3. 双击打开程序。将会显示本部分的 4 和 5 作为简要使用说明。

4. 鼠标操作方法：
   
   - 单击 “抽取” 按钮以随机抽取一个姓名
   - 单击 “退出” 按钮以退出程序

5. 键盘操作方法：
   
   - 按 “Enter” 键以随机抽取一个姓名
   - 长按 “Enter” 键以进行 **“更具有视觉效果”** 的随机抽取
   - 按 “Esc” 键以退出程序

## 兼容性

### Version 1.0 Release

使用在 64 位的 Windows 7 系统上运行的 [PyInstaller v5.4.1](https://github.com/pyinstaller/pyinstaller/releases/tag/v5.4.1) 打包，并且至少兼容 64 位的 Windows 7 系统及 64 位的 Windows 10 系统。

### Version 1.1 Release

使用在 64 位的 Windows 10 系统上运行的 [PyInstaller v5.5](https://github.com/pyinstaller/pyinstaller/releases/tag/v5.5) 打包，并且至少兼容 64 位的 Windows 10 系统。

## 其他

- 本程序使用 Python 3 语言编写，遵守 MIT License 开源发布。该许可证可以在本项目中找到。

- 使用 [LXGW Bright GB](https://github.com/lxgw/LxgwBright) 字体，至少需要系统内安装有该字体的 Regular 字重才可以正常使用。
  
  - 如果安装了该字体家族但未安装该字重，程序将自动使用该字体家族的另外一个字重替代显示。
    *尚不确定程序如何选择该字重。*
  
  - 如果未安装该字体家族，程序将自动使用系统内的某个字体来替代显示。
    *尚不确定程序如何选择该字体。*

- 如果您发现了任何问题或想要提出任何建议，请在 [本项目的 Issues 页面](https://github.com/PumpkinJui/Selector/issues) 反馈，或 [发邮件到 feedback@pumpkinjui.aleeas.com](mailto:feedback@pumpkinjui.aleeas.com)。
