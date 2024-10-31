_A='Plugins must implement the method'
from abc import ABC,abstractmethod
class FileReaderInterface(ABC):
	@property
	@abstractmethod
	def category(self):0
	def __init__(A,path,name='',encoding='',ignore=None,curve_parser=None,reader_options=None):raise NotImplementedError(_A)
	def get_raw_lines(A,line_nb,pre=0,post=0):raise NotImplementedError(_A)
	def find_patterns_lines_nb(A,patterns):raise NotImplementedError(_A)
	def class_info(A):raise NotImplementedError(_A)
	def info(A):B={'reader':A.__class__.__name__,'reader_category':A.category,'name':A.name,'path':A.path};B.update(A.class_info());return B