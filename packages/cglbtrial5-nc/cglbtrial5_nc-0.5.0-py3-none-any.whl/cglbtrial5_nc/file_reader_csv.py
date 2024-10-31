_B='curves'
_A=None
import csv
from cglbtrial5.readers.file_reader_interface import FileReaderInterface
def is_num(x):
	try:return float(x)
	except ValueError:return
def csv_row_detect_header(first_row):
	A=first_row
	if all(not A.isdigit()for A in A):return True,A
	else:return False,[f"Column {A}"for(A,B)in enumerate(A)]
def csv_row_detect_cols_num(row):return[A for(A,B)in enumerate(row)if is_num(B)!=_A]
def csv_detect(path):
	with open(path,'r')as B:A=csv.reader(B);C=next(A);D,E=csv_row_detect_header(C);F=next(A);G=csv_row_detect_cols_num(F);return D,E,G
class FileReaderCsv(FileReaderInterface):
	category='data';extensions=['CSV']
	def __init__(A,path,name='',encoding='',ignore=_A,curve_parser=_A,reader_options=_A):
		D=ignore;C=path;A.path=C;A.name=name;A.encoding=encoding or'utf-8';A.ignore=D;B,K,L=csv_detect(C);A.has_header=B;A.cols=K;A.numeric_col_indexes=L;H=open(C,'r',encoding=A.encoding);M=csv.reader(H);E=[]
		for N in M:E+=[N]
		if B:E.pop(0)
		H.close();A.data_rows=E;A.raw_lines_number=len(A.data_rows)+(1 if B else 0);F=[];A.ignore_patterns=[A['pattern']for A in D]if D else[];A.ignore_lines=F;A.ignore_lines_number=len(F);A.curves=A._get_curves();G=[]
		if A.numeric_col_indexes:
			for(O,P)in enumerate(A.data_rows):
				I=[float(P[A])for A in A.numeric_col_indexes]
				if I:
					J=O+1
					if not J in F:G.append({'line':J+(1 if B else 0),'floats':I})
		A.floats_lines=G;A.floats_lines_number=len(G);A.index=0
	def find_patterns_lines_nb(A,patterns):return False,[]
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
		B=line_nb;min=B-pre;max=B+post+1
		if min<0:min=0
		if max>A.raw_lines_number:max=A.raw_lines_number
		return''.join([','.join(A.data_rows[B+(-1 if A.has_header else 0)])for B in range(min,max)])
	def class_info(A):return{'encoding':A.encoding,'raw_lines_number':A.raw_lines_number,'ignore_patterns':A.ignore_patterns,'ignore_lines_number':A.ignore_lines_number,'ignore_lines':A.ignore_lines,'floats_lines_number':A.floats_lines_number,_B:A.curves}
	def _get_curves(C):
		G='title';A=C.cols;E=C.numeric_col_indexes[0];H=[B for(A,B)in enumerate(C.numeric_col_indexes)if A!=0];D=[];F=[]
		for B in H:I={G:A[B],'short_title':A[B],'series':[[float(A[E]),float(A[B])]for A in C.data_rows]};D+=[I];J={G:A[B],'type':'simple','xaxis':A[E],'yaxis':A[B],_B:[len(D)-1]};F+=[J]
		return{_B:D,'charts':F}