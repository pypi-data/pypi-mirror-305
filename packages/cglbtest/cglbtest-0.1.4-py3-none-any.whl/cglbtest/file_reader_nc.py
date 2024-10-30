_D='unit'
_C='data'
_B='name'
_A=None
from.file_reader_interface import FileReaderInterface
from netCDF4 import Dataset
def explore_group(group,indent=0):
	D='----';B=indent;A=group;print(D*B+f"Group: {A.path}")
	for(E,C)in A.variables.items():print(D*(B+1)+f"Variable: {E}, Shape: {C.shape}, Data Type: {C.dtype}")
	for(G,F)in A.groups.items():explore_group(F,B+1)
def get_variable_eligible(variable):return variable.ndim==1
def get_variable_data(variable,conversion=_A):A=conversion;B=[A for A in variable[:]];return list(map(A,B))if A else B
class NetcdfHelper:
	def __init__(A,dataset,unit_attribute=_A,x_variable_name=_A):A.dataset=dataset;A.unit_attribute=unit_attribute;A.x_variable_name=x_variable_name
	def get_variables_from_group(G,group,exclude_keys=_A,include_keys=_A,conversion=_A):
		D=include_keys;C=exclude_keys;E=G.unit_attribute;F=[]
		for(B,A)in group.variables.items():
			if D and B not in D:continue
			if C and B in C:continue
			if get_variable_eligible(A):F.append({_B:B,_D:A.getncattr(E)if E in A.ncattrs()else'',_C:get_variable_data(A,conversion=conversion)})
		return F
	def build_graph(A):
		D=[];B=A.x_variable_name;C=A.get_variables_from_group(A.dataset,include_keys=[B]);F=C[0]if C else _A
		for(G,E)in A.dataset.groups.items():H=A.get_variables_from_group(E,include_keys=[B]);I=A.get_variables_from_group(E,exclude_keys=[B],conversion=float);J={_B:G,'x_serie':C[0]if H else F,'y_series':I};D.append(J)
		return D
class FileReaderNc(FileReaderInterface):
	category=_C
	def __init__(A,path,name='',encoding='',ignore=_A,curve_parser=_A,reader_options=_A):
		B=reader_options;A.path=path;A.name=name;A.encoding=encoding or'utf-8';A.ignore=ignore;A.type=B['type'];A.units_attribute=B['units_attribute'];A.dataset=Dataset(path,mode='r')
		if A.type=='framesseries_2D':A.frame_variable=B['frame_variable'];A.frame_steps=B.get('frame_steps',_A);A.framesseries=A.build_graph_framesseries()
		A.dataset.close()
	def build_graph_framesseries(A):
		I='variables';H='frames_variable';G='frames_number';D=A.dataset;C={G:0,H:_A,I:[]};B=D.variables[A.frame_variable];E=B[:].tolist();C[G]=len(E);C[H]={_B:A.frame_variable,_D:B.getncattr(A.units_attribute)if A.units_attribute in B.ncattrs()else'',_C:E}
		if A.frame_steps:B=D.variables[A.frame_steps];E=B[:].tolist();C['frames_steps_variable']={_B:A.frame_steps,_D:B.getncattr(A.units_attribute)if A.units_attribute in B.ncattrs()else'',_C:E}
		J=sorted([B for(B,C)in D.variables.items()if B!=A.frame_variable and C.ndim==2])
		for F in J:B=D.variables[F];C[I].append({_B:F,_D:B.getncattr(A.units_attribute)if A.units_attribute in B.ncattrs()else'',_C:B[:].tolist()})
		return C
	def info(A):return{'reader':A.__class__.__name__,_B:A.name,'path':A.path,'encoding':A.encoding,'info':f"type: {A.type}, units_attribute: {A.units_attribute}",'framesseries':A.framesseries}
	def save(A):
		import json
		if A.framesseries:
			with open(f"{A.path}.json",'w')as B:json.dump(A.framesseries,B)
	def explore_group(B):A=Dataset(B.path,mode='r');explore_group(A);A.close()