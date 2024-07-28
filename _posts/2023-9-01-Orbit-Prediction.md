	---
layout: post
title: 'Precise and Efficient Orbit Prediction in LEO with Machine Learning using Exogenous Variables'
description: A brief summary on utilizing machine learning for accurate orbit prediction in Low Earth Orbit (LEO).
image: assets/images/iso_earth.png
code:
---
The increasing volume of space objects in Earth's orbit presents a significant challenge for Space Situational Awareness (SSA). Accurate orbit prediction is crucial to anticipate the position and velocity of space objects, for collision avoidance and space debris mitigation. However, conventional propagator methods like the SGP4 inadequately account for non-conservative forces, leading to uncertainty in future positions.

To address this limitation, in the paper we propose an orbit prediction algorithm utilizing machine learning. By leveraging past positions and environmental variables like atmospheric density, the algorithm forecasts the future state vectors on a spacecraft. The study utilizes precision ephemeris data from the International Laser Ranging Service (ILRS) for almost a year, as an initial approach that can, in the future, be generalized to more spacecrafts.
The key element of the paper is that no traditional propagation method was used, meaning that the model is fully able to encode the complex physical phenomenae that affect the spacecraft and forecast a resoanable good estimate in 3 minutes intervals, for 3 days.



<h3>Contributions:</h3>
<ul class="alt">
<li>An advancement in orbit determination by eliminating the reliance on a hybrid error-correction method;</li>
<li>The integration of exogenous variables to capture the effects of non-conservative forces;</li>
<li>The testing in a real world setting with a data-centric approach;</li>
<li>A machine learning model outperforming in error a J2 numerical propagator, using less compute time;</li>
<li>Empirical validation of computational costs.</li>
</ul>


Using a two-layer architecture, the model is able to first, approximate the real future states with a coarse model, and then, in the second layer, independently trained, refine the initial prediction by incorporating covariates.

## Results

The results of the study demonstrate that the machine learning-based orbit prediction algorithm achieves low positioning errors while maintaining a low computational cost. This significant improvement in accuracy and efficiency enhances SSA capabilities, enabling faster and more reliable orbit determination for the growing number of space objects.

## Conclusion

In conclusion, the utilization of machine learning and time-series techniques in orbit prediction offers a promising solution to the challenges posed by the increasing volume of space objects in LEO. The algorithm presented in this paper provides precise and efficient orbit determination, contributing to improved Space Situational Awareness and collision avoidance efforts.

<ul class="actions fit">
						<li><a href= "https://arxiv.org/pdf/2407.11026" class="button special fit">Paper</a></li>
</ul>
<div style="text-align: center;">
    <iframe src="https://drive.google.com/file/d/1iXL7yUqJTIZqNAGXW7zTpYhHdF99S3AA/preview"
            style="display: block; margin: 0 auto;">
    </iframe>
</div>
