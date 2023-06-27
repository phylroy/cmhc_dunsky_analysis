

import yaml
import pathlib
import os
output_folder = r".\output"
template_file = r".\template.yml"

location_maps = [
    ['CAN_QC_Montreal-Trudeau.Intl.AP.716270_CWEC2016.epw', 'Montreal'],
    ['CAN_NS_Halifax.Dockyard.713280_CWEC2016.epw', "Halifax"],
    ['CAN_AB_Edmonton.Intl.AP.711230_CWEC2016.epw', "Edmonton"],
    ['CAN_BC_Vancouver.Intl.AP.718920_CWEC2016.epw', "Vancouver"],
    ['CAN_ON_Toronto.Pearson.Intl.AP.716240_CWEC2016.epw', "Toronto"],
    ['CAN_NT_Yellowknife.AP.719360_CWEC2016.epw', "YellowKnife"]
]

#Dunsky only optimizing for NG.
fuel_types = [
    #['Electricity', 'Elec'],
    ['NaturalGas', 'NG'],
    #['ElectricityHPElecBackup', 'HP']
]

building_types = [
    ['MidriseApartment', 'Mid'],
    ['HighriseApartment', 'High'],
    ['LowriseApartment', 'Low']
]
def create_optimization_input_yml()
    # Optimization
    for location_map in location_maps:
        for building_type in building_types:
            for fuel_type in fuel_types:
                # load yml file.
                # Open the yaml in analysis dict.
                with open(template_file, 'r') as stream:
                    template = yaml.safe_load(stream)
                analysis_name = f"dky_{location_map[1]}_Optim_{fuel_type[1]}_{building_type[1]}"
                #modify template
                template[':analysis_name'] = analysis_name
                template[':algorithm_nsga_n_generations'] =  20
                template[':algorithm_nsga_population'] =  40
                template[':algorithm_nsga_prob'] = 0.85
                template[':algorithm_type'] = 'nsga2'
                template[':options'][':building_type'] = location_map[0]

                # set yml file path to save to.
                filepath = pathlib.Path(os.path.join(output_folder, f"dky_{location_map[1]}_Optim_{fuel_type[1]}_{building_type[1]}","input.yml"))
                #make folder
                filepath.parent.mkdir(parents=True, exist_ok=True)
                # save yml file.
                with open(filepath, 'w') as outfile:
                    yaml.dump(template, outfile, default_flow_style=False)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
