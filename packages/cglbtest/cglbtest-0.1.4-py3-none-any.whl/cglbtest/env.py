_e='report_html'
_d='report_json'
_c='report_txt'
_b='report_lines'
_a='reader_options'
_Z='ignore'
_Y='encoding'
_X='extension_unknown_ignore'
_W='extension_fallback'
_V='extension_mapping'
_U='command_suffix'
_T='pre_folder_creation'
_S='pre_folder_delete'
_R='sections'
_Q='error_rule_patterns'
_P='execute'
_O='assets_mgmt'
_N=False
_M='env_var'
_L='meta'
_K='boolean'
_J='list'
_I='file_check'
_H='compare'
_G='string'
_F='exemple'
_E=None
_D='default'
_C='description'
_B='type'
_A='name'
import os,yaml
from.utils_compare import UtilsCompare
from.utils_execute import UtilsExecute
from.process_execute_and_compare import ProcessExecuteAndCompare
from.process_compare import ProcessCompare
import logging
logger=logging.getLogger('env')
CONF_BLOCKS={_L:[{_A:'title',_B:_G,_D:'',_F:'"CGLB / Comparison Results /"',_M:'CGLBTEST_META_TITLE',_C:'Prefix Title of the tests. It is used in the html report with the name of the test.'},{_A:'image',_B:_G,_D:'',_F:'"https://media.cesgenslab.fr/logos/logo30x30.png"',_C:'Web Image source. It is used for html reports. Could be url or encoded source like data:image/png;base64,iVB...'},{_A:'report_success_collapse',_B:'booleab',_D:True,_F:'true',_C:'Collapse success tests in html reports'}],_O:[{_A:'foldername',_B:_G,_F:'"test_assets_forlder"',_D:'',_M:'CGLBTEST_ASSETS_MGMT_FOLDERNAME',_C:'Name of the folder where test assets will we placed.'}],_P:[{_A:_S,_B:_J,_F:'["DEBUG", "LOG", "OUT"]',_C:'List of folders to delete before execution'},{_A:_T,_B:_J,_F:'["INI", "DAT"]',_C:'List of folders to create before execution'},{_A:_U,_B:_G,_D:'',_F:'" --token DGDFGDFGDH"',_M:'CGLBTEST_EXECUTE_COMMAND_SUFFIX',_C:'Suffix to add to the command. Typically when secrets are used.'}],_H:[{_A:_V,_B:'dict',_C:'Map of source extension to target extension. For exemple process .txt as .csv',_F:'{"txt": "csv"}'},{_A:_W,_B:_G,_C:'If no reader found for an extension, use this extension as fallback.'},{_A:_X,_B:_K,_D:True,_C:'If no reader found for an extension, skip the file without generate an error'},{_A:_Y,_B:_G,_D:'',_C:'Encoding used to read the files.'},{_A:_Z,_B:_J,_C:'List of patterns to ignores'},{_A:_a,_B:'dict',_C:'Dict of specific options of a Reader'},{_A:_b,_B:_J},{_A:_c,_B:_K,_D:_N},{_A:_d,_B:_K,_D:_N},{_A:_e,_B:_K,_D:_N}],_I:[{_A:_Q,_B:_J}]}
CONF_PROCESSORS_BLOCKS={_H:{_R:[_L,_O,_I,_H],_C:'Compare two folders'},'execute_and_compare':{_R:[_L,_O,_P,_I,_H],_C:'Execute binaries and, compare two folders resuls or one reference folder to an execution folder'}}
class Env:
	def __init__(B,yaml_file=''):
		E=yaml_file;F={};C={}
		if E:
			logger.info(f"loading configuration file {E}")
			with open(E,'r')as J:
				try:C=yaml.safe_load(J)
				except yaml.YAMLError as K:raise Exception(f"Error in configuration file {E}: {K}")
		else:logger.info(f"no configuration file provided")
		try:B.processor=C.get('processor',_E)
		except:B.processor=_E
		if not B.processor:raise Exception(f"can't derive processor")
		if B.processor in CONF_PROCESSORS_BLOCKS:
			for A in CONF_PROCESSORS_BLOCKS[B.processor][_R]:
				F[A]={}
				if not C.get(A,_N):C[A]={}
				if CONF_BLOCKS[A]=='*':F[A].update(C[A])
				else:
					for G in CONF_BLOCKS[A]:
						H=G[_A];type=G[_B];L=G.get(_D,_E);I=G.get(_M,_E);D=_E
						if I:D=os.getenv(I)
						if D==_E:D=C[A].get(H,L)
						if type==_K:D=D==True
						F[A][H]=D
		else:raise Exception(f"processor {B.processor} is not recognized in configuration file {E}")
		B.conf=F
	def _get_UtilsExecute(B):A=B.conf[_P];return UtilsExecute(pre_folder_delete=A[_S],pre_folder_creation=A[_T],command_suffix=A[_U])
	def _get_UtilsCompare(B,curve_parser=_E):A=B.conf[_H];return UtilsCompare(meta=B.conf[_L],extension_mapping=A[_V],extension_fallback=A[_W],extension_unknown_ignore=A[_X],ignore=A[_Z],reader_options=A[_a],report_lines=A[_b],report_txt=A[_c],report_json=A[_d],report_html=A[_e],encoding=A[_Y],curve_parser=curve_parser)
	def processor_execute_and_compare(A,test_exe_path,ref_exe_path,prefix_files_path='',curve_parser=_E):B=A.conf;C=A._get_UtilsExecute();D=A._get_UtilsCompare(curve_parser=curve_parser);E=ProcessExecuteAndCompare(utils_execute=C,utils_compare=D,test_exe_path=test_exe_path,ref_exe_path=ref_exe_path,dir_to_compare='',error_rule_patterns=B[_I].get(_Q,_E),prefix_files_path=prefix_files_path);return E
	def processor_compare(A,prefix_files_path='',curve_parser=_E):B=A.conf;C=A._get_UtilsCompare(curve_parser=curve_parser);D=ProcessCompare(utils_compare=C,dir_to_compare='',error_rule_patterns=B[_I].get(_Q,_E),prefix_files_path=prefix_files_path);return D