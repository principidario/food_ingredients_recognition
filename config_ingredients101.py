def load_parameters():
    """
        Loads the defined parameters
    """

    # Input data params
    #DATA_ROOT_PATH = '/media/HDD_2TB/marc/multimodal_keras_wrapper/data/sample_data/' # Root path to the data
    DATA_ROOT_PATH = '/media/HDD_3TB/DATASETS/Ingredients101/'
    #DATA_ROOT_PATH = '/media/HDD_3TB/DATASETS/Recipes5k/'
    CLASSIFICATION_TYPE = 'multi-label' # 'single-label' or 'multi-label'
    INGREDIENTS_TYPE = 'simplified'  # 'simplified' or 'complete'

    if CLASSIFICATION_TYPE == 'single-label':

        DATASET_NAME = 'Food_Recognition'  # Dataset name
        NUM_CLASSES = 2  # number of labels/classes of the dataset
        CLASSES_PATH = 'annotations/classes.txt'

        IMG_FILES = {'train': 'annotations/train.txt',  # Images files
                     'val': 'annotations/val.txt',
                     'test': 'annotations/test.txt'
                    }
        LABELS_FILES = {'train': 'annotations/train_labels.txt',  # Labels files
                        'val': 'annotations/val_labels.txt',
                        'test': 'annotations/test_labels.txt',
                        }

        # Evaluation
        METRICS = ['multiclass_metrics']  # Metric used for evaluating model
        STOP_METRIC = 'accuracy'  # Metric for the stop

        CLASSIFIER_ACTIVATION = 'softmax'  # 'softmax', 'sigmoid' (multi-label?), etc.
        LOSS = 'categorical_crossentropy'  # 'categorical_crossentropy' (better for sparse labels), 'binary_crossentropy', etc.


    elif CLASSIFICATION_TYPE == 'multi-label':

        if 'Ingredients101' in DATA_ROOT_PATH:

            if INGREDIENTS_TYPE == 'simplified':
                DATASET_NAME = 'Food_Ingredients101_simplified'  # Dataset name
                NUM_CLASSES = 228  # number of labels/classes of the dataset
                CLASSES_PATH = 'annotations/ingredients_simplified.txt'
                IMG_FILES = {'train': 'annotations/train_images.txt',  # Images files
                             'val': 'annotations/val_images.txt',
                             'test': 'annotations/test_images.txt'
                             }
                LABELS_FILES = {'train': 'annotations/train_labels.txt',  # Labels files
                                'val': 'annotations/val_labels.txt',
                                'test': 'annotations/test_labels.txt',
                                }

            elif INGREDIENTS_TYPE == 'complete':
                DATASET_NAME = 'Food_Ingredients101_complete'  # Dataset name
                NUM_CLASSES = 446  # number of labels/classes of the dataset
                CLASSES_PATH = 'annotations/ingredients.txt'
                IMG_FILES = {'train': 'annotations/train_images.txt',  # Images files
                             'val': 'annotations/val_images.txt',
                             'test': 'annotations/test_images.txt'
                             }
                LABELS_FILES = {'train': 'annotations/train_labels.txt',  # Labels files
                                'val': 'annotations/val_labels.txt',
                                'test': 'annotations/test_labels.txt',
                                }

        elif 'Recipes5k' in DATA_ROOT_PATH:

            if INGREDIENTS_TYPE == 'simplified':
                DATASET_NAME = 'Food_Recipes5k_simplified'  # Dataset name
                NUM_CLASSES = 1014  # number of labels/classes of the dataset
                CLASSES_PATH = 'annotations/ingredients_simplified_Recipes5k.txt'
                IMG_FILES = {'train': 'annotations/train_images.txt',  # Images files
                             'val': 'annotations/val_images.txt',
                             'test': 'annotations/test_images.txt'
                             }
                LABELS_FILES = {'train': 'annotations/train_labels.txt',  # Labels files
                                'val': 'annotations/val_labels.txt',
                                'test': 'annotations/test_labels.txt',
                                }

            elif INGREDIENTS_TYPE == 'complete':
                DATASET_NAME = 'Food_Recipes5k_complete'  # Dataset name
                NUM_CLASSES = 3213  # number of labels/classes of the dataset
                CLASSES_PATH = 'annotations/ingredients_Recipes5k.txt'
                IMG_FILES = {'train': 'annotations/train_images.txt',  # Images files
                             'val': 'annotations/val_images.txt',
                             'test': 'annotations/test_images.txt'
                             }
                LABELS_FILES = {'train': 'annotations/train_labels.txt',  # Labels files
                                'val': 'annotations/val_labels.txt',
                                'test': 'annotations/test_labels.txt',
                                }

        # Evaluation
        METRICS = ['multilabel_metrics']  # Metric used for evaluating model after each epoch. Possible values: 'multiclass' (see more information in utils/evaluation.py
        #STOP_METRIC = 'average precision'
        STOP_METRIC = 'f1'

        MIN_PRED_VAL = 0.5
        
        CLASSIFIER_ACTIVATION = 'sigmoid'  # 'softmax', 'sigmoid' (multi-label?), etc.
        LOSS = 'binary_crossentropy'  # 'categorical_crossentropy' (better for sparse labels), 'binary_crossentropy', etc.


    NETWORK_TYPE = 'Inception' # 'TestModel' for testing

    if NETWORK_TYPE == 'Inception':
        # InceptionV3
        IMG_SIZE = [342, 342, 3]
        IMG_SIZE_CROP = [299, 299, 3]
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


    # Image pre-processingparameters
    NORMALIZE_IMAGES = False
    MEAN_SUBSTRACTION = True
    DATA_AUGMENTATION = True  # only applied on training set

    # Evaluation params
    EVAL_ON_SETS = ['val', 'test']  # Possible values: 'train', 'val' and 'test'
    START_EVAL_ON_EPOCH = 1  # First epoch where the model will be evaluated

    # Optimizer parameters (see model.compile() function)
    OPTIMIZER = 'adam'
    LR_DECAY = 1  # number of minimum number of epochs before the next LR decay (set to None to disable)
    LR_GAMMA = 0.995  # multiplier used for decreasing the LR
    LR = 0.001  # general LR (0.001 recommended for adam optimizer)
    PRE_TRAINED_LR_MULTIPLIER = 0.001  # LR multiplier for pre-trained network (LR x PRE_TRAINED_LR_MULTIPLIER)
    NEW_LAST_LR_MULTIPLIER = 1.0  # LR multiplier for the newly added layers (LR x NEW_LAST_LR_MULTIPLIER)

    # Training parameters
    MAX_EPOCH = 50  # Stop when computed this number of epochs
    PATIENCE = 20    # number of epoch we will wait to possibly obtain a higher accuracy
    BATCH_SIZE = 10
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
    EXTRA_NAME = '8_inception_ingredients101_simplified' # custom name assigned to the model
    MODEL_NAME = MODEL_TYPE+'_'+EXTRA_NAME
    
    REUSE_MODEL_NAME = None # 'trained_models/Inception_inception_recipes_v2' # None default
    LAST_LAYER = 'flatten_1'  # 'flatten' #(InceptionV3)
    REUSE_MODEL_RELOAD = 0

    VERBOSE = 1  # Verbosity
    REBUILD_DATASET = True  # build again (True) or use stored instance (False)
    MODE = 'training'  # 'training' or 'predict' (if 'predict' then RELOAD must be greater than 0 and EVAL_ON_SETS will be used)

    RELOAD = 0  # If 0 start training from scratch, otherwise the model saved on epoch 'RELOAD' will be used
    STORE_PATH = 'trained_models/' + MODEL_NAME  # models and evaluation results
    

    # ============================================
    parameters = locals().copy()
    return parameters
