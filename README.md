# ParticleSizeAnalysiser


The particle size distribution of coffee powder can directly affect the flavor of coffee, but the average family will not buy a professional analyzer. This program will give you an idea of the size distribution of the coffee powder coming out of your grinder. 

## Environment
1.python3

2.opencv4

3.matplotlib

## Usage
```
python ParticleSizeAnalysiser.py ./c40.jpg
```
The *c40.jpg* is just an example picture, you can replace it with your own picture.

your picture should be like *c40.jpg*, whose background is white and coffee powder doesn't overlap.

## Result

The first output is the grade, the higher grade means more powder in similar volume.

The second output is the standard deviation of median volume, the smaller standard deviation means the median volume more average.

The graph shows volume proportion of powder particles with different relative radii.

Here we test lagom mini, C40, we can see C40 has a better result!

![avatar](https://github.com/bishopAL/ParticleSizeAnalysiser/blob/master/lagomMini_result.png)

![avatar](https://github.com/bishopAL/ParticleSizeAnalysiser/blob/master/c40_result.png)
