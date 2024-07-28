layout: post
title: 'Precise and Efficient Orbit Prediction in LEO with Machine Learning using Exogenous Variables'
description: A brief summary on utilizing machine learning for accurate orbit prediction in Low Earth Orbit (LEO).
image: assets/images/iso_earth.png
---

The increasing volume of space objects in Earth's orbit presents a significant challenge for Space Situational Awareness (SSA). Accurate orbit prediction is crucial to anticipate the position and velocity of space objects for collision avoidance and space debris mitigation. However, conventional propagator methods like the SGP4 inadequately account for non-conservative forces, leading to uncertainty in future positions.

To address this limitation, in the paper we propose an orbit prediction algorithm utilizing machine learning. By leveraging past positions and environmental variables like atmospheric density, the algorithm forecasts the future state vectors of a spacecraft. The study utilizes precision ephemeris data from the International Laser Ranging Service (ILRS) for almost a year, as an initial approach that can, in the future, be generalized to more spacecraft.

The key element of the paper is that no traditional propagation method was used, meaning that the model is fully able to encode the complex physical phenomena that affect the spacecraft and forecast a reasonably good estimate in 3-minute intervals for 3 days.

### Contributions:

- An advancement in orbit determination by eliminating the reliance on a hybrid error-correction method;
- The integration of exogenous variables to capture the effects of non-conservative forces;
- Testing in a real-world setting with a data-centric approach;
- A machine learning model outperforming in error a J2 numerical propagator, using reduced computational time;
- Empirical validation of computational costs.

![Machine Learning](assets/images/model.jpg)

Using a two-layer architecture, the model is able to first, approximate the real future states with a coarse model, and then, in the second layer, independently trained, refine the initial prediction by incorporating covariates.

## Results

The results of the study demonstrate that the machine learning-based orbit prediction algorithm achieves low positioning errors while maintaining a low computational cost. This significant improvement in accuracy and efficiency enhances SSA capabilities, enabling faster and more reliable orbit determination for the growing number of space objects.

## Conclusion

In conclusion, the utilization of machine learning and time-series techniques in orbit prediction offers a promising solution to the challenges posed by the increasing volume of space objects in LEO. The algorithm presented in this paper provides precise and efficient orbit determination, contributing to improved Space Situational Awareness and collision avoidance efforts.

![Space Debris](assets/images/space-debris.jpg)
*Image source: [Unsplash](https://unsplash.com/photos/123458)*
