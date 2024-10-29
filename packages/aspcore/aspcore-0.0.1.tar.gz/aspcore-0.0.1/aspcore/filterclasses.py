"""A collection of classes implementing linear convolution. 

The functionality offered beyond what is available in numpy and scipy is
inherent support for MIMO filters in different forms, as well as
streaming filtering, where only a part of the signal is known at a time. 
It is also possible to filter with a time-varying impulse response.

The classes are JIT compiled using numba's experimental jitclass to keep
computational cost low.

The main function of the module is create_filter, which constructs the appropriate 
filter object according to the chosen parameters. The only required parameters is
either an impulse response or the dimensions of the impulse response. In the 
latter case, the impulse response is initialized to zero.
"""
import numpy as np
import itertools as it

import aspcore.freqdomainfiltering as fdf
import aspcore.filterclassesdynamic as fcd
import scipy.signal as spsig
import numba as nb



def create_filter(
    ir=None, 
    num_in=None, 
    num_out=None, 
    ir_len=None, 
    broadcast_dim=None, 
    sum_over_input=True, 
    dynamic=False):
    """
    Returns the appropriate filter object for the desired use.

    All filters has a method called process which takes one parameter 
    signal : ndarray of shape (num_in, num_samples)
    and returns an ndarray of shape (out_dim, num_samples), where 
    out_dim depends on which filter. 

    Either ir must be provided or num_in, num_out and ir_len. In the
    latter case, the filter coefficients are initialized to zero.  

    Parameters
    ----------
    ir : ndarray of shape (num_in, num_out, ir_len)
    num_in : int
        the number of input channels
    num_out : int
        the number of output channels
    ir_len : int
        the length of the impulse response
    broadcast_dim : int
        Supply this value if the filter should be applied to more than one set of signals
        at the same time. 
    sum_over_input : bool
        Choose true to sum over the input dimension after filtering. For a canonical MIMO
        system choose True, for example when simulating sound in a space with multiple 
        loudspeakers.
        Choose False otherwise, in which case filter.process will return a ndarray of 
        shape (num_in, num_out, num_samples)
    dynamic : bool
        Choose true to use a convolution specifically implemented for time-varying systems.
        More accurate, but takes more computational resources. 

    Returns
    -------
    filter : Appropriate filter class from this module
    """
    if num_in is not None and num_out is not None and ir_len is not None:
        assert ir is None
        ir = np.zeros((num_in, num_out, ir_len))

    if ir is not None:
        #assert numIn is None and numOut is None and irLen is None
        if broadcast_dim is not None:
            if dynamic:
                raise NotImplementedError
            if sum_over_input:
                raise NotImplementedError
            assert ir.ndim == 3 and isinstance(broadcast_dim, int) # A fallback to non-numba MD-filter can be added instead of assert
            return FilterBroadcast(broadcast_dim, ir)
        
        if sum_over_input:
            if dynamic:
                return fcd.FilterSumDynamic(ir)
            return FilterSum(ir)
        return FilterNosum(ir)

spec_filtersum = [
    ("ir", nb.float64[:,:,:]),
    ("num_in", nb.int32),
    ("num_out", nb.int32),
    ("ir_len", nb.int32),
    ("buffer", nb.float64[:,:]),
]
@nb.experimental.jitclass(spec_filtersum)
class FilterSum:
    """A class for implementing an LTI MIMO system. 

    The input dimension will be summed over. 
    The signal can be processed in chunks of arbitrary size, and the
    internal buffer will be updated accordingly.

    Parameters
    ----------
    ir : ndarray of shape (num_in, num_out, ir_len)
        The impulse response of the filter
    """
    def __init__(self, ir):
        self.ir = ir
        self.num_in = ir.shape[0]
        self.num_out = ir.shape[1]
        self.ir_len = ir.shape[2]
        self.buffer = np.zeros((self.num_in, self.ir_len - 1))

    def process(self, data_to_filter):
        """Filter the data with the impulse response.
        
        Parameters
        ----------
        data_to_filter : ndarray of shape (num_in, num_samples)
            The data to be filtered
        
        Returns
        -------
        filtered : ndarray of shape (num_out, num_samples)
            The filtered data
        """
        num_samples = data_to_filter.shape[-1]
        buffered_input = np.concatenate((self.buffer, data_to_filter), axis=-1)

        filtered = np.zeros((self.num_out, num_samples))
        for out_idx in range(self.num_out):
            for i in range(num_samples):
                filtered[out_idx,i] += np.sum(self.ir[:,out_idx,:] * np.fliplr(buffered_input[:,i:self.ir_len+i]))

        self.buffer[:, :] = buffered_input[:, buffered_input.shape[-1] - self.ir_len + 1 :]
        return filtered


spec_filtermd = [
    ("ir", nb.float64[:,:,:]),
    ("ir_dim1", nb.int32),
    ("ir_dim2", nb.int32),
    ("ir_len", nb.int32),
    ("data_dims", nb.int32),
    ("buffer", nb.float64[:,:]),
]
@nb.experimental.jitclass(spec_filtermd)
class FilterBroadcast:
    """Filters all channels of the input signal with all channels of the impulse response.
    
    Parameters
    ----------
    data_dims : int
        The number of channels of the input signal
    ir : ndarray of shape (ir_dim1, ir_dim2, ir_len)
        The impulse response of the filter
    """
    def __init__(self, data_dims, ir):
        self.ir = ir
        self.ir_dim1 = ir.shape[0]
        self.ir_dim2 = ir.shape[1]
        self.ir_len = ir.shape[-1]
        self.data_dims = data_dims

        self.buffer = np.zeros((self.data_dims, self.ir_len - 1))

    def process(self, data_to_filter):
        """Filters all input channels with all impulse response channels.
        
        Parameters
        ----------
        data_to_filter : ndarray of shape (data_dims, num_samples)
            The data to be filtered
        
        Returns
        -------
        filtered : ndarray of shape (data_dims, dim1, dim2, num_samples)
            The filtered data
        """
        num_samples = data_to_filter.shape[-1]

        buffered_input = np.concatenate((self.buffer, data_to_filter), axis=-1)
        filtered = np.zeros((self.ir_dim1, self.ir_dim2, self.data_dims, num_samples))

        for i in range(num_samples):
            filtered[:, :, :,i] = np.sum(np.expand_dims(self.ir,2) * \
                    np.expand_dims(np.expand_dims(np.fliplr(buffered_input[:,i:self.ir_len+i]),0),0),axis=-1)

        self.buffer[:, :] = buffered_input[:, -self.ir_len + 1:]
        return filtered



class FilterNosum:
    """Filters a signal with a MIMO filter without summing over the input dimension.
    
    Is essentially equivalent to FilterBroadcast with ir_dims1=1, 
    although this can be more convenient to use in some cases.

    Is not JIT compiled, and is therefore generally slower than FilterBroadcast
    and FilterSum.

    Parameters
    ----------
    ir : ndarray of shape (num_in, num_out, ir_len)
        The impulse response of the filter
    """

    def __init__(self, ir=None, ir_len=None, num_in=None, num_out=None):
        if ir is not None:
            self.ir = ir
            self.num_in = ir.shape[0]
            self.num_out = ir.shape[1]
            self.ir_len = ir.shape[2]
        elif (ir_len is not None) and (num_in is not None) and (num_out is not None):
            self.ir = np.zeros((num_in, num_out, ir_len))
            self.ir_len = ir_len
            self.num_in = num_in
            self.num_out = num_out
        else:
            raise Exception("Not enough constructor arguments")
        self.buffer = np.zeros((self.num_in, self.ir_len - 1))

    def process(self, data_to_filter):
        """Filter the data with the impulse response.

        Parameters
        ----------
        data_to_filter : ndarray of shape (num_in, num_samples)
            The data to be filtered
        
        Returns
        -------
        filtered : ndarray of shape (num_in, num_out, num_samples)
            The filtered data   
        """
        num_samples = data_to_filter.shape[-1]
        buffered_input = np.concatenate((self.buffer, data_to_filter), axis=-1)

        filtered = np.zeros((self.num_in, self.num_out, num_samples))
        if num_samples > 0:
            for in_idx, out_idx in it.product(range(self.num_in), range(self.num_out)):
                filtered[in_idx, out_idx, :] = spsig.convolve(
                    self.ir[in_idx, out_idx, :], buffered_input[in_idx, :], "valid"
                )

            self.buffer[:, :] = buffered_input[:, buffered_input.shape[-1] - self.ir_len + 1 :]
        return filtered


class FilterMD_slow_fallback:
    """Equivalent to FilterBroadcast, but can handle arbitrary number of dimensions.

    Is not JIT compiled, and is therefore generally slower than FilterBroadcast

    Parameters
    ----------
    data_dims : tuple of ints
        The number of channels of the input signal
    ir : ndarray of shape (ir_dim1, ir_dim2, ..., ir_dimN, ir_len)
        The impulse response of the filter    
    """
    def __init__(self, data_dims, ir=None, ir_len=None, ir_dims=None):
        if ir is not None:
            self.ir = ir
            self.ir_len = ir.shape[-1]
            self.ir_dims = ir.shape[0:-1]
        elif (ir_len is not None) and (ir_dims is not None):
            self.ir = np.zeros(ir_dims + (ir_len,))
            self.ir_len = ir_len
            self.ir_dims = ir_dims
        else:
            raise Exception("Not enough constructor arguments")

        if isinstance(data_dims, int):
            self.data_dims = (data_dims,)
        else:
            self.data_dims = data_dims

        self.output_dims = self.ir_dims + self.data_dims
        self.num_data_dims = len(self.data_dims)
        self.num_ir_dims = len(self.ir_dims)
        self.buffer = np.zeros(self.data_dims + (self.ir_len - 1,))

    def process(self, data_to_filter):
        """Filters all input channels with all impulse response channels.

        Parameters
        ----------
        data_to_filter : ndarray of shape (b0, b1, ..., bn, num_samples)
            The data to be filtered

        Returns
        -------
        filtered : ndarray of shape (a0, a1, ..., an, b0, b1, ..., bn, num_samples)
            The filtered data
        """
        num_samples = data_to_filter.shape[-1]

        buffered_input = np.concatenate((self.buffer, data_to_filter), axis=-1)
        filtered = np.zeros(self.ir_dims + self.data_dims + (num_samples,))

        for idxs in it.product(*[range(d) for d in self.output_dims]):
            filtered[idxs + (slice(None),)] = spsig.convolve(
                self.ir[idxs[0 : self.num_ir_dims] + (slice(None),)],
                buffered_input[idxs[-self.num_data_dims :] + (slice(None),)],
                "valid",
            )

        self.buffer[..., :] = buffered_input[..., -self.ir_len + 1 :]
        return filtered


















class FilterBroadcastFreq:
    """ir is the time domain impulse response, with shape (a0, a1,..., an, irLen)
    tf is frequency domain transfer function, with shape (2*irLen, a0, a1,..., an),

    input of filter function is shape (b0, b1, ..., bn, irLen)
    output of filter function is shape (a0,...,an,b0,...,bn,irLen)

    dataDims must be provided, which is a tuple like (b0, b1, ..., bn)
    filtDim is (a0, a1,..., an) and must then be complemented with irLen or numFreq
    If you give to many arguments, it will propritize tf -> ir -> numFreq -> irLen"""

    def __init__(
        self, data_dims, tf=None, ir=None, filt_dim=None, ir_len=None, num_freq=None
    ):
        # assert(tf or ir or (numIn and numOut and irLen) is not None)
        if tf is not None:
            assert tf.shape[0] % 2 == 0
            self.tf = tf
        elif ir is not None:
            self.tf = fdf.fft_transpose(
                np.concatenate((ir, np.zeros_like(ir)), axis=-1)
            )
        elif filt_dim is not None:
            if num_freq is not None:
                self.tf = np.zeros((num_freq, *filt_dim), dtype=complex)
            elif ir_len is not None:
                self.tf = np.zeros((2 * ir_len, *filt_dim), dtype=complex)
        else:
            raise ValueError("Arguments missing for valid initialization")

        if isinstance(data_dims, int):
            self.data_dims = (data_dims,)
        else:
            self.data_dims = data_dims

        self.ir_len = self.tf.shape[0] // 2
        self.num_freq = self.tf.shape[0]
        self.filt_dim = self.tf.shape[1:]

        self.buffer = np.zeros((*self.data_dims, self.ir_len))

    def process(self, samples_to_process):
        assert samples_to_process.shape == (*self.data_dims, self.ir_len)
        output_samples = fdf.convolve_euclidian_ft(
            self.tf, np.concatenate((self.buffer, samples_to_process), axis=-1)
        )

        self.buffer[...] = samples_to_process
        return output_samples

    def process_freq(self, freqs_to_process):
        """Can be used if the fft of the input signal is already available.
        Assumes padding is already applied correctly."""
        assert freqs_to_process.shape == (self.num_freq, *self.data_dims)
        output_samples = fdf.convolve_euclidian_ff(self.tf, freqs_to_process)

        self.buffer[...] = fdf.ifft_transpose(freqs_to_process, remove_empty_dim=False)[
            ..., self.ir_len :
        ]
        return output_samples

class FilterSumFreq:
    """ir is the time domain impulse response, with shape (numIn, numOut, irLen)
    tf is frequency domain transfer function, with shape (2*irLen, numOut, numIn),
    it is also possible to only provide the dimensions of the filter, numIn and numOut,
    together with either number of frequencies or ir length, where 2*irLen==numFreq
    dataDims is extra dimensions of the data to broadcast over. Input should then be
    with shape (*dataDims, numIn, numSamples), output will be (*dataDims, numOut, numSamples)

    If you give to many arguments, it will propritize tf -> ir -> numFreq -> irLen"""

    def __init__(
        self,
        tf=None,
        ir=None,
        num_in=None,
        num_out=None,
        ir_len=None,
        num_freq=None,
        data_dims=None,
    ):
        if tf is not None:
            assert all(arg is None for arg in [ir, num_in, num_out, ir_len, num_freq])
            assert tf.ndim == 3
            assert tf.shape[0] % 2 == 0
            self.tf = tf
        elif ir is not None:
            assert all(arg is None for arg in [tf, num_in, num_out])
            if ir_len is not None:
                assert num_freq is None
                tot_len = ir_len*2
            elif num_freq is not None:
                assert ir_len is None
                tot_len = num_freq
            else:
                tot_len = 2*ir.shape[-1]

            self.tf = np.transpose(
                np.fft.fft(np.concatenate((ir, np.zeros(ir.shape[:-1]+(tot_len-ir.shape[-1],))), axis=-1), axis=-1),
                (2, 1, 0),
            )

            # self.tf = np.transpose(
            #     np.fft.fft(np.concatenate((ir, np.zeros_like(ir)), axis=-1), axis=-1),
            #     (2, 1, 0),
            # )
        elif num_in is not None and num_out is not None:
            assert all(arg is None for arg in [tf, ir])
            if num_freq is not None:
                self.tf = np.zeros((num_freq, num_out, num_in), dtype=complex)
            elif ir_len is not None:
                self.tf = np.zeros((2 * ir_len, num_out, num_in), dtype=complex)
        else:
            raise ValueError("Arguments missing for valid initialization")

        self.ir_len = self.tf.shape[0] // 2
        self.num_freq = self.tf.shape[0]
        self.num_out = self.tf.shape[1]
        self.num_in = self.tf.shape[2]

        if data_dims is not None:
            if isinstance(data_dims, int):
                self.data_dims = (data_dims,)
            else:
                self.data_dims = data_dims
            self.len_data_dims = len(self.data_dims)
            self.buffer = np.zeros((*self.data_dims, self.num_in, self.ir_len))
        else:
            self.buffer = np.zeros((self.num_in, self.ir_len))
            self.len_data_dims = 0

    def process(self, samples_to_process):
        assert samples_to_process.shape == self.buffer.shape
        freqs_to_process = fdf.fft_transpose(
            np.concatenate((self.buffer, samples_to_process), axis=-1), add_empty_dim=True
        )
        tf_new_shape = self.tf.shape[0:1] + (1,) * self.len_data_dims + self.tf.shape[1:]
        output_samples = fdf.ifft_transpose(
            self.tf.reshape(tf_new_shape) @ freqs_to_process, remove_empty_dim=True
        )

        self.buffer[...] = samples_to_process
        return np.real(output_samples[..., self.ir_len :])

    def process_freq(self, freqs_to_process):
        """Can be used if the fft of the input signal is already available.
        Assumes padding is already applied correctly."""
        assert freqs_to_process.shape == (self.num_freq, self.num_in, 1)
        tf_new_shape = self.tf.shape[0:1] + (1,) * self.len_data_dims + self.tf.shape[1:]
        output_samples = fdf.ifft_transpose(
            self.tf.reshape(tf_new_shape) @ freqs_to_process, remove_empty_dim=True
        )

        self.buffer[...] = fdf.ifft_transpose(freqs_to_process, remove_empty_dim=True)[
            ..., self.ir_len :
        ]
        return np.real(output_samples[..., self.ir_len :])

    def process_without_sum(self, samples_to_process):
        assert samples_to_process.shape == self.buffer.shape
        freqs_to_process = fdf.fft_transpose(
            np.concatenate((self.buffer, samples_to_process), axis=-1), add_empty_dim=True)
        tf_new_shape = self.tf.shape[0:1] + (1,) * self.len_data_dims + self.tf.shape[1:]
        output_samples = fdf.ifft_transpose(
            np.swapaxes(self.tf.reshape(tf_new_shape),-1,-2) * freqs_to_process)

        self.buffer[...] = samples_to_process
        return np.real(output_samples[..., self.ir_len :])

    def process_euclidian(self, samples_to_process):
        """Will filter every channel of the input with every channel of the filter
            outputs shape (filt0)"""
        #assert dataDims is not None
        raise NotImplementedError

    def set_ir(self, ir_new):
        assert ir_new.shape == (self.num_in, self.num_out, self.ir_len)
        self.tf = np.transpose(
                np.fft.fft(np.concatenate((ir_new, np.zeros_like(ir_new)), axis=-1), axis=-1),
                (2, 1, 0),
            )
