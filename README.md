# Selector

[![GitHub License](https://img.shields.io/github/license/PumpkinJui/Selector)](https://github.com/PumpkinJui/Selector/blob/main/LICENSE)
[![GitHub Releases](https://img.shields.io/github/v/release/PumpkinJui/Selector?display_name=release&sort=date)](https://github.com/PumpkinJui/Selector/releases/latest)

Made with **TRUE LOVE**❤ by PumpkinJui

> A simple program which can randomly select one name in a name list.
> 
> 一个简洁的程序，可以从给定的名称列表中抽取一个名称。
> 
> 当前版本：Version 1.4.1 Release 230215

## 程序版本

### Releases

- Internal：为满足我自己使用需求而制作的版本。
- Public：适用于更多人的推广版本，自 Version 1.1 Release 起加入。

### Testers

- Version 1.2 SL1.2-EXPModule：用于测试 fileread 中 if-else 结构效果与 try-except 结构效果的模块。

- Version 1.3.1 Public Tester：用于测试 fileread 结果的带命令行版本，由 1.3 Public 衍生。

### ???

- 由 Internal 衍生的恶搞版本。

- ~~*为了防止我同学把这些拿到班级里用，*~~ 仅在仓库中存放 .py 格式的文件。

### Releases 页面中的文件

- Version 1.4 Release 前的程序仅有 .exe 格式的版本。
- 自 Version 1.4 Release 起，引入了 .zip 格式版本的程序，用于包含所有需要的文件并减少启动耗时。字体文件也包含在该版本的程序中，位于 fonts 目录下，但仍需要手动安装。在解压缩后启动其中的 .exe 程序以运行本版本的程序。

## 使用说明

1. 下载程序。可以在 [本项目的 Releases 页面](https://github.com/PumpkinJui/Selector/releases) 下载已打包的程序。

2. - 对于 Public 及其衍生版本：
     
     - 如果您需要给出名称列表，请查看 [名称列表格式规范](#%E5%90%8D%E7%A7%B0%E5%88%97%E8%A1%A8%E6%A0%BC%E5%BC%8F%E8%A7%84%E8%8C%83)。
     
     - 如果您没有给出名称列表，程序将自动使用一个包含 0~9 十个整数的备用列表运行。
     
     - 如果您给出的 list.txt 文件为空，或使用的不是 ANSI 编码或 UTF-8 编码，程序将会弹出一个消息框，然后自动使用上述备用列表运行。
   
   - 对于 Internal 及其衍生版本：
     名称列表已被直接写入程序代码中 —— 您没有选择。

3. 双击打开程序。将会显示本部分 4 中的 “手动模式” 部分作为简要使用说明。

4. 您可以选择使用 “手动模式” 或 “自动模式”。

### 名称列表格式规范

> 仅适用于 Public 及其衍生版本。

- 请在程序的目录下新建一个 list.txt 文件，然后将列表写入。每一行写入列表中的一个元素。

- list.txt 文件仅支持 ANSI 编码和 UTF-8 编码。

- list.txt 文件不应为空。

- 以 “%%%” 开头的一行将被视为注释，不被计为一个元素。*行内注释尚未添加。*

- 列表读取后将会在程序内部自动去重。

- 列表中的空行将被自动忽略。

- 列表中的所有空格将会正常显示。
  即，形如 “a b” 和 “ab     ” 的元素将会按它们现在的样子显示。

- 这是一个拥有四个元素的名称列表示例文件：

> 0  
> 1  
> 2  
> 3

### 模式使用说明

- 如果您选择使用 “手动模式”(默认值)：
  
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
  - 每次点击，程序会随机抽取 5 次 (1.5s) 至 25 次 (7.5s)，然后才显示最终结果。
  - 您可以在窗口标题处查看抽取过程。
  - 在随机抽取过程中，**请不要再次进行随机抽取，包括进行 “更具有视觉效果” 的随机抽取**。
    开发者测试结果，这可能只是相当于抽取结束后立即点击抽取，也可能只是令抽取耗时加长。但开发者不保证也无法保证不会出现其他后果，如程序崩溃等。
    因此，在 “自动模式” 下连续进行随机抽取所引发的 bug，**一律不予修复**。

### 音效

> 仅适用于自动模式。手动模式下，音效开关将不可用且不会发出音效。

- 使用了 [Minecraft Wiki](#%E4%BD%BF%E7%94%A8%E7%9A%84%E8%BE%85%E5%8A%A9%E5%B7%A5%E5%85%B7) 上的 “[获得经验](https://static.wikia.nocookie.net/minecraft_zh_gamepedia/images/2/2e/Succesfull_Hit.ogg)” 和 “[玩家：升级](https://static.wikia.nocookie.net/minecraft_zh_gamepedia/images/b/b0/Random_levelup.ogg)” 音效，分别作为中间音效和最终音效。
  - 如果程序未加载最终音效，将会使用播放间隔 0.1s 的三次中间音效代替。
- 如果程序未加载任何音效，音效开关将不可用且自动处于 “音效关” 状态。
- 如果程序加载了部分或全部音效，音效开关将自动处于 “音效开” 状态，在自动模式下可用。每抽取一次将会播放一次中间音效，最后一次抽取完毕时将会播放最终音效。

## FAQ

参看 [FAQ](https://github.com/PumpkinJui/Selector/blob/main/FAQ.md)。

## 使用的辅助工具

就这么叫吧……我也不知道下面这些该怎么称呼合适了。  
如果有人有更好的称呼，请 [进行反馈](#%E5%8F%8D%E9%A6%88)。

- README：[MarkText](https://github.com/marktext/marktext)、[Shields.io](https://shields.io)

- 字体：[LXGW Bright GB](https://github.com/lxgw/LxgwBright)

- 音效：[pygame](https://www.pygame.org)、[Minecraft Wiki](https://minecraft.fandom.com/zh/wiki/%E7%BB%8F%E9%AA%8C#%E9%9F%B3%E6%95%88)

- 打包：[PyInstaller](https://pyinstaller.org)

- [fileread 逻辑图]((https://github.com/PumpkinJui/Selector/tree/main/Tools%26EXPs/fileread))：[Mermaid](https://mermaid-js.github.io)

## 其他

- 本程序使用 Python 3 语言编写，遵守 MIT License 开源发布。该许可证可以在本项目中找到。

- 本程序**不含病毒，没有任何恶意代码**，但 360 可能会进行误报 (类似 HEUR/QVM202.0.424F.Malware.Gen)。如果您电脑上安装了 360，请确保本程序已被加入白名单。

- 用于正常使用的，一般没有必要下载仓库中 Testers 和 ??? 两文件夹中存放的文件。请下载 Releases 文件夹中的文件。

- 其实两种 **“更具有视觉效果”** 的随机抽取，键盘的应该更具有视觉效果。因为鼠标的限制了等待时间为 1000ms，执行间隔时间为 50ms。而键盘的没有限制 (至少我没写限制代码)，应该是完全取决于性能的。

## 反馈

- 如果您想要询问任何问题、提出任何建议或汇报任何漏洞，请在 [本项目的 Issues 页面](https://github.com/PumpkinJui/Selector/issues) 反馈，或 [发邮件到 feedback@pumpkinjui.aleeas.com](mailto:feedback@pumpkinjui.aleeas.com)。
