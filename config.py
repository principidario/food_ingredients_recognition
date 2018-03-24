def load_parameters():
    """
        Loads the defined parameters
    """

    # Input data params
    #DATA_ROOT_PATH = '/root/sharedfolder/multimodal_keras_wrapper-0.7/data/sample_data/' # Root path to the data
    #DATA_ROOT_PATH = '/root/sharedfolder/Ingredients101/'
    #DATA_ROOT_PATH = '/root/sharedfolder/Recipes5k/'
    DATA_ROOT_PATH = '/media/HDD3TB/datasets/Recipes1M/'
    CLASSIFICATION_TYPE = 'multi-label' # 'single-label' or 'multi-label'


    if CLASSIFICATION_TYPE == 'single-label':

        DATASET_NAME = 'Food_Recognition'  # Dataset name
        NUM_CLASSES = 2  # number of labels/classes of the dataset
        CLASSES_PATH = 'Annotations/classes.txt'

        IMG_FILES = {'train': 'Annotations/train.txt',  # Images files
                     'val': 'Annotations/val.txt',
                     'test': 'Annotations/test.txt'
                    }
        LABELS_FILES = {'train': 'Annotations/train_labels.txt',  # Labels files
                        'val': 'Annotations/val_labels.txt',
                        'test': 'Annotations/test_labels.txt',
                        }

        # Evaluation
        METRICS = ['multiclass_metrics']  # Metric used for evaluating model
        STOP_METRIC = 'accuracy'  # Metric for the stop

        CLASSIFIER_ACTIVATION = 'softmax'  # 'softmax', 'sigmoid' (multi-label?), etc.
        LOSS = 'categorical_crossentropy'  # 'categorical_crossentropy' (better for sparse labels), 'binary_crossentropy', etc.

    elif CLASSIFICATION_TYPE == 'multi-label':

        if 'Ingredients101' in DATA_ROOT_PATH:
            DATASET_NAME = 'Food_Ingredients101'  # Dataset name
            NUM_CLASSES = 446 # 13  # number of labels/classes of the dataset
            CLASSES_PATH = 'Annotations/ingredients.txt'

            IMG_FILES = {'train': 'Annotations/train_split.txt',  # Images files
                         'val': 'Annotations/val_split.txt',
                         'test': 'Annotations/test.txt'
                        }
            LABELS_FILES = {'train': 'Annotations/train_labels.txt',  # Labels files
                            'val': 'Annotations/val_labels.txt',
                            'test': 'Annotations/test_labels.txt',
                            }
            
        elif 'Recipes5k' in DATA_ROOT_PATH:
            DATASET_NAME = 'Food_Recipes5k'  # Dataset name
            #NUM_CLASSES = 3213  # number of labels/classes of the dataset
            NUM_CLASSES = 1013  # number of labels/classes of the dataset
            #CLASSES_PATH = 'Annotations/ingredients_Recipes5k.txt'
            CLASSES_PATH = 'Annotations/ingredients_simplified_Recipes5k.txt'

            IMG_FILES = {'train': 'Annotations/train_images.txt',  # Images files
                         'val': 'Annotations/val_images.txt',
                         'test': 'Annotations/test_images.txt'
                        }
            LABELS_FILES = {'train': 'Annotations/train_labels.txt',  # Labels files
                            'val': 'Annotations/val_labels.txt',
                            'test': 'Annotations/test_labels.txt',
                            }

        elif 'Recipes1M' in DATA_ROOT_PATH:
            DATASET_NAME = 'Food_Recipes1M'  # Dataset name
            #NUM_CLASSES = 18252  # 286 for the small dataset and 18252 for the full dataset.
            #NUM_CLASSES = 2947  # 2947 ingredients, after running clean_ingredients.py.
            #NUM_CLASSES = 4257  # 4257 luego de pasar los tres scripts de limpieza. Tuve que rehacer porque el script clean_ingredients es malo
            NUM_CLASSES = 1243#4248
            #NUM_CLASSES = 2
            #CLASSES_PATH = 'Annotations/ingredients_Recipes1M.txt'
            #CLASSES_PATH = 'Annotations/ingredients_simplified_Recipes1M.txt'
            CLASSES_PATH = 'Annotations/ingredients_third_clean.test.txt'
            #CLASSES_PATH = 'Annotations/ingredients_equal.txt'
            '''
            IMG_FILES = {'train': 'Annotations/train_i.txt',  # Images files
                         'val': 'Annotations/val_i.txt',
                         'test': 'Annotations/test_i.txt'
                        }
            LABELS_FILES = {'train': 'Annotations/train_l.txt',  # Labels files
                            'val': 'Annotations/val_l.txt',
                            'test': 'Annotations/test_l.txt'
                            }
            '''
            IMG_FILES = {'train': 'Annotations/train_images.clean.test.txt',  # Images files
                         'val': 'Annotations/val_images.clean.test.txt',
                         'test': 'Annotations/test_images.clean.test.txt'
                        }
            LABELS_FILES = {'train': 'Annotations/train_labels.clean.test.txt',  # Labels files
                            'val': 'Annotations/val_labels.clean.test.txt',
                            'test': 'Annotations/test_labels.clean.test.txt'
                            }
        # Evaluation
        METRICS = ['multilabel_metrics']  # Metric used for evaluating model after each epoch. Possible values: 'multiclass' (see more information in utils/evaluation.py
        #STOP_METRIC = 'average precision'
        STOP_METRIC = 'f1'

        MIN_PRED_VAL = 0.5
        
        CLASSIFIER_ACTIVATION = 'sigmoid'  # 'softmax', 'sigmoid' (multi-label?), etc.
        LOSS = 'binary_crossentropy'  # 'categorical_crossentropy' (better for sparse labels), 'binary_crossentropy', etc.


    NETWORK_TYPE = 'Inception' # 'TestModel' for testing, 'Arch_D' for SOTA comparison

    if NETWORK_TYPE == 'Inception':
        # InceptionV3
        IMG_SIZE = [342, 342, 3]
        #IMG_SIZE = [3,342, 342]
        IMG_SIZE_CROP = [299, 299, 3]
        #IMG_SIZE_CROP = [3,299, 299]
        INPUTS_IDS_MODEL = ['input_1']

        INPUTS_MAPPING = {'input_1': 0}

    elif NETWORK_TYPE == 'VGG16' or NETWORK_TYPE == 'TestModel' or NETWORK_TYPE == 'ResNet50' or NETWORK_TYPE == 'Arch_D':

        IMG_SIZE = [256, 256, 3] # resize applied to the images
        IMG_SIZE_CROP = [224, 224, 3] # input size of the network (images will be cropped if DATA_AUGMENTATION==True)
        INPUTS_IDS_MODEL = ['image']  # Corresponding inputs of the built model

        INPUTS_MAPPING = {'image': 0}

    # Dataset parameters
    INPUTS_IDS_DATASET = ['image']  # Corresponding inputs of the dataset

    OUTPUTS_IDS_DATASET = ['ingredients']  # Corresponding outputs of the dataset
    OUTPUTS_IDS_MODEL = ['ingredients']  # Corresponding outputs of the built model
    OUTPUTS_MAPPING = {'ingredients': 0}

    MEAN_IMAGE = [104.0067, 116.6690, 122.6795] # image mean on the RGB channels of the training data

    
    if NETWORK_TYPE == 'Arch_D':
        # Additional data
        DATASET_NAME = 'Food_and_Ingredients_Ingredients101'  # Dataset name

        LABELS_FILES_FOOD = {'train': 'Annotations/train_labels.txt',  # Labels files
                            'val': 'Annotations/val_labels.txt',
                            'test': 'Annotations/test_labels.txt',
                            }
        
        OUTPUTS_IDS_DATASET.append('food')
        OUTPUTS_IDS_MODEL.append('food')
        OUTPUTS_MAPPING['food'] = 1
        
        LOSS = [LOSS, 'categorical_crossentropy'] # add loss for food classification
        NUM_CLASSES_FOOD = 101
        CLASSIFIER_ACTIVATION_FOOD = 'softmax'
        
        # lambda parameter for weighting the loss functions (see bottom right page 6 in the paper)
        LOSS_WIGHTS = [0.2, 1] # 'loss_weights' for [0] ingredients (lambda in paper) and for [1] food

    # Image pre-processingparameters
    NORMALIZE_IMAGES = True
    MEAN_SUBSTRACTION = False #True
    DATA_AUGMENTATION = True  # only applied on training set

    # Evaluation params
    EVAL_ON_SETS = ['val','test']  # Possible values: 'train', 'val' and 'test'
    START_EVAL_ON_EPOCH = 1  # First epoch where the model will be evaluated

    # Optimizer parameters (see model.compile() function)
    OPTIMIZER = 'adam'
    LR_DECAY = 1  # number of minimum number of epochs before the next LR decay (set to None to disable)
    LR_GAMMA = 0.995  # multiplier used for decreasing the LR
    LR = 0.001  # general LR (0.001 recommended for adam optimizer)
    #LR = 0.01  # general LR (0.001 recommended for adam optimizer)
    PRE_TRAINED_LR_MULTIPLIER = None  # LR multiplier for pre-trained network (LR x PRE_TRAINED_LR_MULTIPLIER)
    NEW_LAST_LR_MULTIPLIER = 1.0  # LR multiplier for the newly added layers (LR x NEW_LAST_LR_MULTIPLIER)

    # Training parameters
    MAX_EPOCH = 200  # Stop when computed this number of epochs
    #PATIENCE = 20    # number of epoch we will wait to possibly obtain a higher accuracy
    PATIENCE = 10    # number of epoch we will wait to possibly obtain a higher accuracy
    BATCH_SIZE = 15
    PARALLEL_LOADERS = 8  # parallel data batch loaders
    EPOCHS_FOR_SAVE = 1  # number of epochs between model saves
    WRITE_VALID_SAMPLES = True  # Write valid samples in file

    # Model parameters
    # ===
    # Possible MODEL_TYPE values: 
    #                          [ Recommended Models ]
    #
    #                          VGG16
    #                          ResNet50
    # ===
    MODEL_TYPE = NETWORK_TYPE

    # Results plot and models storing parameters
    #EXTRA_NAME = '3_inception_recipes5k_higherLR' # custom name assigned to the model
    EXTRA_NAME = 'Recipe1M' # custom name assigned to the model
    MODEL_NAME = MODEL_TYPE+'_'+EXTRA_NAME
    
    REUSE_MODEL_NAME = None #'trained_models/ResNet50_5_resnet50_ingredients101' # 'trained_models/Inception_inception_recipes_v2' # None default
    #REUSE_MODEL_NAME = '/home/dariop/food_ingredients_recognition-LDA/trained_models/Inception_Recipe1M'
    LAST_LAYER = 'flatten' # 'flatten' #(InceptionV3)
    REUSE_MODEL_RELOAD = 30

    VERBOSE = 1  # Verbosity
    REBUILD_DATASET = True  # build again (True) or use stored instance (False)
    MODE = 'training'  # 'training' or 'predict' (if 'predict' then RELOAD must be greater than 0 and EVAL_ON_SETS will be used)

    RELOAD = 0  # If 0 start training from scratch, otherwise the model saved on epoch 'RELOAD' will be used
    STORE_PATH = 'trained_models/' + MODEL_NAME  # models and evaluation results
    

    # ============================================
    parameters = locals().copy()
    return parameters
