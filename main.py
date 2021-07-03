import pandas as pd

class Assembly:
    def __init__(self, component_list, parsed_list=None):
        self.component_list = component_list

    @property
    def components(self):
        return self._parse_components(self.component_list)

    def _parse_components(self, cl):
        components = {}
        for part in cl.strip().split(','):
            qty, upc = part.split('x')

            components[upc] = qty

        return components

    def __add__(self, other):        
        combined_components = self.components

        for upc, qty in other.components.items():
            combined_components[upc] += qty

        return Assembly(self.component_list + ',' + other.component_list)

    def __repr__(self):
        return str(self.components)


def get_data():
    fn = r'Cleaned Power Parts Database.xlsx'
    #header_line = 0 # i.e. the first row
    df = pd.read_excel(fn)#, index_col=header_line, index_col=None)
    #print (df)

    #print ( df[(df.COST < 3) & (df.Category == 'Receptacles')] )

    cl = '2x3448110030, 3x3448110031, 1x3448110030, 1x3448110033'

    assy1 = Assembly(cl)
    assy2 = Assembly(cl)

    print (assy1, assy2, assy1+assy2)
    
if __name__ == '__main__':
    get_data()
    
