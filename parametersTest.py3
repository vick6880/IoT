#!/usr/bin/python3
#coding=UTF-8

#	sys模块:在Python中，sys模块是一个非常常用且十分重要的模块，通过模块中的 sys.argv
#				就可以访问到所有的命令行参数，它的返回值是包含所有命令行参数的列表(list),
#				我们看到通过 sys.argv 我们可以获得运行 Python 程序中所有的命令行参数
#	getopt模块:	谈到 Python 的命令行参数，有一个模块是不得不提的，那就是 getopt,我们
#				先来看一下这个函数： getopt.getopt(args, options[, long_options]) 我们先
#				来看一下里面参数的含义： args: 表示的是要被处理的命令行参数列表（通常是通
#				过上述的 sys.argv 获得的结果） options: 它表示的是命令行参数中的选项，通常
#				是一个字母，就像我们在 Linux 中对于某个命令不熟悉时所使用的帮助选项-h一样。
#				如果说该选项需要一个参数的话，需要在该字母后边加上一个冒号:,表示该选项需要
#				一个参数（如果这句不明白可以看下边的示例程序） long_options: 它是一个可选
#				的参数，表示的是选项的长格式，上边的options是短格式，长格式的选项的参数格
#				式示例为--input=input.txt,具体如何使用，详见下边的示例程序。
#	sys.argv 是命令行参数列表。
#	len(sys.argv) 是命令行参数个数。
#	注：sys.argv[0] 表示脚本名。
#	getopt.getopt 方法用于解析命令行参数列表，语法格式如下：
#	getopt.getopt(args, options[, long_options])
#	方法参数说明：
#    args: 要解析的命令行参数列表。
#    options: 以列表的格式定义，options后的冒号(:)表示该选项必须有附加的参数，不带冒号表示该选项不附加参数。
#    long_options: 以字符串的格式定义，long_options后的等号(=)表示如果设置该选项，必须有附加的参数，否则就不附加参数。
#    该方法返回值由两个元素组成: 第一个是 (option, value) 元组的列表。 第二个是参数列表，包含那些没有'-'或'--'的参数。

import sys, getopt

def main(argv) :
	inputfile = ""
	outputfile = ""

	try :
# 这里的h就表示该选项无参数, i:表示i选项后需要有参数
		opts, args = getopt.getopt(argv, "hi:o:",["infile=", "outfile="])
#	except getopt.GetoptError as err:
#		print help information and exit:
#		print str(err) # will print something like "option -a not recognized"
#		usage()
#		sys.exit(2)

	except getopt.GetoptError:
		print ('Error: parametersTest.py3 -i <inputfile> -o <outputfile>')
		print ('or: parametersTest.py3 --infile=<inputfile> --outfile=<outputfile>')
		sys.exit(2)

	for opt, arg in opts :
		if opt == "-h":
			print ('parametersTest.py3 -i <inputfile> -o <outputfile>')
			print ('or: parametersTest.py3 --infile=<inputfile> --outfile=<outputfile>')
			sys.exit()
		elif opt in ("-i", "--infile") :
			inputfile = arg
		elif opt in ("-o", "--outfile") :
			outputfile = arg

	print ('Input file : ', inputfile)
	print ('Output file: ', outputfile)

if __name__ == "__main__" :
	main(sys.argv[1:])