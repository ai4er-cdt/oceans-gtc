# AI4ER Guided Team Challenge 2024

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10841513.svg)](https://doi.org/10.5281/zenodo.10841513) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Project Description

In this study, we demonstrate that machine learning techniques can predict abyssal MOC strength using only satellite-observable variables. We train a suite of models for this task using the "Estimating the Circulation and Climate of the Ocean" (ECCO) state estimate, obtaining state-of-the-art performance. We incorporate the "Australian Community Climate and Earth System Simulator Ocean Model" (ACCESS), a high-resolution numerical ocean circulation model; and observational "Rapid Climate Change-Meridional Overturning Circulation and Heatflux Array" (RAPID) data, a cross-basin sensor array that directly measures the Atlantic MOC strength. Our experiments indicate an approximately linear relationship between satellite-observable variables and abyssal MOC strength. We additionally demonstrate the utility of observational data for predicting long-range oceanic dependencies through the integration of RAPID, and show that a deep learning model is able to accurately capture latitude-invariant features for MOC strength prediction. Through these experiments, we present a methodology for predicting abyssal circulation, which will be instrumental in informing climate policy and empowering further oceanographic research. 

Please see our final report ([`assets/gtc_report_FINAL.pdf`](assets/gtc_report_FINAL.pdf)) for full details.

This work was carried out as part of the [Artificial Intelligence for Environmental Risks](https://ai4er-cdt.esc.cam.ac.uk/) (AI4ER) Centre for Doctoral Training Guided Team Challenge (GTC), which ran from November, 2023 to March, 2024.

## Documentation

Please see the included [`DOCUMENTATION.md`](DOCUMENTATION.md) file for an overview of the repository structure. We include [tables](https://github.com/ai4er-cdt/OTP/blob/main/DOCUMENTATION.md#reproducing-report-figures-and-tables) that direct the user towards the appropriate notebook for reproducing each table and figure in the final report.

-----

## Team Members

<table>
  <tr>
    <td><img src="assets/ninab.png" alt="Nina Baranduin" style="border-radius: 50%; width: 80px; height: 80px;"></td>
    <td><a href="mailto:ngb34@cam.ac.uk">Nina Baranduin</a></td>
    <td><img src="assets/tomc.png" alt="Tom Cowperthwaite" style="border-radius: 50%; width: 80px; height: 80px;"></td>
    <td><a href="mailto:tc656@cam.ac.uk">Tom Cowperthwaite</a></td>
    <td><img src="assets/emiliolr.png" alt="Emilio Luz-Ricca" style="border-radius: 50%; width: 80px; height: 80px;"></td>
    <td><a href="mailto:el590@cam.ac.uk">Emilio Luz-Ricca</a></td>
  </tr>
  <tr>
    <td><img src="assets/sharanm.png" alt="Sharan Maiya" style="border-radius: 50%; width: 80px; height: 80px;"></td>
    <td><a href="mailto:sm2783@cam.ac.uk">Sharan Maiya</a></td>
     <td><img src="assets/alinevd.png" alt="Aline Van Driessche" style="border-radius: 50%; width: 80px; height: 80px;"></td>
    <td><a href="mailto:av656@cam.ac.uk">Aline Van Driessche</a></td>
  </tr>

</table>

## Acknowledgements

We would like to thank our faculty supervisors--Ali Mashayek, Laura Cimoli, and Alberto Naveira Garabato--as well as our project mentors--Josh Lanham and Kate Oglethorpe. Their guidance throughout was instrumental in our success as a team. We would also like to thank the AI4ER support staff--Annabelle Scott and Adriana Dote--for their help navigating the complex logistics of the GTC.

-----

## License and Citation

If you use the code in this repository, please consider citing it--see the [`citation.cff`](citation.cff) file or use the "Cite this repository" function on the right sidebar. All code is under the MIT license--see the [`LICENSE`](LICENSE) file.

-----

## Data Availability

### ECCO 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10832706.svg)](https://doi.org/10.5281/zenodo.10832706)

All ECCO data that we extracted is included in the Zenodo repository linked in the badge directly above. To facilitate interpretation of the code in this repository, we have copied over dataset metadata--see [`DATA_README.md`](DATA_README.md). Raw ECCO data is available for download from [NASA PO.DAAC](https://podaac.jpl.nasa.gov/); see the table in `DATA_README.md` for the PO.DAAC entries that we used.

### ACCESS

ACCESS data was provided to us directly by colleagues at the National Oceanography Centre (NOC; Southampton, UK) and is not publicly available but may be provided upon reasonable request. Team member emails are linked above.

### RAPID

[![DOI](https://img.shields.io/badge/DOI-10.5285%2F04c79ece--3186--349a--e063--6c86abc0158c-blue)](https://doi.org/10.5285/04c79ece-3186-349a-e063-6c86abc0158c)

RAPID data can be downloaded from the NOC British Oceanographic Data Centre (linked in the badge directly above). This data was used in the provided format. We primarily make use of `moc_transports_200404_2022215.nc` and `moc_vertical_200404_2022215.nc`. 

-----

<p align="middle">
  <a href="https://ai4er-cdt.esc.cam.ac.uk/"><img src="assets/ai4er_logo.png" width="15%"/></a>
  <a href="https://www.cam.ac.uk/"><img src="assets/cambridge_logo.png" width="56%"/></a>
</p>
