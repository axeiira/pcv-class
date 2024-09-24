import cv2 as cv
import numpy as np

def convolve2d(frame, kernel):
    # Get the dimensions of the frame and kernel
    frame_height = frame.shape[0]
    frame_width = frame.shape[1]
    kernel_height = kernel.shape[0]
    kernel_width = kernel.shape[1]
    
    # Output dimensions after applying the kernel (no padding, stride 1)
    output_height = frame_height - kernel_height + 1
    output_width = frame_width - kernel_width + 1
    
    # Create an output array of the appropriate size
    output = np.zeros((output_height, output_width))
    
    # Perform the convolution operation
    for i in range(output_height):
        for j in range(output_width):
            # Element-wise multiplication and sum over the kernel
            output[i, j] = np.sum(frame[i:i+kernel_height, j:j+kernel_width] * kernel)
    
    return output

# Example usage:
frame = cv.imread("test.jpg")
kernel = np.ones((9,9))/81

convolved_frame = convolve2d(frame, kernel)
cv.imshow("window",convolved_frame)
cv.waitKey(0)
