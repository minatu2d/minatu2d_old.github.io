'''
Softmax Regression using Gradient Formula

'''
import tensorflow as tf

# Import MNIST data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# Parameters
learning_rate = 0.01
training_epochs = 10
batch_size = 100
display_step = 1

# Parameters
learning_rate = 0.01
training_epochs = 10
batch_size = 100
display_step = 1

# tf Graph Input
x = tf.placeholder(tf.float32, [None, 784]) # mnist data image of shape 28*28=784
y = tf.placeholder(tf.float32, [None, 10]) # 0-9 digits recognition => 10 classes

# Set model weights
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# Construct model
pred = tf.nn.softmax(tf.matmul(x, W)) # Softmax

# Minimize error using cross entropy
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), reduction_indices=1))


W_grad =  - tf.matmul ( tf.transpose(x) , y - pred) 
b_grad = - tf.reduce_mean( tf.matmul(tf.transpose(x), y - pred), reduction_indices=0)

new_W = W.assign(W - learning_rate * W_grad)
new_b = b.assign(b - learning_rate * b_grad)

init = tf.global_variables_initializer()


with tf.Session() as sess:
    sess.run(init)

    # Training cycle
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples/batch_size)
        # Loop over all batches
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            # Fit training using batch data
            _, _, c = sess.run([new_W, new_b, cost], feed_dict={x: batch_xs, y: batch_ys})
            
        
            # Compute average loss
            avg_cost += c / total_batch
        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            print ("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost))

    print ("Optimization Finished!")

    # Test model
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    # Calculate accuracy for 3000 examples
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print ("Accuracy:", accuracy.eval({x: mnist.test.images[:3000], y: mnist.test.labels[:3000]}))
    
    
# Output
# Extracting /tmp/data/train-images-idx3-ubyte.gz
# Extracting /tmp/data/train-labels-idx1-ubyte.gz
# Extracting /tmp/data/t10k-images-idx3-ubyte.gz
# Extracting /tmp/data/t10k-labels-idx1-ubyte.gz
# Epoch: 0001 cost= 0.432943137
# Epoch: 0002 cost= 0.330031527
# Epoch: 0003 cost= 0.313661941
# Epoch: 0004 cost= 0.306443773
# Epoch: 0005 cost= 0.300219418
# Epoch: 0006 cost= 0.298976618
# Epoch: 0007 cost= 0.293222957
# Epoch: 0008 cost= 0.291407861
# Epoch: 0009 cost= 0.288372261
# Epoch: 0010 cost= 0.286749691
# Optimization Finished!
# Accuracy: 0.898
