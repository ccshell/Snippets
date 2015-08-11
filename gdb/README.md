# savebreakpoint.py
### -----此功能gdb已经内置支持了,如下方式使用：
	(gdb) save breakpoints /tmp/break
参考：

[Writing a new gdb command](http://tromey.com/blog/?p=501)

使用方法

	(gdb) source savebreakpoint.py
	(gdb) save breakpoints /tmp/break
	Saved to file '/tmp/break'.

如果不知道怎么用可以参考：

[Debugging with GDB: How to create GDB Commands in Python](http://www.cinsk.org/wiki/Debugging_with_GDB:_How_to_create_GDB_Commands_in_Python)

如果使用有问题可以将程序适当修改，可以利用python的dir命令查看具体的对象成员变量和属性。

	(gdb) python print dir(gdb.Breakpoint)
	['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'commands', 'condition', 'delete', 'enabled', 'expression', 'hit_count', 'ignore_count', 'is_valid', 'location', 'number', 'silent', 'task', 'thread', 'type', 'visible']
	(gdb)

# pzh.py

在Linux中，将文件保存成pzh.py（文件名自己取），修改gdb的配置文件~/.gdbinit,添加一句

	source 文件路径/pzh.py

启动gdb，使用pzh Name示例如下

	(gdb) pzh GetTxt()
	const String &
	放到洒c发的发
现在只支持gdb输出，cgdb的终端不能输出中文不能打中文字符

可能在某些硬件平台上有问题，使用中的问题请反馈给我。
