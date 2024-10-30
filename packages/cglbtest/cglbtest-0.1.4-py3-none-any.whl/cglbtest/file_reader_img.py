from.file_reader_interface import FileReaderInterface
class FileReaderImg(FileReaderInterface):
	category='img'
	def __init__(A,path,name='',encoding='',ignore=None,curve_parser=None,reader_options=None):A.path=path;A.name=name
	def class_info(A):return{}