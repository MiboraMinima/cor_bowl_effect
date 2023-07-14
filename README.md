# Remove bowl effect from DOD

**Still under development...** 

## Get parameters for batch processing

If you have a lot a file to process, you probably may want to use a [batch process](https://docs.qgis.org/3.28/en/docs/user_manual/processing/batch.html). This tool allows you to generate a parameter file. 

For the tool to work, your files need to be sorted by directory of places in a directory and each file should contain years in the format `YYYY_YYYY`. Look at the example :

```
.
├── Katlahraun
│   ├── Katlahraun_2015_2016_DOD_mask_cordon.tif
│   ├── Katlahraun_2016_2017_DOD_mask_cordon.tif
│   ├── Katlahraun_2017_2018_DOD_mask_cordon.tif
│   ├── Katlahraun_2018_2019_DOD_mask_cordon.tif
│   ├── Katlahraun_2019_2021_DOD_mask_cordon.tif
│   ├── Katlahraun_2021_2022_DOD_mask_cordon.tif
│   └── Katlahraun_2022_2023_DOD_mask_cordon.tif
├── Kerling
│   ├── Kerling_2015_2016_DOD_mask_cordon.tif
│   ├── Kerling_2016_2017_DOD_mask_cordon.tif
│   ├── Kerling_2017_2018_DOD_mask_cordon.tif
│   ├── Kerling_2018_2021_DOD_mask_cordon.tif
│   ├── Kerling_2021_2022_DOD_mask_cordon.tif
│   └── Kerling_2022_2023_DOD_mask_cordon.tif
```

If you have a similar directory, you can use. 

```shell
python -m param_gen.gen_param "input/dir/DODs" "output/dir/results" --years 2015_2016 --places Site_1 Site_2 "param_gen/params.json"
```

For a quick help :

```shell
python -m param_gen.gen_param -h
```

By default `--year` is `None` so as `--places`, they are optional.

