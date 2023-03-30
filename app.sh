options=$1
if [ $options = "CPU" ]; then
  sh CPU/docker.sh
elif [ $options = "GPU" ]; then
  sh GPU/docker.sh
fi