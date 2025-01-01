

The funamdnental unit of the nueral network is the neuron. You can make 1000x imporvements by improvming that fundamental unit.

There needs to be some aspect of time. will be a complete game changer

One idea is to use the error signal


 (w*x + b) + temporal_bias
 
 backprop = e

 w += -0.0001 * e
 b += -0.0001 * e

temporal_bias = k*e - k*e_dot + k*sum(e)

This type of neural network, can directly be used for motor control!!!


 https://www.sciencedirect.com/science/article/abs/pii/S0168169923005136

 Time-series data.

 There is a strong coorelation between previous prediction error and current prediction

 We are trying to track reality.

https://link.springer.com/chapter/10.1007/978-3-642-53932-9_28