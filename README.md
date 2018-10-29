# DRAW_pytorch
DRAW: A Recurrent Neural Network For Image Generation(https://arxiv.org/pdf/1502.04623.pdf)

<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/suhoy901/DRAW_pytorch/master/asset/image_01.png"/></td>
    <td><img src="https://raw.githubusercontent.com/suhoy901/DRAW_pytorch/master/asset/image_02.png"/></td>
    <td><img src="https://raw.githubusercontent.com/suhoy901/DRAW_pytorch/master/asset/image_03.png"/></td>
  </tr>
</table>

## Result
 - attention

| Loss | Ground truth |
|:---:|:---:| 
|<img src="https://raw.githubusercontent.com/suhoy901/DRAW_pytorch/master/save_results/MNIST/DRAW/DRAW_loss.png" alt="loss">|<img src="https://raw.githubusercontent.com/suhoy901/DRAW_pytorch/master/save_results/MNIST/DRAW/example.png" alt="groundtruth">|


| Timestep | Generated | Timestep | Generated |
|:---:|:---:|:---:|:---:| 
|3000|<img src="https://raw.githubusercontent.com/suhoy901/DRAW_pytorch/master/save_results/MNIST/DRAW/count_3000_test_total.gif" alt="3000"/>|6000|<img src="https://raw.githubusercontent.com/suhoy901/DRAW_pytorch/master/save_results/MNIST/DRAW/count_6000_test_total.gif" alt="6000"/>|
|24000|<img src="https://raw.githubusercontent.com/suhoy901/DRAW_pytorch/master/save_results/MNIST/DRAW/count_24000_test_total.gif" alt="24000"/>|27000|<img src="https://raw.githubusercontent.com/suhoy901/DRAW_pytorch/master/save_results/MNIST/DRAW/count_27000_test_total.gif" alt="27000"/>|

## References
* https://github.com/vivanov879/draw
* https://github.com/chenzhaomin123/draw_pytorch
