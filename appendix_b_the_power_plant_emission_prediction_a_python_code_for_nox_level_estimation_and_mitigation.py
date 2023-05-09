from math import tanh

AMT, AMP, AMH, AFP, GTE, TIT, TAT, TEY, CO = 23.7, 1015.62, 80.1, 4.2, 24.6, 1096.9, 550.0, 11.2, 2.5

scaled_AMT = (AMT - 17.71269989) / 7.447450161
scaled_AMP = (AMP - 1013.070007) / 6.463329792
scaled_AMH = (AMH - 77.86699677) / 14.46140003
scaled_AFP = (AFP - 3.925519943) / 0.7739359736
scaled_GTE = (GTE - 25.56380081) / 4.195960045
scaled_TIT = (TIT - 1081.430054) / 17.53639984
scaled_TAT = (TAT - 546.1589966) / 6.84236002
scaled_TEY = (TEY - 12.06050014) / 1.088799953
scaled_CO = (CO - 2.372469902) / 2.26267004

perceptron_layer_1_output_0 = tanh(-0.380295 + (scaled_AMT * -0.519949) + (scaled_AMP * 0.278811) + (scaled_AMH * 0.00723753) + (scaled_AFP * 0.181552) + (scaled_GTE * 0.457739) + (scaled_TIT * -0.124874) + (scaled_TAT * -0.265811) + (scaled_TEY * -0.315751) + (scaled_CO * 0.00903988))
perceptron_layer_1_output_1 = tanh(1.02069 + (scaled_AMT * 0.00912198) + (scaled_AMP * -0.0443043) + (scaled_AMH * -0.379155) + (scaled_AFP * 0.593596) + (scaled_GTE * 0.328413) + (scaled_TIT * -0.987505) + (scaled_TAT * 1.35337) + (scaled_TEY * 0.882933) + (scaled_CO * -0.175156))
perceptron_layer_1_output_2 = tanh(0.431469 + (scaled_AMT * -0.0999057) + (scaled_AMP * 0.13582) + (scaled_AMH * 0.0109351) + (scaled_AFP * -0.0731824) + (scaled_GTE * 0.516438) + (scaled_TIT * -0.715798) + (scaled_TAT * 0.334144) + (scaled_TEY * -0.442496) + (scaled_CO * -0.369129))
perceptron_layer_1_output_3 = tanh(-0.0981637 + (scaled_AMT * 0.252855) + (scaled_AMP * -0.0125287) + (scaled_AMH * -0.253679) + (scaled_AFP * -0.697587) + (scaled_GTE * -0.157837) + (scaled_TIT * 0.564888) + (scaled_TAT * -1.30342) + (scaled_TEY * -1.34226) + (scaled_CO * 1.5704))
perceptron_layer_1_output_4 = tanh(-0.259476 + (scaled_AMT * -0.470843) + (scaled_AMP * -0.272964) + (scaled_AMH * -0.253526) + (scaled_AFP * 0.377247) + (scaled_GTE * -0.0695821) + (scaled_TIT * -0.379319) + (scaled_TAT * -0.000309811) + (scaled_TEY * -0.142314) + (scaled_CO * -0.169072))
perceptron_layer_1_output_5 = tanh(-0.947733 + (scaled_AMT * 0.43) + (scaled_AMP * -0.0865479) + (scaled_AMH * 0.116354) + (scaled_AFP * -0.0647504) + (scaled_GTE * 0.667274) + (scaled_TIT * 0.654937) + (scaled_TAT * 1.01807) + (scaled_TEY * 0.818052) + (scaled_CO * -0.0773065))
perceptron_layer_1_output_6 = tanh(-1.97194 + (scaled_AMT * 0.481142) + (scaled_AMP * -0.139147) + (scaled_AMH * 0.168919) + (scaled_AFP * 0.0225099) + (scaled_GTE * -0.0823365) + (scaled_TIT * 0.582238) + (scaled_TAT * 0.96622) + (scaled_TEY * -1.07367) + (scaled_CO * 0.0423755))
perceptron_layer_1_output_7 = tanh(-0.654302 + (scaled_AMT * 0.0107965) + (scaled_AMP * -0.218166) + (scaled_AMH * -0.12067) + (scaled_AFP * -0.00605676) + (scaled_GTE * -1.63209) + (scaled_TIT * 2.47512) + (scaled_TAT * -0.703865) + (scaled_TEY * -0.798305) + (scaled_CO * 0.791648))
perceptron_layer_1_output_8 = tanh(0.255455 + (scaled_AMT * 0.10727) + (scaled_AMP * 0.00233202) + (scaled_AMH * 0.38321) + (scaled_AFP * 0.594141) + (scaled_GTE * -0.176241) + (scaled_TIT * 0.900328) + (scaled_TAT * 0.196238) + (scaled_TEY * -0.483133) + (scaled_CO * -1.57369))

perceptron_layer_2_output_0 = (0.187898 + (perceptron_layer_1_output_0 * 1.03729) + (perceptron_layer_1_output_1 * -0.657434) + (perceptron_layer_1_output_2 * 1.47082) + (perceptron_layer_1_output_3 * 0.972752) + (perceptron_layer_1_output_4 * 1.02519) + (perceptron_layer_1_output_5 * 0.83472) + (perceptron_layer_1_output_6 * -1.53002) + (perceptron_layer_1_output_7 * 1.49679) + (perceptron_layer_1_output_8 * 0.923166))

unscaling_layer_output_0 = perceptron_layer_2_output_0 * 11.67840004 + 65.29309845

print("NOx [mg/m³]:", unscaling_layer_output_0)
