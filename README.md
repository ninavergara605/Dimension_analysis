# Methods for Calculating Fractal Dimension
 
**Author**: *Nina Vergara*
  
## Overview
- [Background & Purpose]()
- [Data]()
- [Algorithms]()
  - [Box Counting]()
  - [Minkowski-Bouligand]()
  - [Horizontal Segmentation Method]()
- [Results]()
  - [Box Counting]()
  - [Minkowski-Bouligand]()
  - [Horizontal Segmentation Method]()
- [Conclusions]()
- [Repository Structure]()
  
## Background & Purpose
Fractal Dimension is a measure of how smooth or rough a curve is, while taking into account the space filling properties as well. This analysis can be applied to data of dimensions greater than one. 
It's commonly used within material's science, geographical, and financial contexts. There are many techniques available for calculating this measure, each sensitive to the properties of the curves themselves. 
This project aims to assess the performance of popular methods when tested on 2-d test curves that vary in smoothness, roughness, and sample size.
 
## Data
![test curves](https://github.com/ninavergara605/dimension_analysis/blob/13db2adb864f48822341ad61d94c55545d40aeb8/images/test_curves.png)
These curves are self-affine, meaning its features are scaled differently. Due to the scaleing differences, zooming in on a self-affine curve can reveal details that would otherwise be missed. This property can be seen in the FBM curves. This property isn't readily apparent in the Koch curve since a small sample of points is utilized for this analysis.

The Koch Curve (n=160) was created by Niels Fabian Helge von Koch in 1904, and has a theoretical dimension of ~1.261. With a sample size of n=160, this curve will represent the low dimension, low sample size test case.  

Two Fractal Brownian Motion (FBM) curves were utilized in this analysis. FBM curves originated from the works of Hurst (1951, 1957, and 1968) and expanded by Mandelbrot and Van Ness (1968), and Mandelbrot and Wallis (1968,1969).
The hurst component (H) is used to modify the roughness of the curve (Mandelbrot & Von Ness, 1968), with the fractal dimension (d) of the curve being: d = 2-H. 
The FMB curve with the dimension of 1.2 (n=1000) has two functions. When compared to the Koch curve it will serve as a low dimension, high sample size test case. When compared to the high dimension FBM curve, it will be evaluated on its relative smoothness. The FBM curve with a dimension of 1.75 (n=1000) will be the 'rough' curve test case.

-- modify and put this in a future considerations section -- 
Although the Koch curve (d= ~1.261) and FBM curve (d= 1.2) have similar fractal dimensions, the Koch curve occupies a larger region of the sample space. Comparing these two curves could offer a (hackish) glimpse into the effectiveness of each technique
on lower dimensional curves with varying space filling properties. This probably isn't a true measure of space filling properties because the sample sizes are massively different. will try interpolation for koch curve to level the playing field. 

## Algorithms
### Generalized Cover

### Box Counting
![box counting grid](https://github.com/ninavergara605/dimension_analysis/blob/13db2adb864f48822341ad61d94c55545d40aeb8/images/box_counting_grid.png)

### Minkowski-Bouligand
![nd- distance transform](https://github.com/ninavergara605/dimension_analysis/blob/13db2adb864f48822341ad61d94c55545d40aeb8/images/nd_distance_transform.png)

### Horizontal Segmentation Method
![1d-distance transform](https://github.com/ninavergara605/dimension_analysis/blob/13db2adb864f48822341ad61d94c55545d40aeb8/images/1d_distance_transform.png)

## Results

### Box Counting
![box counting result](https://github.com/ninavergara605/dimension_analysis/blob/c7b9e5cf784385f2fff854878a77c4bbbc4c8f8b/images/box_counting_result.png)

### Minkowski-Bouligand
![Minkowski-Bouligand result](https://github.com/ninavergara605/dimension_analysis/blob/c7b9e5cf784385f2fff854878a77c4bbbc4c8f8b/images/minkowski_performance.png)

### Horizontal Segmentation Method
![HSM result](https://github.com/ninavergara605/dimension_analysis/blob/c7b9e5cf784385f2fff854878a77c4bbbc4c8f8b/images/hsm_performance.png)

## Conclusions
    

## Repositroy Structure
 ```
├── images                             <- Stores technique performance, distance transforms, and test curve visualizations                                  
├── Minkowski_Bouligand_and_HSM.ipynb  <- Notebook for Minkowski-Bouligand and HSM implemenations
├── box_counting_method.ipynb          <- Notebook for the box counting method
├── test_curve_visualization.ipynb     <- Notebook for FBM curve creation and test curve visualization  
└── README.md                          <- Project description
