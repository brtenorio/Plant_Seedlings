from config import *
from data_generator import *
from train_cnn import *

def evaluate_cnn():
    model = train_cnn() 
    test_generator.reset()
    eval = model.evaluate(test_generator)
    return eval

def evaluate_vgg():
    model = train_vgg()
    test_generator.reset()
    eval = model.evaluate(test_generator)
    return eval

if __name__ == "__main__":
    eval = evaluate_cnn()
    print('Test loss: ', eval[0])
    print('Test Accuracy: ', eval[1])