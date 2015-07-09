
#-*-coding:utf-8--*-

#import gdb.types
import struct
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class PrintZh(gdb.Command):
	"""输出OO中的字符串: pzh NAME

支持中文输出
The terminals need to support Chinese
用例:pzh NAME
NAME 为变量名

支持
rtl_uString, OUString, OString, String, char, util::URL

Author
=====
www.ccshell.com
=====
Version
=====
0.3
"""

	def __init__(self):
		gdb.Command.__init__(self, "pzh", gdb.COMMAND_OBSCURE) 
	
	def getzh( self, aStr, nLen):
		if nLen > 255 :
			nLen = 255

		slist = []
		n = 0
		try:
			while n <= nLen:
				slist[n:n] = unichr(aStr[n])
				n = n +1
		except ValueError as e:
			print "字符串中的元素不是标准的字符"

		ss = ''.join( slist[0:] )
		return ss

	def invoke(self, arg, from_tty):
		try:
			dest = gdb.parse_and_eval( arg )
			srcType = str(dest.type)
			#print srcType

			try:
				if 'rtl_uString' in srcType:
					#display rtl_uString
					print PrintZh.getzh( self, dest[ 'buffer'], dest[ 'length' ] )
				elif 'OUString' in srcType:
					#display rtl::OUString
					print PrintZh.getzh( self, dest[ 'pData' ][ 'buffer' ], dest[ 'pData' ]['length'] )
				elif 'OString' in srcType:
					#display rtl::OString
					print PrintZh.getzh( self, dest[ 'pData' ][ 'buffer' ], dest[ 'pData' ]['length'] )
				elif 'String' in srcType:
					#display (Uni)String
					print PrintZh.getzh( self, dest[ 'mpData' ][ 'maStr' ], dest[ 'mpData' ]['mnLen'] )
				elif 'char' in srcType:
					print dest
				elif 'util::URL' in srcType:
					#display util::URL
					for key in [ "Complete", "Main", "Protocol", "User", "Password", "Server", "Path", "Name" ]:
						buff = dest[ key ][ 'pData' ][ 'buffer' ]
						nlen = dest[ key ][ 'pData' ]['length']
						print("%s =%s" %(key, PrintZh.getzh(self,buff,nlen)) )
					print "Port = %i" % dest[ 'Port' ]
			except RuntimeError as e:
				print "请用有效的参数,使用'help pzh'获得帮助"

		except RuntimeError as e:
			print "参数对应的变量不存在或发生了未知错误，使用'help pzh'获得帮助"
		

PrintZh()

