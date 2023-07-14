import os
import re

def populate_dict(dict_file, input_dir, output_dir, subdir, file, date):
    # Inputs
    input_path = f"'{input_dir}/{subdir}/{file}'"
    output_detail = f"{output_dir}/{subdir}/{subdir}_{date}_bowl_details"

    # Create the dir if it doesn't exist
    if not os.path.exists(output_detail):
        os.makedirs(output_detail)

    # Outputs
    output_dod_filtered = f"{output_detail}/{subdir}_{date}_dod_filtered.tif"
    output_dod_filtered_extract = f"{output_detail}/{subdir}_{date}_dod_extract.gpkg"
    output_sample_points = f"{output_detail}/{subdir}_{date}_sample_points.gpkg"
    output_bspline = f"{output_detail}/{subdir}_{date}_bspline.tif"  # Can't write it in gpkg format
    output_cleaned = f"{output_dir}/{subdir}/{subdir}_{date}_dod_cor_bowl.tif"

    # Fill the dictionary with paths
    dict_file['PARAMETERS']['INPUT'] = input_path
    dict_file['OUTPUTS']['OUTPUT_DOD_FILTERED'] = output_dod_filtered
    dict_file['OUTPUTS']['OUTPUT_DOD_FILTERED_EXTRACT'] = output_dod_filtered_extract
    dict_file['OUTPUTS']['OUTPUT_SAMPLE_POINTS'] = output_sample_points
    dict_file['OUTPUTS']['OUTPUT_BSPLINE'] = output_bspline
    dict_file['OUTPUTS']['OUTPUT_CLEANED'] = output_cleaned

    return dict_file


def reset_dict():
    dict_file = {
        "PARAMETERS": {
            "INPUT": None
        },
        "OUTPUTS": {
            "OUTPUT_DOD_FILTERED": None,
            "OUTPUT_DOD_FILTERED_EXTRACT": None,
            "OUTPUT_SAMPLE_POINTS": None,
            "OUTPUT_BSPLINE": None,
            "OUTPUT_CLEANED": None
        }
    }

    return dict_file


def process_files(input_dir, output_dir, years, places):
    list_all = []
    for root, dirs, files in os.walk(input_dir):
        for subdir in dirs:
            if places and not years:
                if subdir in places:
                    print(subdir)
                    dict_file = reset_dict()
                    for file in os.listdir(f"{root}/{subdir}"):
                        print(file)
                        date = re.search(r'(\d{4}_\d{4})', file).group(1)
                        dict_res = populate_dict(dict_file, input_dir, output_dir, subdir, file, date)
                        list_all.append(dict_res)
                        dict_file = reset_dict()

            elif places and years:
                if subdir in places:
                    print(subdir)
                    dict_file = reset_dict()
                    for file in os.listdir(f"{root}/{subdir}"):
                        date = re.search(r'(\d{4}_\d{4})', file).group(1)
                        if date in years:
                            print(file)
                            dict_res = populate_dict(dict_file, input_dir, output_dir, subdir, file, date)
                            list_all.append(dict_res)
                            dict_file = reset_dict()
            elif not places and years:
                print(subdir)
                dict_file = reset_dict()
                for file in os.listdir(f"{root}/{subdir}"):
                    date = re.search(r'(\d{4}_\d{4})', file).group(1)
                    if date in years:
                        print(file)
                        dict_res = populate_dict(dict_file, input_dir, output_dir, subdir, file, date)
                        list_all.append(dict_res)
                        dict_file = reset_dict()
            else:
                print(subdir)
                dict_file = reset_dict()
                for file in os.listdir(f"{root}/{subdir}"):
                    print(file)
                    date = re.search(r'(\d{4}_\d{4})', file).group(1)
                    dict_res = populate_dict(dict_file, input_dir, output_dir, subdir, file, date)
                    list_all.append(dict_res)
                    dict_file = reset_dict()

    print(list_all)

    return list_all

