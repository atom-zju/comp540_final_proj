import caffe
import numpy as np

blob = caffe.proto.caffe_pb2.BlobProto()
data = open( '/home/atom/caffe/examples/cifar10/mean.binaryproto', 'rb' ).read()
blob.ParseFromString(data)
arr = np.array( caffe.io.blobproto_to_array(blob) )
out = arr[0]
np.save( '/home/atom/caffe/examples/cifar10/mean.cifar10.npy', out)