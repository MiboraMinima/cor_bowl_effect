# Remove bowl effect from DOD

This plugin finds non-moving areas in a DoD (Difference of DEMs) based on
empirical thresholds and generate an interpolated surface (IDW) from points
sampled in those non-moving areas. The surface is used to correct the bowl
effect.

> The algorithm will work for DoDs generated from DEM containing very coarse
> sediments like Coastal Boulder Deposits (CBDs). It is not going to work with
> DoDs created with DEMs of sandy or gravel beach.

This is an **experimental plugin**.

## Install

Download the repository as `.zip`. Open QGIS and install the plugin : 
Click on `Plugins > Manage and Install Plugins > Install from ZIP`.

## Get parameters for batch processing

If you have lot a of file to process, you probably may want to use a [batch
process](https://docs.qgis.org/3.28/en/docs/user_manual/processing/batch.html).
The repo contain a tool that allows you to generate a `.json` parameter file
that can be load in the batch processing tool of QGIS.

For the tool to work, your files need to be sorted by directory of places in a
directory and each file should contain years in the format `YYYY_YYYY`. Look at
the example :

```
.
├── Katlahraun
│   ├── Katlahraun_2015_2016_DOD_mask_cordon.tif
│   ├── Katlahraun_2016_2017_DOD_mask_cordon.tif
│   ├── Katlahraun_2017_2018_DOD_mask_cordon.tif
│   ├── Katlahraun_2018_2019_DOD_mask_cordon.tif
│   ├── Katlahraun_2019_2021_DOD_mask_cordon.tif
│   ├── Katlahraun_2021_2022_DOD_mask_cordon.tif
│   └── Katlahraun_2022_2023_DOD_mask_cordon.tif
├── Kerling
│   ├── Kerling_2015_2016_DOD_mask_cordon.tif
│   ├── Kerling_2016_2017_DOD_mask_cordon.tif
│   ├── Kerling_2017_2018_DOD_mask_cordon.tif
│   ├── Kerling_2018_2021_DOD_mask_cordon.tif
│   ├── Kerling_2021_2022_DOD_mask_cordon.tif
│   └── Kerling_2022_2023_DOD_mask_cordon.tif
```

If you have a similar directory, you can run a similar command in your
terminal : 

```shell
python -m param_gen.gen_param "input/dir/DODs" "output/dir/results" "param_gen/params.json" --years 2015_2016 --places Site_1 Site_2
```

For a quick help :

```shell
python -m param_gen.gen_param -h
```

By default, `--year` is `None` so as `--places`, they are optional.

