import numpy as np

def forward_error(true_value, approx_value):
    return abs(true_value - approx_value)

def backward_error(function, approx_value):
    return abs(function(approx_value))

def main():
    func = lambda x: 1 - np.cos(x)
    root = 0
    rad = 1
    approx_root = 1.0E-4 * rad

    forward_err = forward_error(root, approx_root)
    backward_err = backward_error(func, approx_root)

    print("Forward Error: {:.10f}".format(forward_err))
    print("Backward Error: {:.10f}".format(backward_err))

    return 0

if __name__ == '__main__':
    main()
