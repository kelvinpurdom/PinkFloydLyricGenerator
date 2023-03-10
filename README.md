# Pink Floyd Lyric Generator


#### Dataset: https://www.kaggle.com/datasets/joaorobson/pink-floyd-lyrics

#### Streamlit app: https://pinkfloydlyricgenerator.streamlit.app/

## Introduction
I have created a project that uses a LSTM model, to generate new and interesting suggestions for lyrics by letting the user input a seed text(or starting lyrics), then using the Pink Floyd Lyric database to suggest potential words to follow the seed text. It is a fun project but has some limitations regarding the size of the data, so results can be a little strange. Trained on a larger dataset, we would see better results.

## Screenshot of App
![test](PinkScreen.png)


## Installing Dependencies
The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for PinkFloydLyricGenerator in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/PinkFloydLyricGenerator`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "PinkFloydLyricGenerator"
git remote add origin git@github.com:{group}/PinkFloydLyricGenerator.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
PinkFloydLyricGenerator-run
```

# Install

Go to `https://github.com/{group}/PinkFloydLyricGenerator` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/PinkFloydLyricGenerator.git
cd PinkFloydLyricGenerator
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
PinkFloydLyricGenerator-run
```
