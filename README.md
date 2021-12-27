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
This project aims to assess the performance of popular methods when tested on 2-d test curves with the following properties: smoothness, roughness, and the degree to which a curve occupies its sample space.
 
## Data
![test curves](https://github.com/ninavergara605/dimension_analysis/blob/13db2adb864f48822341ad61d94c55545d40aeb8/images/test_curves.png)
    
The Koch Curve (n=160) was created by Niels Fabian Helge von Koch in 1904, and has a theoretical dimension of ~1.261. This curve is self-affine, meaning its features are scaled differently. Due to the scaleing differences, zooming in on a self-affine curve can reveal details that would otherwise be missed. 
This property isn't readily apparent in this test curve used since a small sample (n=160) is used. The scaling differences present are sufficient to satisfy the requirements of this analysis. 

Two Fractal Brownian Motion (FBM) curves were utilized in this analysis. FBM curves originated from the works of Hurst (1951, 1957, and 1968) and expanded by Mandelbrot and Van Ness (1968), and Mandelbrot and Wallis (1968,1969).
The hurst component (H) is used to modify the roughness of the curve (Mandelbrot & Von Ness, 1968), with the fractal dimension (d) of the curve being : d = 2-H. FBM curves of any dimension exhibit self-similarity. 
The FMB curve with the dimension of 1.2 will be the 'smooth' curve test case, while the curve with a dimension of 1.75 will be the 'rough' curve test case.

Although the Koch curve (d= ~1.261) and FBM curve (d= 1.2) have similar fractal dimensions, the Koch curve occupies a larger region of the sample space. 
The small sample size of the Koch Curve is used to minimize it's self-affine property, which could otherwise effect the accuracy scores of sensitive techniques. Comparing these two curves could offer a (hackish) glimpse into the effectiveness of each technique
on lower dimensional curves with varying space filling properties.

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

### Percent Error

## Conclusions
    

## Repositroy Structure
 ```
├── images                             <- Stores technique performance, distance transforms, and test curve visualizations                                  
├── Minkowski_Bouligand_and_HSM.ipynb  <- Notebook for Minkowski-Bouligand and HSM implemenations
├── box_counting_method.ipynb          <- Notebook for the box counting method
├── test_curve_visualization.ipynb     <- Notebook for FBM curve creation and test curve visualization  
└── README.md                          <- Project description
