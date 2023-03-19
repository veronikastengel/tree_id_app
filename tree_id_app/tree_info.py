def tree_infos():
    tree_dict = {'Eucalyptus': 
                    ['Eucalyptus','Eucalyptus', 'eucalyptus', 
                    'This is the species that covers the largest area in Mainland Portugal: 26% of the forest area are Eucalyptus, which corresponds to 845 mil ha.'],
                'Pinus Pinaster': 
                    ['Maritime Pine','Pinheiro Bravo', 'pinuspinaster', 
                    'This is one of the 3 main species of trees in Mainland Portugal. It covers 22% of the forest area (713 mil ha). However, it is also the species with the biggest decline in area, loosing 265 mil hectars between 1995 and 2015.'],
                'Pinus Pinea': 
                    ['Stone Pine','Pinheiro Manso', 'pinuspinea', 
                    'This tree species covers 6% of forest area in Mainland Portugal. Since 2005, this species has increased its area by 21 mil ha.'],
                'Quercus Rotundifolia': 
                    ['Holm Oak','Azinheira', 'quercusrotundifolia', 
                    'This tree species covers 11% of forest area in Mainland Portugal. Since 2005, this species has increased its area by 14 mil ha.'],
                'Quercus Suber': 
                    ['Cork Oak','Sobreiro', 'quercussuber', 
                    'This is one of the 3 main species of trees in mainland Portugal. It covers 22% of the forest area (720 mil ha).']
                }
    return tree_dict


if __name__ == "__main__":
    infodict = tree_infos()
    print(infodict['Eucalyptus'])