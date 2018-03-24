#PYTHONPATH=$PYTHONPATH:/home/dariop/multimodal_keras_wrapper-0.7-1:/home/dariop/keras-1.4 THEANO_FLAGS='optimizer=fast_compile,optimizer_including=fusion,lib.cnmem=0.5', python -u main.py
#export PYTHONPATH=$PYTHONPATH:/home/dariop/multimodal_keras_wrapper-0.7-1:/home/dariop/keras-1.4
#export PYTHONPATH=$PYTHONPATH:/home/dariop/multimodal_keras_wrapper-0.7-1:/home/dariop/keras
#export PYTHONPATH=$PYTHONPATH:/home/dariop/multimodal_keras_wrapper:/home/dariop/keras
export PYTHONPATH=/media/HDD3TB/dariop/libs/Theano:/media/HDD3TB/dariop/libs/multimodal_keras_wrapper:/media/HDD3TB/dariop/libs/keras:$PYTHONPATH
#THEANO_FLAGS='device=cuda1,optimizer=fast_compile,optimizer_including=fusion,lib.cnmem=0.3'
python -u main.py
