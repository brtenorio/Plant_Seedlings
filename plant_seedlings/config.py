
# set a random state number
rs = 42

# set the path for the data base containing the images
file_path = "/Users/brncat/Downloads/AltaVerde/GitHub/seeds_db/"


# Define paths
main_dir = file_path+'main'
train_dir = file_path+'train'
val_dir = file_path+'valid'
test_dir = file_path+'test'

# Define split ratios
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

num_classes = 12

image_resize = 224

batch_size_training = 8
batch_size_validation = 8

num_epochs = 5

