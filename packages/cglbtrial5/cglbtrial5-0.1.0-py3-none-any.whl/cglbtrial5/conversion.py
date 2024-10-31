def unit_one_2_unit_two(value_unit_one):A=3.22*(value_unit_one-12.)+111.11;return A
from importlib.metadata import entry_points
def load_plugins():
	A=[]
	for B in entry_points().get('main_package.reader_plugins',[]):C=B.load();A.append(C)
	return A