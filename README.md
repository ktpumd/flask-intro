# Flask 101

## What is Flask?

Flask is a web framework written in Python that makes it really simple to build a web application. Some popular websites that include Flask in their technology stack include Netflix, Lyft, and Reddit. Flask is most commonly used to develop REST APIs (for the purposes of this tutorial, you don't really need to know that that means). It's also pretty popular in the industry and is a really useful skill to have on your resume, especially if you are interested in web development.

### What We're Going to Do

In this walkthrough, we're going to create a small application to show you just some of what you can do with Flask. The code for the app we will create is included in this repo for reference.

### Prerequisites

For this tutorial, you should have some basic familiarity with Python as well as some basic knowledge about how HTTP requests work.

## Set Up

First install `Python 3` and the latest version of `pip`, a popular Python package manager (they are most likely already installed but if not you can find instructions online). Then, create a directory where you want store your flask app and navigate to that directory. I'll call mine `app`. Once here, we need to create a virtual environment.

Let's just quickly talk about why we need virtual environments. Over time, you or apps you have installed onto your computer may have installed many different Python packages and libraries. A virtual environment is isolated from all this and acts as a fresh machine with no packages or libraries installed. This helps you keep track of what libraries and packages your specific application uses. Usually, these requirements are stored in a `requirements.txt` file that we will create later in this tutorial, so don't worry about it for now.

Use the following two lines to create and then enter the environment call myEnv:

```
$ python3 - m venv myEnv
$ source myEnv/bin/activate
```

When using GitHub, make sure to not include your virtual environment in your commits since it is technically not part of your project's codebase. Now that we are in our virtual environment, we can install Flask through pip:

```
$ pip install flask
```

If you're building an app and end up needing to install other packages or libraries, remember to activate your virtual environment before you do any installs to keep track of your dependencies.

Now we have everything we need, so we can start actually creating our application.

## Let's Build An App!

### Creating a Route

First thing we need to do is create a main file for app to live in. Let's call it `app.py` and put it in our `app` directory.


### Rendering a Webpage




## What Next?
