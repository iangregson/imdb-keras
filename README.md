# imdb-keras

Depends on the `ufoym/deepo` Machine Learning docker image.

```bash
docker pull ufoym/deepo:cpu
```

--------------------------------

## Useful commands

**Start container and run Tensorboard**

```bash
docker run --rm -d \
  -v $PWD/src:/src:rw \
  -v $PWD/data:/data:rw \
  -v $PWD/output:/output:rw \
  -p 0.0.0.0:6006:6006 \
  ufoym/deepo:cpu \
  tensorboard --logdir=./logs && export CONTAINER_ID=$(docker ps -lq)
```

**Get a shell on the ML container**

```bash
docker exec -it $CONTAINER_ID bash
```

**Train classifier**

```bash
docker exec -it $CONTAINER_ID python src/imdb_cnn.py data/imdb.csv
```

**Demo classifier**

```bash
docker exec -it $CONTAINER_ID python src/demo_classifier.py output/cnn_classifier.h5
```

**Run classifier**

```bash
docker exec -it $CONTAINER_ID python src/run_classifier.py cnn_classifier.h5 data/sr_test_data.csv SERREP_DESCRIPTION
```
