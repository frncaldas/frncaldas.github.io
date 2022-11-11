---
layout: post
title: 'A Temporal Fusion Transformer for Long-term
Explainable Prediction of Emergency
Department Overcrowding'
description: Using a Deep Learning model to forecast Emergency Departments affluence in Portugal
image: assets/images/urgencias2.jpg
code:
---

Emergency Departments (EDs) are a fundamental element of the Portuguese National Health Service, serving as an entry point for users with diverse and very serious medical problems. Due to the inherent characteristics of the ED, forecasting the number of patients using the services is particularly challenging. And a mismatch between the affluence and the number of medical professionals can lead to a decrease in the quality of the services provided and create problems that have repercussions for the entire hospital, with the requisition of health care workers from other departments and the postponement of surgeries.

ED overcrowding is driven, in part, by non-urgent patients, that resort to emergency services despite not having a medical emergency and which represent almost half of the total number of daily patients. This paper describes a novel deep learning architecture, the Temporal Fusion Transformer, that uses calendar and time-series covariates to forecast prediction intervals and point predictions for a 4 week period. We have concluded that patient volume can be forecasted with a Mean Absolute Percentage Error (MAPE) of 9.87%  for Portugal’s Health Regional Areas (HRA) and a Root Mean Squared Error (RMSE) of 178 people/day. The paper shows empirical evidence supporting the use of a multivariate approach with static and time-series covariates while surpassing other models commonly found in the literature.

In the future, this model can increase in granularity, forecasting at the hospital level instead of aggregated values by HRAs. Although a greater challenge, due to the increased noise and randomness that comes from the decrease in the study population, we expect that the combination of a large number of time-series could improve the robustness and global quality of the model, specifically if we add more relevant static variables. Furthermore, at the hospital level, some new variables can be introduced, representing the socio-economic characterisation of the patient population.

<ul class="actions fit">
						<li><a href= "https://arxiv.org/abs/2207.00610?context=cs" class="button special fit">Paper</a></li>
						{% if page.code != null %}
						<li><a href="#" class="button fit">Code</a></li>
						{% endif %}
						{% if page.code == null %}
						<li><a href="#" class=" button fit disabled">Code</a></li>
						{% endif %}
						</ul>

<!--<sub>Image from ''Urgências do Hospital S. João do Porto'' © David Tiago/Global Imagens</sub> -->
