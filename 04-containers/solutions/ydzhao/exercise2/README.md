# Docker hands-on exercise 2

## Introduction
This exercise will guide you through using an existing image, the one you created in exercise 1, to create a new image. 

**Note:** Please complete [**exercise 1**](/04-containers/exercise1/) first before you work on this.

## Instructions

####  1. **Work on the cloned repository**:
You already have the forcked copy GitHub repo https://github.com/asntech/bios259-a24 locally.
Next change the working directory to  `04-containers/exercise2`  where you will find Dockerfile and the Python application `app2.py`.

```bash
cd bios259-a24/04-containers/exercise2
```

#### 2. Create a solution directory for excercise 2
Create a folder for excercise2 now in the solutions folder under your SUNet ID:
Replace `<your-SUNet-id>` with your SUNet ID.

```bash
mkdir -p 04-containers/solutions/<your-SUNet-id>/exercise2
```

#### 3. Copy the excerise files and work on your solutions
Inside the directory you just created, write your solution to the exercise 2.

```bash
cp 04-containers/exercise2/Dockerfile 04-containers/solutions/<your-SUNet-id>/exercise2/
cp 04-containers/exercise2/app2.py 04-containers/solutions/<your-SUNet-id>/exercise2/
```

#### 4. **Modify the Dockerfile**:
Open the `Dockerfile` in a text editor or vim. You need to use the docker image from your docker hub account that your peer pushed in exercise 1 as the starting point. You will see in the app2.py that it now also requires `seaborn` package to run `app2.py` and we already have `python` and `click` pre-installed.

Instrcutions are added to `Dockerfile` to make the edits.

#### 5. **Build the Docker image**:
Once you have modified the Dockerfile, build the Docker image using the `docker build` command. Replace `<image_name>` with a `bios259` and tag it `a24_v2`.

```bash
docker build -t bios259:a24_v2 .
```

#### 6. **Run the Docker container**:
After the image is built successfully, you can run a container from the image to ensure it works as expected.

```bash
docker run bios259:a24_v2
```
By default, it will print the descriptive statistics for a `seaborn` dataset.

#### 7. **Push the Docker image to Docker Hub**: 

Use the same steps from excercise 1 to push the updated image to your DockerHub. And confirm that your Docker image has been pushed successfully to the same repo with an updated version `a24_v2`.

#### 8. Push changes to GitHub:
Let's repeat the same steps from excercise 1.
Optionally, you can create a `README.md` file in the directory with your name and some details.

#### 9. Make a Pull Request:
Let's repeat the same steps from excercise 1.

#### 10. **Bonus task**:
If you've access to HPC, create a `Singularity` image using the Docker image you just pushed to Docker Hub and try to run it as a Singularity container on an HPC. If you don't have access to HPC, please pair-up with one who has access.

## Conclusion
Congratulations!! You have successfully built a Docker image by extending an existing one in the Docker Hub and installing the tools you need to run the application inside the container. This exercise demonstrates an advanced workflow for Docker image creation, distribution and running it on HPC as a Singularity container.
