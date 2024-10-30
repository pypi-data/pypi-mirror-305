#ifndef METHODS_H
#define METHODS_H

#include "Float_tensor.h"

//helper functions
void cal_stride(int* shape, int* stride, int dim);
void broadcast_stride(int* shape, int* stride, int* r_stride1, int dim, int max_dim);
int broadcast_shape(int* shape1, int dim1, int* shape2, int dim2, int *ans);
void display_tensor(FloatTensor *tensor);
int matmul_broadcast_shape(int dim1, int dim2, int* shape1, int* shape2, int* shape3);
void matmul2d(float* data1, float* data2, float* ans_data, int I_shape, int J_shape, int K_shape);
void transpose2d(float* src_matrix, float* dst_matrix, int rows, int cols);

//initalization
FloatTensor* init_tensor(float *data, int *shape, int dim);

//oprations
FloatTensor* add_tensor(FloatTensor* tensor1, FloatTensor* tensor2);
FloatTensor* mul_ele_tensor(FloatTensor* tensor1, FloatTensor* tensor2);
FloatTensor* pow_tensor(FloatTensor* tenosr1, float num);
FloatTensor* pow_two_tensor(FloatTensor* tensor1, FloatTensor* tenso2);

// matrix
FloatTensor* matmulNd(FloatTensor* tensor1, FloatTensor* tensor2);
FloatTensor* transposeNd(FloatTensor* input_tensor);

//random number methods
FloatTensor* random_tensor(int *shape, int ndim,int min, int max, int seed);
FloatTensor* random_tensor_n(int *shape, int ndim, int seed);
#endif