# HistoImgProcessing
## Full slide to Jpeg
`FullSlidesToJpeg.py`:

+ Create a single jpeg file from an .svs or an .mrxs file, reading independently 8*8=64 independent areas and then pasting them together after reducing each cell by a factor 10.

+ Argument: --inputdir : directory containing the slides
            --outputdir: directory where the jpeg files will be saved.
            
`FullSlidesToJpg.sh`:

Exemple of a bash file.

## Vahadane
`Vahadane.py`: 

Main script to normalize a picture through the Vahadane algorithm.

`HE_NormLNEN.py` to run with `VahanneLNENHE.sh`.

The target tile is a constant given at the begining of the script. 

Normalize all tiles to HE.

**Arg:**
 
--inputdir: Directory where the **tiles** to normalized are saved.
--outputdir : Directory where the **tiles** normalized will be stored.

Note: The inputdir and outputdir will have the same organisation such that:

Expected organisation:

- Main Folder:
    - Sample_id
        - Accept
            - .jpg
        - Reject
            - .jpg

`HESHE_NormLNEN.py` to run with `VahanneLNENHESHE.sh`, same at the previous programs, but this one normalize the tiles to HES or HE according the original staining given in the table `/home/mathiane/ImgProcessing/Data/Slides_LNEN_CIRC.csv`

## Tiling

`Tiling.py`: 

Main script to cut a slide into tiles of size 512*512px.

For each region the criteria to accept or reject a tile are:

+ Proportion of background (Luedde et al.)
+ Vertical & horizontal Gradient (Yu Fu et al.)

**Args :**
+ --inputdir : Where the slides are stored
+ --outputdir : Main folder where the tiles will be stored. The output organisation is :
- Main Folder:
    - Sample_id
        - Accept
            - .jpg
        - Reject
            - .jpg
            
`Tiling/PRADTiles.sh` Bash script for the TCGA data.

`Tiling/LNENTIling.sh` Bash script for LNEN data.

## Creation Of The Set Second Experiment PC-Chip
Jupyter notebook with the instruction that allowed creating the set for the second experiment with PC-CHIP (TCGA + LNEN).

## Test Confounding Factors : examles Scanner/Origine

`summarize_by_tile.py`

For each sample we collect randomly 50 tiles for which we calculated the mean and the variances of pixels values by channels. The data are store into a .csv.

`stats_image.ipynb`

Jupyter notebook that summurized if the Vahadane HE or HE/HES color normalization have removed the unwanted effect of the scanner, the stainin process and the origine on pixels color values.

## Macenko Normalisation HES Experiments

Experimental notebooks where we tried to generalized Macenko color normalisation technique to HES slides. 

**Conclusion: In the majority of the cases it cannot work since it is actually a PCA on the slides so there is any guarantee that each eigenvectors (which are BTW orthogonal) explained INDEPENDENTLY the contribution of the three stains most of the time it will be a composition of two. Therefore the technique IS NOT generalisable!**

## General tools 

+ `get_slide_magnificiance.py`
+ `statTCGA_picturesdb.py`

## Artefacts detection 
+ Bubbles classiers
+ Pen Marks detectetors
# HistoImgPreProcessing
