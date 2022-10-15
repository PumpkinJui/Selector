# Selector

Made with **TRUE LOVE**❤ by PumpkinJui

> A simple program which can randomly select one name in a name list.
> 
> 一个简洁的程序，可以从给定的名称列表中抽取一个名称。

## 程序版本

- Internal：为满足我自己使用需求而制作的版本。
- Public：适用于更多人的推广版本。
- Version 1.0 Release 仅包含 Internal 版本。
- Version 1.3 Release 仅包含 Public 版本。

## 使用说明

1. 下载程序。可以在 [本项目的 Releases 页面](https://github.com/PumpkinJui/Selector/releases) 下载打包的 EXE 版本。

2. - 对于 Public 版本：
     
     - 如果您需要给出名称列表，请在程序的目录下新建一个 list.txt 文件，然后将列表写入。每一行写入列表中的一个元素。
       
       - list.txt 文件仅支持 ANSI 编码和 UTF-8 编码。
       
       - list.txt 文件不应为空。
       
       - 列表读取后将会在程序内部自动去重。
       
       - 列表中如果存在空行，空行将被计为一个元素。
       
       - 列表中的所有空格将会正常显示。
         即，形如 “a b” 和 “ab     ” 的元素将会按它们现在的样子显示。
       
       - 这是一个拥有四个元素的名称列表示例文件：
         
         > 0  
         > 1  
         > 2  
         > 3
     
     - 如果您没有给出名称列表，程序将自动使用一个包含 0~9 十个整数的备用列表运行。
     
     - 如果您给出的 list.txt 文件为空，或使用的不是 ANSI 编码或 UTF-8 编码，程序将会弹出一个消息框，然后自动使用上述备用列表运行。
   
   - 对于 Internal 版本：
     名称列表已被直接写入程序代码中 —— 您没有选择。

3. 双击打开程序。将会显示本部分 4 中的 “手动模式” 部分作为简要使用说明。

4. 您可以选择使用 “手动模式” 或 “自动模式”。
   
   - 如果您选择使用 “手动模式”(默认项)：
     
     - 鼠标操作方法：
       
       - 单击 “抽取” 按钮以随机抽取一个姓名
       - 长按 “抽取” 按钮以进行 **“更具有视觉效果”** 的随机抽取
       - 单击 “退出” 按钮以退出程序
     
     - 键盘操作方法：
       
       - 按 “Enter” 键以随机抽取一个姓名
       - 长按 “Enter” 键以进行 **“更具有视觉效果”** 的随机抽取
       - 按 “Esc” 键以退出程序
   
   - 如果您选择使用 “自动模式”：
     
     - 操作方法同 “手动模式” 部分。
     - 每次点击，程序会随机抽取 5 次 (0.5s) 至 50 次 (5s)，然后才显示最终结果。
     - 您可以在窗口标题处查看抽取过程。
     - 在随机抽取过程中，**务必不要再次进行随机抽取，包括进行 “更具有视觉效果” 的随机抽取**。
       开发者测试结果，这可能只是相当于抽取结束后立即点击抽取，也可能只是令抽取耗时加长。但开发者不保证也无法保证不会出现其他后果，如程序崩溃等。
       因此，在 “自动模式” 下连续进行随机抽取所引发的 bug，**一律不予修复**。

## 兼容性

### Version 1.0 Release

- 使用在 64 位的 Windows 7 系统上运行的 [PyInstaller v5.4.1](https://github.com/pyinstaller/pyinstaller/releases/tag/v5.4.1) 打包。

- 仅兼容 Windows 系统，且不兼容 32 位系统。

- 开发者测试结果，兼容 64 位的 Windows 7 系统、64 位的 Windows 10 系统和 64 位的 Windows 11 系统。

### Version 1.1 Release ~ Version 1.3 Release

- 使用在 64 位的 Windows 10 系统上运行的 [PyInstaller v5.5](https://github.com/pyinstaller/pyinstaller/releases/tag/v5.5) 打包。

- 仅兼容 Windows 系统，且不兼容 32 位系统。

- 开发者测试结果，兼容 64 位的 Windows 10 系统和 64 位的 Windows 11 系统。

## 其他

- 本程序使用 Python 3 语言编写，遵守 MIT License 开源发布。该许可证可以在本项目中找到。

- 本程序使用 [LXGW Bright GB](https://github.com/lxgw/LxgwBright) 字体，至少需要系统内安装有该字体的 Regular 字重才可以正常显示。
  
  - 如果安装了该字体家族但未安装该字重，程序将自动使用该字体家族的另外一个字重替代显示。  
    
    *尚不确定程序如何选择该字重。*
  
  - 如果未安装该字体家族，程序将自动使用系统内的某个字体来替代显示。  
    
    *尚不确定程序如何选择该字体。*

- 其实两种 **“更具有视觉效果”** 的随机抽取，键盘的应该更具有视觉效果。因为鼠标的限制了等待时间为 1000ms，执行间隔时间为 50ms。而键盘的没有限制 (至少我没写限制代码)，应该是完全取决于硬件性能的。

- 如果您想要询问任何问题、提出任何建议或汇报任何漏洞，请在 [本项目的 Issues 页面](https://github.com/PumpkinJui/Selector/issues) 反馈，或 [发邮件到 feedback@pumpkinjui.aleeas.com](mailto:feedback@pumpkinjui.aleeas.com)。
