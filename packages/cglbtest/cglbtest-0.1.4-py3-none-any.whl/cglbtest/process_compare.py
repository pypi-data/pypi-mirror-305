from.utils_compare import UtilsCompare
class ProcessCompare:
	def __init__(A,utils_compare,prefix_files_path='',error_rule_patterns=None,dir_to_compare=''):
		A.utils_compare=utils_compare;A.prefix_files_path=prefix_files_path;A.error_rule_patterns=error_rule_patterns;A.dir_to_compare=dir_to_compare
		if A.dir_to_compare and A.dir_to_compare[0]!='/':A.dir_to_compare='/'+A.dir_to_compare
	def compare(A,test_dir='test',ref_dir='reference',name='',report_dir=''):C=ref_dir;B=test_dir;B=A.prefix_files_path+B.rstrip('/');C=A.prefix_files_path+C.rstrip('/');return A.utils_compare.compare_directory(f"{B}{A.dir_to_compare}",f"{C}{A.dir_to_compare}",report_dir=report_dir,name=name,error_rule_patterns=A.error_rule_patterns)