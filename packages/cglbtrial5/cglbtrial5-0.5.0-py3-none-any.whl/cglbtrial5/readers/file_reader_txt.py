_B='pattern'
_A=None
from.file_reader_interface import FileReaderInterface
def string_2_floats(text):
	A=[];B=text.split()
	for C in range(len(B)):
		try:A.append(float(B[C]))
		except ValueError:pass
	return A
class FileReaderTxt(FileReaderInterface):
	category='data';extensions=['TXT']
	def __init__(A,path,name='',encoding='',ignore=_A,curve_parser=_A,reader_options=_A):
		F=curve_parser;C=ignore;A.path=path;A.name=name;A.encoding=encoding or'utf-8';A.ignore=C;G=open(path,'r',encoding=A.encoding);A.raw_lines=G.readlines();G.close();A.raw_lines_number=len(A.raw_lines);D=[]
		if C:
			O,K=A.find_patterns_lines_nb([A[_B]for A in C])
			for(L,H)in enumerate(C):
				B=K[L]['lines']
				if B:B=A.get_raw_siblings_nb(B,pre=H.get('pre',0),post=H.get('post',0));D+=B
			B=list(set(B));B.sort()
		A.ignore_patterns=[A[_B]for A in C]if C else[];A.ignore_lines=D;A.ignore_lines_number=len(D);A.curves=F.get_curves(A.raw_lines)if F else _A;E=[]
		for(M,N)in enumerate(A.raw_lines):
			I=string_2_floats(N)
			if I:
				J=M+1
				if not J in D:E.append({'line':J,'floats':I})
		A.floats_lines=E;A.floats_lines_number=len(E);A.index=0
	def find_patterns_lines_nb(D,patterns):
		A=patterns;B=False;map={A:[]for A in A}
		for(E,F)in enumerate(D.raw_lines):
			for C in A:
				if F.find(C)!=-1:map[C].append(E+1);B=True
		return B,[{_B:A,'lines':map[A]}for A in A]
	def get_raw_siblings_nb(B,lines_nb_array,pre=0,post=0):
		A=[]
		for C in lines_nb_array:
			min=C-pre;max=C+post+1
			if min<0:min=0
			if max>B.raw_lines_number+1:max=B.raw_lines_number+1
			for D in range(min,max):
				if D not in A:A.append(D)
		return A
	def get_raw_lines(A,line_nb,pre=0,post=0):
		B=line_nb;min=B-1-pre;max=B-1+post+1
		if min<0:min=0
		if max>A.raw_lines_number:max=A.raw_lines_number
		return''.join([A.raw_lines[B]for B in range(min,max)])
	def info(A):return{'reader':A.__class__.__name__,'name':A.name,'path':A.path,'encoding':A.encoding,'raw_lines_number':A.raw_lines_number,'ignore_patterns':A.ignore_patterns,'ignore_lines_number':A.ignore_lines_number,'ignore_lines':A.ignore_lines,'floats_lines_number':A.floats_lines_number,'curves':A.curves}